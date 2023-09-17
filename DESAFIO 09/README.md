# DESAFIO 09: BIG BASE!
## Descrição 
Escreva um programa que leia um arquivo texto contendo uma lista de três numeros por linha: base_entrada, base_saida e numero_entrada e imprima o número fornecido (já na base de entrada) convertido para a base de saída.

O formato exato da entrada é:
```
base_entrada base_saida numero_entrada
```

* Exemplo:
```
10 16 1500
36 10 GOODBYE
36 16 HELLOWORLD
10 2 32452867
2 10 1234
```

* Exemplo de saida para a entrada acima:
```
5DC
36320638406
647B8839EB1B1
1111011110011000100000011
???
```

## Considerações importantes:
* O programa deverá converter de qualquer base entre 2 e 62 para qualquer outra entre 2 e 62.
* Imprima ??? caso um dos seguintes erros tenha sido detectado:
Base inválida (tanto a base de entrada quanto a de saída devem estar entre 2 e 62, inclusive).
* Número negativo.
* Número muito grande (ver considerações sobre limite abaixo).
* Número inválido para a base especificada.
* Para conversões acima de bases acima de 10, use o seguinte conjunto de caracteres: 
```
0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz (z = 61). 
```
* Observe que com isso, todas as conversões para hexadecimal usam letras maísculas.
* O programa deve lidar com numeros grandes. O limite superior deverá ser o equivalente a ‘zzzzzzzzzzzzzzzzzzzzzzzzzzzzzz’, em base 62.
* Escreva o algoritmo. Não use as rotinas de conversão da sua linguagem preferida, se ela já possuir.

## Validação. 
* Baixe o arquivo de teste.
* Descompacte o arquivo localmente com gzip -d baseconv.txt.gz.
* Rode o seu programa usando o arquivo como entrada.
* Quanto estiver razoavelmente satisfeito com os resultados, visite a página de validação de desafios. Escolha o número do desafio, digite o seu usuário no Github e cole a sua solução.
* Se tudo estiver OK, a página de validação emitirá um token. * Crie um arquivo texto chamado .valid no diretório da sua solução contendo o token na primeira linha. 
* Adicione esse arquivo ao commit com a solução e envie o PR.
* Ao enviar o PR, clique na página do PR e verifique se todos os testes passaram. 
* Clique no link Details na página do teste em caso de falha.

## Dificuldade 
Fácil

## Pontuação 
30 pontos.

## Enviando os resultados 
* Teste o seu programa localmente e verifique que está operando de forma desejada.
* Se o desafio necessitar de validação (desafio-08 em diante), siga os procedimentos de validação descritos acima.
* Crie um Pull Request (PR) seguindo as instruções na documentação no repositório op-desafios.
* Envie o PR para revisão. Um dos admins irá aprovar o PR ou requisitar modificações.
* Após o PR ter sido aprovado, a pontuação será automaticamente contabilizada na página de hi-scores a cada 15 minutos.

* [SAIBA MAIS](https://osprogramadores.com/desafios/d09/)