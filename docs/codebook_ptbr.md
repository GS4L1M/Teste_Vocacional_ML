# Codebook do Dataset RIASEC (tradução para português)

> **Fonte original:** [Open Psychometrics - Raw Data](https://openpsychometrics.org/_rawdata/) - arquivo `codebook.txt` do dataset *"Answers to the Holland Code (RIASEC) Test"*.
>
> **Tradução livre** feita para fins educacionais por Gustavo Salim, no projeto *Teste Vocacional com Machine Learning*. O arquivo original, em inglês, permanece intacto em `dados/Dados originais/codebook.txt`.
>
> **Licença:** consulte a licença de uso dos dados na página de origem do Open Psychometrics antes de qualquer reutilização.

---

## Sobre a coleta

Os dados foram coletados entre **2015 e 2018** por meio de um teste RIASEC / Código de Holland online, que os usuários da internet acessavam para obter resultados personalizados.

O teste tinha **uma página com os 48 itens** usados para calcular as escalas RIASEC. Numa segunda página, os participantes eram convidados a responder uma **pesquisa adicional opcional**. Este dataset contém **todas as pessoas que aceitaram** responder essa pesquisa.

A única exclusão feita pelos autores foi a de pessoas que informaram **idade menor que 13 anos**. Por isso, os dados **podem exigir uma limpeza significativa**.

---

## 1. Itens RIASEC (colunas `R1` a `C8`)

Cada item foi avaliado numa escala de **1 a 5**, indicando o quanto a pessoa **gostaria de realizar** aquela tarefa:

| Valor | Original | Tradução |
|---|---|---|
| 1 | Dislike | Não gosto |
| 3 | Neutral | Neutro |
| 5 | Enjoy | Gosto muito |

> Os valores 2 e 4 não tinham rótulo; são intermediários.

### R - Realista (atividades práticas, máquinas, ferramentas)

| Coluna | Original | Tradução |
|---|---|---|
| R1 | Test the quality of parts before shipment | Testar a qualidade de peças antes do envio |
| R2 | Lay brick or tile | Assentar tijolos ou azulejos |
| R3 | Work on an offshore oil-drilling rig | Trabalhar numa plataforma de petróleo em alto-mar |
| R4 | Assemble electronic parts | Montar componentes eletrônicos |
| R5 | Operate a grinding machine in a factory | Operar uma máquina retificadora numa fábrica |
| R6 | Fix a broken faucet | Consertar uma torneira quebrada |
| R7 | Assemble products in a factory | Montar produtos numa fábrica |
| R8 | Install flooring in houses | Instalar pisos em casas |

### I - Investigativo (pesquisa, análise, ciência)

| Coluna | Original | Tradução |
|---|---|---|
| I1 | Study the structure of the human body | Estudar a estrutura do corpo humano |
| I2 | Study animal behavior | Estudar o comportamento dos animais |
| I3 | Do research on plants or animals | Fazer pesquisas sobre plantas ou animais |
| I4 | Develop a new medical treatment or procedure | Desenvolver um novo tratamento ou procedimento médico |
| I5 | Conduct biological research | Realizar pesquisas biológicas |
| I6 | Study whales and other types of marine life | Estudar baleias e outras formas de vida marinha |
| I7 | Work in a biology lab | Trabalhar num laboratório de biologia |
| I8 | Make a map of the bottom of an ocean | Fazer um mapa do fundo do oceano |

### A - Artístico (criação, expressão, arte)

| Coluna | Original | Tradução |
|---|---|---|
| A1 | Conduct a musical choir | Reger um coral |
| A2 | Direct a play | Dirigir uma peça de teatro |
| A3 | Design artwork for magazines | Criar artes para revistas |
| A4 | Write a song | Compor uma música |
| A5 | Write books or plays | Escrever livros ou peças de teatro |
| A6 | Play a musical instrument | Tocar um instrumento musical |
| A7 | Perform stunts for a movie or television show | Fazer cenas de ação (dublê) para cinema ou TV |
| A8 | Design sets for plays | Criar cenários para peças de teatro |

### S - Social (ajudar, ensinar, cuidar)

| Coluna | Original | Tradução |
|---|---|---|
| S1 | Give career guidance to people | Dar orientação profissional às pessoas |
| S2 | Do volunteer work at a non-profit organization | Fazer trabalho voluntário numa ONG |
| S3 | Help people who have problems with drugs or alcohol | Ajudar pessoas com problemas com drogas ou álcool |
| S4 | Teach an individual an exercise routine | Ensinar uma rotina de exercícios a uma pessoa |
| S5 | Help people with family-related problems | Ajudar pessoas com problemas familiares |
| S6 | Supervise the activities of children at a camp | Supervisionar atividades de crianças num acampamento |
| S7 | Teach children how to read | Ensinar crianças a ler |
| S8 | Help elderly people with their daily activities | Ajudar idosos em suas atividades diárias |

### E - Empreendedor (liderar, vender, negociar)

| Coluna | Original | Tradução |
|---|---|---|
| E1 | Sell restaurant franchises to individuals | Vender franquias de restaurantes |
| E2 | Sell merchandise at a department store | Vender produtos numa loja de departamentos |
| E3 | Manage the operations of a hotel | Gerenciar as operações de um hotel |
| E4 | Operate a beauty salon or barber shop | Administrar um salão de beleza ou barbearia |
| E5 | Manage a department within a large company | Gerenciar um departamento numa grande empresa |
| E6 | Manage a clothing store | Gerenciar uma loja de roupas |
| E7 | Sell houses | Vender imóveis |
| E8 | Run a toy store | Administrar uma loja de brinquedos |

### C - Convencional (organização, dados, rotinas)

| Coluna | Original | Tradução |
|---|---|---|
| C1 | Generate the monthly payroll checks for an office | Gerar a folha de pagamento mensal de um escritório |
| C2 | Inventory supplies using a hand-held computer | Fazer o inventário de materiais usando um coletor de dados portátil |
| C3 | Use a computer program to generate customer bills | Usar um programa de computador para emitir cobranças de clientes |
| C4 | Maintain employee records | Manter os registros (cadastros) de funcionários |
| C5 | Compute and record statistical and other numerical data | Calcular e registrar dados estatísticos e numéricos |
| C6 | Operate a calculator | Operar uma calculadora |
| C7 | Handle customers' bank transactions | Realizar transações bancárias de clientes |
| C8 | Keep shipping and receiving records | Manter registros de expedição e recebimento de mercadorias |

---

## 2. Tempos de resposta (medidos no servidor)

| Coluna | Original | Tradução |
|---|---|---|
| introelapse | The time spent on the introduction/landing page (in seconds) | Tempo gasto na página de introdução (em segundos) |
| testelapse | The time spent on all the RIASEC questions | Tempo gasto em todas as perguntas RIASEC (deveria equivaler à soma do tempo de cada pergunta) |
| surveyelapse | The time spent answering the supplemental demographic survey | Tempo gasto respondendo a pesquisa demográfica complementar |

---

## 3. TIPI - Inventário de Personalidade de Dez Itens (colunas `TIPI1` a `TIPI10`)

Mede os **Cinco Grandes Fatores de personalidade** (*Big Five*) de forma resumida.

> Referência: Gosling, S. D., Rentfrow, P. J., & Swann, W. B., Jr. (2003). *A Very Brief Measure of the Big Five Personality Domains*. Journal of Research in Personality, 37, 504-528.

Cada item completa a frase **"Eu me vejo como:"** *(I see myself as:)*

| Coluna | Original | Tradução |
|---|---|---|
| TIPI1 | Extraverted, enthusiastic. | Extrovertido, entusiasmado. |
| TIPI2 | Critical, quarrelsome. | Crítico, briguento. |
| TIPI3 | Dependable, self-disciplined. | Confiável, autodisciplinado. |
| TIPI4 | Anxious, easily upset. | Ansioso, facilmente irritável. |
| TIPI5 | Open to new experiences, complex. | Aberto a novas experiências, complexo. |
| TIPI6 | Reserved, quiet. | Reservado, quieto. |
| TIPI7 | Sympathetic, warm. | Compreensivo, afetuoso. |
| TIPI8 | Disorganized, careless. | Desorganizado, descuidado. |
| TIPI9 | Calm, emotionally stable. | Calmo, emocionalmente estável. |
| TIPI10 | Conventional, uncreative. | Convencional, pouco criativo. |

Escala de resposta:

| Valor | Original | Tradução |
|---|---|---|
| 1 | Disagree strongly | Discordo totalmente |
| 2 | Disagree moderately | Discordo moderadamente |
| 3 | Disagree a little | Discordo um pouco |
| 4 | Neither agree nor disagree | Nem concordo nem discordo |
| 5 | Agree a little | Concordo um pouco |
| 6 | Agree moderately | Concordo moderadamente |
| 7 | Agree strongly | Concordo totalmente |

---

## 4. VCL - Lista de Verificação de Vocabulário (colunas `VCL1` a `VCL16`)

Os itens foram apresentados como uma lista, com a instrução: **"Na grade abaixo, marque todas as palavras cuja definição você tem certeza que sabe"**.

- **1** = marcada
- **0** = não marcada

| Coluna | Palavra | Tradução |
|---|---|---|
| VCL1 | boat | barco |
| VCL2 | incoherent | incoerente |
| VCL3 | pallid | pálido |
| VCL4 | robot | robô |
| VCL5 | audible | audível |
| VCL6 | cuivocal | ⚠️ **palavra inventada** |
| VCL7 | paucity | escassez |
| VCL8 | epistemology | epistemologia |
| VCL9 | florted | ⚠️ **palavra inventada** |
| VCL10 | decide | decidir |
| VCL11 | pastiche | pastiche (imitação de estilo artístico) |
| VCL12 | verdid | ⚠️ **palavra inventada** |
| VCL13 | abysmal | abismal, péssimo |
| VCL14 | lucid | lúcido |
| VCL15 | betray | trair |
| VCL16 | funny | engraçado |

> ⚠️ **Verificação de validade:** as palavras de **VCL6, VCL9 e VCL12 não existem**. Quem marcou alguma delas afirmou conhecer uma palavra inventada, o que indica respostas desatentas ou pouco sinceras. Essas colunas podem ser usadas para **filtrar respostas inválidas** na etapa de limpeza.

---

## 5. Perguntas demográficas

| Coluna | Pergunta (tradução) | Valores |
|---|---|---|
| education | "Qual nível de escolaridade você concluiu?" | 1 = Menos que o ensino médio, 2 = Ensino médio, 3 = Graduação, 4 = Pós-graduação |
| urban | "Em que tipo de região você morava quando criança?" | 1 = Rural (interior/campo), 2 = Suburbana, 3 = Urbana (cidade) |
| gender | "Qual é o seu gênero?" | 1 = Masculino, 2 = Feminino, 3 = Outro |
| engnat | "O inglês é sua língua nativa?" | 1 = Sim, 2 = Não |
| age | "Quantos anos você tem?" | número (idade em anos) |
| hand | "Com qual mão você escreve?" | 1 = Direita, 2 = Esquerda, 3 = Ambas |
| religion | "Qual é a sua religião?" | 1 = Agnóstico, 2 = Ateu, 3 = Budista, 4 = Cristão (Católico), 5 = Cristão (Mórmon), 6 = Cristão (Protestante), 7 = Cristão (Outro), 8 = Hindu, 9 = Judeu, 10 = Muçulmano, 11 = Sikh, 12 = Outra |
| orientation | "Qual é a sua orientação sexual?" | 1 = Heterossexual, 2 = Bissexual, 3 = Homossexual, 4 = Assexual, 5 = Outra |
| race | "Qual é a sua raça/etnia?" | 1 = Asiático, 2 = Árabe, 3 = Negro, 4 = Indígena australiano / Nativo americano / Branco, 5 = Outra ⚠️ |
| voted | "Você votou numa eleição nacional no último ano?" | 1 = Sim, 2 = Não |
| married | "Qual é o seu estado civil?" | 1 = Nunca foi casado(a), 2 = Casado(a) atualmente, 3 = Já foi casado(a) |
| familysize | "Incluindo você, quantos filhos sua mãe teve?" | número |
| major | "Se você cursou uma universidade, qual foi o seu curso (ex.: "psicologia", "inglês", "engenharia civil")?" | **texto livre** |

> ⚠️ **race:** segundo os autores, houve um **erro de codificação** no questionário: três opções diferentes (indígena australiano, nativo americano e branco) receberam o **mesmo valor (4)**. Por isso, essa coluna não permite distinguir esses grupos.

---

## 6. Informações técnicas (calculadas pelos autores)

| Coluna | Tradução |
|---|---|
| uniqueNetworkLocation | **1** se o registro é o único vindo daquela rede (endereço de internet) no dataset; **2** se há mais de um. Pode haver mais de um registro da mesma rede quando ela é compartilhada (ex.: uma escola) ou quando a pessoa refez o teste. |
| country | País da rede de onde o usuário se conectou (código de 2 letras, ex.: `US`, `BR`). |
| source | Origem do acesso: **1** = veio do Google, **2** = veio de um link interno do site, **0** = veio de outro site ou não foi possível determinar. |

---

## 📝 Observações do tradutor (para a etapa de limpeza)

Pontos que **não estão no codebook**, mas foram observados na exploração dos dados (`01_coleta.ipynb`):

1. **Valor 0 nas respostas:** o codebook define a escala RIASEC de **1 a 5**, mas os dados têm valores **0**. Provavelmente indicam **pergunta não respondida**. A hipótese deve ser investigada.
2. **Coluna `Unnamed: 93`:** não existe no codebook. É uma coluna "fantasma" criada pelo TAB extra no final de cada linha do arquivo `data.csv`.
3. **`age` e `familysize`:** têm valores máximos absurdos (cerca de 2,1 bilhões), o que indica erros de digitação ou valores inválidos que precisarão de tratamento.
4. **`major`:** é texto livre, com muitas grafias diferentes para o mesmo curso, e está vazia para cerca de 36% dos registros.
5. **`uniqueNetworkLocation = 2`:** pode indicar **pessoas que refizeram o teste** (possíveis duplicatas), a ser avaliado na limpeza.

## 📝 Notas sobre a tradução dos itens RIASEC

Algumas escolhas de adaptação ao contexto brasileiro:

- **R3** *offshore oil-drilling rig*: traduzido como "plataforma de petróleo em alto-mar", termo muito familiar no Brasil.
- **R5** *grinding machine*: "máquina retificadora" é o termo técnico. Para o público do site, pode ser simplificado para "máquina de desbaste/lixamento industrial".
- **A7** *perform stunts*: não há um verbo direto em português. Optou-se por "fazer cenas de ação (dublê)".
- **C2** *hand-held computer*: nos anos 2010, isso se referia a coletores de dados portáteis usados em estoques.
- **C3** *customer bills*: "emitir cobranças" (boletos/faturas) é mais natural no Brasil do que "contas de clientes".

> Estes itens serão usados como perguntas do formulário da aplicação web. Antes do deploy, vale revisar se cada tradução **mede o mesmo interesse** do item original e se é compreensível para um jovem brasileiro.
