# [DESAFIO 10: TURING MACHINE](https://osprogramadores.com/desafios/d10/)

## INTRODUÇÃO: 
Uma Máquina de Turing é um modelo computacional matemático que define uma máquina abstrata. Essa máquina manipula símbolos numa fita de papel de acordo com uma tabela de regras simples. Apesar da simplicidade do modelo, é possível construir uma Máquina de Turing capaz de simular qualquer algoritmo computacional.

## FUNCIONAMENTO: 
Uma máquina de Turing lê os dados de uma “fita” infinita, caracter por caracter (também conhecidos como “símbolos” na terminologia original) A máquina está sempre em um determinado “estado” (estado inicial == string “0”). As regras contém instruções para “casar” um determinado par estado/símbolo e executar determinadas ações.

O primeiro caracter a ser lido é sempre o primeiro caracter da “fita”, no nosso caso, o primeiro caracter do string de dados.

## AS REGRAS PERMITEM QUE:
* Determinada regra seja selecionada por estado corrente e símbolo.
* Uma vez selecionada uma regra, a máquina pode, opcionalmente executar uma (ou várias) das tarefas abaixo:

_ Gravar um novo símbolo na posição corrente.
_ Mover a posição de leitura para a direita.
_ Mover a posição de leitura para a esquerda.
_ Mudar o estado atual da máquina.

## EXEMPLO:
* Data a entrada:
```
A/B/C/D@
```
* E as regras:
```
1: state=0  simbolo=@  novo_simbolo=.  direção=*        novo_estado=halt
2: state=0  simbolo=*  novo_simbolo=*  direção=direita  novo_estado=0
3: state=0  simbolo=/  novo_simbolo=x  direção=direita  novo_estado=y
4: state=y  simbolo=@  novo_simbolo=.  direção=*        novo_estado=halt
5: state=y  simbolo=*  novo_simbolo=*  direção=direita  novo_estado=y
6: state=y  simbolo=/  novo_simbolo=y  direção=direita  novo_estado=0
```

* A seguinte saída seria produzida:
```
AxByCxD.
```

* O funcionamento pode ser detalhado da seguinte forma:
* A máquina inicializa, no estado “0” e lê o primeiro símbolo da fita (A)
* A regra 2 acima produz o melhor casamento. No caso, estado=“0” e símbolo=”*“ indicando “qualquer símbolo”.
* A regra 2 não faz qualquer substituição de símbolo, já que o novo símbolo é “*”. A posição na fita é movida para a direita de acordo com a instrução em “direção” e o estado permanece em “0”.
* As regras são re-executadas com o segundo símbolo (/), ainda em estado “0”.
* Dessa vez, a regra 3 casa mais especificamente (estado=“0”, símbolo = “/”).
* A regra 3 substitui o símbolo corrente na fita (“/”) por x, move a fita para a direita e muda o estado corrente para y
* O próximo caracter é lido (B)
* Dessa vez, a regra 5 é utilizada (estado=“y”, símbolo=”*”). A única ação concreta é mover a fita para a direita.
* Outro caracter é lido (/). Como o estado ainda é “y”, a regra 6 é executada. Dessa vez, troca o caracter por um “y”, move a fita para a direita e muda o estado para “0”.

## AS REGRAS SÃO EXECUTADAS ATÉ QUE:
* Uma combinação de estado/símbolo seja encontrada na fita que não existe nas regras. Nesse caso, o programa é abortado.
* Um estado chamado halt-<qualquer_coisa> seja encontrado. Este estado causa a finalização do programa após a execução das instruções contidas nesta regra.
* Observe que a fita é infinita, ou seja, pode crescer indefinidamente para a esquerda ou para a direita. Mover para a direita além do tamanho corrente dos dados causa a inserção de um espaço no final da fita. Mover a posição para e esquerda causa a inserção de um espaço a esquerda dos dados atuais.

## EXEMPLO:
* Antes: [ABCD], posição em D, mover a posição para a direita transforma a fita em [ABCD ].
* Antes: [ABCD], posição em A, mover a posição para a esquerda transforma a fita em [ ABCD].

## DESAFIO: 
Escreva um programa que leia dois arquivos: O primeiro contendo um “conjunto de regras” (o “programa”) e o segundo contendo o nome do arquivo de regras a ser usado e os dados. O programa deverá executar as regras usando os dados como entrada e emitir a saída no formato definido abaixo. Observe que o arquivo de dados contém o nome do arquivo de regras a ser usado para cada linha.

As próximas seções definem os formatos de entrada e saída em maiores detalhes.

## ARQUIVO DE DADOS:
O arquivo de dados contem apenas dois campos por linha, separados por uma vírgula. O primeiro campo especifica o nome do arquivo de regras a ser usado para os dados nessa linha, e o segundo especifica o dado em si.

## EXEMPLO:
```
prime.tur,101
prime.tur,102
pali.tur,1001001
```
No caso acima, o valor “101” deverá ser executado com as regras no arquivo prime.tur e os resultados impressos. Em seguida, execute prime.tur usando o valor 102, e finalmente, execute pali.tur usando o valor “1001001”.

## ARQUIVO DE REGRAS: 
O arquivo de regras define as regras a serem aplicadas, com uma regra por linha. Cada linha é composta por 5 campos, separados por um espaço, no seguinte formato:
```
current_state current_symbol new_symbol direction new_state
```

## ONDE:
* current_state & current_symbol: Esta regra só deverá ser executada se current_state casar com o estado corrente da máquina e current_symbol casar com o símbolo lido da fita de dados.
* O valor de current_state pode ser “*” indicando “case qualquer estado”.
* O valor de current_symbol pode ser “*”, indicando “case qualquer valor”.
* O valor de current_symbol pode ser “_” (underscore) para casar o espaço.
* No caso de duas regras com o mesmo current_state casando um símbolo de entrada, a mais específica deverá ser usada. * Exemplo típico: duas regras, uma com current_symbol=* e outra com current_symbol=A. No caso, para todos os valores de entrada, exceto “A”, a primeira regra deverá ser usada. Se o valor de entrada for “A”, a segunda deverá ser usada por ser mais específica.
* Caso existam duas regras genéricas (i.e, usando “*” no current_state ou current_symbol válidas, apenas a primeira deverá ser usada.
* new_symbol: Se a regra corrente for executada, substitua o símbolo corrente por este símbolo.

_ new_symbol=_ indica “troque por espaço”.
_ new_symbol=* indica “não substitua”.
_ direction: Pode ser “l” para “left” (esquerda), “r” para “right” (direita), ou “*” para indicar “não mova a posição”. 

Qualquer outro valor devera resultar em erro.

_ new_state: O novo estado da máquina. Pode ser qualquer valor alfanumérico. Qualquer string começando com halt causa a finalização do programa após a execução desta regra.

Linhas em branco ou começando com “;” devem ser ignoradas. Dados após um caracter “;” em qualquer posição da linha deve ser ignorados (comentários inline).

O exemplo dado na seção “Funcionamento” poderia ser representado no formato de regras como:
```
0 @ . * halt
0 * * r 0
0 / x r y
y @ . * halt
y * * r y
y / y r 0
```

## FORMATO DE SAÍDA:
Imprima uma linha contendo 3 campos, separados por vírgulas contendo:

## NOME DO ARQUIVO DE REGRAS UTILIZADO:
Valor de entrada
Valor de saída
Ex:
```
foo.tur,100,001
foo.tur,101,101
bar.tur,1001,:)
meh.tur,9999,ERR
```
Em caso de erro na saída, imprimir apenas “ERR” na coluna de resultado.

## VALIDAÇÃO: 
* Baixe o [arquivo contendo o arquivo de dados e os arquivos de regras](https://osprogramadores.com/files/d10/turing.tar.gz).
* Descompacte o arquivo localmente com tar zxvf turing.tar.gz.
* Rode o seu programa usando o arquivo de dados como entrada.
* Quanto estiver razoavelmente satisfeito com os resultados, visite a página de validação de desafios. Escolha o número do desafio, digite o seu usuário no Github e cole a sua solução.
* Se tudo estiver OK, a página de validação emitirá um token. Crie um arquivo texto chamado .valid no diretório da sua solução contendo o token na primeira linha. Adicione esse arquivo ao commit com a solução e envie o PR.
* Ao enviar o PR, clique na página do PR e verifique se todos os testes passaram. 
* Clique no link Details na página do teste em caso de falha.


