Putere=int(input('Dati Puterea(W):'))
Timp=int(input('Dati Timmpul(h):'))
Energie=Putere*Timp/1000
print(f'Spre achitare {Energie:.2f}kW/h')
Tarif=float(input('Dati tariful actual:'))
Cost=Energie*Tarif
print(f'Spre achitare {Cost:.2f}lei')