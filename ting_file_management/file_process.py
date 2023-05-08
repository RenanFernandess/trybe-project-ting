from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer
import sys


def process(path_file: str, instance: Queue):
    for item in list(instance.data):
        if item["nome_do_arquivo"] == path_file:
            return
    txt = txt_importer(path_file)
    data = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(txt),
        "linhas_do_arquivo": txt,
    }
    instance.enqueue(data)
    print(data, file=sys.stdout)


def remove(instance: Queue):
    try:
        data: dict = instance.dequeue()
        path = data["nome_do_arquivo"]
        print(f"Arquivo { path } removido com sucesso", file=sys.stdout)
    except IndexError:
        print("Não há elementos", file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
