#Treść zadania:
#Dla podnej wejściowej sekwencji jednoliterowej
#wypisz sekwencję w notacji trzyliterowej.
#Tablica kodów:
#A,ALA R,ARG N,ASN D,ASP C,CYS Q,GLN E,GLU G,GLY H,HIS I,ILE L,LEU K,LYS M,MET F,PHE P,PRO S,SER T,THR W,TRP Y,TYR V,VAL

INPUT="VARNDCQEGHHILKMFPSTWYVARNDCQEGHHILKMFPSTWY"
OUTPUT="VAL,ALA,ARG,ASN,ASP,CYS,GLN,GLU,GLY,HIS,HIS,ILE,LEU,LYS,MET,PHE,PRO,SER,THR,TRP,TYR,VAL,ALA,ARG,ASN,ASP,CYS,GLN,GLU,GLY,HIS,HIS,ILE,LEU,LYS,MET,PHE,PRO,SER,THR,TRP,TYR"

######### Kod do modyfikacji #########
#Dane wejściowe są w zmiennej INPUT
#Wynik należy umieścić w zmiennej wynik
def amino1na3(sekw:str)->str:
   """Funkcja konwertująca sekwencję w notacji 1 literowej na sekwencję w notacji trzyliterowej -
      aminokwasy powinny być oddzielone przecinkami"""
   #Zainicjalizuj słownik - wykorzystaj list comprehensions
   alfabet = "A,ALA R,ARG N,ASN D,ASP C,CYS Q,GLN E,GLU G,GLY H,HIS I,ILE L,LEU K,LYS M,MET F,PHE P,PRO S,SER T,THR W,TRP Y,TYR V,VAL"
   slownik=dict()
   for i in range(0, len(alfabet), 6):
     slownik[alfabet[i]] = alfabet[i+2:i+5]
   #Zbuduj nowy łańcuch w pętli koarzystając z sekw i slownik
   output=""
   for i in range(0, len(sekw)):
    output += slownik[sekw[i]]
    if i != len(sekw)-1:
      output += ','
   return output

wynik=amino1na3(INPUT)

###### Koniec kodu do modyfikacji #####

if (wynik == OUTPUT):
  print("{0}\nTest 1: OK\n".format(wynik))
else:
  print("Twój wynik:\n{0} \nTest 1: ERROR\n".format(wynik))
  print( "Prawidłowy wynik to: \n{0}\n".format(OUTPUT))