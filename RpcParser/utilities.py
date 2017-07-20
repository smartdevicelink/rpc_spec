NEW_LINE = '\n'
TABLE_DIVIDER_2 = '| ---------- |:-----------:|'
PAGE_BREAK = '\n<div style="page-break-after: always;"></div>\n'


def write_element_header(outfile):
    outfile.write('\n##### Elements\n\n')
    outfile.write('| Value | Description | \n')
    outfile.write(TABLE_DIVIDER_2)
    outfile.write(NEW_LINE)


def write_param_header(outfile):
    outfile.write('\n##### Param\n\n')
    outfile.write('| Value | Description | \n')
    outfile.write(TABLE_DIVIDER_2)
    outfile.write(NEW_LINE)


def write_header(outfile, elem_param):
    outfile.write('\n##### ')
    outfile.write(elem_param)
    outfile.write('\n\n')
    outfile.write('| Value | Description | \n')
    outfile.write(TABLE_DIVIDER_2)
    outfile.write(NEW_LINE)


def write_iter_section(markdown, child, elem_or_param):
    markdown.write('### ')
    markdown.write(child.attrib['name'])

    if child.tag == 'function':
        markdown.write('\nMessage Type: **' + child.attrib['messagetype'] + '**\n')

    # Write the values in the enum
    first_element = True
    for element in child:
        if first_element:
            first_element = False
            if element.tag == 'description':
                # We have a description for out previous entry
                markdown.write(NEW_LINE + element.text.lstrip() + NEW_LINE)
                write_header(markdown, elem_or_param)
                continue
            else:
                write_header(markdown, elem_or_param)

        # For incorrect syntax
        if element.tag == 'description':
            continue

        value = element.attrib['name']

        if value:
            markdown.write('|`' + value + '`|')
            description = element.find('description')

        if description is not None:
            markdown.write(description.text.encode('utf-8').lstrip().replace('\n', ''))

        markdown.write('|' + NEW_LINE)

    markdown.write('\n\n')
