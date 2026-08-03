n=int(input("combien de nbr:"))
list =[]
for i in range(n):
    nbr=int(input("donner un nbr"))
    list.append(nbr)
print(list)
list.sort()
list.remove(5)
print(list)
