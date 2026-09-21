#Problema 3
a=3
P=4*a
A=6*a**2
V=a**3
print('Perimentrul=', P)
print('Aria=', A)
print('Volumul=', V)
#Problema 4
n=2
cm=n*100
mg=n*1000000
luni=n*12
zile=n*365
saptamani=zile//7
print('metrii in centimentri=',cm)
print('kilograme in miligrame=',mg)
print('ani in saptamani=',saptamani)
print('ani in zile=',zile)
#Problema 5
x=True
y=False
print(x and y)
print(x or y)
print(not x)
print(not y)
#Problema 6
n1=8726
print('ultima cifra al acestui numar este',n1%10)
print('penultima cifra al acestui numar este', (n1//10)%10)
print('restul impartitii acestui numar cu 9 este', n1%9)
print('catul impartirii acestui numar cu 9 este', int(n1/9))
print('suma cifrelor acestui numar este', (n1//1000)+((n1//100)%10)+((n1//10)%10)+(n1%10))
print('rasturnatul acestui numar este', (n1%10)*1000+((n1//10)%10)*100+((n1//100)%10)*10+(n1//1000))
