#!/usr/bin/env python3
"""Gera o PDF e o JSON das 60 questões de Epidemiologia (Aula 6)."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from fpdf import FPDF

ROOT = Path("/workspace")
sys.path.insert(0, str(Path(__file__).resolve().parent))
JSON_OUT = ROOT / "src" / "data" / "questions.json"
PDF_PUBLIC = ROOT / "public" / "simulado-epidemiologia.pdf"
PDF_ARTIFACTS = ROOT / "artifacts" / "Lista_Exercicios_Epidemiologia_60_questoes.pdf"
FONT_DIR = Path("/usr/share/fonts/truetype/liberation")

NAVY = (21, 34, 56)
STEEL = (42, 85, 112)
CREAM = (243, 238, 228)
INK = (28, 36, 48)
MUTED = (90, 98, 108)
LINE = (196, 186, 168)
WHITE = (255, 253, 248)
ACCENT_BAR = (42, 85, 112)


def wc(text: str) -> int:
    return len(re.findall(r"\S+", text))


QUESTIONS = [
    {
        "n": 1,
        "tema": "Estudo ecológico",
        "stem": (
            "Pesquisadores compararam, em um único ano calendário, o consumo médio per capita de cerveja "
            "e o coeficiente de mortalidade por acidente de trânsito em três países, usando apenas "
            "estatísticas de produção, importação e atestados de óbito, sem examinar qualquer indivíduo. "
            "Qual é a classificação mais precisa desse delineamento segundo o quadro de desenhos de investigação?"
        ),
        "options": {
            "A": "Trata-se de uma série temporal, porque a mortalidade se acumula ao longo dos meses e o estudo seria, portanto, longitudinal e agregado.",
            "B": "Trata-se de uma coorte clássica, pois há comparação entre populações com maior ou menor consumo de álcool e o desfecho observado é a morte.",
            "C": "Trata-se de um estudo ecológico: agregado, observacional e transversal, cuja unidade de observação é o grupo e que serve para gerar hipóteses, não para concluir.",
            "D": "Trata-se de um ensaio comunitário, já que o consumo de cerveja funciona como intervenção coletiva comparada entre países no mesmo recorte temporal.",
        },
        "answer": "C",
        "explain": (
            "A unidade de observação é o país (grupo), a exposição é a média do coletivo e a análise "
            "ocorre em um único recorte temporal, sem acompanhamento. No quadro da aula, isso é estudo "
            "ecológico: agregado, observacional e transversal. Ele não confirma associação causal; apenas "
            "gera hipótese. Série temporal exigiria vários pontos no tempo; coorte e ensaio exigem "
            "indivíduos (ou intervenção alocada pelo pesquisador)."
        ),
    },
    {
        "n": 2,
        "tema": "Relato de caso",
        "stem": (
            "Em um congresso de ortopedia, apresentou-se a migração intratorácica de fio de Kirschner "
            "após fixação de clavícula em quatro pacientes, descrevendo a complicação imprevisível, a "
            "técnica e a evolução de cada um, sem grupo comparador. Qual é o estudo epidemiológico empregado?"
        ),
        "options": {
            "A": "Relato de casos, porque são menos de dez pacientes, a apresentação é científica simples e descreve uma complicação imprevisível em congresso, sem comparação de grupos.",
            "B": "Série de casos, pois qualquer descrição de mais de um paciente já ultrapassa o relato único e passa automaticamente a ser série, segundo Fletcher e colaboradores.",
            "C": "Estudo de prevalência, porque cada paciente foi avaliado uma única vez e a exposição cirúrgica foi aferida no mesmo momento em que se descreveu a complicação.",
            "D": "Estudo de caso-controle, já que os quatro doentes funcionam como casos e a literatura citada na discussão serve como grupo controle implícito da comparação.",
        },
        "answer": "A",
        "explain": (
            "O corte de Fletcher et al. (1996) é claro: 10 ou mais pacientes = série de casos; menos de 10 "
            "= relato de casos. Quatro pacientes com complicação imprevisível apresentada em congresso é "
            "o exemplo clássico da aula. Comparar achados com a literatura na discussão não torna o "
            "trabalho analítico nem caso-controle."
        ),
    },
    {
        "n": 3,
        "tema": "Coorte histórica e caráter temporal",
        "stem": (
            "Em 2026, pesquisadores recuperaram prontuários de 2010 de mil trabalhadores de uma indústria "
            "química, separaram expostos e não expostos ao asbesto (nenhum com neoplasia no início) e "
            "seguiram os registros até o presente, avaliando também os pacientes hoje para mesotelioma. "
            "Como se classifica o caráter temporal desse estudo na nomenclatura da aula?"
        ),
        "options": {
            "A": "Longitudinal retrospectivo e concorrente, porque os dados já existiam no passado e o pesquisador caminhou junto com o tempo desde 2010 até 2026.",
            "B": "Transversal observacional, pois a consulta aos prontuários ocorre em poucos dias no presente e cada trabalhador é lido uma única vez no arquivo.",
            "C": "Longitudinal retrospectivo e não concorrente, já que o slide rotula a coorte histórica como retrospectiva e a seta aponta necessariamente para trás.",
            "D": "Longitudinal prospectivo e não concorrente: começa no passado, a seta aponta para a frente até o presente e o estudo não caminha de mãos dadas com o tempo.",
        },
        "answer": "D",
        "explain": (
            "Na aula, o rótulo “retrospectiva” do slide vem entre aspas. A direção da coorte histórica é "
            "prospectiva (do passado para o presente) e não concorrente (usa registros, sem caminhar com "
            "o tempo). Coorte clássica = prospectiva concorrente. Caso-controle = retrospectivo não "
            "concorrente. Usar dados passados não define retrospectivo; o que define é a direção da seta."
        ),
    },
    {
        "n": 4,
        "tema": "Viés ecológico",
        "stem": (
            "Um estudo ecológico encontrou correlação positiva entre cigarros vendidos per capita e "
            "mortalidade cardiovascular em diversos países. Um aluno conclui que o indivíduo que mais "
            "fuma é exatamente aquele com maior risco de morrer por infarto. Qual erro conceitual foi cometido?"
        ),
        "options": {
            "A": "Viés de publicação, porque apenas os países que encontraram associação significativa teriam divulgado as estatísticas de tabaco e mortalidade cardiovascular.",
            "B": "Falácia ou viés ecológico: inferir no indivíduo uma relação causal baseada em associações encontradas na comparação de populações, atribuindo ao sujeito o que se observou no todo.",
            "C": "Viés de memória, pois os atestados de óbito dependem de familiares recordarem o hábito tabágico do falecido e isso distorce a média nacional de consumo.",
            "D": "Viés de seleção de controles, porque os países com baixa venda de cigarros não constituem um grupo sadio adequado para comparar com os países de alto consumo.",
        },
        "answer": "B",
        "explain": (
            "Viés, na aula, é sinônimo de erro. A falácia ecológica é inferir no indivíduo o que só foi "
            "observado no coletivo: a média do país pode não representar cada pessoa. Hipóteses "
            "ecológicas precisam ser testadas por estudos individuados (por exemplo, uma coorte). "
            "É um tema muito cobrado em prova."
        ),
    },
    {
        "n": 5,
        "tema": "Pré-requisitos da coorte",
        "stem": (
            "Na construção de uma coorte clássica sobre obesidade e gonartrose, mil adultos são "
            "examinados no início com raio X, mobilidade e inspeção do joelho. Um deles já apresenta "
            "artrose. Segundo os quesitos cobrados em prova, qual conduta e qual justificativa estão corretas?"
        ),
        "options": {
            "A": "Excluir esse indivíduo, porque ninguém pode ter o desfecho no início: o objetivo é incidência (surgimento), e incluí-lo misturaria caso prevalente com caso novo.",
            "B": "Mantê-lo no grupo dos expostos, já que a obesidade é o fator de risco e a artrose inicial apenas documenta a gravidade basal da exposição mecânica sobre a cartilagem.",
            "C": "Transferi-lo para um terceiro braço de prevalência, transformando o mesmo protocolo simultaneamente em estudo transversal e em coorte, o que aumenta a eficiência estatística.",
            "D": "Incluí-lo somente se houver grupo controle de não obesos, porque a análise comparativa corrige o fato de o desfecho já estar presente no baseline da coorte.",
        },
        "answer": "A",
        "explain": (
            "Pergunta de prova: ninguém, no início, pode ter o desfecho. Quem já tem artrose é excluído "
            "(passam a ser 999). Outros quesitos: observação por período suficiente, seguimento rígido e "
            "exposições pré-estabelecidas. Desfechos podem ser múltiplos, desde que previstos e pontuados "
            "desde o início."
        ),
    },
    {
        "n": 6,
        "tema": "Estudo de incidência",
        "stem": (
            "Acompanham-se mil pessoas obesas, todas sem gonartrose no início, durante cinco anos, "
            "repetindo anualmente o exame do joelho para estimar a taxa de aparecimento de artrose. "
            "Não se constitui grupo de não obesos. Qual é o delineamento e a sua combinação de características?"
        ),
        "options": {
            "A": "Coorte clássica: individuada, observacional, longitudinal e analítica, porque a obesidade já funciona como exposição e a história natural da artrose está sendo seguida.",
            "B": "Estudo de prevalência de período, pois a artrose pode surgir em qualquer momento dos cinco anos e cada paciente responde se teve ou não o desfecho naquele intervalo.",
            "C": "Estudo de incidência: descritivo, não analítico, observacional, individuado e longitudinal, sem grupo controle, medindo apenas o surgimento de casos novos na população obesa.",
            "D": "Ensaio clínico de fase 2, já que o pesquisador seleciona doentes (obesos) e acompanha o efeito mecânico do peso sobre a articulação ao longo de anos de seguimento.",
        },
        "answer": "C",
        "explain": (
            "Incidência e coorte compartilham ser individuadas, observacionais e longitudinais. O que "
            "falta na incidência é a análise: não há grupo de comparação. Ao acrescentar não obesos, o "
            "mesmo desenho vira coorte (analítica). Sem comparador, permanece descritivo."
        ),
    },
    {
        "n": 7,
        "tema": "Fases do ensaio clínico",
        "stem": (
            "Uma substância julgada superior à quimioterapia para câncer de mama passou da fase 2 e "
            "entra na fase 3, com centenas a milhares de doentes. Sobre o grupo controle e o que essa "
            "fase efetivamente estabelece, assinale a alternativa correta segundo a aula."
        ),
        "options": {
            "A": "Usa-se placebo, porque só o mascaramento completo com “farinha” isola o efeito específico da nova substância e permite calcular a eficácia verdadeira da medicação.",
            "B": "A fase 3 é feita em voluntários saudáveis, em dezenas de pessoas, para confirmar toxicidade residual antes de administrar a substância a pacientes com câncer de mama.",
            "C": "A aprovação sanitária e a comercialização já ocorreram ao fim da fase 2; a fase 3 existe apenas como farmacovigilância em milhões de usuários da rede pública.",
            "D": "Compara-se a nova substância com o tratamento tradicional em doentes; placebo é antiético em doença grave, e é esta fase que estabelece a eficácia de fato, após a qual pode haver aprovação.",
        },
        "answer": "D",
        "explain": (
            "Fase 1: dezenas de saudáveis — segurança, toxicidade, tolerabilidade. Fase 2: centenas de "
            "doentes — eficácia preliminar. Fase 3: centenas a milhares de doentes com controle = "
            "tratamento padrão (não placebo em doença grave) — eficácia de fato; a aprovação vem depois. "
            "Fase 4: comercializada, milhões, farmacovigilância."
        ),
    },
    {
        "n": 8,
        "tema": "Caso-controle",
        "stem": (
            "Uma doença neurológica rara foi diagnosticada em 150 pessoas; os pesquisadores selecionaram "
            "também 300 sadios da mesma população, avaliaram todos individualmente e investigaram "
            "exposição prévia a um agrotóxico. Por que não se pode calcular diretamente a incidência da "
            "doença entre expostos e não expostos com esses dados?"
        ),
        "options": {
            "A": "Porque o estudo é transversal: exposição e desfecho foram aferidos no mesmo instante, o que impede distinguir casos novos de casos prevalentes na amostra.",
            "B": "Porque os pesquisadores escolheram quantos casos e quantos controles incluir; a proporção de doentes na amostra não reflete a da população, e o caso-controle não analisa incidência.",
            "C": "Porque a doença é rara e a coorte seria o único desenho capaz de medir incidência; qualquer outro estudo observacional produz apenas razões de chances inválidas.",
            "D": "Porque faltou randomização e cegamento, requisitos indispensáveis para transformar frequências amostrais em taxas de incidência cumulativa na população-fonte.",
        },
        "answer": "B",
        "explain": (
            "O caso-controle parte do desfecho já estabelecido (doentes × sadios) e faz retroanálise da "
            "exposição. A fração de casos é definida pelo pesquisador (aqui 150:300), não pela "
            "ocorrência natural. Por isso não se analisa incidência — desvantagem explícita do slide. "
            "As medidas de risco desse desenho são outras (2º bimestre)."
        ),
    },
    {
        "n": 9,
        "tema": "Série temporal",
        "stem": (
            "Em Jardim Olinda (PR), estatísticas mostraram que a mortalidade por cirrose hepática "
            "aumentou de 1959 a 1990, em relação direta com o consumo per capita de álcool e inversa "
            "com o preço das bebidas, sem exame individual dos óbitos. Qual estudo é esse e o que o "
            "diferencia do ecológico clássico?"
        ),
        "options": {
            "A": "Estudo de incidência populacional, porque mede casos novos de morte por cirrose ao longo de três décadas em uma coorte aberta do município.",
            "B": "Ensaio comunitário, já que o preço das bebidas funciona como intervenção econômica alocada ao coletivo e comparada antes e depois da mudança.",
            "C": "Série temporal (estudo ecológico longitudinal): agregado e observacional, com o efeito medido em diversos pontos do tempo; o ecológico clássico é transversal.",
            "D": "Coorte histórica municipal, pois os registros começam no passado (1959) e avançam prospectivamente até 1990, com expostos e não expostos ao álcool.",
        },
        "answer": "C",
        "explain": (
            "Série temporal = agregado, observacional, longitudinal (efeito em vários pontos do tempo). "
            "É “mais de um estudo ecológico” e também gera hipótese. A avaliação antes e depois da "
            "suposta causa permite ver se o efeito flutua como esperado. Não há indivíduos, nem "
            "intervenção alocada pelo pesquisador."
        ),
    },
    {
        "n": 10,
        "tema": "Prevalência pontual",
        "stem": (
            "Durante um ano inteiro registram-se malformações congênitas ao nascimento: cada recém-nascido "
            "é examinado uma única vez, no parto, ainda que as datas do calendário sejam diferentes. "
            "Não há comparação com outra população. Como se classifica esse estudo?"
        ),
        "options": {
            "A": "Estudo de prevalência pontual: descritivo, não analítico, observacional, individuado e transversal; o ponto de referência comum é o nascimento, não o mesmo dia do calendário.",
            "B": "Estudo de prevalência de período, porque o levantamento cobre doze meses e qualquer malformação ocorrida nesse intervalo entra no numerador da medida.",
            "C": "Estudo de incidência neonatal, já que a malformação é um caso novo que se manifesta exatamente no momento do parto e o seguimento dura um ano.",
            "D": "Série de casos hospitalar, pois se descrevem todos os recém-nascidos malformados atendidos no serviço ao longo de um ano civil completo.",
        },
        "answer": "A",
        "explain": (
            "Pontual: todos avaliados no mesmo ponto de referência (nascimento ou dia do recrutamento "
            "militar). O fato de o calendário cobrir um ano não importa. Período seria perguntar se a "
            "condição existiu em algum momento de um intervalo (dor lombar nos últimos 12 meses). "
            "Sem comparação = descritivo, não analítico."
        ),
    },
    {
        "n": 11,
        "tema": "Cegamento",
        "stem": (
            "Em um ensaio de artrose de joelho, participantes e médico assistente ignoram o que é "
            "administrado. O pesquisador, porém, interpreta pessoalmente radiografias e ressonâncias "
            "para decidir se a artrose melhorou. Por que a aula recomenda, nesse cenário, o triplo cego?"
        ),
        "options": {
            "A": "Porque o triplo cego é o único desenho em que o banco de dados também desconhece os códigos, o que elimina qualquer possibilidade de quebra de sigilo estatístico.",
            "B": "Porque o triplo cego substitui a randomização quando a avaliação de imagem é subjetiva e os grupos não puderam ser sorteados de forma equilibrada por sexo e idade.",
            "C": "Porque no duplo cego o médico assistente ainda sabe o tratamento e pode trocar pacientes de grupo por julgamento pessoal, o que o triplo cego impede por definição.",
            "D": "Porque a análise do pesquisador é subjetiva: se ele souber quem tomou o quê, pode ser parcial ao descrever o resultado; no triplo cego só o banco de dados sabe o código.",
        },
        "answer": "D",
        "explain": (
            "Aberto: todos sabem. Simples cego: só pesquisador e médico assistente sabem; participantes "
            "não. Duplo: nem participantes nem médico assistente (o médico trata os grupos igualmente). "
            "Triplo: nem o pesquisador; só o banco de dados — útil quando a avaliação é subjetiva "
            "(interpretar imagens)."
        ),
    },
    {
        "n": 12,
        "tema": "Inquérito",
        "stem": (
            "Uma pesquisa nutricional aplicou questionário de renda e medidas de peso e altura a 3.641 "
            "crianças, encontrando 4% de desnutrição acima de um salário mínimo e 21% abaixo de um quarto "
            "de salário. Qual afirmação distingue corretamente inquérito e tipo de estudo?"
        ),
        "options": {
            "A": "O inquérito é um tipo de estudo analítico transversal; o questionário transforma o levantamento em caso-controle porque compara duas faixas de renda.",
            "B": "O inquérito (questionário ou entrevista) é ferramenta do estudo de prevalência, não um tipo de estudo; o delineamento permanece prevalência, com exposição e evento no mesmo momento.",
            "C": "Como há duas prevalências segundo a renda, o trabalho deixa de ser descritivo e passa a ser uma coorte contemporânea de desnutrição infantil estratificada por salário.",
            "D": "Trata-se de metanálise de inquéritos prévios, pois sintetiza resultados de milhares de indivíduos e aumenta o nível de significância da associação renda-desnutrição.",
        },
        "answer": "B",
        "explain": (
            "Slide: inquérito = administração de perguntas (questionário, entrevista) e é ferramenta do "
            "estudo de prevalência, não um tipo de estudo. O exemplo das 3.641 crianças é prevalência: "
            "sem seleção de casos, levantamento na população, exposição e evento no mesmo momento."
        ),
    },
    {
        "n": 13,
        "tema": "Da incidência à coorte",
        "stem": (
            "Parte-se de um estudo que acompanha 500 obesos sem artrose por cinco anos. Em seguida "
            "acrescentam-se cerca de 500 não obesos, pareados por idade e sexo (diferença de tamanho "
            "tolerada em torno de 10%), e compara-se o surgimento de gonartrose. O que esse acréscimo "
            "muda no nome e nas características do estudo?"
        ),
        "options": {
            "A": "O estudo deixa de ser apenas incidência descritiva e passa a ser coorte clássica: individuada, observacional, longitudinal, descritiva e analítica, com grupo controle.",
            "B": "O estudo vira ensaio clínico, porque criar um grupo controle de não obesos equivale a intervir na exposição para testar se a obesidade causa degeneração articular.",
            "C": "O estudo permanece incidência, pois o desfecho continua sendo casos novos; o grupo adicional só aumenta a amostra e não altera o tipo operativo nem a análise.",
            "D": "O estudo torna-se ecológico, já que agora se comparam dois grupos (médias de IMC) e a unidade de interesse deixa de ser o joelho de cada paciente.",
        },
        "answer": "A",
        "explain": (
            "A coorte nasce da incidência à qual se acrescenta um grupo de comparação. Continua "
            "descrevendo incidência em cada braço, mas passa a ser analítica. É o estudo observacional "
            "mais relevante (e o mais caro e demorado). Ter grupo controle não a torna agregada: cada "
            "indivíduo é examinado (peso, altura, raio X)."
        ),
    },
    {
        "n": 14,
        "tema": "Metanálise",
        "stem": (
            "Uma análise estatística combina e sintetiza resultados de vários estudos sobre o mesmo tema, "
            "incluindo trabalhos divergentes, para aumentar o nível de significância. Qual desvantagem "
            "específica desse procedimento é destacada na aula e nos slides?"
        ),
        "options": {
            "A": "Incapacidade de comparar resultados contraditórios, porque a síntese estatística obriga a descartar qualquer estudo cujo intervalo de confiança cruze o nulo.",
            "B": "Impossibilidade de aumentar a precisão analítica, já que reunir amostras heterogêneas dilui o efeito e reduz a representatividade da evidência combinada.",
            "C": "Viés de publicação, além da dificuldade no tratamento dos dados e da análise estatística complexa, por desprezar trabalhos considerados de insignificância estatística.",
            "D": "Necessidade ética de randomizar novamente todos os participantes originais, o que torna a metanálise experimental e impede seu uso em estudos observacionais.",
        },
        "answer": "C",
        "explain": (
            "Vantagens da metanálise: síntese de informação, aumento da precisão analítica, melhor "
            "representatividade e comparação de resultados contraditórios. Desvantagens: dificuldade no "
            "tratamento de dados, análise estatística complexa e viés de publicação (desprezar trabalhos "
            "por insignificância). Exige conhecimento estatístico aprofundado."
        ),
    },
    {
        "n": 15,
        "tema": "Ensaio comunitário",
        "stem": (
            "Na década de 1990, em país africano com 95% de infecção por hepatite B até os 15 anos, "
            "sortearam-se duas cidades, ofertou-se vacina nos postos (sem obrigar ninguém) e comparou-se "
            "a incidência com as demais cidades. Qual é o delineamento e a sua lógica operativa?"
        ),
        "options": {
            "A": "Ensaio clínico de fase 3, porque a vacina é uma intervenção julgada benéfica, há grupo controle e o desfecho é a eficácia contra um vírus de alta letalidade.",
            "B": "Coorte clássica vacinal, pois os pesquisadores apenas observaram quem optou por se vacinar e acompanharam a história natural da hepatite B nas duas cidades.",
            "C": "Estudo ecológico de vacinação, já que a unidade é a cidade e não se sabe, indivíduo a indivíduo, quem recebeu ou não a dose no posto de saúde.",
            "D": "Ensaio comunitário: experimental, agregado e longitudinal, com alocação da intervenção a comunidades; alternativa quando a aleatorização individual é pouco prática, voltado à prevenção primária.",
        },
        "answer": "D",
        "explain": (
            "Ensaio comunitário = intervenção em nível de comunidades, não de indivíduos. Ideal para "
            "prevenção primária, mais econômico que o clínico, útil quando randomizar indivíduo é "
            "antiético ou pouco prático. Exemplos: vacina contra hepatite B e fluoretação da água. "
            "Desvantagens: difícil isolar a comunidade, difícil observar efeitos colaterais, privação do "
            "benefício ao controle."
        ),
    },
    {
        "n": 16,
        "tema": "Caráter temporal",
        "stem": (
            "Hoje o médico faz eletrocardiograma, exames de sangue e ausculta; em seguida consulta o "
            "prontuário antigo do mesmo paciente. Um aluno afirma que o estudo só seria longitudinal se "
            "houvesse retorno futuro. O que a aula estabelece sobre o caráter temporal?"
        ),
        "options": {
            "A": "A consulta ao prontuário não conta, porque avaliação retrospectiva é sempre transversal: o corte no tempo é o dia de hoje, e o passado serve apenas como anamnese.",
            "B": "Duas avaliações no mesmo paciente já caracterizam estudo longitudinal; a segunda pode estar no futuro ou no passado, de modo que o longitudinal não vai somente para a frente.",
            "C": "O estudo é concorrente apenas se o prontuário tiver sido escrito pelo próprio pesquisador; do contrário, a segunda avaliação não existe do ponto de vista operativo.",
            "D": "Longitudinal exige no mínimo três avaliações, sendo uma no presente, uma no passado e uma no futuro, para distinguir coorte, caso-controle e prevalência de período.",
        },
        "answer": "B",
        "explain": (
            "Transversal: cada pessoa avaliada uma única vez, sem acompanhamento. Longitudinal: pelo "
            "menos duas avaliações. A aula enfatiza que o longitudinal também pode ir ao passado: "
            "presente + prontuário = segunda avaliação. Isso fundamenta caso-controle e coorte histórica "
            "como longitudinais."
        ),
    },
    {
        "n": 17,
        "tema": "Tipo operativo",
        "stem": (
            "Alunos argumentam que toda coorte seria agregada, porque existem um grupo de expostos e um "
            "grupo controle. Usando a analogia das notas da turma, qual é a distinção correta entre "
            "individuado e agregado?"
        ),
        "options": {
            "A": "Agregado é qualquer estudo com dois ou mais braços; individuado é apenas o relato de caso, no qual não existe grupo e cada paciente é a própria unidade de análise.",
            "B": "A coorte é agregada porque se calcula a incidência média de cada grupo; o raio X individual é apenas um meio para obter a média que de fato interessa ao pesquisador.",
            "C": "Se dentro de cada grupo se avalia cada indivíduo (nota de um aluno versus outro), o estudo é individuado; agregado compara coletivos (média da turma com média de outra turma).",
            "D": "Individuado e transversal são sinônimos: avaliado uma vez é individuado; avaliado várias vezes é agregado, independentemente de se olhar pessoa ou cidade.",
        },
        "answer": "C",
        "explain": (
            "Dúvida comum da aula: ter grupo e grupo controle não torna o estudo agregado. No "
            "individuado, cada paciente é analisado. No agregado, comparam-se cidades, países, bairros, "
            "hospitais — a média pode não representar o indivíduo. Agregado é mais fácil e barato; "
            "individuado é mais refinado e difícil."
        ),
    },
    {
        "n": 18,
        "tema": "Estudo de Framingham",
        "stem": (
            "O estudo iniciado em 1949 selecionou 5.127 pessoas de 30 a 59 anos, sem doença coronariana, "
            "de um total de 10.000, com avaliações bianuais por 30 anos, e associou hipertensão, "
            "colesterol, tabagismo, intolerância à glicose e hipertrofia ventricular esquerda ao risco de "
            "DC. Por que esse é o exemplo clássico de coorte?"
        ),
        "options": {
            "A": "Porque reúne pessoas sadias (sem o desfecho), homogêneas em características e heterogêneas nos fatores de risco, com exposições pré-estabelecidas, seguimento rígido e período suficiente.",
            "B": "Porque partiu de doentes coronarianos e sadios, investigando no passado os cinco fatores de risco, o que o torna o caso-controle de maior seguimento da literatura cardiovascular.",
            "C": "Porque a alocação dos 5.127 participantes aos fatores de risco foi experimental e randomizada, fazendo de Framingham o primeiro ensaio clínico comunitário de prevenção coronariana.",
            "D": "Porque utilizou apenas médias municipais de pressão e colesterol em Framingham, caracterizando um estudo ecológico longitudinal de trinta anos sobre mortalidade cardíaca.",
        },
        "answer": "A",
        "explain": (
            "Framingham ilustra os quesitos da coorte: ninguém tinha DC no início; observou-se por "
            "período suficiente (30 anos) com seguimento rígido (bianual); as exposições estavam "
            "definidas; os grupos eram homogêneos em idade/área e heterogêneos nos fatores de risco. "
            "Demonstrou aumento de risco para PA elevada, colesterol, fumo, glicose e HVE."
        ),
    },
    {
        "n": 19,
        "tema": "Observacional versus experimental",
        "stem": (
            "Para saber se o cigarro causa câncer de pulmão, seria antiético sortear pessoas para fumar "
            "duas carteiras por dia durante dez anos. Como, então, se estuda um fator de risco, e o que "
            "é lícito experimentar?"
        ),
        "options": {
            "A": "Experimenta-se o fator de risco em animais na fase pré-clínica e, se tolerável, replica-se em humanos saudáveis na fase 1, nunca em doentes.",
            "B": "Fator de risco pode ser experimentado desde que haja consentimento e cegamento triplo; o que se proíbe é apenas o uso de placebo em doença grave.",
            "C": "O único desenho ético é o caso-controle, porque olha o passado do fumante já doente e dispensa qualquer acompanhamento prospectivo de pessoas sadias.",
            "D": "Fator de risco nunca se experimenta, só se observa (quem optou fumar versus quem não optou); no experimental testa-se algo que se julga benéfico, ainda que a maioria dos ensaios não chegue ao fim.",
        },
        "answer": "D",
        "explain": (
            "Aula: jamais se experimenta fator de risco — o pesquisador seria preso. Observa-se quem "
            "escolheu fumar. No experimental, testa-se o que se julga benéfico (julga, porque não há "
            "certeza). Muitos ensaios param no caminho: a substância curava uma doença e gerava outra, "
            "ou tinha efeitos adversos graves."
        ),
    },
    {
        "n": 20,
        "tema": "Série de casos",
        "stem": (
            "Um serviço de oftalmologia descreve 18 pacientes com complicação raríssima após determinada "
            "técnica cirúrgica, detalhando idade, comorbidades, tempo até o evento e evolução, sem "
            "constituir grupo sem a complicação. Qual identificação e qual limite inferencial estão corretos?"
        ),
        "options": {
            "A": "Relato de caso ampliado: como a entidade é rara, o número de pacientes é irrelevante e o trabalho permanece relato, insuficiente apenas por não ter resumo estruturado.",
            "B": "Série de casos (dez ou mais pacientes, Fletcher et al., 1996), descritiva e não analítica; sem comparador não se estima risco nem se demonstra que a técnica causou a complicação.",
            "C": "Caso-controle sem controles nominais, porque os 18 já são os casos e a ausência de complicação na literatura funciona como controle histórico da mesma técnica.",
            "D": "Coorte retrospectiva cirúrgica, já que há seguimento da evolução pós-operatória e o desfecho (complicação) foi observado após a exposição (técnica).",
        },
        "answer": "B",
        "explain": (
            "Dez ou mais = série de casos. Ser analítico depende de comparar grupos, não do tamanho da "
            "amostra. Sem comparador não se sabe quantos operados não complicaram, nem se outras "
            "técnicas também complicam. O estudo levanta hipótese a ser testada por desenho analítico."
        ),
    },
    {
        "n": 21,
        "tema": "Prevalência de período",
        "stem": (
            "Pergunta-se, uma única vez, se o paciente teve dor lombar em algum momento dos últimos doze "
            "meses. Ele pode ter tido dor no primeiro mês, no terceiro ou só na última semana, e em "
            "qualquer desses casos responde “sim”. Qual é o tipo de prevalência e o caráter temporal?"
        ),
        "options": {
            "A": "Prevalência de período, ainda transversal: cada pessoa é avaliada uma só vez, mas a pergunta captura a existência da condição em algum ponto de um intervalo de tempo.",
            "B": "Prevalência pontual, porque a entrevista ocorre em um único dia e o ponto de referência é a data da coleta, independentemente do intervalo recordado.",
            "C": "Incidência acumulada de doze meses, pois só entram casos novos de dor lombar e o denominador é a população livre de dor no início do período.",
            "D": "Coorte retrospectiva de dor, longitudinal não concorrente, já que o paciente olha para o passado dos últimos doze meses a partir do presente.",
        },
        "answer": "A",
        "explain": (
            "Pontual: mesmo ponto de referência (nascimento, recrutamento). Período: a condição existiu "
            "em algum momento de um intervalo. Nos dois, cada pessoa é vista uma vez = transversal. "
            "Não vira longitudinal só porque a pergunta menciona doze meses."
        ),
    },
    {
        "n": 22,
        "tema": "Exposições pré-estabelecidas",
        "stem": (
            "No segundo ano de uma coorte de obesos versus não obesos para gonartrose, o pesquisador "
            "decide também separar diabéticos, fumantes e praticantes de esporte, embora glicemia, "
            "tabaco e atividade física não tenham sido medidos no início. Qual pré-requisito foi violado?"
        ),
        "options": {
            "A": "Ninguém pode ter o desfecho no início, porque incluir diabetes no meio do caminho transforma a artrose já existente em desfecho prevalente e invalida a incidência.",
            "B": "O seguimento deixou de ser rígido, já que acrescentar variáveis no segundo ano equivale a perder padronização e cria viés de registro típico da coorte histórica.",
            "C": "As exposições devem estar pré-estabelecidas no início; não se pode inserir nova exposição no meio do estudo, pois o exame correspondente já deveria ter sido feito no baseline.",
            "D": "Os desfechos não podem ser múltiplos: a coorte só admite um evento (gonartrose) e qualquer desfecho adicional, ainda que previsto, compromete o protocolo.",
        },
        "answer": "C",
        "explain": (
            "Exposições são fixas no início. Desfechos, ao contrário, podem ser múltiplos (joelho, quadril, "
            "tornozelo; infarto, AVC, dissecção de aorta), desde que imaginados e pontuados no baseline, "
            "para excluir quem já os tinha. Se só se pensa no quadril depois, o caso pode ser prevalência, "
            "não incidência."
        ),
    },
    {
        "n": 23,
        "tema": "Caso-controle versus coorte",
        "stem": (
            "O pesquisador escolhe a doença rara, reúne doentes e sadios parecidos e olha o passado do "
            "suposto fator de exposição. Qual conjunto descreve corretamente direção, concorrência e "
            "indicação desse delineamento?"
        ),
        "options": {
            "A": "Longitudinal prospectivo concorrente, indicado para exposições raras, porque acompanha doentes e sadios para a frente até confirmar a latência prolongada do fator.",
            "B": "Transversal analítico, indicado para doenças de alta incidência, pois casos e controles são avaliados uma única vez no presente com inquérito de exposição atual.",
            "C": "Longitudinal prospectivo não concorrente, equivalente à coorte histórica, com a única diferença de partir do desfecho em vez de partir da exposição ocupacional.",
            "D": "Longitudinal retrospectivo e sempre não concorrente: parte do desfecho, olha para trás; indicado para baixa incidência e latência prolongada; não estabelece incidência.",
        },
        "answer": "D",
        "explain": (
            "Caso-controle: doentes × sadios, retroanálise da exposição. Direção: presente → passado "
            "(retrospectivo), nunca concorrente. Bom para doença rara e latência longa. Vantagens: "
            "rápido, barato, múltiplas exposições, 3 ou 4 controles por caso aumentam poder. "
            "Desvantagens: não analisa incidência, viés de memória, registros, seleção de controles."
        ),
    },
    {
        "n": 24,
        "tema": "Vantagens do estudo ecológico",
        "stem": (
            "Um gestor quer, com baixo custo e rapidez, explorar se a mortalidade cardiovascular varia "
            "com o consumo médio de vinho entre países desenvolvidos, usando alfândega, produção agrícola "
            "e vigilância epidemiológica. Qual potencial e qual limite a aula atribui a esse desenho?"
        ),
        "options": {
            "A": "Confirma causalidade com simplicidade analítica, desde que a correlação seja estatisticamente significativa, o que dispensa estudos individuados posteriores.",
            "B": "É fácil, rápido, barato e gera hipóteses, inclusive sobre impacto de políticas; não serve para concluir, e a média do país pode não representar o indivíduo que bebe vinho.",
            "C": "Permite calcular incidência e risco relativo de morte cardiovascular por taça de vinho, porque o denominador é a população adulta de cada país no ano estudado.",
            "D": "Equivale eticamente a um ensaio comunitário de vinho, já que a “intervenção” é o padrão cultural de consumo alocado naturalmente às nações comparadas.",
        },
        "answer": "B",
        "explain": (
            "Vantagens do ecológico: facilidade, rapidez, baixo custo, impacto de programas/políticas/"
            "legislação, simplicidade analítica, gerar hipóteses. O nome não tem relação com meio "
            "ambiente. Aprofundar a hipótese exige estudo individuado (coorte de taças versus garrafas, "
            "grupos parecidos, critério de exclusão se mudar o consumo)."
        ),
    },
    {
        "n": 25,
        "tema": "Coorte mista",
        "stem": (
            "Uma coorte histórica de asbesto começou nos registros de 2010, chegou a 2026 e, a partir "
            "de hoje, os mesmos trabalhadores continuam sendo examinados até 2030. Como deve ser "
            "nomeado o estudo, segundo a aula?"
        ),
        "options": {
            "A": "A partir de 2026 o nome muda para coorte clássica, porque o seguimento passa a ser concorrente com o tempo e os dados futuros serão padronizados pelo próprio pesquisador.",
            "B": "Passa a ser caso-controle aninhado, pois os mesoteliomas já ocorridos funcionam como casos e os trabalhadores ainda sadios, como controles internos da mesma indústria.",
            "C": "Continua sendo coorte histórica (mista): o uso do registro do passado define o nome; a coorte clássica tem de iniciar no presente, ainda que o seguimento depois se prolongue.",
            "D": "Torna-se ensaio comunitário ocupacional, porque manter o acompanhamento após 2026 implica intervir na vigilância de saúde dos expostos ao asbesto.",
        },
        "answer": "C",
        "explain": (
            "A aula admite a mistura histórica + clássica, mas o nome permanece coorte histórica porque "
            "se usou o registro do passado. Clássica tem de começar no presente. Consentimento já deve "
            "existir desde o início; a avaliação final é pessoal, não só prontuário recente."
        ),
    },
    {
        "n": 26,
        "tema": "Fator de risco pode ser doença",
        "stem": (
            "Crianças com gastroenterite, nenhuma desidratada no início, são agrupadas em só diarreia, "
            "só vômito ou ambos, e observa-se quem desidrata em horas ou dias. Por que isso continua "
            "sendo coorte, ainda que todos já estejam doentes?"
        ),
        "options": {
            "A": "Porque o desfecho é a desidratação, não a gastroenterite; o fator de risco pode ser uma doença (vômito, diarreia), as exposições foram pré-estabelecidas e ninguém tinha o desfecho no início.",
            "B": "Porque qualquer acompanhamento de doentes em enfermaria é ensaio clínico de fase 2, no qual se avalia a eficácia preliminar da hidratação contra o desfecho desidratação.",
            "C": "Porque o estudo é caso-controle: as crianças desidratadas são os casos e as que só tiveram diarreia são os controles sadios da comparação retrospectiva.",
            "D": "Porque o tempo curto (horas) torna o desenho transversal de prevalência de período, medindo a existência de desidratação em algum momento da gastroenterite.",
        },
        "answer": "A",
        "explain": (
            "O fator de risco pode ser uma doença: reinfarto (precisa já ter tido o primeiro infarto) e "
            "gastroenterite (vômito desidrata mais que diarreia; o grupo vômito + diarreia desidrata "
            "ainda mais). “Sadios” na coorte significa sem o desfecho, não necessariamente sem qualquer "
            "doença. Quem já estava desidratado saía do estudo."
        ),
    },
    {
        "n": 27,
        "tema": "Triplo cego",
        "stem": (
            "No triplo cego, nem o participante, nem o médico assistente, nem o pesquisador sabem o que "
            "foi administrado; hoje isso se faz com código de barras ou QR code. Qual é a finalidade "
            "específica de cegar também o pesquisador?"
        ),
        "options": {
            "A": "Impedir o efeito placebo no participante, função que o simples cego já não cumpre quando o médico assistente conhece o envelope do tratamento.",
            "B": "Garantir que o médico trate os grupos igualmente e não troque pessoas de braço por julgamento pessoal, objetivo clássico do cegamento simples.",
            "C": "Substituir a randomização quando o tamanho amostral é pequeno, equilibrando por código os grupos de experimento e controle sem sorteio formal.",
            "D": "Evitar parcialidade do pesquisador na escrita dos resultados quando a avaliação clínica é subjetiva; só o banco de dados conhece o mascaramento.",
        },
        "answer": "D",
        "explain": (
            "Cada nível de cegamento ataca um viés diferente. Participante cego: placebo. Médico "
            "assistente cego: trata igual, não troca de grupo. Pesquisador cego: não fica parcial ao "
            "descrever resultados subjetivos. Se não há subjetividade na avaliação, o duplo cego basta."
        ),
    },
    {
        "n": 28,
        "tema": "Desvantagens do ensaio comunitário",
        "stem": (
            "Na fluoretação da água, não se controla quem bebe ou usa aquela água; compara-se a cidade "
            "com flúor à cidade sem flúor. Além da lógica agregada, quais desvantagens os slides "
            "atribuem a esse tipo de ensaio?"
        ),
        "options": {
            "A": "Custo maior que o do ensaio clínico, necessidade de placebo individual e obrigação ética de randomizar cada morador antes de ofertar o flúor na rede.",
            "B": "Dificuldade de isolar uma comunidade, dificuldade de observar efeitos colaterais e privação do benefício para o grupo-controle que não recebe a intervenção coletiva.",
            "C": "Impossibilidade de avaliar prevenção primária, porque o ensaio comunitário só testa tratamento de doentes já estabelecidos em nível de bairro ou município.",
            "D": "Dependência exclusiva de prontuários antigos, viés de memória dos moradores e incapacidade de gerar qualquer hipótese sobre cárie dentária.",
        },
        "answer": "B",
        "explain": (
            "Slides de desvantagens: (1) difícil isolar a comunidade; (2) difícil observar efeitos "
            "colaterais; (3) privação do benefício ao controle. Vantagens: prevenção primária, alternativa "
            "quando aleatorização individual é antiética/pouco prática, mais econômico que o clínico."
        ),
    },
    {
        "n": 29,
        "tema": "Prevalência versus incidência",
        "stem": (
            "Até determinado ponto da aula, prevalência e incidência compartilham ser descritivas, não "
            "analíticas, observacionais e individuadas. Qual característica as separa de modo decisivo "
            "e como isso aparece na literatura?"
        ),
        "options": {
            "A": "O caráter temporal: prevalência é transversal (corte, “foto”, às vezes usada como sinônimo de estudo transversal); incidência é longitudinal, com acompanhamento de casos novos.",
            "B": "O tipo operativo: prevalência é agregada porque levanta a população; incidência é individuada porque segue cada pessoa até o surgimento da doença.",
            "C": "A ação do pesquisador: prevalência observa, incidência experimenta o surgimento da doença ao induzir o fator de risco no grupo acompanhado.",
            "D": "A presença de grupo controle: prevalência nunca compara, incidência sempre compara expostos e não expostos para calcular risco relativo.",
        },
        "answer": "A",
        "explain": (
            "A aula insiste: conhecendo as características, muitas vezes se descobre o nome do estudo. "
            "Prevalência = transversal (alguns autores usam os termos como sinônimos). Incidência = "
            "longitudinal, sem grupo controle. A coorte é a incidência analítica."
        ),
    },
    {
        "n": 30,
        "tema": "Coorte histórica: vantagens e limites",
        "stem": (
            "Comparada à coorte clássica, a histórica reduz tempo e custo porque tudo já aconteceu nos "
            "registros. Qual é a principal limitação e por que, ainda assim, a clássica é considerada "
            "melhor na aula?"
        ),
        "options": {
            "A": "A histórica não mede incidência; a clássica é melhor apenas porque é concorrente e, por caminhar com o tempo, produz risco relativo interpretável.",
            "B": "A histórica é experimental, o que gera problemas éticos com exposições ocupacionais passadas; a clássica observa e por isso se padroniza melhor.",
            "C": "Depende de registros escritos por outros, com viés de registro, de memória e de padronização; a clássica permite examinar a todos do mesmo modo e organizar melhor o estudo.",
            "D": "A histórica só serve para doenças raras, ao passo que a clássica é o único desenho capaz de estudar latência prolongada como a do mesotelioma por asbesto.",
        },
        "answer": "C",
        "explain": (
            "Quando o próprio pesquisador escreve, escreve tudo igual; prontuário de terceiros “vira "
            "bagunça”. Quanto melhores os registros, mais a histórica se parece com a clássica. Mesmo "
            "assim, a clássica é melhor pela padronização. A histórica é estudo de incidência e é "
            "vantajosa para longa latência (não para doença rara — aí o caso-controle é melhor)."
        ),
    },
]

from questions_rest import QUESTIONS as QUESTIONS_REST

QUESTIONS.extend(QUESTIONS_REST)

# Gabarito embaralhado de verdade (15 de cada; sem 3 iguais seguidas; sem ciclo curto).
TARGET_KEY = "BCACADDCCDBCDBDBCBCDACDAADDBABCADDAABDCBBABADCDACDCBACAABBCB"


def remap_answers(questions: list[dict], target: str) -> None:
    assert len(target) == len(questions)
    for q, want in zip(questions, target):
        old = q["answer"]
        if old == want:
            continue
        q["options"][old], q["options"][want] = q["options"][want], q["options"][old]
        q["answer"] = want


remap_answers(QUESTIONS, TARGET_KEY)



class ExamPDF(FPDF):
    def __init__(self) -> None:
        super().__init__(format="A4", unit="mm")
        self.set_auto_page_break(auto=True, margin=18)
        self.add_font("LSerif", "", str(FONT_DIR / "LiberationSerif-Regular.ttf"))
        self.add_font("LSerif", "B", str(FONT_DIR / "LiberationSerif-Bold.ttf"))
        self.add_font("LSerif", "I", str(FONT_DIR / "LiberationSerif-Italic.ttf"))
        self.add_font("LSerif", "BI", str(FONT_DIR / "LiberationSerif-BoldItalic.ttf"))
        self.add_font("LSans", "", str(FONT_DIR / "LiberationSans-Regular.ttf"))
        self.add_font("LSans", "B", str(FONT_DIR / "LiberationSans-Bold.ttf"))
        self.add_font("LSans", "I", str(FONT_DIR / "LiberationSans-Italic.ttf"))
        self.section = "questoes"

    def header(self) -> None:
        if self.page_no() == 1:
            return
        self.set_fill_color(*NAVY)
        self.rect(0, 0, 210, 12, "F")
        self.set_xy(16, 3.2)
        self.set_font("LSans", "", 8)
        self.set_text_color(*CREAM)
        label = {
            "questoes": "Lista de exercícios  ·  identificar o tipo de estudo",
            "gabarito": "Gabarito oficial  ·  15 A  ·  15 B  ·  15 C  ·  15 D",
            "comentarios": "Gabarito comentado  ·  fundamentação exclusiva da Aula 6",
        }[self.section]
        self.cell(0, 6, "Epidemiologia  ·  Aula 6  ·  Prof. Cássio Zini", align="L")
        self.set_xy(16, 3.2)
        self.cell(178, 6, label, align="R")
        self.set_y(16)

    def footer(self) -> None:
        if self.page_no() == 1:
            return
        self.set_y(-14)
        self.set_draw_color(*LINE)
        self.set_line_width(0.2)
        self.line(16, self.get_y(), 194, self.get_y())
        self.set_font("LSans", "", 8)
        self.set_text_color(*MUTED)
        self.set_y(-12)
        self.cell(0, 6, "Breno Holzmann  ·  turma 78  ·  prova 1º de outubro de 2026", align="L")
        self.set_xy(16, -12)
        self.cell(178, 6, str(self.page_no() - 1), align="R")

    def cover(self) -> None:
        self.add_page()
        self.set_fill_color(*NAVY)
        self.rect(0, 0, 210, 297, "F")
        self.set_fill_color(*STEEL)
        self.rect(0, 0, 7, 297, "F")
        self.set_fill_color(*CREAM)
        self.rect(0, 248, 210, 49, "F")

        self.set_xy(24, 28)
        self.set_font("LSans", "", 10)
        self.set_text_color(196, 210, 220)
        self.cell(0, 6, "MEDICINA  ·  EPIDEMIOLOGIA  ·  AULA 6")

        self.set_xy(24, 48)
        self.set_font("LSerif", "B", 32)
        self.set_text_color(*CREAM)
        self.multi_cell(162, 14, "Lista de exercícios")
        self.set_xy(24, 80)
        self.set_font("LSerif", "I", 16)
        self.set_text_color(210, 220, 228)
        self.multi_cell(162, 8, "Tipos de estudos epidemiológicos,\ndesenhos de pesquisa e coortes")

        self.set_fill_color(*STEEL)
        self.rect(24, 122, 42, 1.2, "F")

        self.set_xy(24, 136)
        self.set_font("LSans", "", 11)
        self.set_text_color(*CREAM)
        lines = [
            "60 questões de múltipla escolha  ·  nível de prova",
            "Identificar o estudo pela leitura: característica, vantagem, desvantagem e exemplo",
            "Fonte exclusiva: apostilas, slides e anotações da Aula 6",
            "Prof. Cássio Zini  ·  17 de setembro de 2026",
        ]
        for line in lines:
            self.set_x(24)
            self.cell(0, 8, line)
            self.ln(8)

        self.set_xy(24, 188)
        self.set_font("LSans", "B", 11)
        self.cell(0, 7, "Como usar")
        self.set_xy(24, 198)
        self.set_font("LSans", "", 10)
        self.set_text_color(210, 220, 228)
        self.multi_cell(
            162,
            5.6,
            "Leia o enunciado como se fosse um artigo. Classifique primeiro as características "
            "(descritivo/analítico, transversal/longitudinal, individuado/agregado, observacional/"
            "experimental) e só então o nome do estudo. Marque uma alternativa. Confira o gabarito "
            "ao final — cada item traz o comentário ancorado no material da aula.",
        )

        self.set_xy(24, 258)
        self.set_font("LSans", "B", 12)
        self.set_text_color(*NAVY)
        self.cell(0, 7, "Breno Holzmann")
        self.set_xy(24, 266)
        self.set_font("LSans", "", 10)
        self.set_text_color(*STEEL)
        self.cell(0, 6, "Turma 78  ·  Simulado para 1º de outubro de 2026")
        self.set_xy(24, 274)
        self.set_font("LSans", "I", 9)
        self.set_text_color(*MUTED)
        self.cell(0, 5, "Gabarito embaralhado  ·  15 respostas A, B, C e D  ·  sem sequência de três iguais")

    def instruction_page(self) -> None:
        self.section = "questoes"
        self.add_page()
        self.set_fill_color(*CREAM)
        self.rect(0, 12, 210, 285, "F")
        self.set_xy(16, 20)
        self.set_font("LSerif", "B", 18)
        self.set_text_color(*NAVY)
        self.cell(0, 10, "Instruções")
        self.ln(12)
        self.set_font("LSans", "", 10)
        self.set_text_color(*INK)
        body = (
            "1. São 60 questões de múltipla escolha, com quatro alternativas (A, B, C, D) e uma única resposta correta.\n\n"
            "2. O enunciado descreve um protocolo ou confronta dois desenhos. O objetivo da prova de 1º de outubro "
            "é identificar o tipo de estudo pela leitura, conhecendo característica, vantagem, desvantagem e exemplo.\n\n"
            "3. No segundo bimestre serão calculadas medidas de risco e de efeito: coorte e caso-controle não compartilham "
            "as mesmas medidas — por isso esta lista treina primeiro o reconhecimento do desenho.\n\n"
            "4. Armadilhas recorrentes da aula: coorte histórica é prospectiva não concorrente (o “retrospectiva” do slide "
            "vem entre aspas); 10 ou mais pacientes = série de casos (Fletcher et al., 1996); ecológico gera hipótese e não "
            "conclui; o nome ecológico não se refere a meio ambiente; inquérito é ferramenta, não tipo de estudo; fator de "
            "risco nunca se experimenta; todo experimental é longitudinal; caso-controle não estabelece incidência; fase 3 "
            "em doença grave não usa placebo; grupo controle não torna o estudo agregado.\n\n"
            "5. Não há consulta. Marque à tinta. Tempo sugerido: 90 a 120 minutos. Gabarito e comentários ao final."
        )
        self.multi_cell(178, 5.8, body)
        self.ln(8)
        self.set_fill_color(*WHITE)
        self.set_draw_color(*LINE)
        self.set_line_width(0.3)
        x, y, w, h = 16, self.get_y(), 178, 42
        self.rect(x, y, w, h, "FD")
        self.set_xy(x + 6, y + 5)
        self.set_font("LSans", "B", 10)
        self.set_text_color(*STEEL)
        self.cell(0, 6, "Temas cobertos")
        self.set_xy(x + 6, y + 13)
        self.set_font("LSans", "", 9)
        self.set_text_color(*INK)
        self.multi_cell(
            w - 12,
            5,
            "Características (descritivo/analítico, temporal, operativo, ação do investigador)  ·  "
            "relato e série de casos  ·  prevalência (pontual e de período) e inquérito  ·  incidência  ·  "
            "coorte clássica, histórica e mista  ·  caso-controle  ·  metanálise  ·  ecológico, série temporal "
            "e falácia ecológica  ·  ensaio clínico (fases e cegamento)  ·  ensaio comunitário.",
        )

    def questions_pages(self) -> None:
        self.section = "questoes"
        self.add_page()
        self.set_fill_color(*CREAM)
        # fill remaining page background via rect each page in header? skip, white paper with cream accents
        for q in QUESTIONS:
            needed = 42
            if self.get_y() + needed > 275:
                self.add_page()
            self._draw_question(q)

    def _draw_question(self, q: dict) -> None:
        y0 = self.get_y()
        if y0 > 250:
            self.add_page()
            y0 = self.get_y()

        self.set_fill_color(*STEEL)
        self.rect(16, self.get_y(), 8, 7, "F")
        self.set_xy(16, self.get_y() + 0.6)
        self.set_font("LSans", "B", 9)
        self.set_text_color(*CREAM)
        self.cell(8, 6, f"{q['n']:02d}", align="C")
        self.set_xy(26, self.get_y())
        self.set_font("LSans", "B", 9)
        self.set_text_color(*STEEL)
        self.cell(0, 6, q["tema"].upper())
        self.ln(9)

        self.set_font("LSerif", "", 11)
        self.set_text_color(*INK)
        self.set_x(16)
        self.multi_cell(178, 5.6, q["stem"])
        self.ln(2.5)

        for letter in "ABCD":
            if self.get_y() > 272:
                self.add_page()
            text = f"{letter})  {q['options'][letter]}"
            self.set_font("LSans", "", 10)
            self.set_text_color(*INK)
            self.set_x(16)
            self.multi_cell(178, 5.2, text)
            self.ln(1.6)

        self.ln(3)
        self.set_draw_color(*LINE)
        self.set_line_width(0.2)
        self.line(16, self.get_y(), 194, self.get_y())
        self.ln(5)

    def gabarito_page(self) -> None:
        self.section = "gabarito"
        self.add_page()
        self.set_font("LSerif", "B", 18)
        self.set_text_color(*NAVY)
        self.cell(0, 10, "Gabarito")
        self.ln(8)
        self.set_font("LSans", "", 10)
        self.set_text_color(*INK)
        self.multi_cell(
            178,
            5.5,
            "Proporção exigida: 15 A, 15 B, 15 C e 15 D, embaralhadas, sem três letras iguais consecutivas. "
            "Confira primeiro o quadro; os comentários vêm na seção seguinte.",
        )
        self.ln(6)

        col_w = 28.5
        row_h = 8
        headers = ["Nº", "Resp.", "Nº", "Resp.", "Nº", "Resp.", "Nº", "Resp.", "Nº", "Resp.", "Nº", "Resp."]
        # 6 columns of (n, answer) = 10 questions per row... 60/6 = 10 rows. Better: 4 columns of 15.
        groups = [QUESTIONS[i * 15 : (i + 1) * 15] for i in range(4)]
        col_width = 44
        x0 = 16
        y0 = self.get_y()

        for i, title in enumerate(["1–15", "16–30", "31–45", "46–60"]):
            self.set_xy(x0 + i * col_width, y0)
            self.set_fill_color(*NAVY)
            self.set_text_color(*CREAM)
            self.set_font("LSans", "B", 9)
            self.cell(col_width - 4, 8, title, align="C", fill=True)

        for row in range(15):
            for col, group in enumerate(groups):
                q = group[row]
                x = x0 + col * col_width
                y = y0 + 8 + row * row_h
                fill = CREAM if row % 2 == 0 else WHITE
                self.set_fill_color(*fill)
                self.rect(x, y, col_width - 4, row_h, "F")
                self.set_xy(x + 2, y + 1.2)
                self.set_font("LSans", "", 9)
                self.set_text_color(*MUTED)
                self.cell(12, 6, f"{q['n']:02d}")
                self.set_font("LSans", "B", 11)
                self.set_text_color(*NAVY)
                self.cell(18, 6, q["answer"])

        self.set_y(y0 + 8 + 15 * row_h + 10)
        counts = {k: sum(1 for q in QUESTIONS if q["answer"] == k) for k in "ABCD"}
        self.set_font("LSans", "", 9)
        self.set_text_color(*MUTED)
        seq = "".join(q["answer"] for q in QUESTIONS)
        self.multi_cell(
            178,
            5,
            f"Contagem: A = {counts['A']}   B = {counts['B']}   C = {counts['C']}   D = {counts['D']}.  "
            f"Sequência: {seq}",
        )

    def comments_pages(self) -> None:
        self.section = "comentarios"
        self.add_page()
        self.set_font("LSerif", "B", 18)
        self.set_text_color(*NAVY)
        self.cell(0, 10, "Gabarito comentado")
        self.ln(4)
        self.set_font("LSans", "I", 10)
        self.set_text_color(*STEEL)
        self.multi_cell(
            178,
            5.4,
            "Cada comentário restringe-se ao que foi dito em aula e nas apostilas. Não há conteúdo externo.",
        )
        self.ln(6)

        for q in QUESTIONS:
            if self.get_y() > 248:
                self.add_page()
            self.set_fill_color(*NAVY)
            self.rect(16, self.get_y(), 8, 7, "F")
            self.set_xy(16, self.get_y() + 0.5)
            self.set_font("LSans", "B", 9)
            self.set_text_color(*CREAM)
            self.cell(8, 6, f"{q['n']:02d}", align="C")
            self.set_xy(26, self.get_y())
            self.set_font("LSans", "B", 10)
            self.set_text_color(*STEEL)
            self.cell(120, 6, q["tema"])
            self.set_font("LSans", "B", 10)
            self.set_text_color(*NAVY)
            self.cell(0, 6, f"Resposta: {q['answer']}", align="R")
            self.ln(8)
            self.set_font("LSans", "", 10)
            self.set_text_color(*INK)
            self.set_x(16)
            self.multi_cell(178, 5.3, q["explain"])
            self.ln(5)


def validate() -> None:
    assert len(QUESTIONS) == 60, len(QUESTIONS)
    nums = [q["n"] for q in QUESTIONS]
    assert nums == list(range(1, 61)), nums
    counts = {k: 0 for k in "ABCD"}
    seq: list[str] = []
    for q in QUESTIONS:
        assert set(q["options"]) == set("ABCD")
        assert q["answer"] in "ABCD"
        stem_n = wc(q["stem"])
        assert stem_n >= 20, (q["n"], stem_n, q["stem"])
        counts[q["answer"]] += 1
        seq.append(q["answer"])
        for letter, text in q["options"].items():
            n = wc(text)
            if n < 15:
                print(f"aviso: Q{q['n']} {letter} tem {n} palavras")
    assert counts == {k: 15 for k in "ABCD"}, counts
    for i in range(len(seq) - 2):
        assert not (seq[i] == seq[i + 1] == seq[i + 2]), (i + 1, seq)
    print("validação ok:", "".join(seq), counts)


def dump_json() -> None:
    JSON_OUT.parent.mkdir(parents=True, exist_ok=True)
    payload = []
    for q in QUESTIONS:
        payload.append(
            {
                "id": q["n"],
                "tema": q["tema"],
                "stem": q["stem"],
                "options": q["options"],
                "answer": q["answer"],
                "explain": q["explain"],
            }
        )
    JSON_OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("json:", JSON_OUT)


def write_pdf() -> None:
    pdf = ExamPDF()
    pdf.cover()
    pdf.instruction_page()
    pdf.questions_pages()
    pdf.gabarito_page()
    pdf.comments_pages()
    PDF_PUBLIC.parent.mkdir(parents=True, exist_ok=True)
    PDF_ARTIFACTS.parent.mkdir(parents=True, exist_ok=True)
    pdf.output(str(PDF_PUBLIC))
    pdf.output(str(PDF_ARTIFACTS))
    print("pdf:", PDF_PUBLIC)
    print("pdf:", PDF_ARTIFACTS)


if __name__ == "__main__":
    validate()
    dump_json()
    write_pdf()
