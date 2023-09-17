# ATENÇÃO:
* 💣ESSE REPOSITÓRIO É APENAS PARA O ARQUIVAMENTO DOS CÓDIGOS FEITOS PELO VILHALVA.
* [ESTE REPOSITÓRIO É O ESPELHO DOS DESAFIOS DO "OS PROGRAMADORES"](https://osprogramadores.com/desafios/)
* [FAÇA O PR APENAS NO REPOSITÓRIO OFICIAL](https://github.com/OsProgramadores/op-desafios)

![](https://i.imgur.com/waxVImv.png)
# Repositório de desafios
## Instruções
Este documento contém informações importantes sobre como enviar o seu desafio,
assim como práticas recomendadas. Os admins recomendam a leitura integral do
documento antes do envio de PRs, mesmo para aqueles que já possuam
familiaridade com git e github.

## Conteúdo
Este repositório contém os desafios enviados pelos participantes do grupo
de programação [OsProgramadores](http://t.me/osprogramadores). O site do grupo
contém a [lista de desafios](https://osprogramadores.com/desafios/) com descrições
individuais de cada desafio.

## Como contribuir

1. Visite o [repositório op-desafios no github](https://github.com/osprogramadores/op-desafios).

1. Faça um _fork_ deste repositório clicando no botão `Fork` no canto superior
   da tela. Isso criará uma cópia completa do repositório sob o seu controle,
   no github.

1. Faça um clone do repositório para a sua estação de trabalho:
   ```
   git clone https://github.com/<seu_usuario_no_github>/op-desafios
   ```
1. Entre no diretório criado pelo git (`op-desafios`).

1. Crie um "git remote" chamado "upstream" apontando para o repositório
   principal. Isso facilitará a atualização do seu repositório local:

   ```
   git remote add upstream https://github.com/osprogramadores/op-desafios
   ```

1. **Antes de começar a trabalhar em qualquer desafio**: é importante resetar os números de
   _commit_ entre a sua cópia local e o repositório principal (isso acontece porque o
   repositório principal usa _rebase_ ao invés de _feature branches_). Existem
   duas maneiras de efetuar essa operação, mas a mais simples é usar "git reset"
   como indicado abaixo:

   ```
   git remote update
   git reset upstream/master --hard
   ```

   > **ATENÇÃO**
   >
   > Os comandos acima irão reverter **TODAS** as modificações no seu repositório.
   > É importante executá-los antes de introduzir qualquer modificação. Se você tem
   > modificações a preservar, a maneira mais simples (para um iniciante) é copiar
   > os arquivos a serem preservados para outro diretório, efetuar o `git reset`
   > indicado acima, e copiar os arquivos de volta.

1. Crie um _branch_ de trabalho com um nome adequado. No nosso exemplo, usaremos o nome "dev":

   ```
   git checkout -b dev
   ```

1. Trabalhe normalmente no _branch_ de desenvolvimento. Quando estiver satisfeito
   com o resultado, faça o _commit_ e o _push_ com:

   ```
   git push origin dev --force
   ```

1. O `git push` transfere o conteúdo do seu branch corrente ("dev" nesse caso)
   para a o seu _fork_ no github. Visite a página do seu _fork_ no github
   (normalmente, https://github.com/SEU-USUARIO-NO-GITHUB/op-desafios) e clique
   no botão para abrir um PR.

## O que fazer depois do envio?

Quando um PR é criado, o github envia um email para os admins, que farão a
revisão das modificações e, em caso de aprovação, a incorporação (ou _merge_)
das suas mudanças no repositório principal.

Um PR (ou _pull request_) é um **pedido** para incorporar as suas modificações
ao repositório principal. A sua tarefa só estará terminada quando os admins
tiverem incorporado as suas mudanças ao repositório principal (através de uma
operação _merge_).

O repositório principal contém testes de integração que procuram por erros
comuns e bloqueiam a aprovação até que estes tenham sido corrigidos. Por isso,
**fique atento ao seu email e a página do seu PR no github**. Verifique que os
testes de integração passaram e procure por mensagens dos admins relacionadas
ao seu PR.

Em caso de erros nos testes de integração ou pedido de mudança por parte dos admins,
corrija o problema no seu repositório local e crie outro commit com `git commit`,
seguido por `git push`. **Não crie outro PR, e não use o comando git reset até que
as suas modificações tenham sido incorporadas no repositório principal.**

PRs sem atividade por duas semanas serão automaticamente fechados.

## Linguagens de programação e estrutura de diretórios

Ao criar um novo desafio, é importante observar a estrutura de diretórios usada
pelo grupo:

```
desafio-XX/
  seu_usuario_no_github/
    linguagem/
      Seu código fonte(...)
      README.md <-- comentários, opcional.
```

Onde:

* `seu_usuário_no_github`, é o seu usuário no github. :)

* `linguagem` é o nome de diretório usado para uma das linguagens aceitas:
  * `c`: C
  * `cpp`: C++
  * `csharp`: C#
  * `java`: Java
  * `javascript`: Javascript
  * `go`: Go
  * `php`: PHP
  * `python`: Python (versão 3.x)

> Nota: Apenas desafios feitos em uma das linguagens acima serão aceitos.

Exemplo de um desafio em Java:

```
desafio-02/johndoe/java/MeuPrograma.java
desafio-02/johndoe/java/README.md
```

> **Importante**: Envie um PR por por desafio. PRs com múltiplos desafios serão
  rejeitados.

## Testes de integração

Os testes de integração rodam em todos os PRs e capturam vários erros comuns.
Os admins só farão a revisão do seu PR se os testes de integração estiverem
passando.

Algumas dicas básicas:

* Tente limitar ao máximo o envio de bibliotecas adicionais com os seus desafios.

* Não envie arquivos de configuração do seu IDE.

* Arquivos com espaços ou caracteres não ASCII no nome (acentos, Emoji, etc)
  não serão aceitos no repositório.

* Arquivos com conteúdo binário serão automaticamente rejeitados.

* Alguns editores (quando mal configurados) destroem caracteres UTF-8 (ou
  mandam caracteres inválidos). Arquivos com conteúdo UTF-8 inválido serão
  bloqueados pela integração.

* Arquivos contendo espaços ou tabs no final da linha (_trailing spaces_) serão
  rejeitados.

* Algumas linguagens de programação (ver abaixo) possuem checagens mais
  específicas. Nesse caso, algumas restrições se aplicarão ao código em si
  (estilo de formatação, erros, etc).  Consulte a próxima seção para maiores
  detalhes.

## Testes de linguagens específicas

### Go

Use tabs para indentar o seu código (seguindo o padrão Go).

O seu código deverá passar sem erro pelas seguinte ferramentas padrão:

* `golint`
* `go vet`
* `gofmt -s -l`
* `go build`

Leia a documentação da linguagem Go sobre como obter essas ferramentas
(normalmente, instaladas por default ou com um comando extra).

### Java

1. O código deve ser formatado utilizando o [estilo de desenvolvimento do
   Google](https://google.github.io/styleguide/javaguide.html).

1. O código será testado utilizando a OpenJDK VM na última versão **LTS** disponível: 17.

1. Utilizamos uma [biblioteca open-source disponibilizada pelo
   Google](https://github.com/google/google-java-format) para verificar a
   formatação do código. Dentro do repositório dela há mais informações sobre
   como integrá-la com ferramentas como Maven e Gradle caso deseje. A versão
   utilizada atualmente é a 1.15.0.

1. Para formatar os arquivos de acordo com o padrão utilizado, basta seguir os seguintes passos:

   ```shell
   curl -LJO "https://github.com/google/google-java-format/releases/download/v1.15.0/google-java-format-1.15.0-all-deps.jar"
   java -jar <caminho-para-o-jar-baixado>/google-java-format-1.15.0-all-deps.jar --replace <lista-arquivos-java>
   ```

1. Pull Requests contendo código em Java serão automaticamente verificados pela
   biblioteca indicada. Ao submeter um PR, observe a tela do PR e verifique se
   a integração falhou. Em caso de erro, clique no link e verifique as
   mensagens de erro.

1. Se precisar realizar alguma correção,faça no **mesmo PR** em que criou a
   solução original, não precisa abrir outro.

### Python

1. Apenas Python 3.x é suportado.

1. Use **espaços** (não tabs!) para indentar o seu código.

1. Use indentação em **4 espaços**.

1. Cheque o seu código com o [pylint](http://pylint.org) antes de enviar. O
   arquivo de configuração usado pelo depo está em `ci/pylint3.rc`. Para
   checar o seu programa, rode:

   ```
   pylint --rcfile=<diretorio_do_seu_repo>/ci/pylint3.rc <nome_do_seu_arquivo.py>
   ```

1. Pull Requests contendo código em Python serão automaticamente verificados
   pelo pylint. Ao submeter um PR, observe a tela do PR e verifique se a
   integração falhou. Em caso de erro, clique no link e verifique as mensagens
   de erro do pylint. Corrija o código, faça outro submit e push.

### Javascript

1. O código será inspecionado pela ferramenta [ESlint](https://eslint.org/docs/latest/user-guide/getting-started), utilizando as configurações padrões da ferramenta.

1. Instale NodeJS na sua máquina, [seguindo as instruções aqui](https://nodejs.org/en/download/package-manager/)

1. Feche e abra o prompt de comando e faça o download do plugin do eslint no repositório localmente:
   ```sh
   cd <diretorio_do_seu_repo>
   npm install --save-dev eslint-config-standard-with-typescript@23.0.0 eslint@8.24.0
   ```

1. Cheque o seu código com o eslint antes de enviar. O
   arquivo de configuração usado pelo repo está em `ci/.eslintrc.yml`. Para
   checar o seu programa, rode:

   ```
   npx eslint -c <diretorio_do_seu_repo>/ci/.eslintrc.yml <caminho_arquivo.js>
   ```

   Por exemplo, se seu diretório está em `/home/user/op-desafios`, o arquivo se chama `primos.js` e está na pasta atual, o comando deve ser:

   ```
   npx eslint -c /home/user/op-desafios/ci/.eslintrc.yml primos.js
   ```

1. Pull Requests contendo código em Javascript serão automaticamente verificados
   pelo eslint. Ao submeter um PR, observe a tela do PR e verifique se a
   integração falhou. Em caso de erro, clique no link e verifique as mensagens
   de erro do eslint. Corrija o código, faça outro submit e push.

> :warning: Não faça commit da pasta `node_modules` e dos arquivos `package.json` e `package-lock.json`. Não faça `git add *`, adicione *somente* sua pasta de solução no commit.

## Ainda tem dúvidas?

Em caso de problemas ou dúvidas, entre em contato com um dos administradores
no nosso [canal no Telegram](http://t.me/osprogramadores)
