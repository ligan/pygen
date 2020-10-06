from .utils import write_indent, write_method_declaration


def create_to_json(file, description):
    write_method_declaration(file, 1, "__init__")
