# TreeOrSoil
Este código objetiva detectar a partir de fotos de satélite se as imagens contém árvores ou apenas solo.  Para isso utiliza Machine Learning.

##Execução da CNN

Para executar o script que faz a inferência de rede é necessário primeiro ter Python instalado, os arquivos para instalação estão no site oficial Python. Selecione o arquivo adequado para seu sistema operacional. Em Windows é necessário que adicione ao PATH no instalador.
Após instalação buscar o repositório git e importa-lo através do terminal utilizando o comando. Caso não tenha git instalado há instruções no site oficial git:
Após essa etapa executar através de um terminal o seguinte código (em PowerShell) para criação de um ambiente virtual no diretório em que estiver localizado. 

//PS C:\Users\usuarioum\Documents\VENVTEST> python -m venv ArvoreOuSolo
//PS C:\Users\usuarioum\Documents\VENVTEST> .\ArvoreOuSolo\Scripts\activate
 
Neste caso o comando instala o ambiente virtual no diretório C:\Users\usuarioum\Documents\VENVTEST. Seu terminal deve estar agora com o texto (ArvoreOuSolo) no início da linha de comando.
Dentro do ambiente execute o seguinte comando para instalar as dependências:

//pip install  tensorflow numpy scikit-learn pillow optuna

Para analisar o próprio conjunto de imagens, que devem ter 50 por 50 pixels e formato RGB, vá até o diretório da pasta AI e execute o comando 

//python AI.py

O programa deve executar e retornar um arquivo “results.csv” no mesmo diretório.

##Treinamento da CNN

Para executar os códigos para treinamento basta executar o comando dentro do ambiente virtual criado:

//python main.py 

Durante a execução será pedido o diretório do conjunto de dados para treino.  O programa cria dois arquivos, model.h5 e results.csv. Caso obtenha um modelo com maior acuracidade ou menor perda pode substituir o arquivo model.h5 do diretório AI.
 
