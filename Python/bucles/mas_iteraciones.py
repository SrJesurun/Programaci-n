
frutas = ["banana","manzana","ciruela","pera","naranja","granada","durazno"]

#evitando que se coma una granada con la sentecia continue
for fruta in frutas:
    if fruta =="granada":
        continue
    print(f"me voy a comer una {fruta}")
    
#evitar que el bucle siga ejecutandose
for fruta in frutas:
    print(f"me voy a comer una {fruta}")
    if fruta =="pera":
        break
    
print("bucle terminado")