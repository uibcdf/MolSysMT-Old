def is_file_smi(item):

    output = False

    if type(item)==str:
        output = item.endswith('.smi')

    return output

