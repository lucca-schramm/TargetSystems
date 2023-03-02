"""4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.
"""
dict={
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.45,
    "Outros": 19849.53
}

total = sum(dict.values())

for i in dict.values():
    percent = 100* i/total
    percent = round(percent)
    print(str(percent)+"%")

