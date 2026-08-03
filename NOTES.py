note = float (input("donner la moyenne "))
if note < 0 or note >20:
    print ("invalide")
elif note <10:
    print ("inssufisant")
elif note <12 :
    print("passable")
elif note <16 :
    print("montion bien ")
else  :
    print("montion tres bien ")