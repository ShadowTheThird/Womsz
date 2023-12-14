def nowy_lad(mamona):
    def ulga(arg):
        w=mamona(arg)*0.91
        return w
    return ulga
###########Kod do modyfikacji###########
#Zmodyfikuj działanie funkcji wyplata###
#za pomocą dekoratora -vide powyżej  ###
########################################

@nowy_lad
def wyplata(pensja):
    return 0.7*pensja

#Koniec kodu do modyfikacji#
if (wyplata(100)==70):
    print("Nie uwzględniono wpływu nowy_lad na wysokość wypłaty-wprowadź poprawkę")
else:
    print("Wypłacono pensję w wysokości {0}".format(wyplata(100)))