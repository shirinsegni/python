def est_pair(nbr):
    if nbr%2==0:
        return True
    else :
        return False
n=int(input("donner un nbr:"))
if est_pair(n):
    print("paire")
else:
    print("impaire")
    
