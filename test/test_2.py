import re
INPUT="""
Rano rano rano budzi się się życie
Nowy nowy, kolejny dzień dzień
Śniegiem śniegiem wszystko okryte
Słońce przebija przebija przebija się
Tańczy na szybach mróz
W saniach płyniemy już
"""

OUTPUT="""
Rano budzi się życie
Nowy, kolejny dzień
Śniegiem wszystko okryte
Słońce przebija się
Tańczy na szybach mróz
W saniach płyniemy już
"""

print("Dane wejściowe")
print(INPUT)
print("\n\n")
######     Kod do modyfikacji     #####
#Zadanie: Zmodyfikuj kod we wskazanych poniżej miejscach tak,
#aby usunąć powtórzenia wyrazów w łańcuchu INPUT. Tekst wynikowy
#powinien znaleźć się w zmiennej wynik
def duplikatySio(we: str) ->str:
   """To jest Twoja implementacja funkcji usuwającej duplikaty
   zaimplementuj ją z wykorzystaniem wyrażeń regularnych"""
   return re.sub(r'\b(\w+)\b(\s+\1\b)+',r'\1',we, flags=re.I) #Zmodyfikuj funkcję - podpowiedź wykorzystaj wyrażenia regularne

wynik=duplikatySio(INPUT)

###### Koniec kodu do modyfikacji #####
if (wynik == OUTPUT):
  print("{0}\nTest 1: OK\n".format(wynik))
else:
  print("Twój wynik:\n{0} \nTest 1: ERROR\n".format(wynik))
  print( "Prawidłowy wynik to: {0}\n".format(OUTPUT))