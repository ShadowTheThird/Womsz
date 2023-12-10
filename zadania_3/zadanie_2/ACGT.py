ifile = open("E:\Programowanie\Womsz\zadania_3\zadanie_1\sekwencja.txt", "r")

def ACGT(seq: str):
    element = [0,0,0,0]
    for i in seq:
        if i == 'A':
            element[0] += 1
        elif i == 'C':
            element[1] += 1
        elif i == 'G':
            element[2] += 1
        else:
            element[3] += 1
    return element

seq = ""
for i in ifile:
    if i[0] == ">":
        seq += ifile.readline()
array = ACGT(seq)
print("A\tC\tG\tT")
print(f"{array[0]}\t{array[1]}\t{array[2]}\t{array[3]}")
        