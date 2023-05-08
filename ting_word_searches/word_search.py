from ting_file_management.queue import Queue


def exists_word(word: str, instance: Queue):
    """verifica a existência de uma palavra em todos os
    arquivos processados."""
    result = list()
    for data in list(instance.data):
        occurrences = list()
        for index in range(len(data["linhas_do_arquivo"])):
            if word.lower() in data["linhas_do_arquivo"][index].lower():
                occurrences.append({"linha": (index + 1)})

        if len(occurrences):
            result.append(
                {
                    "palavra": word,
                    "arquivo": data["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )

    return result


def search_by_word(word: str, instance: Queue):
    """Busca uma palavra em todos os arquivos processados."""
    result = list()
    for data in list(instance.data):
        occurrences = list()
        for index in range(len(data["linhas_do_arquivo"])):
            if word.lower() in data["linhas_do_arquivo"][index].lower():
                occurrences.append(
                    {
                        "linha": (index + 1),
                        "conteudo": data["linhas_do_arquivo"][index],
                    }
                )

        if len(occurrences):
            result.append(
                {
                    "palavra": word,
                    "arquivo": data["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )

    return result
