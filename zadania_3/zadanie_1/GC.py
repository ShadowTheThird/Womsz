ifile = open("E:\Programowanie\Womsz\zadania_3\zadanie_1\sekwencja.txt", "r")

def GC(seq: str):
    counter = 0
    for i in seq:
        if i == "G" or i == "C":
            counter += 1
    return (counter*100)/len(seq)

dictionary = {}
for i in ifile:
    if i[0] == ">":
        name = i
        seq = ifile.readline()
        dictionary[name] = GC(seq)
for key, value in dictionary.items():
    print(key, ":\t", value, "%")