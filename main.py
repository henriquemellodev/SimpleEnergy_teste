import os
from bs4 import BeautifulSoup
import requests

# Função para baixar arquivos
def downloadArquivos(url, diretorio, nome_arquivo, headers):
    # Definir local do Arquivo
    local_arquivo = diretorio + '/' + nome_arquivo
    
    # Chamada para baixar Arquivo, setando headers e stream = True
    with requests.get(url, headers=headers ,stream=True) as r:
        r.raise_for_status()
        
        # Cria arquivo no diretorio correpondente e escreve
        with open(local_arquivo, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
  
    return local_arquivo
  
# Url da chamada
url = "https://simpleenergy.com.br/teste/"

# Preenchimento do Header, informando um navegador para captura de todos os dados
headers = {
  "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36"
}

# Captura da parâmetro csrf, para usar nas requisições
requisicao = requests.get(url, headers=headers)

# Parser HTML para facilitar busca.
site = BeautifulSoup(requisicao.text, "html.parser")

# Busca pelo input da página para a captura do valor
pesquisa = site.find("input")
csrf = str(pesquisa['value'])

# Definição do diretório raiz
diretorio_raiz = 'Downloads'

# Criar diretório se não existir
os.makedirs(diretorio_raiz, exist_ok=True)

# Códigos dos Arquivos
list_codigo = [98465, 321465]

for codigo in list_codigo:

  # Criação da Pasta do Codigo Correspondente
  os.makedirs(diretorio_raiz + '/' + str(codigo), exist_ok=True)
  diretorio_arquivos = diretorio_raiz + '/' + str(codigo)
  
  # Metodo POST, setando headers e form-data
  requisicao = requests.post(url, headers=headers, data={'csrf': csrf, 'codigo': codigo})
  
  # Validação se StatusCode == 200
  if (requisicao.status_code == 200):
    # Parse do HTML.
    site = BeautifulSoup(requisicao.text, "html.parser")

    # Busca por todas as tags a com href preenchido
    links = site.find_all('a', href=True)
    
    # Iterar por todos os Links
    for link in links:
      nome_arquivo = link['href']
      
      # Verifica estensão do arquivo
      if nome_arquivo.endswith('.txt') or nome_arquivo.endswith('.pdf'):
        arquivo_url = url + nome_arquivo.strip('/')

        # Chamada da função downloadArquivos
        try:
          print(f'Fazendo download: {arquivo_url}')
          downloadArquivos(arquivo_url,diretorio_arquivos, nome_arquivo, headers)
          print(f'Download do arquivo {arquivo_url} concluído com sucesso.')
        except Exception as ex:
          print(f'Erro ao baixar arquivo {arquivo_url}: {ex}')
  else:
    print('Requisição sem retorno.')
    
print('Finalizando o programa.') 