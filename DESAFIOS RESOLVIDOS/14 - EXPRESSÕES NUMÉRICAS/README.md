# [DESAFIO 14: EXPRESSÕES NUMÉRICAS](https://osprogramadores.com/desafios/d14/)

## DESCRIÇÃO:
Expressões numéricas são sequências de duas ou mais operações que devem ser realizadas respeitando determinada ordem. Para encontrar sempre um mesmo valor quando calculamos uma expressão numérica, usamos regras que definem a ordem que as operações serão feitas.
```
12 + 3 * 5 = 27
2 * ( 5 - 1 ) = 8
2^2 + 8 / 2 = 8
2^( 3 - 1) = 4
```
E assim por diante.

## INSTRUÇÕES:
Este desafio consiste em:
* Ler um arquivo de números (abaixo), contendo uma expressão por linha.
* Imprimir o resultado numérico da expressão.
* Se o programa encontrar um divisão por zero deverá imprimir ERR DIVBYZERO.
* Se o programa encontrar um erro de sintaxe na expressão deverá imprimir ERR SYNTAX.
* Não deverão ser usadas bibliotecas externas para trabalho com expressões numéricas.

## EXEMPLO:
Considere a lista de números:
```
1 + 3
2 - 3 * 2
2 ^ 3 / 4
0 * 5 * (4 + 1)
5 + 5 / 0
5 + + 1
5 + ( 465 + 1
```
A saída deverá ser:
```
4
-4
2
0
ERR DIVBYZERO
ERR SYNTAX
ERR SYNTAX
```

## VALIDAÇÃO: 
* Baixe o [arquivo de dados](https://osprogramadores.com/files/d14/d14.txt.gz).
* Descompacte o arquivo com gzip -d d14.txt.gz.
* Rode o seu programa usando o arquivo de dados como entrada (d14.txt)
* Quanto estiver razoavelmente satisfeito com os resultados, visite a página de validação de desafios. Escolha o número do desafio, digite o seu usuário no Github e cole a sua solução.
* Se tudo estiver OK, a página de validação emitirá um token. Crie um arquivo texto chamado .valid no diretório da sua solução contendo o token na primeira linha. Adicione esse arquivo ao commit com a solução e envie o PR.
* Ao enviar o PR, clique na página do PR e verifique se todos os testes passaram. Clique no link Details na página do teste em caso de falha.

