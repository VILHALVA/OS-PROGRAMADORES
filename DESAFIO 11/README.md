# DESAFIO 11: PRIMOS EM PI

## Introdução 
O número pi (π) é uma das mais famosas e mais facilmente reconhecidas constantes matemáticas. Originalmente definido como o resultado da divisão da circunferência de um círculo pelo seu diâmetro, π é um número irracional e a sua representação decimal é infinita e não se repete.

## Instruções 
Este desafio consiste em encontrar a sequência mais longa de números primos (entre 2 e 9973) no primeiro 1 milhão de casas decimais de π.

## Em detalhes:
* Localize a sequência mais longa (em dígitos) de números primos nas casas decimais de π no arquivo fornecido (1 milhão de casas decimais).
* Em caso de mais de uma sequência do mesmo tamanho, a sequência com o início mais próximo do ponto decimal deverá ser utilizada.
* Apenas números primos entre 2 e 9973 deverão ser considerados na busca (basicamente, números primos contendo de um a quatro dígitos).

## Exemplo 
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

## Formato de saída 
Imprima uma linha contendo a maior sequência encontrada, sem espaços. Exemplo:
```
4159265358979323
```

## Validação 
* Baixe o arquivo de dados.
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

## Agradecimentos 
* Adriano Roberto de Lima pela sua valiosa ajuda e verificação dos resultados.

## Dificuldade 
Médio

## Pontuação 
60 pontos.

## Enviando os resultados 
* Teste o seu programa localmente e verifique que está operando de forma desejada.
* Se o desafio necessitar de validação (desafio-08 em diante), siga os procedimentos de validação descritos acima.
* Crie um Pull Request (PR) seguindo as instruções na documentação no repositório op-desafios.
* Envie o PR para revisão. Um dos admins irá aprovar o PR ou requisitar modificações.
* Após o PR ter sido aprovado, a pontuação será automaticamente contabilizada na página de hi-scores a cada 15 minutos.

* [SAIBA MAIS](https://osprogramadores.com/desafios/d11/)