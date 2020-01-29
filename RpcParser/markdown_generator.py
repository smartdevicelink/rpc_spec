"""
Generator for Markdown
"""
import logging
import re
import sys
from argparse import ArgumentParser
from collections import namedtuple
from pathlib import Path
from time import sleep
from xml.etree.ElementTree import ParseError as XmlParseError

ROOT = Path(__file__).absolute().parents[0]
sys.path.append(ROOT.parents[0].joinpath('InterfaceParser').as_posix())

try:
    from model.function import Function
    from model.enum import Enum
    from model.struct import Struct
    from model.enum_subset import EnumSubset
    from model.array import Array

    from parsers.rpc_base import ParseError as ModelParseError
    from parsers.sdl_rpc_v2 import Parser
except ModuleNotFoundError as error:
    print(error)
    sys.exit(1)


class Markdown:
    """
    Generator for Markdown
    """

    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
        self.config_logging('verbose')
        self.file_name = 'README.md'

    def get_parser(self):
        """
        Parsing command-line arguments, or evaluating required Paths interactively.
        :return: an instance of argparse.ArgumentParser
        """
        if len(sys.argv) == 2 and sys.argv[1] in ('-v', '--version'):
            print('1.0.0')
            sys.exit(0)

        Paths = namedtuple('Paths', 'name path')
        xml = Paths('source_xml', ROOT.parents[0].joinpath('MOBILE_API.xml'))
        out = Paths('output_directory', ROOT.parents[0].joinpath(self.file_name))

        parser = ArgumentParser(description='Mobile API Spec Generator')
        parser.add_argument('-v', '--version', action='store_true', help='print the version and exit')
        parser.add_argument('-xml', '--source-xml', '--input-file', required=not xml.path.exists(),
                            help='should point to MOBILE_API.xml')
        parser.add_argument('-xsd', '--source-xsd', required=False)
        parser.add_argument('-d', '--output-directory', required=False,
                            help='define the place where the generated output_directory should be placed')
        parser.add_argument('-r', '--regex-pattern', required=False,
                            help='only elements matched with defined regex pattern will be parsed and generated')
        parser.add_argument('--verbose', action='store_true', help='display additional details like logs etc')
        parser.add_argument('-e', '--enums', required=False, action='store_true',
                            help='only specified elements will be generated, if present')
        parser.add_argument('-s', '--structs', required=False, action='store_true',
                            help='only specified elements will be generated, if present')
        parser.add_argument('-m', '-f', '--functions', required=False, action='store_true',
                            help='only specified elements will be generated, if present')
        parser.add_argument('-y', '--overwrite', action='store_true',
                            help='force overwriting of existing files in output_directory file, ignore confirmation '
                                 'message')
        parser.add_argument('-n', '--skip', action='store_true',
                            help='skip overwriting of existing files in output_directory file, ignore confirmation '
                                 'message')

        args, unknown = parser.parse_known_args()

        if unknown:
            self.logger.error('found unknown arguments: %s', ' '.join(unknown))
            parser.print_help(sys.stderr)
            sys.exit(1)

        if args.skip and args.overwrite:
            self.logger.error('please select only one option skip or overwrite')
            sys.exit(1)

        if not args.enums and not args.structs and not args.functions:
            args.enums = args.structs = args.functions = True

        if args.output_directory:
            args.output_directory = self.evaluate_output_directory(args.output_directory)

        for kind in (xml, out):
            if not getattr(args, kind.name):
                while True:
                    try:
                        confirm = input('Confirm default path {} for {} Y/Enter = yes, N = no'
                                        .format(kind.path, kind.name))
                        if confirm.lower() == 'y' or not confirm:
                            self.logger.info('%s set to %s', kind.name, kind.path)
                            setattr(args, kind.name, kind.path)
                            sleep(0.05)
                            break
                        if confirm.lower() == 'n':
                            self.logger.warning('provide argument %s', kind.name)
                            sys.exit(1)
                    except KeyboardInterrupt:
                        self.logger.warning('\nThe user interrupted the execution of the program')
                        sys.exit(1)

        return args

    def evaluate_output_directory(self, output_directory):
        """

        :param output_directory:
        :return:
        """
        if output_directory.startswith('/'):
            path = Path(output_directory).absolute().resolve()
        else:
            path = ROOT.joinpath(output_directory).resolve()
        if not path.exists():
            self.logger.warning('Directory not found: %s, trying to create it', path)
            try:
                path.mkdir(parents=True, exist_ok=True)
            except OSError as message1:
                self.logger.error('Failed to create directory %s, %s', path.as_posix(), message1)
                sys.exit(1)
        return path.joinpath(self.file_name)

    def config_logging(self, verbose):
        """

        :param verbose:
        :return:
        """
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter(fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                               datefmt='%m-%d %H:%M'))
        if verbose:
            handler.setLevel(logging.DEBUG)
            self.logger.setLevel(logging.DEBUG)
        else:
            handler.setLevel(logging.ERROR)
            self.logger.setLevel(logging.ERROR)
        logging.getLogger().handlers.clear()
        root_logger = logging.getLogger()
        root_logger.addHandler(handler)

    @staticmethod
    def extract_type(param):
        """Evaluate and extract type
        :param param: sub-element (Param, FunctionParam) of element from initial Model
        :return: string with sub-element type
        """

        def evaluate(kind):
            if isinstance(kind, EnumSubset):
                return kind.enum.name
            if isinstance(kind, (Struct, Enum)):
                return kind.name
            return type(kind).__name__

        if isinstance(param.param_type, Array):
            return '{}[]'.format(evaluate(param.param_type.element_type))
        return evaluate(param.param_type)

    def process(self, readme_file, interface):
        """Main function for generation Markdown

        :param readme_file: path to README.md
        :param interface: path to MOBILE_API.xml
        """
        try:
            section_name = elem_or_param = ''
            with open(readme_file, 'w') as mark_down:
                mark_down.write('# SmartDeviceLink\n# RPC Spec\n\n###### Version: {}\n\n'
                                .format(interface['params']['version']))
                for i, (kind, items) in enumerate(interface.items()):
                    if kind == 'params':
                        continue
                    if kind == 'enums':
                        container_name = 'elements'
                        section_name = 'Enumerations'
                        elem_or_param = 'Elements'
                    elif kind == 'structs':
                        container_name = 'members'
                        section_name = 'Structs'
                        elem_or_param = 'Parameters'
                    elif kind == 'functions':
                        container_name = 'params'
                        section_name = 'Remote Procedure Calls'
                        elem_or_param = 'Parameters'

                    mark_down.write('## {}\n\n'.format(section_name))
                    for item in items.values():
                        mark_down.write('### {}'.format(item.name))
                        if isinstance(item, Function):
                            mark_down.write('\nMessage Type: **{}**\n'.format(item.message_type.name))
                        if item.deprecated and item.since:
                            mark_down.write('\ndeprecated since ' + item.since)
                        if item.description:
                            mark_down.write('\n{}\n'.format(re.sub(r'\s{2,}', ' ', ''.join(item.description)).strip()))

                        if getattr(item, container_name):
                            mark_down.write('\n##### {}\n\n| Value | '.format(elem_or_param))
                            if isinstance(item, Enum):
                                mark_down.write('Description | \n| ---------- |:-----------:|')
                            else:
                                mark_down.write(' Type | Mandatory | Description | \n'
                                                '| ---------- | ---------- |:-----------: |:-----------:|')
                            mark_down.write('\n')
                            for param in getattr(item, container_name).values():
                                mark_down.write('|`' + param.name + '`|')
                                if isinstance(item, (Struct, Function)):
                                    mark_down.write('{}|{}|'.format(self.extract_type(param), str(param.is_mandatory)))
                                mark_down.write(re.sub(r'\s{2,}', ' ', ''.join(param.description)).strip() + '|\n')
                        mark_down.write('\n\n')
                    if i < len(interface) - 2:
                        mark_down.write('\n<div style="page-break-after: always;"></div>\n\n')
        except (IsADirectoryError, NotADirectoryError) as error1:
            self.logger.error(error1)
            sys.exit(1)

    @staticmethod
    def filter_pattern(interface, pattern):
        """
        Filtering Interface to extract only items matched with regex pattern
        :param interface: Interface model
        :param pattern: regex
        :return:
        """
        match = {i: {} for i in vars(interface).keys()}
        match['params'] = interface.params
        if pattern:
            for key, value in vars(interface).items():
                if key == 'params':
                    continue
                for name, item in value.items():
                    if re.match(pattern, item.name):
                        if key in match:
                            match[key].update({name: item})
        else:
            return vars(interface)
        return match

    def main(self):
        """
        Main functions calls
        """
        args = self.get_parser()
        self.config_logging(args.verbose)

        try:
            interface = Parser().parse(args.source_xml, args.source_xsd)
        except (ModelParseError, XmlParseError) as error1:
            self.logger.error(error1)
            sys.exit(1)

        filtered = self.filter_pattern(interface, args.regex_pattern)

        if not args.enums:
            del filtered['enums']
        if not args.structs:
            del filtered['structs']
        if not args.functions:
            del filtered['functions']

        if args.output_directory.is_file():
            if args.skip:
                self.logger.info('Skipping %s', args.output_directory.as_posix())
                return
            if args.overwrite:
                self.logger.info('Overriding %s', args.output_directory.as_posix())
                self.process(args.output_directory, filtered)
            else:
                while True:
                    try:
                        confirm = input('File already exists {}. Overwrite? Y/Enter = yes, N = no\n'
                                        .format(args.output_directory.as_posix()))
                        if confirm.lower() == 'y' or not confirm:
                            self.logger.info('Overriding %s', args.output_directory.as_posix())
                            self.process(args.output_directory, filtered)
                            break
                        if confirm.lower() == 'n':
                            self.logger.info('Skipping %s', args.output_directory.as_posix())
                            break
                    except KeyboardInterrupt:
                        self.logger.info('\nThe user interrupted the execution of the program')
                        sys.exit(1)
        else:
            self.logger.info('Writing new %s', args.output_directory.as_posix())
            self.process(args.output_directory, filtered)


if __name__ == '__main__':
    Markdown().main()
