import math
unghi_grade=int(input('Dati valoarea in grade'))
unghi_rad=math.radians(unghi_grade)
print('sinusul de',unghi_grade,'grade =',round( math.sin(unghi_rad),4))
print('cosinusul de',unghi_grade,'grade =',round( math.cos(unghi_rad),4))