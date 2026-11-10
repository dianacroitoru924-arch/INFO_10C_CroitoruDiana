#Eticheta elevului
prenume: str=input()
varsta: int=int(input())
print(prenume, varsta)

#2. Actualizarea unui stoc
s: int= int(input('Valoarea stocului initial este:'))
p: int= int(input('Valoarea actualizarii:'))
s+=p
print(s)

#3. Schimbul valorilor
a=2
b=4
a,b=b,a
print(a,b)

#4.Pretul fix al unui caiet
PRET_CAIET=8.50
n=int(input('Numarul de caiete este:'))
total=n*PRET_CAIET
print(f'Costul total este: {total:.2f}')

