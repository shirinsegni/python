#Ouvrir un fichier :
open()
#Écriture dans un fichier
f = open("test.txt","w")
f.write("Bonjour")
f.close()
#Lire un fichier
f = open("test.txt","r")
contenu = f.read()
print(contenu)
f.close()