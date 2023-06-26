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
 - Mude para o diretório 'back': `cd back`
 - Para construir: `docker-compose build`
 - Para rodar: `docker-compose up` ou `docker-compose up -d`

Com a instância de pé, já é possível acessar o 
[Painel admin do Django](http://0.0.0.0:8000/), usando:
   > Username: admin
   
   > Password: nicepassword

No Painel, em Proposals, você terá o Form Structure, e o Proposals.

 - Em Form Structure, você tem acesso a um Singleton. Se é seu primeiro uso, ainda não
há uma instância. Ao tentar acessar qualquer endpoint da API, essa instância é
gerada com os campos default. O campo de 'cpf' não é necessário nessa estrutura, pois
é obrigatório para as instâncias de Proposals.
É possível editar o Form Structure adicionando, removendo ou editando os campos.
Depois de criado, não é possível adicionar outras instâncias, nem deletar a que já existe,
mantendo o padrão Singleton da estrutura.

- Em Proposals, você tem acesso à lista de propostas de empréstimo recebidas, indicadas
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


### Instalando Dependências
Você precisará ter instalado:
 - Docker
 - Chrome
 - Git
 - VSCode

Também será necessário:
 - Intalar o OpenJDK 8:
    ```
    sudo apt install openjdk-8-jre
    sudo apt install openjdk-8-jdk
    ```
 - Instalar o Snapd:
    ```
    sudo apt update
    sudo apt install snapd
    ```
 - Instalar o SDK do FLutter:
    ```
    sudo snap install flutter --classic
    ```
 - Você ppode verificar  o path com:
    ```
    flutter sdk-path
    ```

Com este setup, já é possível rodar o front em Flutter web.
 - No VSCode, abra a pasta `front/sysloan_client/`
 - Abra o terminal do VSCode e entre com o comando: `flutter pub get`,
 para instalar as dependências.

### Build e Execução
 - Rode: `flutter build web`
 - Quando finalizado, rode o projeto com o seguinte comando:
    `flutter run -d chrome --web-browser-flag "--disable-web-security"`
 Como o flutter irá rodar no Chrome, e iremos realizar a comunicação com
 o backend rodando em localhost, será necessário usar a flag para desabilitar
 a segurança web nessa janela que irá abrir, contornando o problema do Chrome
 com as validações de CORS em ambiente local.

Após rodar o comando de run, o Flutter irá se conectar ao Chrome e abrir uma
janela com a aplicação.

Insira as informações desejadas. Se estiver tudo ok, ao clicar em Enviar,
a requisição será feita para o back e uma mensagem de Toast irá aparecer na borda
inferior, informando do envio.


## MELHORIAS

A mais crítica, seria conseguir a comunicação dos conteineres do docker do back e do front.

Depois, é possível enviar para o front os tipos dos campos e validações, para construir um
formulário mais complexo.

Uma outra melhoria é no próprio layout do front.

## Autoria
Alvaro Munhoz Mota, 24/06/2023
