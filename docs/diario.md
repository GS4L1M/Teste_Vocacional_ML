# Diário de decisões

Registro das decisões tomadas ao longo do projeto e do motivo de cada uma. A ideia é poder explicar, a qualquer momento, por que o projeto está do jeito que está.

## 29/09/2026 - Planejamento

**Premissa do projeto.** A ideia inicial era usar premissas como "pessoas antissociais tendem a fazer TI". Descartei por ser estereótipo, sem base científica. Adotei o modelo RIASEC de Holland, que é o padrão em orientação vocacional e tem seis dimensões de interesse.

**Base de treino.** As bases nacionais (INEP, e-MEC) dizem quantas pessoas se formam em cada curso, mas não trazem nada sobre o perfil delas. Para treinar um modelo supervisionado é preciso ter, para cada pessoa, o perfil e o curso escolhido. O dataset RIASEC do Open Psychometrics tem as duas coisas. As bases brasileiras ficam como contexto.

**O que prever.** Áreas de formação, e não o curso exato. Prever entre centenas de cursos seria inviável e pouco útil. O sistema vai recomendar as 3 áreas mais compatíveis, então a métrica principal será a acurácia top-3.

**Organização.** Um notebook por etapa da pipeline (coleta, limpeza, EDA, modelagem, avaliação). Os projetos do curso usam um notebook só, mas este projeto vai ter várias fontes de dados e uma limpeza longa. Separar deixa cada arquivo com um objetivo claro e permite rodar só a etapa em que estou trabalhando. Regra adotada: no 01 descubro o problema, no 02 resolvo.

**Ambiente.** Ambiente virtual `.venv` criado manualmente, com Python 3.14. O pandas instalado é a versão 3, e o material do curso usa a 2. Algumas diferenças podem aparecer (por exemplo, texto agora tem o tipo `str` em vez de `object`).

## 29/09/2026 - Coleta (01_coleta)

**Separador.** O `data.csv` usa TAB como separador (`sep='\t'`).

**Tradução do codebook.** Traduzi o dicionário de dados para português (`docs/codebook_ptbr.md`), mantendo o original intacto. Serve para quem não domina o inglês e porque as 48 perguntas RIASEC traduzidas vão virar as perguntas do formulário do site.

**Coluna fantasma.** A coluna `Unnamed: 93` aparece porque cada linha do arquivo termina com um TAB sobrando. Antes de apagar, investiguei: havia um único valor, o curso *economics* de um participante russo, deslocado porque ele digitou um TAB antes do nome. Lição: nunca apagar sem olhar o que está sendo apagado.

**Funções: print ou return.** Escrevi duas versões da função de porcentagem de ausentes. A com `print` só mostra o valor; a com `return` devolve o valor para ser usado no código (por exemplo, num `if`). Na maioria dos casos, a versão com `return` é mais útil.

## 29/09/2026 - Limpeza (02_limpeza)

**Nomes das colunas.** Traduzidos para português, em minúsculas, sem acento e com `_` entre as palavras. As colunas de códigos (`R1` a `C8`, `TIPI`, `VCL`) mantiveram o nome, porque são siglas de instrumentos científicos. Dois nomes merecem nota:
- `urban` virou `area_infancia`, porque a pergunta é sobre onde a pessoa morava quando criança.
- `familysize` virou `qtd_irmaos`. A pergunta conta os filhos da mãe incluindo a própria pessoa, então 1 significa filho único.

**Zeros nas perguntas RIASEC.** A escala do codebook vai de 1 a 5, e o 0 significa pergunta não respondida.
- 73% de quem deixou perguntas em branco deixou só uma. 61 pessoas não responderam nenhuma.
- Removi quem deixou 5 ou mais em branco (mais de 10% do teste). O corte custou só 361 pessoas (0,25%).
- Nos demais, o 0 virou `NaN`. Se ficasse como 0, entraria na média como se fosse uma nota muito baixa.

**Hipótese de gênero.** Achei que as mulheres deixariam mais em branco as perguntas de trabalho manual. Os dados mostraram o contrário: os homens deixam mais perguntas em branco, em todas as dimensões. Porém as mulheres marcam "não gosto" com mais frequência nas perguntas Realistas (54% contra 31%). Isso não é defeito dos dados, é o teste medindo interesses. Mas é um risco de viés no modelo, então:
- `genero` não será usado como variável de entrada;
- o desempenho será avaliado separadamente por gênero.

**Perguntas mais puladas.** Operar uma máquina retificadora, reger um coral, vender franquias. O ponto em comum é serem atividades pouco familiares. Vou reescrevê-las com mais clareza na versão brasileira do formulário.

**Palavras inventadas.** O próprio codebook avisa que `VCL6`, `VCL9` e `VCL12` são palavras que não existem. Cerca de 20% das pessoas marcaram pelo menos uma. Cortar em 1 descartaria muita gente, e marcar uma palavra pode ser confusão com outra parecida. Removi quem marcou 2 ou mais (7.283 pessoas).

**Idade e irmãos inválidos.** Idades como 666, 1997 e 2.147.483.647 (o maior inteiro de 32 bits). Essas colunas não entram no modelo, então não removi as pessoas: só troquei o valor inválido por `NaN`. Apagar a linha jogaria fora 48 respostas boas por causa de uma idade mal digitada. Faixas válidas: idade de 13 a 100 e irmãos de 1 a 20.

**Duplicatas.** Nenhuma linha idêntica. A coluna `rede_unica = 2` indica rede compartilhada (escolas, empresas), não duplicata, então esses registros foram mantidos.

**Curso.** Mantive só quem informou o curso, que é o alvo do modelo (aprendizado supervisionado precisa do rótulo). O texto foi padronizado (minúsculas, só letras) e agrupado nas 10 áreas gerais da CINE Brasil por regras de palavras-chave (expressões regulares). A ordem das regras importa: a primeira que combinar define a área. Cerca de 5% dos cursos não foram reconhecidos e ficaram de fora.

**Escores RIASEC.** Cada dimensão recebe a média das perguntas que a pessoa respondeu. Não preenchi as lacunas com a média geral, porque isso colocaria a opinião média de milhares de pessoas dentro do perfil de um indivíduo. No site, o cálculo será o mesmo, garantindo que o modelo receba os dados do jeito que recebeu no treino.

**Resultado.** 81.692 participantes, de 145.828 no início.

**Pontos em aberto para a modelagem.**
- As áreas Serviços (192) e Agricultura e veterinária (141) têm poucos exemplos. Decidir se junto, removo ou mantenho.
- A área de Ciências sociais tem 23 mil participantes (muita psicologia). A base está desbalanceada, o que reforça o uso de F1 macro na avaliação.

## 29/09/2026 - Organização

- As funções escritas nos notebooks foram movidas para `src/limpeza.py` e passaram a ser importadas.
- Criados `.gitignore` (sem o ambiente virtual e sem os CSVs) e `requirements.txt`.
