def calcular(n1, n2, op):
  if op == "+":
    return n1 + n2
  elif op == "-":
    return n1 - n2
  elif op == "*":
      return n1 * n2
  elif op == "/":
    if n2 != 0:
      return n1 / n2
    else:
      return "Error: divisao por zero!"
  else:
    return "Operador invalido!"
  
def main():
    numero1 = float(input("digite o numero"))
    operador = input("digite um operador(+, -, *, /)")
    numero2 = float(input("digite um numero"))
    calcular(numero1, numero2, operador)
    resultado = calcular(numero1, numero2, operador)
    print(resultado)

main()
