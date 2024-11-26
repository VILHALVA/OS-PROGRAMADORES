# [DESAFIO 08: FRAÇÕES SIMPLES](https://osprogramadores.com/desafios/d08/)

## DESAFIO: 
Escreva um programa que leia um arquivo texto contendo uma lista de frações em ASCII (uma por linha) e produza na saída a versão simplificada de cada fração. Números simples assumem denominador 1 (apenas imprima o número). Divisões inteiras como 81/9 devem imprimir o número inteiro 9. Em caso de erros na entrada (como divisão por zero), imprima “ERR” em maíusculas.

Por exemplo, data a entrada abaixo:
```
14/3
3/8
4/8
4/3
5
10/0
48/12
```

A seguinte saída seria produzida:
```
4 2/3
3/8
1/2
1 1/3
5
ERR
4
```

## VALIDAÇÃO:
* Baixe o [arquivo de teste](https://osprogramadores.com/files/d08/frac.txt.gz).
* Descompacte o arquivo localmente com gzip -d frac.txt.gz.
* Rode o seu programa usando o arquivo como entrada.
* Quanto estiver razoavelmente satisfeito com os resultados, visite a página de validação de desafios. 
* Escolha o número do desafio, digite o seu usuário no Github e cole a sua solução.
* Se tudo estiver OK, a página de validação emitirá um token. 
* Crie um arquivo texto chamado .valid no diretório da sua solução contendo o token na primeira linha. 
* Adicione esse arquivo ao commit com a solução e envie o PR.
* Ao enviar o PR, clique na página do PR e verifique se todos os testes passaram. 
* Clique no link Details na página do teste em caso de falha.
* Não será permitido o uso de bibliotecas externas que auxiliam no processamento de frações, como o módulo `fractions` do Python ou a biblioteca `fraction.js`.

