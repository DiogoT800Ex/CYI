def leituraVariavel():
  variavel = input()
  print (variavel)
  
def leituraLista():
  lista = []
  tamanho = int(input())
  i=0
  while tamanho > i:
    elemento = int(input())
    lista.append(elemento)
    i = i + 1

  for elemento in lista:
    print(elemento)
    
def main():
    leituraVariavel()
    leituraLista()
  
main()
