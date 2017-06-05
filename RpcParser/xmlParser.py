import xml.etree.ElementTree as ET
import utilities as Tools

# https://docs.python.org/3/library/xml.etree.elementtree.html

tree = ET.parse('../MOBILE_API.xml')
root = tree.getroot()
markdown = open('../README.md', 'w')

markdown.write('# SmartDeviceLink\n')
markdown.write('# RPC Spec\n\n')
markdown.write('###### Version: ' + root.attrib['version'])
markdown.write('\n\n')

# ADDING ENUMS
markdown.write('## Enumerations\n\n')
for child in root.iter('enum'):
    Tools.write_iter_section(markdown, child, 'Elements')

# ADDING STRUCTS
markdown.write(Tools.PAGE_BREAK + Tools.NEW_LINE + '## Structs\n\n')
for child in root.iter('struct'):
    Tools.write_iter_section(markdown, child, 'Parameters')

# ADDING RPCS
markdown.write(Tools.PAGE_BREAK + Tools.NEW_LINE + Tools.NEW_LINE + '## Remote Procedure Calls\n\n')
for child in root.iter('function'):
    Tools.write_iter_section(markdown, child, 'Parameters')

markdown.close()


