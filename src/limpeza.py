"""Funções de apoio à exploração e limpeza dos dados do projeto Teste Vocacional.

Uso nos notebooks (pasta notebook/):

    import sys
    sys.path.append('../src')
    from limpeza import relatorio_valores_ausentes_por_coluna
"""

import re

import numpy as np
import pandas as pd


# Nomes das 48 colunas RIASEC: R1...R8, I1...I8, A1...A8, S1...S8, E1...E8, C1...C8
COLUNAS_RIASEC = [f'{letra}{numero}' for letra in 'RIASEC' for numero in range(1, 9)]


# ---------------------------------------------------------------------------
# Valores ausentes
# ---------------------------------------------------------------------------

def calcular_porcentagem_valores_ausentes(data):
    """Exibe a porcentagem de células vazias (NaN) no DataFrame inteiro."""
    # Calcula o total de células do dataset
    total_de_celulas = np.prod(data.shape)
    # Conta o número de valores ausentes por coluna
    quantidade_ausentes_por_coluna = data.isnull().sum()
    # Calcula o total de valores ausentes em todo o conjunto de dados
    total_ausentes = quantidade_ausentes_por_coluna.sum()
    # Calcula a porcentagem de valores ausentes em relação ao total de células
    porcentagem_ausentes = (total_ausentes / total_de_celulas) * 100
    # Exibe a porcentagem de valores ausentes no conjunto de dados
    print(f"O conjunto de dados tem {round(porcentagem_ausentes, 2)}% de valores ausentes.")


def obter_porcentagem_valores_ausentes(data):
    """Versão com return: DEVOLVE a porcentagem de células vazias em vez de apenas exibir."""
    total_de_celulas = np.prod(data.shape)
    quantidade_ausentes_por_coluna = data.isnull().sum()
    total_ausentes = quantidade_ausentes_por_coluna.sum()
    porcentagem_ausentes = (total_ausentes / total_de_celulas) * 100
    # Devolve a porcentagem para quem chamou a função
    return porcentagem_ausentes


def relatorio_valores_ausentes_por_coluna(data):
    """Tabela com quantidade, porcentagem e tipo de dado das colunas que possuem ausentes."""
    quant_valores_ausentes = data.isnull().sum()
    porcent_valores_ausentes = 100 * quant_valores_ausentes / len(data)
    tipo_de_dado = data.dtypes
    # axis=1 junta as três Series lado a lado, como colunas
    resumo_valores_ausentes = pd.concat([quant_valores_ausentes, porcent_valores_ausentes, tipo_de_dado], axis=1)
    # Renomeia as colunas
    resumo_valores_ausentes.columns = ['Quantidade de Ausentes', 'Porcentagem de Ausentes', 'Tipo de Dado']
    # Remove as colunas sem valores ausentes e classifica em ordem decrescente por porcentagem de valores ausentes
    resumo_valores_ausentes = resumo_valores_ausentes[resumo_valores_ausentes['Quantidade de Ausentes'] > 0].sort_values('Porcentagem de Ausentes', ascending=False).round(2)
    # Exibe um resumo do relatório
    print(f"O conjunto de dados tem {data.shape[1]} colunas. \nForam encontradas {resumo_valores_ausentes.shape[0]} colunas com valores ausentes.")
    # Retorna o DataFrame com informações sobre valores ausentes por coluna
    return resumo_valores_ausentes


def relatorio_zeros_por_coluna(data, colunas):
    """Tabela com quantidade e porcentagem de zeros nas colunas informadas (0 = não respondeu)."""
    # (data[colunas] == 0) gera True onde o valor é zero; o .sum() conta os True de cada coluna
    quant_zeros = (data[colunas] == 0).sum()
    porcent_zeros = 100 * quant_zeros / len(data)
    # axis=1 junta as duas Series lado a lado, como colunas
    resumo_zeros = pd.concat([quant_zeros, porcent_zeros], axis=1)
    # Renomeia as colunas
    resumo_zeros.columns = ['Quantidade de Zeros', 'Porcentagem de Zeros']
    # Mantém só as colunas com zeros, da maior para a menor
    resumo_zeros = resumo_zeros[resumo_zeros['Quantidade de Zeros'] > 0].sort_values('Porcentagem de Zeros', ascending=False).round(2)
    # Exibe um resumo do relatório
    print(f"Das {len(colunas)} colunas analisadas, {resumo_zeros.shape[0]} possuem valores zero.")
    return resumo_zeros


# ---------------------------------------------------------------------------
# Classificação dos cursos em áreas de formação
# ---------------------------------------------------------------------------

# Dicionário: área de formação (CINE Brasil) -> padrão de palavras-chave (expressão regular)
# A ORDEM IMPORTA: a primeira área cujo padrão for encontrado no curso é a escolhida
mapa_areas = {
    'Sem curso': r'^(no|none|n a|na|nothing|other|undecided|undeclared|not applicable|nope|null|x|unknown|idk|yes|high school|senior high school|not sure|never|nil|n|no major|not yet|general|general studies)$|^(i )?(did not|didn t|didnt|have not|haven t|havent|never|dont|don t) ',
    'Computação e TIC': r'comput|\bit\b|\bict\b|\bmis\b|information tech|software|informatic|information system|data science|\bcs\b|programming|cyber|networking',
    'Engenharia, produção e construção': r'engin|architect|construction|mechatronic|electronic|manufactur|automotive|aeronaut|petroleum|mining|urban planning|surveying|food tech|industrial tech|welding|mechanics|^(civil|mechanical|electrical)$',
    'Saúde e bem-estar': r'nurs|medic|pre med|doctor|pharm|dentist|dental|health|physiolog|physiother|physical therap|occupational|kinesiol|nutrition|dietet|mbbs|surg|optom|radiolog|paramedic|social work|social services|rehab|recreation|midwif|speech|veterinar|sport|exercise|athletic',
    'Negócios, administração e direito': r'b\w*s\w*ness|account|\bcpa\b|financ|\becon|\bbba\b|market|advertis|manag|commerce|\blaw|legal|juris|human resource|\bhrm?\b|administra|\bmba\b|entrepreneur|banking|real estate|insurance|logistic|supply chain|paralegal|hospitality|tourism|leadership',
    'Ciências sociais, comunicação e informação': r'ps\w*chol|\bpsy|\bpys|\bpsc|\bpych|psic|psik|phych|sociol|politic|government|public policy|anthropol|international|global studies|asian studies|communica|journal|media|geograph|social science|public relations|criminol|library|counsel|human servic|human relations|criminal|human development|child development|family studies|gender stud|social stud',
    'Ciências naturais, matemática e estatística': r'biolog|\bbio|chemi|physic|math|statist|science|zoolog|ecolog|environment|geolog|marine|astronom|neuro|genetic|microbio|botan|forensic',
    'Educação': r'educat|teach|pedagog|early child',
    'Artes e humanidades': r'\barts?\b|english|histor|archaeolog|philosoph|music|design|illustrat|literat|language|linguist|translat|theat|acting|theolog|relig|biblical|ministry|film|cinema|writing|french|spanish|german|russian|chinese|japanese|filipino|philolog|dance|fashion|photograph|humanit|liberal|classic|creative|animation|drama|culinary|american studies',
    'Agricultura e veterinária': r'agric|forest|agronom|animal science|horticult',
    'Serviços': r'hotel|police|fire|military|security|aviation|pilot|cosmetol|beauty',
}


def mapear_area(curso):
    """Devolve a área de formação de um curso já padronizado (minúsculo, só letras)."""
    # Percorre as áreas na ordem do dicionário
    for area, padrao in mapa_areas.items():
        # re.search procura o padrão em qualquer parte do texto do curso
        if re.search(padrao, curso):
            return area
    # Nenhum padrão encontrado
    return 'Não classificado'
