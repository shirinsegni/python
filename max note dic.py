note={
    "sherin":20,
    "moetaz":19,
    "wassim":17
    }
meilleur=""
max=0
for nom in note:
    if note[nom]>max:
        max=note[nom]
        meilleur=nom
print("meilleur:",meilleur)
print("maximum=",max)