INPUT="""
Mikołaj, Mikołaj jedzie samochodem
bo gdzieś zgubił saneczki w tę mroźną pogodę.

Ref. U - chu . cha, tra . la . la
Co to za Mikołaj?
U - chu . cha, tra . la . la
Co to za Mikołaj?
"""

OUTPUT="cha, tra";

print(INPUT)
print("\n\n")
######     Kod do modyfikacji     #####
#Zadanie: Zmodyfikuj kod we wskazanych poniżej miejscach tak,
#aby zawartość zmiennej wynik była równa:
#"cha, tra"
#Uwaga: konstrukcja wynik="cha, tra" nie
#jest dopuszczalnym rozwiązaniem

tmp=INPUT.split(" . ")
wynik=tmp[1] #Podpowiedz wykorzystaj tablicę tmp

###### Koniec kodu do modyfikacji #####
if (wynik == OUTPUT):
  print("{0}\nTest 1: OK\n".format(wynik))
else:
  print("Twój wynik:\n{0} \nTest 1: ERROR\n".format(wynik))
  print( "Prawidłowy wynik to: {0}\n".format(OUTPUT))