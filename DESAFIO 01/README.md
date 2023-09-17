# DESAFIO 01: Git básico
## Objetivo 
Neste desafio, o seu objetivo é adicionar o seu nome à lista de participantes do grupo no GitHub.

## Instruções 
1. Leia o tutorial sobre Git. Caso você use Windows, leia as instruções de instalação neste artigo. A documentação oficial do Git em português está disponível no site do Git.

2. Crie sua conta no GitHub (ou use uma conta previamente criada, se já existir).

3. Visite o projeto do site do grupo e faça o fork do projeto para a sua conta no GitHub clicando no botão Fork no canto superior direito da tela.

4. Instale o git na sua máquina. Se o seu Sistema Operacional (SO) já possui o git em um pacote pronto, é extremamente recomendável instalá-lo através dos comandos do seu SO.

5. Acesse a linha de comando (Windows) ou abra um terminal (Linux ou macOS).

6. Crie um diretório onde você deseja instalar o projeto do site.

7. Crie um clone do seu fork no github, na sua máquina. A opção --recursive é importante neste caso:

git clone --recursive https://github.com/<seu usuário do GitHub>/op-website-hugo.git
Crie um remote apontando pro repositório original:

8. git remote add upstream https://github.com/osprogramadores/op-website-hugo.git

9. Crie um branch de trabalho com o commando:
git checkout -b desafio
Adicione os seus dados ao arquivo PARTICIPANTES.md, usando o seu editor favorito, e grave o arquivo. Dicas importantes:

10. Sugestões de Editores: vim, Visual Studio Code, NetBeans, Sublime Text and many others.

11. O arquivo é ordenado alfabeticamente por nome!

12. Mantenha a estrutura já existente no arquivo (adicione as barras verticais como nos casos já existentes).
Use apenas espaços (não tabs).

13. Cuidado com espaços extras no final da linha.

14. As suas alterações serão automaticamente rejeitadas se as condições acima não forem observadas.

15. Encerre o seu editor e retorne para a linha de comando do Windows, macOS ou Linux:
Digite o comando git status e pressione enter ou return no teclado.

16. O git irá exibir uma mensagem semelhante a: modified: PARTICIPANTES.md

17. Use o comando git add nome-arquivo onde nome-arquivo deve ser substituído pelo nome do arquivo que foi modificado (incluindo o path/caminho para o arquivo).

18. Confirme suas modificações com o comando git commit -m "Mensagem aqui". A mensagem deverá se limitar a 60 caracteres. Use sentenças completas (começando com uma letra maiúscula e terminando com um ponto). O texto deve ser sucinto e descritivo. Exemplos de boas e más descrições:

* Inclusao: Ruim, pois não possui detalhes suficientes.
include de participante: Ruim. Não começa com maiúscula, sem pontuação, informação insuficiente.
* particpantes.md: Ruim. Não descritivo. Nome do arquivo errado.
* Inclusão de participante: @seuusername.: Bom exemplo.

19. Envie suas modificações para o seu fork usando comando git push origin desafio.

20. Acesse o fork do repositório op-website-hugo na sua conta do GitHub e solicite um Pull Request para o repositório do OsProgramadores

21. Visite a página do Pull Request e aguarde a validação automática da sua solução. Em caso de erros clique no link Details e efetue o conserto. Nesses casos:

22. Faça a atualização do seu repositório local com git pull -r upstream master. Não há risco de perder as suas alterações com esse comando.
Se o git indicar conflito, edite novamente o arquivo PARTICIPANTES.md e remova o conflito. Observe que nesses casos o git coloca marcadores de conflito no arquivo, que também devem ser removidos.

23. Edite o arquivo e conserte o problema indicado pela validação automática.

24. Crie outro commit com git commit -m "Mensagem aqui" e use uma descrição adequada (ex: Conserto de problema X.)
Envie o commit para o seu fork com git push origin desafio.
Importante: Não é necessário (ou recomendável) fechar o PR e reabrir.

25. Repita o processo: Verifique se a validação automática finalizou a checagem sem problemas. Em caso de problemas, repita os passos acima.

26. Aguarde a resposta dos admins. É importante prestar atenção aos comentários feitos pelos admins e corrigir eventuais problemas. Observe que Pull Requests (PRs) inativos por duas semanas serão automaticamente fechados.

27. Quando o seu PR tiver sido aceito (status = Merged no github), remova o branch criado com git checkout master seguido de git branch -d desafio.

Nível de dificuldade: Fácil. 

* [SAIBA MAIS](https://osprogramadores.com/desafios/d01/)
