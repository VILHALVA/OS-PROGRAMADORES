# [DESAFIO 11: PRIMOS EM PI](https://osprogramadores.com/desafios/d11/)

## INTRODUÇÃO:
O número pi (π) é uma das mais famosas e mais facilmente reconhecidas constantes matemáticas. Originalmente definido como o resultado da divisão da circunferência de um círculo pelo seu diâmetro, π é um número irracional e a sua representação decimal é infinita e não se repete.

## INSTRUÇÕES:
Este desafio consiste em encontrar a sequência mais longa de números primos (entre 2 e 9973) no primeiro 1 milhão de casas decimais de π.

## EM DETALHES:
* Localize a sequência mais longa (em dígitos) de números primos nas casas decimais de π no arquivo fornecido (1 milhão de casas decimais).
* Em caso de mais de uma sequência do mesmo tamanho, a sequência com o início mais próximo do ponto decimal deverá ser utilizada.
* Apenas números primos entre 2 e 9973 deverão ser considerados na busca (basicamente, números primos contendo de um a quatro dígitos).

## EXEMPLO: 
Considere π com 20 decimais:
```
3.14159265358979323846
```

Neste caso, a maior sequência de numeros primos seria:
```
41 59 2 653 5 89 7 9323
```

Que resulta na sequência:
```
4159265358979323
```

## FORMATO DE SAIDA:
Imprima uma linha contendo a maior sequência encontrada, sem espaços. Exemplo:
```
4159265358979323
```

## VALIDAÇÃO:
* [Baixe o arquivo de dados](https://osprogramadores.com/files/d11/pi-1M.tar.gz).
* Descompacte o arquivo localmente com tar zxvf pi-1M.tar.gz.
* Rode o seu programa usando o arquivo de dados como entrada (pi-1M.txt)
* Dica: (Linux) Use o comando “cut” para produzir arquivos menores e testar o seu programa. Por exemplo, para produzir um arquivo chamado pi-1000.txt com as primeiras 1000 casas decimais de π, use:
```
$ cut -c1-1001 <pi-1M.txt >pi-1000.txt
```
Onde 1001 representa o número de decimais desejadas + 1.

* Quanto estiver razoavelmente satisfeito com os resultados, visite a página de validação de desafios. Escolha o número do desafio, digite o seu usuário no Github e cole a sua solução.
* Se tudo estiver OK, a página de validação emitirá um token. Crie um arquivo texto chamado .valid no diretório da sua solução contendo o token na primeira linha. Adicione esse arquivo ao commit com a solução e envie o PR.

* Ao enviar o PR, clique na página do PR e verifique se todos os testes passaram. Clique no link Details na página do teste em caso de falha.


