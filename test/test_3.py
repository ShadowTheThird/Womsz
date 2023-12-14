#Uzupełnij definicję generatora get_random_dna 
#tak aby generował on losową sekwencję DNA
#w miejsce .... wpisz odpowiednie wyrażenia

import random

#Kod do modyfikacji
def get_random_dna(count):
  print("Rozpoczynam generowanie sekwencji DNA")
  bp=['A','C','G','T']
  output = ""
  for x in range(0,count):
    output += random.choice(bp)
  print("\nsekwencja została wygenerowana")
  return output

#Koniec kodu do modyfikacji#
bps_generator = get_random_dna(10)
#print(type(bps_generator))
for i in bps_generator:
   print(i,end="")