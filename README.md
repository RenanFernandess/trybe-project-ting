<a name="readme-top"></a>
# Boas-vindas ao repositório do TING (Trybe is not Google)!

<details>
  <summary>Índice</summary>
  <ol>
    <li>
      <a href="#sobre-o-projeto">Sobre o Projeto</a>
      <ul>
        <li><a href="#construido-com">Construido Com</a></li>
      </ul>
    </li>
    <li>
      <a href="#começando">Começando</a>
      <ul>
        <li><a href="#instalação">Instalação</a></li>
        <li><a href="#ambiente-virtual">Ambiente virtual</a></li>
        <li><a href="#tests">Tests</a></li>
      </ul>
    </li>
    <li><a href="#uso">Uso</a></li>
    <li><a href="#contato">Contato</a></li>
    <li><a href="#agradecimentos">Agradecimentos</a></li>
  </ol>
</details>

## Sobre o Projeto
Neste projeto foi responsável por implementar um programa que simula um algoritmo de indexação de documentos similar ao do Google. Seu programa deverá ser capaz de identificar ocorrências de termos em arquivos TXT.

**Para isso, foi desenvolvido deverá ter dois módulos:**
- Módulo de gerenciamento de arquivos que permite anexar arquivos de texto (formato TXT) e;
- Módulo de buscas que permite operar funções de busca sobre os arquivos anexados.


### Habilidades trabalhadas
- Manipular Pilhas;
- Manipular Deque;
- Manipular Nó & Listas Ligadas e;
- Manipular Listas Duplamente Ligadas.

### Construido Com

* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* ![pytest](https://img.shields.io/badge/pytest-3670A0?style=for-the-badge&logo=pytest&logoColor=ffdd54)

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

## Começando

### Instalação

1. Clonar o repositorio

        git clone git@github.com:RenanFernandess/trybe-project-ting.git

2. Entrar na pasta project-job-insights

        cd ./trybe-project-ting

### Ambiente virtual

O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

1. **criar o ambiente virtual**

        python3 -m venv .venv

2. **ativar o ambiente virtual**

        source .venv/bin/activate

3. **instalar as dependências no ambiente virtual**

        python3 -m pip install -r dev-requirements.txt

> Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando `deactivate`. Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

### Tests

 Para executar os testes certifique-se de que você está com o ambiente virtual ativado.

  <strong>Executar os testes</strong>

    python3 -m pytest

  <details>
  <summary>Mais comandos</summary>
  
   O arquivo `pyproject.toml` já configura corretamente o pytest. Entretanto, caso você tenha problemas com isso e queira explicitamente uma saída completa, o comando é:

  ```bash
  python3 -m pytest -s -vv
  ```

  Caso precise executar apenas um arquivo de testes basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py
  ```

  Caso precise executar apenas uma função de testes basta executar o comando:

  ```bash
  python3 -m pytest -k nome_da_func_de_tests
  ```

  Para executar um teste específico de um arquivo, basta executar o comando:

  ```bash
  python3 -m pytest tests/nomedoarquivo.py::test_nome_do_teste
  ```

</details>

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

## Uso
- ting_file_management/queue.py
    * **Class Queue**
        - A fila (Queue) é uma estrutura FIFO, ou seja, o primeiro item a entrar, deve ser o primeiro a sair. Utilizando conhecimentos de estruturas de dados para otimizar as operações implementadas.
        - A fila possui os métodos de inserção (enqueue), remoção (dequeue) e busca (search).

- ting_file_management/file_management.py
    * **txt_importer**
        - Caso o arquivo TXT não exista, exibe a mensagem "Arquivo {path_file} não encontrado" na stderr, em que {path_file} é o caminho do arquivo;
        - Caso a extensão do arquivo seja diferente de .txt, exibe a mensagem Formato inválido na stderr;
        - A função retorna uma lista contendo as linhas do arquivo.


        ```
        def txt_importer(path_file):
            if not path_file[-4:] == ".txt":
                return print("Formato inválido", file=sys.stderr)
            try:
                with open(path_file) as file:
                    return [line.removesuffix("\n") for line in file]
            except FileNotFoundError:
                return print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
        ```

- ting_file_management/file_process.py
    * **process**
        - A função irá receber como parâmetro um objeto instanciado da fila(Queue) e o caminho para um arquivo;
             
             ```
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
            ```

       - A instância da fila recebida por parâmetro é utilizada para registrar o processamento dos arquivos;
       - A função processa o arquivo passado por parâmetro (ou seja, gerar um dicionário com o formato e informações especificadas abaixo);
       - Ignora arquivos que já tenham sido processados anteriormente (ou seja, arquivos com o mesmo nome e caminho (nome_do_arquivo) não são adicionados à fila novamente);
       - Após cada nova inserção válida, a função mostra via stdout os dados processados, conforme estrutura no exemplo abaixo.
       - **Exemplo da estrutura de saída**
          ```
          {
              "nome_do_arquivo": "arquivo_teste.txt", # Caminho do arquivo recém adicionado
              "qtd_linhas": 3,                        # Quantidade de linhas existentes no arquivo
              "linhas_do_arquivo": [...]              # linhas retornadas pela função txt_importer
          }
          ```
       
    * **remove**
        - A função irá receber como parâmetro a instância da fila(Queue).
            
            ```
            def remove(instance: Queue):
                try:
                    data: dict = instance.dequeue()
                    path = data["nome_do_arquivo"]
                    print(f"Arquivo { path } removido com sucesso", file=sys.stdout)
                except IndexError:
                    print("Não há elementos", file=sys.stdout)
            ```

        - Caso não existam arquivos na fila, a função emite a mensagem "Não há elementos" via stdout;
        - Em caso de sucesso de remoção, emite a mensagem "Arquivo {path_file} removido com sucesso" via stdout, em que {path_file} é o caminho do arquivo.
       
    * **file_metadata**
        - A função irá receber como parâmetro a instância da fila(Queue) e o índice a ser buscado;
            
            ```
            def file_metadata(instance: Queue, position: int):
                try:
                    data = instance.search(position)
                    print(data, file=sys.stdout)
                except IndexError:
                    print("Posição inválida", file=sys.stderr)
             ```

        - Caso a posição não exista, exibe a mensagem de erro "Posição inválida" via stderr;
        - Caso a posição seja válida, as informações relacionadas ao arquivo serão mostradas via stdout, seguindo o exemplo de estrutura abaixo.
        - Exemplo da estrutura de saída em caso de sucesso:
             ```
             {
                 "nome_do_arquivo": "arquivo_teste.txt",
                 "qtd_linhas": 3,
                 "linhas_do_arquivo": [...]
             }
             ```
        

- ting_word_searches/word_search.py
    * **exists_word**
        - A função irá receber como parâmetros a palavra a ser buscada e a instância da fila(Queue);
            
            ```
            def exists_word(word: str, instance: Queue):
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
            ```

        - A função retorna uma lista com as informações de cada arquivo e suas linhas em que a palavra foi encontrada, conforme exemplo da estrutura de retorno;
        - A busca é case insensitive (não diferenciar maiúsculas e minúsculas);
        - **Exemplo da estrutura de retorno**

            ```
            [{
                "palavra": "de",
                "arquivo": "arquivo_teste.txt",
                "ocorrencias": [
                    { "linha": 2 },
                    { "linha": 7 }
                ]
             }]
            ```

    * **search_by_word**
        - A função irá receber como parâmetros a palavra a ser buscada e a instância da fila(Queue);
        
            ```
            def search_by_word(word: str, instance: Queue):
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
            ```

        - A função retorna uma lista com as informações de cada arquivo e suas linhas em que a palavra foi encontrada, conforme exemplo da estrutura de retorno;
        - A busca é case insensitive (não diferenciar maiúsculas e minúsculas);
        - **Exemplo da estrutura de retorno**

            ```
            [{
                "palavra": "de",
                "arquivo": "arquivo_teste.txt",
                "ocorrencias": [
                    {
                        "linha": 3,
                        "conteudo": "Acima de tudo,"
                    },
                    {
                        "linha": 4,
                        "conteudo": "é fundamental ressaltar que a adoção de políticas descentralizadoras nos obriga"
                    }
                ]
             }]
            ```


<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

## Contato

* Renan Fernandes - [Linkedin](https://www.linkedin.com/in/orenanfernandes/) - renzinestuods@gmail.com

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>

## Agradecimentos

* [Trybe](https://www.betrybe.com/)
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#readme-top">voltar ao topo</a>)</p>
