#!/usr/bin/env python3
"""Questões 31–60. Respostas: D B C A D B A C D B C A D B A C D B A C D B C A D B A C D B"""

QUESTIONS = [
    {
        "n": 31,
        "tema": "Experimental é sempre longitudinal",
        "stem": (
            "Um aluno argumenta que um ensaio clínico de dose única, no qual o desfecho de segurança é "
            "lido no mesmo dia da administração, deveria ser classificado como transversal, porque cada "
            "participante seria avaliado em um único recorte de calendário. O que a aula estabelece sobre "
            "o caráter temporal dos estudos experimentais?"
        ),
        "options": {
            "A": "O caráter temporal depende só do calendário: se tudo ocorre em 24 horas, o ensaio é transversal, ainda que haja intervenção e duas medidas (antes e depois da dose).",
            "B": "Apenas o ensaio comunitário é obrigatoriamente longitudinal; o ensaio clínico de fase 1, por ser curto e em saudáveis, admite corte transversal de segurança.",
            "C": "O experimental só é longitudinal quando há grupo controle; um estudo aberto de um único braço permanece transversal, pois não há comparação ao longo do tempo.",
            "D": "Todo estudo experimental é longitudinal: há necessariamente pelo menos duas avaliações (antes e depois da intervenção), ainda que o intervalo seja de horas no mesmo dia.",
        },
        "answer": "D",
        "explain": (
            "A aula é categórica: todo estudo experimental é longitudinal. Intervir implica medir o estado "
            "antes e o efeito depois — duas avaliações no mesmo indivíduo (ou na mesma comunidade). O "
            "intervalo pode ser curto; o que define transversal é uma única avaliação, sem acompanhamento."
        ),
    },
    {
        "n": 32,
        "tema": "Limiar de Fletcher para série de casos",
        "stem": (
            "Um periódico recebe a descrição de nove pacientes com entidade diagnóstica rara e, na "
            "semana seguinte, um adendo que inclui o décimo caso do mesmo serviço, com a mesma "
            "apresentação e sem grupo comparador. Segundo Fletcher et al. (1996), como muda a "
            "nomenclatura e o que isso não altera?"
        ),
        "options": {
            "A": "Permanece relato de casos até vinte pacientes; o limiar de dez é apenas sugestão didática e não altera a classificação usada em prova.",
            "B": "Com nove pacientes é relato de casos; ao atingir dez, passa a ser série de casos. Nos dois, o trabalho continua descritivo e não analítico, insuficiente para demonstrar causa.",
            "C": "O décimo paciente transforma o texto em estudo de prevalência pontual, porque agora há levantamento sistemático de todos os casos do serviço em um ponto do tempo.",
            "D": "A partir de dez pacientes o desenho vira caso-controle interno, pois os primeiros nove funcionam como casos e o décimo, se evoluir bem, funciona como controle.",
        },
        "answer": "B",
        "explain": (
            "O corte cobrado é 10 ou mais pacientes = série de casos (Fletcher et al., 1996). Menos de 10 "
            "= relato. Mudar o nome não muda a lógica: sem comparador o estudo descreve, não analisa, e "
            "não demonstra que um fator causou o desfecho."
        ),
    },
    {
        "n": 33,
        "tema": "Nome do estudo ecológico",
        "stem": (
            "Um colega afirma que “estudo ecológico” só se aplica quando a exposição é ambiental — "
            "poluição, desmatamento ou clima — e que comparar consumo de vinho e mortalidade "
            "cardiovascular entre países seria, portanto, um estudo de prevalência internacional. Qual "
            "correção a aula faz sobre o nome e o objeto desse desenho?"
        ),
        "options": {
            "A": "O nome ecológico de fato restringe o desenho a exposições do meio ambiente; vinho e mortalidade entre países constituem metanálise de estatísticas vitais.",
            "B": "O estudo ecológico exige que a unidade seja o ecossistema; países são unidades políticas, logo o desenho correto é ensaio comunitário observacional.",
            "C": "O nome não tem relação com meio ambiente: ecológico significa que a unidade de observação é o grupo (exposição média do coletivo), podendo a variável ser vinho, cerveja ou cigarros per capita.",
            "D": "Ecológico é sinônimo de série temporal; só recebe esse nome quando a mesma população é medida em vários anos, independentemente da natureza da exposição.",
        },
        "answer": "C",
        "explain": (
            "A aula alerta expressamente: o nome “ecológico” não tem relação com meio ambiente. O que "
            "define é a unidade (grupo) e a exposição média do coletivo. Exemplos da aula: vinho × "
            "mortalidade cardiovascular; cerveja × mortes no trânsito; cigarros per capita × mortalidade."
        ),
    },
    {
        "n": 34,
        "tema": "Função da randomização",
        "stem": (
            "Em um ensaio de osteoartrose, um programa computacional sorteia 200 pacientes para o "
            "medicamento novo e 200 para o tratamento convencional. Sem esse sorteio, o investigador "
            "tenderia a alocar os mais graves ao fármaco que ele acredita ser superior. Qual é a função "
            "da randomização segundo a aula?"
        ),
        "options": {
            "A": "Formar grupos parecidos, distribuindo de modo equilibrado características como idade e sexo, e impedir que o pesquisador escolha quem vai para cada braço, de modo que a diferença final tenda a vir do tratamento.",
            "B": "Cegar participantes e médico assistente, porque o sorteio eletrônico oculta a alocação e substitui o simples, o duplo e o triplo cego em doenças articulares subjetivas.",
            "C": "Transformar o ensaio em estudo agregado, já que a unidade passa a ser o grupo sorteado e não o joelho de cada paciente avaliado individualmente ao longo dos 12 meses.",
            "D": "Garantir que o comparador seja placebo, condição ética indispensável na fase 3 para isolar o efeito específico da substância em doença grave e crônica.",
        },
        "answer": "A",
        "explain": (
            "Randomização = sorteio para formar grupos parecidos e evitar que o pesquisador escolha a "
            "alocação. Não é cegamento (mascaramento de quem sabe o que está sendo dado) nem muda o "
            "tipo operativo (o ensaio clínico permanece individuado). Em doença grave o comparador da "
            "fase 3 é o tratamento tradicional, não placebo."
        ),
    },
    {
        "n": 35,
        "tema": "Controles no caso-controle",
        "stem": (
            "Ao planejar um caso-controle de uma doença de baixa incidência, o pesquisador discute se "
            "deve usar um único grupo de sadios, vários grupos-controle ou vários controles para cada "
            "caso. Qual combinação a aula apresenta como recurso válido e com qual finalidade?"
        ),
        "options": {
            "A": "Apenas um controle por caso, extraído obrigatoriamente da mesma família, para bloquear viés de memória; múltiplos controles inflariam artificialmente a incidência.",
            "B": "Somente múltiplos grupos-controle, nunca múltiplos controles por caso, porque o poder estatístico depende da heterogeneidade dos sadios e não do número absoluto.",
            "C": "Três ou quatro casos para cada controle, invertendo a razão, a fim de compensar a raridade da doença e permitir o cálculo direto da incidência entre expostos.",
            "D": "Múltiplos grupos-controle (estimativas de risco com diferentes comparadores) e 3 ou 4 controles por caso, estes últimos para aumentar o poder estatístico da análise.",
        },
        "answer": "D",
        "explain": (
            "O slide distingue dois recursos: múltiplos grupos-controle (diferentes comparadores) e "
            "múltiplos controles por caso (3 ou 4 sadios para cada doente) para aumentar o poder "
            "estatístico. Isso não transforma o desenho em estudo de incidência: a fração de casos "
            "continua escolhida pelo pesquisador."
        ),
    },
    {
        "n": 36,
        "tema": "Vantagens da metanálise",
        "stem": (
            "Uma metanálise reúne artigos divergentes sobre o mesmo tema, submete-os a análise "
            "estatística aprofundada e produz uma síntese que eleva o nível de significância. Além da "
            "capacidade de síntese, quais outras vantagens o material da aula lista explicitamente?"
        ),
        "options": {
            "A": "Eliminação completa do viés de publicação, tratamento simples dos dados e dispensa de conhecimento estatístico aprofundado, porque o algoritmo corrige automaticamente estudos insignificantes.",
            "B": "Aumento da precisão analítica, melhor representatividade da evidência disponível e possibilidade de comparar resultados contraditórios que, isolados, não permitiriam decisão.",
            "C": "Transformação automática de estudos ecológicos em coortes individuadas, o que autoriza concluir causalidade a partir de médias populacionais previamente divergentes.",
            "D": "Substituição ética do ensaio clínico de fase 3, permitindo aprovar medicamentos sem grupo controle de doentes quando os artigos observacionais já apontam na mesma direção.",
        },
        "answer": "B",
        "explain": (
            "Vantagens no slide: síntese de informação, aumento da precisão analítica, melhor "
            "representatividade e comparação de resultados contraditórios. Desvantagens: dificuldade no "
            "tratamento de dados, análise estatística complexa e viés de publicação (desprezar trabalhos "
            "por insignificância). Não elimina viés nem substitui ensaio clínico."
        ),
    },
    {
        "n": 37,
        "tema": "Coorte e doença rara",
        "stem": (
            "Pretende-se estudar uma neoplasia de incidência extremamente baixa e latência de duas "
            "décadas. Um orientador sugere coorte clássica de 30 anos; outro, caso-controle. Segundo as "
            "vantagens e desvantagens cobradas, qual escolha e qual justificativa estão alinhadas à aula?"
        ),
        "options": {
            "A": "O caso-controle é o mais adequado para doença rara: parte dos casos já existentes, é relativamente rápido e barato; a coorte é ruim para doença rara porque exigiria acompanhar uma população enorme à espera de poucos eventos.",
            "B": "A coorte clássica é sempre superior, pois é o único desenho que mede incidência e, portanto, o único capaz de estudar tanto doença rara quanto latência prolongada.",
            "C": "A coorte histórica resolve os dois problemas ao mesmo tempo, porque registros passados eliminam a raridade do desfecho e dispensam o caso-controle em qualquer neoplasia.",
            "D": "O ensaio clínico de fase 4 é preferível, já que observa milhões de pessoas após a comercialização e detecta desfechos raros sem os vieses de memória do caso-controle.",
        },
        "answer": "A",
        "explain": (
            "A aula contrapõe: coorte é ruim para doença rara; caso-controle é indicado para baixa "
            "incidência (e também para latência prolongada). A coorte histórica ajuda na latência longa "
            "(os eventos já ocorreram nos registros), mas não corrige a raridade do desfecho: ainda é "
            "estudo de incidência. Fase 4 não é desenho para etiologia de neoplasia rara."
        ),
    },
    {
        "n": 38,
        "tema": "Fase 1 do ensaio clínico",
        "stem": (
            "Após a fase pré-clínica ter sugerido que uma molécula pode ser testada em humanos, inicia-se "
            "o primeiro ensaio clínico. Sobre quem entra nessa fase, o tamanho típico da amostra e o "
            "objetivo principal, assinale a alternativa que reproduz o conteúdo da aula."
        ),
        "options": {
            "A": "Centenas de doentes com a doença-alvo, para obter a primeira evidência de eficácia preliminar e, secundariamente, registrar toxicidade grave.",
            "B": "Dezenas de milhares de doentes, com grupo controle em tratamento padrão, estabelecendo a eficácia de fato que precede a aprovação sanitária.",
            "C": "Dezenas de voluntários saudáveis, para definir segurança, toxicidade e tolerabilidade do tratamento, sem pretender ainda demonstrar eficácia clínica.",
            "D": "Milhões de usuários após a comercialização, em farmacovigilância de efeitos adversos raros que as fases anteriores não teriam poder para detectar.",
        },
        "answer": "C",
        "explain": (
            "Pré-clínica: in vitro/animais, define se é possível ir a humanos. Fase 1: dezenas de "
            "saudáveis — segurança, toxicidade, tolerabilidade. Fase 2: centenas de doentes — eficácia "
            "preliminar (e ainda segurança). Fase 3: centenas a milhares, controle = tratamento padrão. "
            "Fase 4: aprovada, milhões, farmacovigilância."
        ),
    },
    {
        "n": 39,
        "tema": "Concorrente versus não concorrente",
        "stem": (
            "A aula amplia o caráter temporal para além de transversal e longitudinal, introduzindo "
            "concorrente, prospectivo e retrospectivo. Relacionando coorte clássica, coorte histórica e "
            "caso-controle, qual mapeamento está correto?"
        ),
        "options": {
            "A": "As três são prospectivas concorrentes, porque em todas há duas avaliações do mesmo indivíduo e o pesquisador sempre caminha de mãos dadas com o tempo.",
            "B": "Coorte clássica e histórica são retrospectivas não concorrentes; só o caso-controle é prospectivo, pois parte do doente e reconstrói a exposição no passado.",
            "C": "Coorte clássica é transversal concorrente; histórica é longitudinal retrospectiva; caso-controle é ecológico não concorrente, porque compara médias de exposição.",
            "D": "Clássica: longitudinal prospectiva e concorrente (começa no presente e segue o tempo). Histórica: prospectiva não concorrente (passado → presente, por registros). Caso-controle: retrospectivo e sempre não concorrente.",
        },
        "answer": "D",
        "explain": (
            "Concorrente = caminhar junto com o tempo (clássica). Não concorrente = não caminha com o "
            "tempo (histórica e caso-controle). Prospectivo = seta para a frente (ambas as coortes). "
            "Retrospectivo = seta para trás (caso-controle). O “retrospectiva” do slide da histórica vem "
            "entre aspas: a direção continua prospectiva."
        ),
    },
    {
        "n": 40,
        "tema": "Exposição e evento no mesmo momento",
        "stem": (
            "Em um levantamento populacional não se selecionam casos: pesa-se, mede-se a renda e "
            "classifica-se desnutrição na mesma visita, sem retorno ulterior. Qual combinação de "
            "características e de nome de estudo corresponde a esse recorte da aula?"
        ),
        "options": {
            "A": "Incidência descritiva: observacional, individuada e longitudinal, porque a desnutrição é um caso novo captado no instante em que o inquérito é aplicado.",
            "B": "Estudo de prevalência: descritivo, não analítico, observacional, individuado e transversal; exposição e evento são aferidos no mesmo momento, sem seleção de casos.",
            "C": "Caso-controle transversal: as crianças desnutridas são os casos e as nutridas, os controles, com retroanálise da renda familiar no instante da medida.",
            "D": "Coorte clássica nutricional: a renda funciona como exposição pré-estabelecida e a desnutrição como desfecho, ainda que não haja segunda avaliação.",
        },
        "answer": "B",
        "explain": (
            "Marcas do estudo de prevalência no slide: levantamento de dados, transversal, “foto” de um "
            "evento, exposição e evento no mesmo momento, sem seleção de casos. O inquérito é a "
            "ferramenta (questionário ou entrevista), não o tipo de estudo. Sem comparação entre "
            "populações permanece descritivo, não analítico."
        ),
    },
    {
        "n": 41,
        "tema": "Caso-controle versus coorte histórica",
        "stem": (
            "Dois protocolos usam prontuários de 2000 a 2025. No primeiro, identificam-se trabalhadores "
            "expostos e não expostos a um solvente em 2000 e busca-se câncer até 2025. No segundo, "
            "partem-se de 150 cânceres atuais e 300 sadios, investigando a exposição antiga ao solvente. "
            "Qual é a distinção decisiva entre os delineamentos?"
        ),
        "options": {
            "A": "Não há distinção: ambos são coortes históricas, porque utilizam registros passados e, portanto, são prospectivos não concorrentes com a mesma medida de incidência.",
            "B": "O primeiro é caso-controle (olha o passado) e o segundo é coorte clássica (olha o presente), invertendo apenas o calendário em que o pesquisador senta para ler os arquivos.",
            "C": "O primeiro é coorte histórica (parte da exposição no passado e segue para o desfecho); o segundo é caso-controle (parte do desfecho e faz retroanálise da exposição). Só a coorte estabelece incidência.",
            "D": "O primeiro é ensaio clínico retrospectivo e o segundo, ecológico individuado; o uso de prontuário transforma qualquer desenho em experimental não concorrente.",
        },
        "answer": "C",
        "explain": (
            "Usar dado passado não unifica os nomes. A coorte histórica começa pela exposição e a seta "
            "aponta para a frente (prospectiva não concorrente) — é estudo de incidência. O caso-controle "
            "começa pelos doentes e sadios e olha para trás (retrospectivo não concorrente) — não analisa "
            "incidência. Essa distinção é clássica de prova."
        ),
    },
    {
        "n": 42,
        "tema": "Ensaio clínico versus ensaio comunitário",
        "stem": (
            "Dois protocolos testam uma vacina julgada benéfica. No primeiro, cada voluntário é sorteado "
            "para vacina ou comparador e acompanhado individualmente. No segundo, duas cidades recebem "
            "a vacina e as demais servem de controle, sem alocação pessoa a pessoa. Qual par de "
            "classificações está correto no quadro da aula?"
        ),
        "options": {
            "A": "O primeiro é ensaio clínico (individuado, experimental, longitudinal); o segundo é ensaio comunitário (agregado, experimental, longitudinal). A diferença operativa é indivíduo versus coletivo, não a presença de intervenção.",
            "B": "Os dois são ensaios clínicos, porque qualquer vacina aplicada a seres humanos define fase 3 individuada; o sorteio de cidades é apenas uma forma de randomização em cluster sem mudar o nome.",
            "C": "O primeiro é coorte clássica de vacinados e o segundo, estudo ecológico, pois o pesquisador não interage com os indivíduos e apenas observa médias municipais de cobertura.",
            "D": "O primeiro é ensaio comunitário (a vacina é prevenção primária) e o segundo, ensaio clínico de fase 4, porque cidades inteiras equivalem a milhões de usuários após aprovação.",
        },
        "answer": "A",
        "explain": (
            "Ambos são experimentais e, portanto, longitudinais. O que os separa é o tipo operativo: "
            "clínico = individuado; comunitário = agregado (intervenção alocada a grupos/comunidades). "
            "O exemplo da vacina contra hepatite B com duas cidades sorteadas versus as demais é o "
            "ensaio comunitário da aula. Ecológico não intervém; coorte não aloca tratamento."
        ),
    },
    {
        "n": 43,
        "tema": "Ensaio comunitário e prevenção primária",
        "stem": (
            "Discute-se fluoretar a água de um município e comparar a cárie com municípios vizinhos, ou "
            "sortear duas cidades para receber vacina contra hepatite B. Por que a aula apresenta o "
            "ensaio comunitário como desenho especialmente adequado a essas situações?"
        ),
        "options": {
            "A": "Porque é o único experimental transversal, permitindo fotografar a cobertura vacinal e o flúor da rede no mesmo dia em que se conta a cárie, sem acompanhamento comunitário.",
            "B": "Porque substitui a fase 1 do ensaio clínico: comunidades inteiras funcionam como “voluntários saudáveis” para toxicidade, o que acelera a aprovação sanitária da vacina.",
            "C": "Porque gera apenas hipóteses, como o estudo ecológico, e portanto é eticamente mais aceitável quando a aleatorização individual seria antiética ou pouco prática.",
            "D": "Porque é ideal para intervenções de prevenção primária, serve de alternativa quando a aleatorização individual é antiética ou pouco prática, e tende a ser mais econômico que o ensaio clínico.",
        },
        "answer": "D",
        "explain": (
            "Ensaio comunitário: agregado, experimental, longitudinal. Indicações da aula: intervenções "
            "preventivas (prevenção primária), alternativa quando aleatorizar indivíduos é antiético ou "
            "pouco prático, e mais econômico que o clínico. Exemplos: vacina de hepatite B em cidades e "
            "fluoretação da água. Não é ecológico: há intervenção alocada pelo pesquisador."
        ),
    },
    {
        "n": 44,
        "tema": "Viés de registro na coorte histórica",
        "stem": (
            "Uma coorte histórica de asbesto e mesotelioma depende de prontuários escritos por dezenas "
            "de médicos ao longo de quinze anos, com qualidade irregular de exposição e de desfecho. "
            "Qual limitação a aula associa a esse desenho, contrastando-a com a coorte clássica?"
        ),
        "options": {
            "A": "Viés de publicação, porque apenas os prontuários de quem desenvolveu mesotelioma costumam ser arquivados, o que é o mesmo problema da metanálise.",
            "B": "Viés de registro, de memória e de padronização: o dado foi escrito por outros, “vira bagunça”; a clássica é melhor porque o próprio pesquisador examina a todos do mesmo modo.",
            "C": "Viés ecológico, pois médias de exposição ocupacional da fábrica são atribuídas a cada trabalhador, exatamente como no estudo de cigarros per capita.",
            "D": "Impossibilidade de obter consentimento e de avaliar o paciente no presente, o que impede chamar o desenho de coorte e o rebaixa a série temporal hospitalar.",
        },
        "answer": "B",
        "explain": (
            "Desvantagens da histórica: depende de registros (viés de registro, de memória e de "
            "padronização). Quando o pesquisador escreve, escreve tudo igual; prontuário de terceiros "
            "despadroniza. A clássica é melhor pela padronização. Na histórica deve haver consentimento "
            "desde o início e há avaliação atual do paciente — não é essa a falha estrutural."
        ),
    },
    {
        "n": 45,
        "tema": "Descritivo versus analítico",
        "stem": (
            "Um trabalho conta o número de malformações congênitas ao nascimento em um hospital, sem "
            "comparar com a Índia, a Alemanha ou qualquer outra população. Outro trabalho toma dois "
            "desses levantamentos e os confronta. O que muda, na nomenclatura da aula, de um para o outro?"
        ),
        "options": {
            "A": "O primeiro é descritivo (levantamento, sem comparar populações). Ao confrontar dois estudos, o trabalho torna-se analítico, porque analítico é o que compara, em geral grupos.",
            "B": "Os dois permanecem descritivos, pois malformação ao nascimento é sempre prevalência pontual e prevalência, por definição, nunca se torna analítica.",
            "C": "O primeiro já é analítico, porque todo recém-nascido malformado funciona como caso e os nascidos sadios do mesmo hospital funcionam implicitamente como controles.",
            "D": "A comparação internacional transforma o desenho em ensaio comunitário, já que países são coletivos e o pesquisador “aloca” implicitamente o sistema de saúde de cada nação.",
        },
        "answer": "A",
        "explain": (
            "Descritivo: levantamento, não compara. Analítico: compara, geralmente grupos. Uma única "
            "amostra (malformações; dor lombar em 12 meses) não é analítica. Se dois estudos são "
            "comparados, passa a ser analítico. Prevalência e incidência são nomes de estudo descritivo "
            "enquanto não houver grupo de comparação; a coorte é a incidência analítica."
        ),
    },
    {
        "n": 46,
        "tema": "Fase 4 do ensaio clínico",
        "stem": (
            "A substância já foi aprovada pelas instituições de saúde e está comercializada, mas o ensaio "
            "clínico continua em grande escala. Qual fase é essa, em que ordem de magnitude de pessoas "
            "e com qual objetivo a aula a descreve?"
        ),
        "options": {
            "A": "Ainda é fase 3: a aprovação ocorre no fim da fase 2, e a fase 3 se estende por milhões de usuários até se esgotarem os estoques de comparador padrão.",
            "B": "É a fase pré-clínica pós-comercialização, agora em humanos, para decidir se a molécula poderia, em tese, ter sido testada; o tamanho da amostra é de dezenas de saudáveis.",
            "C": "Fase 4: a medicação aprovada e comercializada continua sendo estudada em grande escala, da ordem de milhões de pacientes, em farmacovigilância de efeitos adversos raros.",
            "D": "É um ensaio comunitário de fase 4, porque milhões de pessoas equivalem a populações inteiras e o tipo operativo deixa de ser individuado após a aprovação sanitária.",
        },
        "answer": "C",
        "explain": (
            "Fase 4: aprovada, comercializada, continua o ensaio em grande escala (milhões), "
            "farmacovigilância, efeitos adversos raros. A aprovação vem depois da fase 3, não da 2. O "
            "desenho permanece ensaio clínico (individuado); o número de pessoas não o transforma em "
            "comunitário. Diferentemente da coorte, analisa-se o efeito do tratamento, embora o desenho "
            "se pareça."
        ),
    },
    {
        "n": 47,
        "tema": "Vantagens da coorte",
        "stem": (
            "A coorte é apresentada como o estudo observacional mais relevante — e também o mais caro e "
            "demorado. Qual conjunto reproduz as vantagens listadas na aula, distinguindo-as do que a "
            "coorte precisamente não faz bem?"
        ),
        "options": {
            "A": "É o desenho mais barato e mais rápido; calcula incidência; é o melhor para doença rara; e permite incluir novas exposições no meio do seguimento sem perder validade.",
            "B": "Substitui eticamente o ensaio clínico em qualquer pergunta, experimenta o fator de risco quando a randomização seria antiética, e dispensa grupo de não expostos.",
            "C": "Não mede incidência (só prevalência de período), mas é o único que cega o pesquisador e, por isso, é o melhor substituto do experimento verdadeiro.",
            "D": "É a única forma de estabelecer diretamente a incidência e a história natural; melhor substituto do experimento; avalia vários desfechos para uma exposição registrada no início. É ruim para doença rara.",
        },
        "answer": "D",
        "explain": (
            "Vantagens: única forma de estabelecer a incidência diretamente; segue a história natural; "
            "melhores substitutos de um experimento verdadeiro; avalia fatores registrados no início e "
            "várias doenças para uma exposição; olha com naturalidade o surgimento. Desvantagens: ruim "
            "para doença rara; oneroso; longo; só avalia o que foi registrado no início. Nunca "
            "experimenta fator de risco."
        ),
    },
    {
        "n": 48,
        "tema": "Simples cego",
        "stem": (
            "Em um ensaio de joelho, o paciente ignora se recebe o fármaco novo ou o tratamento "
            "convencional, mas o médico assistente e o pesquisador conhecem a alocação. Como a aula "
            "nomeia esse mascaramento e o que ele ainda não impede?"
        ),
        "options": {
            "A": "Duplo cego, porque dois atores (médico e pesquisador) estão cegos para o desfecho radiográfico, o que já evita tratamento especial e parcialidade na escrita dos resultados.",
            "B": "Simples cego: só o pesquisador e o médico sabem; o participante não. O médico assistente ainda pode tratar os grupos de modo diferente, problema que o duplo cego visa evitar.",
            "C": "Estudo aberto, pois qualquer pessoa da equipe que saiba a alocação descaracteriza o cegamento e o protocolo equivale a não mascarar ninguém.",
            "D": "Triplo cego incompleto, porque o banco de dados já poderia ocultar os códigos do pesquisador; enquanto isso não ocorre, a nomenclatura oficial permanece “aberto”.",
        },
        "answer": "B",
        "explain": (
            "Aberto: o paciente (e em geral todos) sabe se é controle ou não. Simples cego: só "
            "pesquisador e médico sabem; o participante não. Duplo: nem paciente nem médico assistente "
            "(evita tratamento especial). Triplo: nem o pesquisador; só o banco de dados (evita "
            "parcialidade ao escrever resultados, útil se a avaliação é subjetiva)."
        ),
    },
    {
        "n": 49,
        "tema": "Identificação: coorte clássica",
        "stem": (
            "Em 1949, 5.127 pessoas de 30 a 59 anos, sem doença coronariana, foram examinadas e "
            "acompanhadas por cerca de 30 anos. O estudo relacionou hipertensão, colesterol, tabagismo, "
            "intolerância à glicose e hipertrofia ventricular esquerda ao desenvolvimento de doença "
            "coronariana. Qual é o delineamento e o caráter temporal?"
        ),
        "options": {
            "A": "Coorte clássica (Framingham): individuada, observacional, longitudinal, descritiva e analítica; prospectiva e concorrente, com expostos e não expostos acompanhados a partir do presente da época.",
            "B": "Caso-controle aninhado em série temporal, porque a doença coronariana já existia na população e o olhar para os fatores de risco é necessariamente retrospectivo e ecológico.",
            "C": "Ensaio comunitário de Framingham, já que a unidade era a cidade inteira e os pesquisadores intervieram sobre pressão, colesterol e tabaco da população local.",
            "D": "Estudo de prevalência pontual repetido, transversal, pois a cada consulta se fotografa a doença coronariana sem que isso configure seguimento da mesma coorte.",
        },
        "answer": "A",
        "explain": (
            "Framingham é o exemplo mais famoso de coorte clássica da aula: 5.127 pessoas de 30 a 59 "
            "anos sem doença coronariana, ~30 anos, mostrando risco aumentado com PA, colesterol, fumo, "
            "intolerância à glicose e HVE. Clássica = contemporânea, prospectiva concorrente. Ninguém "
            "tinha o desfecho no início; as exposições estavam pré-estabelecidas."
        ),
    },
    {
        "n": 50,
        "tema": "Identificação: caso-controle",
        "stem": (
            "Pesquisadores reúnem 200 adultos com uma doença de baixíssima incidência e 800 adultos "
            "sadios semelhantes, investigam em prontuário e por entrevista a exposição prévia a um "
            "agrotóxico e não pretendem estimar quantos casos novos surgem por ano na região. Qual é o "
            "estudo?"
        ),
        "options": {
            "A": "Coorte histórica ocupacional, prospectiva não concorrente, porque os prontuários estão no passado e a seta, portanto, aponta do agrotóxico para a doença.",
            "B": "Estudo de prevalência analítico, transversal, já que casos e controles são avaliados hoje e a exposição é um atributo presente no mesmo instante da entrevista.",
            "C": "Caso-controle: individuado, observacional, longitudinal retrospectivo e não concorrente; parte do desfecho, olha a exposição passada e não estabelece incidência.",
            "D": "Série de casos com grupo controle externo, descritiva, suficiente para calcular incidência se a população da região for usada como denominador improvisado.",
        },
        "answer": "C",
        "explain": (
            "Marcas: começa pelos doentes e sadios, retroanálise da exposição, 4 controles por caso "
            "(poder estatístico), doença de baixa incidência, não analisa incidência. Características: "
            "individuado, observacional, longitudinal retrospectivo, sempre não concorrente."
        ),
    },
    {
        "n": 51,
        "tema": "Identificação: ensaio clínico",
        "stem": (
            "Quatrocentos pacientes com osteoartrose de joelho são incluídos; um programa sorteia 200 "
            "para um medicamento novo e 200 para o tratamento já usado. Todos são reexaminados ao longo "
            "de 12 meses. O comparador não é placebo. Qual identificação completa está correta?"
        ),
        "options": {
            "A": "Coorte clássica terapêutica: observacional, porque o pesquisador não fabrica a artrose; o sorteio apenas equilibra idade e sexo entre obesos e não obesos.",
            "B": "Ensaio comunitário de fase 3, agregado, pois 200 pacientes em cada braço já constituem coletivos e a artrose é tratada como média de grupo.",
            "C": "Estudo de incidência de melhora articular, descritivo, sem análise, porque todos os 400 já têm a doença no início e ninguém é sadio.",
            "D": "Ensaio clínico randomizado e controlado, fase 3: experimental, individuado e longitudinal, comparando substância nova com tratamento tradicional em doentes.",
        },
        "answer": "D",
        "explain": (
            "Intervenção julgada benéfica + alocação individual + seguimento = ensaio clínico. "
            "Randomização e grupo controle. Como são doentes e o comparador é o tratamento "
            "convencional, corresponde à fase 3 (placebo seria antiético em doença que já tem tratamento). "
            "Todo experimental é longitudinal. Não é coorte: o pesquisador testa, não apenas observa."
        ),
    },
    {
        "n": 52,
        "tema": "Identificação: ensaio comunitário",
        "stem": (
            "Duas cidades são sorteadas para receber vacina contra hepatite B e as demais da região "
            "servem de comparação; a intervenção é alocada ao município, não a cada morador, e o "
            "objetivo é prevenção primária. Qual é o delineamento e uma desvantagem típica cobrada?"
        ),
        "options": {
            "A": "Ensaio clínico de fase 1 em escala municipal, cuja desvantagem é usar voluntários saudáveis em número insuficiente para estimar eficácia populacional.",
            "B": "Ensaio comunitário (agregado, experimental, longitudinal). Desvantagens: difícil isolar a comunidade, difícil observar efeitos colaterais e privação do benefício ao grupo controle.",
            "C": "Estudo ecológico de vacinação, observacional e transversal, cuja desvantagem é a falácia ecológica ao inferir proteção individual a partir da cobertura média.",
            "D": "Série temporal vacinal, porque a incidência de hepatite será lida em vários anos; a desvantagem é não gerar hipótese alguma, apenas concluir eficácia causal.",
        },
        "answer": "B",
        "explain": (
            "Exemplo literal da aula: vacina contra hepatite B com duas cidades sorteadas versus as "
            "demais. Ensaio comunitário = agregado + intervenção + longitudinal. Desvantagens listadas: "
            "difícil isolar a comunidade, difícil observar efeitos colaterais, privação do benefício ao "
            "grupo controle. Ecológico não aloca vacina; série temporal não intervém."
        ),
    },
    {
        "n": 53,
        "tema": "Identificação: prevalência",
        "stem": (
            "No dia do recrutamento militar, todos os jovens de 18 anos daquela turma são examinados "
            "uma única vez para escoliose. Não se selecionam casos, não há retorno em seis meses e não "
            "se compara com outra faixa etária. Qual é o estudo?"
        ),
        "options": {
            "A": "Incidência de escoliose aos 18 anos, longitudinal, porque o desvio da coluna é um caso novo que se manifesta exatamente no exame de ingresso.",
            "B": "Série de casos de escoliose, desde que o serviço descreva pelo menos dez recrutas acometidos, independentemente de ter examinado os demais.",
            "C": "Prevalência pontual: descritiva, não analítica, observacional, individuada e transversal; o ponto de referência comum é o recrutamento aos 18 anos, não o mesmo dia civil.",
            "D": "Coorte clássica militar, prospectiva concorrente, pois as Forças Armadas acompanharão esses jovens ao longo da carreira e a escoliose é exposição para dor lombar futura.",
        },
        "answer": "C",
        "explain": (
            "Exemplo da aula de prevalência pontual: escoliose no recrutamento militar aos 18 anos "
            "(também malformações ao nascimento). Mesmo ponto de referência, cada um visto uma vez, "
            "sem seleção de casos, sem comparação = descritivo, transversal, individuado, observacional."
        ),
    },
    {
        "n": 54,
        "tema": "Identificação: incidência",
        "stem": (
            "Mil mulheres obesas, todas sem câncer de mama no exame inicial, são reavaliadas ao longo "
            "de dez anos para se contar quantos casos novos de câncer surgem. Não se constitui grupo de "
            "não obesas. Qual é o nome do estudo e por que ainda não é coorte?"
        ),
        "options": {
            "A": "Estudo de incidência: descritivo, não analítico, observacional, individuado e longitudinal. Só se tornaria coorte se fosse acrescentado um grupo de comparação (não obesas).",
            "B": "Coorte clássica incompleta: a obesidade já é exposição pré-estabelecida, logo o nome é coorte mesmo sem não expostas, bastando o seguimento rígido.",
            "C": "Prevalência de período de dez anos, transversal, porque a pergunta final é se a mulher teve câncer em algum momento da década, avaliada uma única vez ao cabo do estudo.",
            "D": "Caso-controle de câncer de mama, retrospectivo, já que ao final existem doentes e sadias e se olha para trás a obesidade que as distinguia no baseline.",
        },
        "answer": "A",
        "explain": (
            "O próprio exemplo da aula: câncer de mama em 1.000 obesas. Incidência acompanha o "
            "surgimento de casos novos; ninguém pode ter a doença no início; sem grupo controle permanece "
            "descritiva. A coorte nasce quando se acrescenta o comparador. Reavaliar ao longo de dez "
            "anos é longitudinal, não transversal."
        ),
    },
    {
        "n": 55,
        "tema": "Identificação: coorte histórica",
        "stem": (
            "Em 2026 lê-se a ficha de 1.000 trabalhadores de 2010, separa-se quem teve contato com "
            "asbesto, confirma-se que nenhum tinha mesotelioma naquela época, percorre-se o arquivo até "
            "hoje e ainda se examina o paciente no presente. Se o seguimento continuar depois de 2026, "
            "como a aula nomeia o estudo?"
        ),
        "options": {
            "A": "Passa a ser coorte clássica da data presente em diante, porque agora o pesquisador caminha concorrentemente com o tempo e o trecho histórico deve ser descartado.",
            "B": "Vira caso-controle misto, pois o exame atual identifica doentes e sadios e o arquivo de 2010 fornece a exposição, unindo os dois desenhos em um só protocolo.",
            "C": "Torna-se série temporal ocupacional, agregado e observacional, quando o seguimento ultrapassa o presente, porque a unidade deixa de ser o trabalhador e passa a ser o ano.",
            "D": "Permanece coorte histórica (mista): começar no passado e cruzar o presente não muda o nome; continua prospectiva não concorrente no trecho de registros, com avaliação atual e consentimento.",
        },
        "answer": "D",
        "explain": (
            "Aula: se a histórica continuar após o presente, segue sendo coorte histórica (mista). O nome "
            "não muda. Continua sendo prospectiva (seta para a frente) e não concorrente no trecho que "
            "usa registros. Há consentimento desde o início e avaliação atual do paciente. A clássica é "
            "melhor pela padronização, mas a mista não se converte automaticamente nela."
        ),
    },
    {
        "n": 56,
        "tema": "Identificação: estudo ecológico",
        "stem": (
            "Comparam-se, em um único ano, o consumo médio de vinho e a mortalidade cardiovascular de "
            "vários países, usando apenas estatísticas nacionais, sem saber o que cada indivíduo bebeu "
            "nem de que morreu. Qual é o estudo, o que ele pode e o que ele não pode?"
        ),
        "options": {
            "A": "Coorte agregada internacional, que conclui causalidade se a correlação for linear e monotônica, dispensando teste ulterior em indivíduos.",
            "B": "Estudo ecológico: agregado, observacional e transversal. Serve para gerar hipóteses, não para concluir; a hipótese deve ser testada depois por estudo individuado, por exemplo uma coorte.",
            "C": "Série temporal de países, longitudinal, porque a mortalidade cardiovascular é um fluxo de óbitos ao longo dos doze meses daquele ano calendário.",
            "D": "Ensaio comunitário natural, experimental, pois o hábito cultural de beber vinho funciona como intervenção alocada pelo “estilo de vida” de cada nação.",
        },
        "answer": "B",
        "explain": (
            "Exemplo da aula: consumo de vinho × mortalidade cardiovascular em países. Ecológico = "
            "agregado, observacional, transversal. Superficial, sem acompanhamento, não gera conclusões, "
            "gera hipóteses. O teste posterior é um estudo mais detalhado e individuado (coorte). Série "
            "temporal exigiria vários pontos no tempo; ensaio exige intervenção do pesquisador."
        ),
    },
    {
        "n": 57,
        "tema": "Identificação: série temporal",
        "stem": (
            "Analisa-se o número mensal de internações por bronquiolite em Curitiba de janeiro de 2010 "
            "a dezembro de 2025, buscando tendência e sazonalidade, sem examinar o prontuário de cada "
            "criança. Qual é o estudo e como ele se relaciona com o ecológico?"
        ),
        "options": {
            "A": "Série temporal (estudo ecológico longitudinal): agregado, observacional e longitudinal; é a repetição do recorte ecológico em vários pontos do tempo, também geradora de hipóteses.",
            "B": "Estudo de incidência hospitalar individuado, porque cada internação é um caso novo e quinze anos de calendário configuram seguimento de uma coorte aberta municipal.",
            "C": "Ensaio comunitário de estações do ano, experimental, já que o inverno funciona como intervenção natural alocada à cidade e comparada com o verão.",
            "D": "Prevalência de período de 16 anos, transversal, pois se conta quantas internações existiram em algum momento do intervalo, cada uma fotografada uma única vez.",
        },
        "answer": "A",
        "explain": (
            "Números de internações do coletivo, vários pontos no tempo = série temporal = estudo "
            "ecológico longitudinal (agregado, observacional, longitudinal). O ecológico clássico é um "
            "único corte comparando grupos. A série temporal é “mais de um estudo ecológico” e também "
            "gera hipótese, permitindo ver se o efeito flutua com a suposta causa."
        ),
    },
    {
        "n": 58,
        "tema": "Desfechos múltiplos na coorte",
        "stem": (
            "Uma coorte de tabagismo prevê, já no baseline, pontuar infarto, acidente vascular cerebral "
            "e dissecção de aorta, excluindo quem já tenha qualquer desses eventos. No terceiro ano o "
            "pesquisador quer incluir, pela primeira vez, câncer de bexiga, que não fora examinado no "
            "início. O que a aula autoriza e o que ela veda?"
        ),
        "options": {
            "A": "Autoriza incluir o câncer de bexiga como nova exposição, não como desfecho, porque exposições podem ser acrescentadas livremente desde que o desfecho original permaneça fixo.",
            "B": "Veda qualquer multiplicidade: a coorte só admite um desfecho; infarto, AVC e dissecção deveriam ter sido três coortes separadas desde o primeiro dia.",
            "C": "Desfechos podem ser múltiplos se previstos e avaliados desde o início (infarto, AVC, dissecção). Não se inclui câncer de bexiga agora: quem já o tinha misturaria prevalência com incidência, e exposições também não se acrescentam no meio.",
            "D": "Autoriza o câncer de bexiga como desfecho tardio, porque a vantagem da coorte é exatamente descobrir doenças não imaginadas, olhando com naturalidade o surgimento do inesperado.",
        },
        "answer": "C",
        "explain": (
            "Desfechos podem ser múltiplos, desde que imaginados e pontuados no baseline, para excluir "
            "quem já os tinha (senão é prevalência, não incidência). Exposições, ao contrário, são "
            "pré-estabelecidas e não entram no meio do estudo. “Olhar com naturalidade o surgimento” não "
            "autoriza mudar o protocolo a posteriori."
        ),
    },
    {
        "n": 59,
        "tema": "Ensaio aberto",
        "stem": (
            "Nos dois braços de um ensaio de artrose, pacientes, médico assistente e pesquisador sabem "
            "qual tratamento está sendo administrado. Não há placebo. Qual é o tipo de cegamento e por "
            "que isso importa para a validade da comparação?"
        ),
        "options": {
            "A": "Simples cego invertido: se todos sabem, o mascaramento recai apenas sobre o banco de dados, o que já impede o médico de dar tratamento especial a um dos grupos.",
            "B": "Duplo cego operacional, porque o conhecimento simétrico nos dois braços se anula e equivale, na prática, a ninguém saber a alocação verdadeira.",
            "C": "Triplo cego declarado, útil quando a avaliação é subjetiva: ao saberem todos, ninguém se sente autorizado a enviesar a leitura das imagens.",
            "D": "Estudo aberto: o paciente sabe se é controle ou não (e a equipe também). O médico pode tratar os grupos de modo diferente e o pesquisador pode ser parcial ao interpretar resultados.",
        },
        "answer": "D",
        "explain": (
            "Aberto = todos sabem. A aula liga o duplo cego à necessidade de o médico assistente tratar "
            "os grupos igualmente e o triplo cego à imparcialidade do pesquisador quando a avaliação é "
            "subjetiva. Sem mascaramento, esses dois vieses de conduta e de leitura ficam abertos. "
            "Aberto não é simples cego: no simples, o participante não sabe."
        ),
    },
    {
        "n": 60,
        "tema": "Quadro-resumo do ensaio clínico",
        "stem": (
            "No quadro de desenhos (tipo operativo × ação do investigador × caráter temporal), o ensaio "
            "clínico ocupa uma célula precisa, distinta da coorte, do ecológico e do ensaio comunitário. "
            "Qual combinação de características o identifica de imediato e qual contraste a aula enfatiza "
            "com a coorte?"
        ),
        "options": {
            "A": "Agregado, observacional e transversal — a mesma célula do estudo ecológico — diferindo da coorte apenas por usar medicamento em vez de fator de risco.",
            "B": "Individuado, de intervenção (experimental) e longitudinal. Diferentemente da coorte, analisa-se o efeito do tratamento, embora o desenho (grupos acompanhados no tempo) se pareça.",
            "C": "Individuado, observacional e transversal, porque cada doente é randomizado uma única vez e o desfecho de eficácia é uma fotografia ao fim da fase 3.",
            "D": "Agregado, experimental e retrospectivo, compartilhando a célula do ensaio comunitário e distinguindo-se da coorte histórica apenas pelo uso de placebo.",
        },
        "answer": "B",
        "explain": (
            "Quadro da aula: ensaio clínico = individuado + intervenção + longitudinal. Coorte = "
            "individuado + observacional + longitudinal. Comunitário = agregado + intervenção + "
            "longitudinal. Ecológico = agregado + observacional + transversal. A aula nota que o desenho "
            "clínico se parece com o da coorte, mas o objeto é o efeito do tratamento, não a história "
            "natural da exposição."
        ),
    },
]
