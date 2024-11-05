#Resposta 

Notas = [100, 50, 20, 10, 5, 2]
Moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

cash = float(input())
print('NOTAS:')

for i in Notas:
    qtd = int(cash // i)
    cash = cash % i
    print(f'{qtd} nota(s) de R$ {i}.00')

print('MOEDAS:')
for i in Moedas:
    qtd = int(cash // i)
    cash = cash % i
    if cash < 0.01:
        cash = round(cash, 2)
    print(f'{qtd} moeda(s) de R$ {i:.2f}')