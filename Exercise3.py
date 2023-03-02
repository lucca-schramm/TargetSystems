"""3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
"""
import pandas as pd

df= pd.read_json("dados.json")

df.drop(df.loc[df['valor']<1].index, inplace=True)
soma=df['valor'].sum()
count=df['valor'].count()
med=soma/count
df_1 = (df.loc[df['valor']>med])
x=df_1['valor'].count()

min=df['valor'].min()
max=df['valor'].max()

print(f'O menor valor de faturamento foi: {min}')
print(f'O maior valor de faturamento foi: {max}')
print(f'A média de faturamento foi: {med}')

print(f'Em {x} dias houve faturamento superior à média mensal.')