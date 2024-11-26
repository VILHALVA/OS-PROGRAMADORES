# [DESAFIO 12: POTÊNCIAS DE 2](https://osprogramadores.com/desafios/d12/)

## INTRODUÇÃO:
A base 2 é uma das bases mais usadas em computação. Números nessa base são representados pela equação 2^n. Exemplo:
```
2^0 = 1
2^1 = 2
2^2 = 4
2^3 = 8
```
E assim por diante.

## INSTRUÇÕES:
Este desafio consiste em:
* Ler um arquivo de números (abaixo), contendo um número por linha.
* Se o número for uma potência de 2, imprimir o número seguido de true e o expoente ao qual se deve elevar 2 para obter o número.
* Se o número não for uma potência de 2, imprimir o número seguido de false.

## EXEMPLO: 
Considere a lista de números:
```
1
140
128
137
65535
65536
17179869184
```
A saída deverá ser:
```
1 true 0
140 false
128 true 7
137 false
65535 false
65536 true 16
17179869184 true 34
```

## VALIDAÇÃO:
* [Baixe o arquivo de dados](https://osprogramadores.com/files/d12/d12.txt.gz).
* Descomprima o arquivo usando gzip -d d12.txt.gz (ou outro programa que suporte o formato gzip).
* Rode o seu programa usando o arquivo de dados como entrada (d12.txt)
* Quanto estiver razoavelmente satisfeito com os resultados, visite a página de validação de desafios. Escolha o número do desafio, digite o seu usuário no Github e cole a sua solução.
* Se tudo estiver OK, a página de validação emitirá um token. Crie um arquivo texto chamado .valid no diretório da sua solução contendo o token na primeira linha. Adicione esse arquivo ao commit com a solução e envie o PR.
* Ao enviar o PR, clique na página do PR e verifique se todos os testes passaram. Clique no link Details na página do teste em caso de falha.

