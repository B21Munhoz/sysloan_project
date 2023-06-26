# PROJETO SYSLOAN


# BACK

Backend com a stack: Django, Django-Rest-Framework, PostgreSQL, RabbitMQ,
Redis e Celery, rodando no Docker.
A idéia é que um usuário admin possa acessar o painel admin do Django e
cadastrar campos para um formulário de empréstimo.
Através de uma API REST, é possível submeter propostas de empréstimo.
Ao serem submetidas, elas são salvas com aprovação 'Pendente', e são colocadas
na fila do Celery, para processamento, sendo 'Aprovadas' ou 'Negadas'.


### Build e Execução
 1. Mude para o diretório 'back': `cd back`
 2. Para construir: `docker-compose build`
 3. Para rodar: `docker-compose up` ou `docker-compose up -d`

 4. :exclamation: IMPORTANTE! Com o backend de pé, execute o comando abaixo:
      ```
      docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' server
      ```
   O retorno é o IP do serviço server dentro da network do docker. Copie o valor.
   Vá no arquivo front/sysloan_client/Dockerfile. Edite a linha 26, trocando o valor do
   IP ali presente pelo que você copiou. Salve o arquivo.

 5. Com a instância de pé, já é possível acessar o 
[Painel admin do Django](http://0.0.0.0:8000/) (http://0.0.0.0:8000/), usando:
   > Username: admin
   
   > Password: nicepassword

No Painel, em Proposals, você terá o Form Structure, e o Proposals.

 6. Em Form Structure, você tem acesso a um Singleton. Se é seu primeiro uso, ainda não
há uma instância. Ao tentar acessar qualquer endpoint da API, essa instância é
gerada com os campos default. O campo de 'cpf' não é necessário nessa estrutura, pois
é obrigatório para as instâncias de Proposals.
É possível editar o Form Structure adicionando, removendo ou editando os campos.
Depois de criado, não é possível adicionar outras instâncias, nem deletar a que já existe,
mantendo o padrão Singleton da estrutura.

 7. Em Proposals, você tem acesso à lista de propostas de empréstimo recebidas, indicadas
pelo cpf do cliente, quando foi submetida, e informando se elas foram Aceitas, Negadas,
ou estão com a análise Pendente. Ao clicar no cpf da proposta, é possível ver as informações
fornecidas para os campos cadastrados no Form Structure.


# FRONT: sysloan_client

Consiste em um front-end básico para o projeto.
Feito em Flutter, pode ser executado sem o AndroidStudio na versão web.
É criado um Formulário dinâmico, com base nos campos cadastrados pelo
painel admin do backend.

Infelizmente não foi possível estabelecer a comunicação entre 2 instâncias
de contêiner do Docker, mesmo colocando em bridge ou mesma network.
Dessa forma, será necessária a instalação de algumas dependências.


### Build e Execução
 1. Lembre-se de realizar a 4ª etapa do Build do Backend! 
 2. Mude para o diretório 'front': `cd ../front/sysloan_client/`
 3. Para construir: `docker-compose build`
 4. Para rodar: `docker-compose up` ou `docker-compose up -d`

 5. Depois de finalizado o build e execução, abra o Chrome e acesse
 o [client web](http://0.0.0.0:1000/) (http://0.0.0.0:1000/).
 
Insira as informações desejadas. Se estiver tudo ok, ao clicar em Enviar,
a requisição será feita para o back e uma mensagem de Toast irá aparecer na borda
inferior, informando do envio.


## MELHORIAS

 1. ~~A mais crítica, seria conseguir a comunicação dos conteineres do docker do back e do front.~~
Seria interessante uma forma mais automatizada de pegar o IP do serviço server. Infelizmente,
durante o flutter build, ainda não estamos na network, então não é possível pegar o IP nessa
etapa, nem parsear o service name, pois, ao fazer o build para web, o flutter cria arquivos estáticos
e um javascript que serão servidos pelo nginx.

 2. É possível enviar para o front os tipos dos campos e validações, para construir um
formulário mais complexo.

 3. Uma outra melhoria é no próprio layout do front.

## Autoria
Alvaro Munhoz Mota, 24/06/2023
