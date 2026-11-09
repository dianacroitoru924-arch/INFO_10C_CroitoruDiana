#Stocul inițial disponibil în magazin
stoc=100
#Cantitatea primită recent
cantitate_primita=25
#Actualizarea stocului (stoc= stoc+cantitate_primita)
stoc+=cantitate_primita
print('Stocul actulizat este:', stoc)

a=10
b=20
#Schimbarea valorilor intre ele
a,b=b,a
print(f"a={a}, b={b}")
      
#Definirea unei constante
TARIF=3.0
ore_lucrate=8
cost_total= ore_lucrate*TARIF
print(f'Costul total este: {cost_total}')

