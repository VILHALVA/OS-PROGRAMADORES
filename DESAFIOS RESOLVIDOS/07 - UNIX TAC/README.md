# [DESAFIO 07: UNIX TAC](https://osprogramadores.com/desafios/d07/)

## TAC:
Em Unix (e Linux), o comando cat mostra o conteúdo de um arquivo texto na saída padrão. Um comando similar (e menos conhecido) é o tac, que exibe um arquivo texto invertendo as linhas (da última para a primeira).

## DESAFIO: 
Implemente o comando tac na sua linguagem e bibliotecas preferidas. Condições de funcionamento:

O programa deve ler um arquivo do disco especificado na linha de comando e imprimir o arquivo linha a linha, começando pela última linha e terminando na primeira. Ex:
```
$ cat arquivo
Essa é a primeira linha
Essa é a segunda linha
Essa é a terceira linha
Essa é a última linha

$ tac arquivo
Essa é a última linha
Essa é a terceira linha
Essa é a segunda linha
Essa é a primeira linha
```

O programa deve ler arquivos de qualquer tamanho e funcionar com um limite de 512MB de memória (ler o arquivo inteiro em memória não é uma alternativa viável).

## VERIFICAÇÃO:
* Se estiver rodando em Linux, use ulimit -v 524288 antes de rodar o seu programa. Este comando limita a quantidade de memória que pode ser alocada nesta sessão para 512M. O seu programa deve funcionar com arquivos de qualquer tamanho nestas condições.

* Baixe o [arquivo de teste](https://osprogramadores.com/files/d07/1GB.txt.gz).
* Descompacte o arquivo localmente com gzip -d 1GB.txt.gz.

* Rode o seu programa usando o arquivo como entrada e verifique o md5sum:

* `$ seu_programa 1GB.txt | md5sum
2b4fd25f11d75c285ec69ecac420bd07`
Preste especial atençao ao md5sum que deve ser idêntico ao md5sum acima.
