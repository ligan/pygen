
def write_method_declaration(file, indent, method_name):
    write_indent(file, 1)
    line = f'def {method_name}(self,'
    file.write(line + '\n')
    num_of_space = len(f'def {method_name}(')
    write_indent(file, 1)
    write_space(file, num_of_space)
    file.write("feature_id")


def write_indent(file, indent_depth):
    indent_depth = indent_depth + 1
    for i in range(indent_depth):
        file.write("    ")


def write_space(file, num_of_space):
    num_of_space = num_of_space
    for i in range(num_of_space):
        file.write(' ')
