"""Not used anywhere

"""

from parsers.parse_error import ParseError
from parsers.sdl_rpc_v2 import Parser


def main(source_xml='../MOBILE_API.xml'):
    parser = Parser()
    version = parser.get_version
    print(version)

    try:
        interface = parser.parse(source_xml)
        print(vars(interface))
        return interface
    except (ParseError, KeyboardInterrupt) as error:
        print(error)


if __name__ == '__main__':
    main()
