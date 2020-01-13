
"""Not used anywhere

"""

from os.path import exists

from xmlschema import XMLSchema
from parsers.parse_error import ParseError
from parsers.sdl_rpc_v2 import Parser


def main(source_xml='../MOBILE_API.xml', source_xsd=None):
    """Example of Main function of the parser that does actual work.
    """
    if not source_xsd:
        source_xsd = source_xml.replace('.xml', '.xsd')
        if not exists(source_xsd):
            print(FileNotFoundError('not found', source_xsd))

    print("""
Validating XML and generating model with following parameters:
    Source xml      : {0}
    Source xsd      : {1}
""".format(source_xml, source_xsd))

    xml_schema = XMLSchema(source_xsd)
    if not xml_schema.is_valid(source_xml):
        print(xml_schema.validate(source_xml))

    parser = Parser()
    version = parser.get_version
    print(version)

    # Convert incoming xml to internal model
    try:
        interface = parser.parse(source_xml)
        print(vars(interface))
        return interface
    except (ParseError, KeyboardInterrupt) as error:
        print(error)


if __name__ == '__main__':
    main()
