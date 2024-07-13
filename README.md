# Web Scraping e Download de Arquivos
Este repositório contém um script Python que realiza web scraping em um site específico para baixar arquivos de extensão .txt e .pdf. O script utiliza as bibliotecas requests e BeautifulSoup para fazer requisições HTTP e parsear o HTML da página web.

# Funcionalidades
* Download de Arquivos: O script percorre uma lista de códigos específicos e faz uma requisição POST para cada código, utilizando um parâmetro CSRF capturado previamente. Em seguida, ele busca por links de arquivos .txt e .pdf e os baixa para diretórios correspondentes aos códigos.

* Criação Automática de Diretórios: Caso não existam, são criados diretórios para cada código de arquivo dentro de um diretório raiz chamado Downloads.

## Pré-requisitos
Certifique-se de ter Python 3.x instalado. As bibliotecas necessárias podem ser instaladas via pip com o seguinte comando:

### Instale as bibliotecas
```bash
pip install requests beautifulsoup4
```
### Como Usar
Clone este repositório:

```bash
git clone https://github.com/henriquemellodev/SimpleEnergy_teste.git
```
Navegue até o diretório do projeto:

```bash
cd seu_repositorio
```

### Execute o script Python:

```bash
python main.py
```

### Configuração
- URL Base: A URL base do site de onde os arquivos serão baixados está definida como url = "https://simpleenergy.com.br/teste/".

- Cabeçalhos HTTP: São definidos cabeçalhos HTTP para simular um navegador. Certifique-se de ajustar os cabeçalhos conforme as necessidades do site que está sendo acessado.

- Diretório de Downloads: Os arquivos baixados serão salvos em um diretório chamado Downloads, que será criado automaticamente se não existir.

## Estrutura do Código
O código está estruturado da seguinte forma:

- Define uma função downloadArquivos para baixar arquivos a partir de uma URL fornecida.
- Captura um parâmetro CSRF necessário para as requisições POST.
- Itera sobre uma lista de códigos de arquivos.
- Para cada código, cria um diretório correspondente dentro do diretório Downloads.
- Realiza uma requisição POST para buscar links de arquivos.
- Baixa arquivos .txt e .pdf encontrados para os diretórios correspondentes.
