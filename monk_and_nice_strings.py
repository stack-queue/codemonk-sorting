n = int(input())

liste = []

for index in range(n):
    liste.append(input())

for index, item in enumerate(liste):
    count = 0
    for string in liste[:index]:
        if string < item:
            count +=1
    print(count)
