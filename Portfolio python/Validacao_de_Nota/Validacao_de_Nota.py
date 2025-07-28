nota = int(input("digite uma nota entre 0 e 10:"))
while nota < 10 or nota > 10:
  nota =  int(input("número inválido, digite novamente um valor entre 0 e 10:"))
  
print("sua nota é:",nota)