import click
import os
import json

from pygen.lib.model import create_to_json


def get_indent(times):
    times = times + 1
    spaces = ''
    for i in range(times):
        spaces = spaces + "    "
    return spaces


@click.group()
def main():
    pass


@main.command()
def test():
    file = open('/home/gli/test.py', 'w')
    create_to_json(file, None)


@main.command()
@click.option('-p', '--path', help="Project Root Path")
@click.option('-d', '--definition_path', help="Definition File")
def generate(path, definition_path):
    model_name = "Loggin"

    # try:
    with open(definition_path, 'r') as definition_file:
        definition = json.load(definition_file)
        for d in definition:
            print(d['name'])

        file_path = os.path.join(
            path, f'project/models/{model_name.lower()}.py')
        file = open(file_path, 'w')
        file.write("from project import db\n")
        file.write('\n')
        file.write('\n')
        file.write(f"class {model_name}(db.Model):\n")

        indent = get_indent(1)

        for d in definition:
            file.write(
                f'{indent}{d["name"]} = db.Column(db.{d["type"]}(), nullable={d["nullable"]})\n')

        file.write('\n')
        file.write(f'{indent}def __init__(self')

        for d in definition:
            indent = get_indent(1)
            file.write(f',\n                     {d["name"].lower()}')

        file.write('):\n')

        indent = get_indent(2)

        for d in definition:
            file.write(f'{indent}self.{d["name"]} = {d["name"]}\n')

        file.write('\n')
        indent = get_indent(1)
        file.write(f'{indent}def to_json(self):\n')

        indent = get_indent(2)
        file.write(f'{indent}return {{\n')

        indent = get_indent(3)
        for d in definition:
            name = d["name"]
            file.write(f'{indent}"{name}": self.{name}, \n')

        indent = get_indent(2)
        file.write(f'{indent}}}\n')

        file.close()

    # except Exception as ex:
    #     print(ex)
    #     return


if __name__ == '__main__':
    main()
