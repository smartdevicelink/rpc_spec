"""Generator for Markdown

"""
import re
import sys
from pathlib import Path

sys.path.append(Path(__file__).absolute().parents[1].joinpath('InterfaceParser').as_posix())
try:
    from model.function import Function
    from model.enum import Enum
    from model.struct import Struct
    from model.enum_subset import EnumSubset
    from model.array import Array
    from model.double import Double

    from parsers.rpc_base import ParseError
    from parsers.sdl_rpc_v2 import Parser
except ModuleNotFoundError as error:
    print(error)
    sys.exit(1)


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
        if isinstance(kind, Double):
            return 'Float'
        return type(kind).__name__

    if isinstance(param.param_type, Array):
        return '{}[]'.format(evaluate(param.param_type.element_type))
    return evaluate(param.param_type)


def main(readme_file='../README.md', file_xml='../MOBILE_API.xml'):
    """Main function for generation Markdown

    :param readme_file: path to README.md
    :param file_xml: path to MOBILE_API.xml
    """
    try:
        interface = Parser().parse(file_xml)
        interface = vars(interface)
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
                                mark_down.write('{}|{}|'.format(extract_type(param), str(param.is_mandatory)))
                            mark_down.write(re.sub(r'\s{2,}', ' ', ''.join(param.description)).strip() + '|\n')
                    mark_down.write('\n\n')
                if i < len(interface) - 2:
                    mark_down.write('\n<div style="page-break-after: always;"></div>\n\n')
    except ParseError as error1:
        print(error1)
        sys.exit(1)


if __name__ == '__main__':
    main()
