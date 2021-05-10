def mdc(a, b):
  '''
  mdc(a, b)
  Obtém o máximo divisor comum entre dois inteiros positivos.
  '''
  a = int(a)
  b = int(b)
  # assegura que b >= a
  if a > b:
    aux = a
    a = b
    b = aux
    
  try:
    while b != 0:
      resto = a % b
      a = b
      b = resto
  except ZeroDivisionError:
    return a

  return a

def processInput(value):
  '''
  Avalia string de input e retorna inteiros.
  '''
  numeros = value
  if ' ' in numeros:
    numeros = numeros.split(" ")
    try:
      a, b = int(numeros[0]),int(numeros[1])
    except ValueError as e:
      print("Entrada inválida.")
      print(e)
    
    if a < 1:
      raise Exception("Valor abaixo do limite inferior.")
    elif b > 1000:
      raise Exception("Valor acima do limite superior.")
    return a, b
  else:
    return None
    
def main():
  value = input()
  while (value):
    if processInput(value) is not None:
      a, b = processInput(value)
      print(mdc(a,b))
    try:
        value = input()
    except EOFError:
        break

if __name__ == '__main__':
  main()