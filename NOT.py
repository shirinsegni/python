note = float(input("Entrer la note: "))

if note < 10:
    print("Insuffisant")
elif note < 12:
    print("Passable")
elif note < 16:
    print("Bien")
else:
    print("Très Bien")