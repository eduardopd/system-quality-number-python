import math
from pandas import read_excel, ExcelFile

def converte_str_float(val):
    """
     - Converte string para float
    """

    if ',' in val:
        new_val = val.replace(',','.')
    else:
        new_val = val.replace('.','.')

    return float(new_val)

df = read_excel("/Users/...")

# Trata o arquivo enviado pelo usuário. Utilizar Resultado_Financeiro e Resultado_Pontos como nomes das colunas.

df['Resultado_Financeiro'] = df['Resultado_Financeiro'].astype(str)
df['Resultado_Pontos'] = df['Resultado_Pontos'].astype(str)

df['Resultado_Financeiro'] = df['Resultado_Financeiro'].apply(converte_str_float)
df['Resultado_Pontos'] = df['Resultado_Pontos'].apply(converte_str_float)

df['Resultado_Financeiro'] = df['Resultado_Financeiro'].astype(float)
df['Resultado_Pontos'] = df['Resultado_Pontos'].astype(int)

# Define variáveis de apoio para o cálculo do SQN

trades_negativos = (df.loc[df['Resultado_Pontos'] <= 0])

num_trades = len(df)

r = (trades_negativos.loc[:, "Resultado_Financeiro"].mean())

expectativa = (df.loc[:, "Resultado_Financeiro"] / (-r)).mean()

multiplos_r = (df.loc[:, "Resultado_Financeiro"] / (-r))
desvio_padrao = multiplos_r.std()

raiz_num_trades = math.sqrt(num_trades)

sqn = round(((expectativa / desvio_padrao) * raiz_num_trades), 3)

print(sqn)

"""
    - Avalia SQN de acordo com tabela de Van K Tharp
    Menor que 1.0 -> Ruim
    De 1.01 até 2.0 -> Na média
    De 2.01 até 3.0 -> Bom
    De 3.01 até 5.0 -> Excelente
    De 5.01 até 7.0 -> Muito excelente
    Acima de 7.01 -> Imaculado
"""