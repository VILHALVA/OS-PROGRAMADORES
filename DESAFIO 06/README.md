# DESAFIO 06: ANAGRAMAS

## Anagramas!
Um anagrama é uma palavra ou frase formada com o re-arranjo de todas as letras de uma outra palavra ou frase (sem sobra ou falta). Exemplos:

* A palavra barco é um anagrama da palavra cobra (todas as letras de “cobra” usadas em “barco).
* A palavra mar não é um anagrama da palavra roma (a letra “o” em “roma” não foi usada).
* A palavra sal não é um anagrama da palavra mal (a letra “s” de “sal” não existe em “mal”).

## O problema 
Escreva um programa na sua linguagem e bibliotecas preferidas que:

* Leia a expressão (que pode ser uma frase ou apenas uma palavra) a ser usada para a criação dos anagramas da linha de comando. 
* Apenas as letras de “A” a “Z” deverão ser consideradas (ignore espaços e converta todas as letras minúsculas para maíusculas). 
* Retorne erro e aborte a execução se caracteres inválidos forem encontrados na expressão (qualquer caracter não alfabético que não seja espaço, incluindo números, pontuação, ou caracteres acentuados).
* Leia uma lista de palavras válidas do arquivo words.txt (Download). O arquivo é formatado com uma palavra por linha, com palavras da língua inglesa (Nota: apesar de várias tentativas, o autor não conseguiu achar uma lista “limpa” de palavras da língua portuguesa).
* Imprima todas as combinações possíveis de anagramas (sem repetição de linhas ou palavras). Os anagramas devem conter apenas palavras válidas (lidas do arquivo acima).
* O formato de saída deve conter múltiplas linhas (uma por anagrama), com as palavras ordenadas dentro de cada linha (veja Exemplos abaixo).
* O programa deve ser capaz de calcular e imprimir a lista de anagramas possíveis para uma expressão de até 16 caracteres em menos de 60 segundos.

## Exemplos:
Expressão é uma palavra:
```
$ ./anagramarama "vermelho"
ELM HO REV
ELM OH REV
OHM REVEL
LEVER OHM
ELM HOVER
HOLM VEER
HELM OVER
HELM ROVE
```

Expressão é uma frase (lembre-se de ignorar espaços e converter todas as letras para maiúsculas):
```
$ ./anagramarama "oi gente"
GO I TEEN
GENE I TO
GET I ONE
EON GET I
ENG I TOE
GEE I TON
GEE I NOT
EGO I NET
EGO I TEN
GEE IT NO
GEE IT ON
GO IN TEE
GEE IN TO
GENIE TO
GONE TIE
GEE OINT
GEE INTO
GEE TONI
GINO TEE
GENE ITO
EGO TINE
```

## Dicas 
* Novamente: Por razões de simplicidade, apenas caracteres alfabéticos devem ser considerados (A-Z apenas, excluindo números, pontuação, e caracteres acentuados).
* Esse problema é um caso clássico para um algoritmo recursivo.
Tentativas usando força bruta não vão funcionar.
* Esse desafio pode ser considerado como um desafio médio/difícil. Discuta dúvidas com os administradores e outros participantes no grupo OsProgramadores do Telegram.

## Pontuação 
70 pontos.

## Enviando os resultados 
* Teste o seu programa localmente e verifique que está operando de forma desejada.
* Se o desafio necessitar de validação (desafio-08 em diante), siga os procedimentos de validação descritos acima.
* Crie um Pull Request (PR) seguindo as instruções na documentação no repositório op-desafios.
* Envie o PR para revisão. Um dos admins irá aprovar o PR ou requisitar modificações.
* Após o PR ter sido aprovado, a pontuação será automaticamente contabilizada na página de hi-scores a cada 15 minutos.

* [SAIBA MAIS](https://osprogramadores.com/desafios/d06/)