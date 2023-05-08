import sys


def txt_importer(path_file):
    """função é capaz de importar notícias a partir de um arquivo TXT"""
    if not path_file[-4:] == ".txt":
        return print("Formato inválido", file=sys.stderr)
    try:
        with open(path_file) as file:
            return [line.removesuffix("\n") for line in file]
    except FileNotFoundError:
        return print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
