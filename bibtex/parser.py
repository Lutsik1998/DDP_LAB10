def get_val(data, indentifier):
    lines = []
    for item in data:
        line = ''
        for key, val in item.items():
            if(key == indentifier):
                line = str(val) + ',\n' + line
            else:
                line += key + ' = \t' + str(val) + ',\n'
        lines.append(line)
    return lines


def tex_formatter(data, record_type, indentifier='id'):
    bodies = get_val(data, indentifier)
    text = ''
    for item in bodies:
        text += '@' + record_type + '{' + item + '}'
    return text