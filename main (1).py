## Link Git-hub: 
## Questão 1. 
## Letra a) 
def questao1_a(n):
  if n == 1:
      return 10
  elif n >= 2:
       return questao1_a(n-1)+10
  else:
      return 0
parametro = int(input("Entre com o número: "))
teste = questao1_a(parametro)
print("Resultado: ", teste)

## Letra b)
def questao1_b(n):
  if n == 1:
      return 2
  else:
      return questao1_b(n - 1)** -1
parametro = int(input("Insira o numero:"))
teste = questao1_b(parametro)
print("Resultado:", teste)
  

## Letra c)
def B(n):
  if n == 1:
    return 1
  elif n >= 2:
    return B(n-1)+n**2
  else:
    return 0
    
x = int(input("Escolha o numero desejado para função"))
resultado = B(x)
print("O resultado é", resultado)

## Letra D)
def P(n):

    if n == 1:
        return 1
    else:
        return n*2*(P(n-1) + n - 1)

x = int(input("Escolha o número para a função: "))
resposta = P(x)
print(resposta)

## Letra E)
def D(n):
  if n == 1:
    return 3
  
  elif n ==2:
    return 5

  elif n > 2:
    return (n-1)*D(n-1)+(n-2)*D(n-2)
    
  else:
    return 0

x = int(input("Escolha o numero desejado para função"))
resultado = D(x)
print("O resultado é", resultado)



## Letra F)
def W(n):

  if n == 1:
    return 2
  elif n ==2:
    return 5
  elif n > 2:
    return W(n-1)*W(n - 2)
  else:
    return 0

x = int(input("Escolha o numero desejado para função"))
resultado = D(x)
print("O resultado é", resultado)

## Letra G)

def questao1_g(n):
  if n == 1:
    return n
  elif n == 2:
    return n
  elif n == 3:
    return n
  else:
    return questao1_g(n-1) + 2 * questao1_g(n-2) + 3 * questao1_g(n-3)

parametro = int(input("Entre com o número: "))
teste = questao1_g(parametro)
print("Resultado: ", teste)

## Questao 2.	
def questao_2(a,r,n):
  if n != 0:
    if n == 1:
      return a

    else:
      return r*questao_2(a,r,n-1)
      
  else:
    return 0

x = int(input("Coloque o numeor que voce deseja"))
print("O resultado da Funcao é",questao_2(2,2,x))

# Questao 3
def T(n):
    if n % 2 == 0:
        return T(n//2)
    elif ((n - 3)// 2) != 2:
        return T((n-3)//2)
    else:
        return  False


numero = [6,7,19,12]
resultado = []

for n in numero:
    if T(n):
        resultado.append(n)

print(resultado)


# Questao 4
def M(n):
  if n == 2 or n ==3:
    return True
  if n % 2 == 0:
    return M(n // 2)
  if n % 3 == 0:
    return M(n // 3)
  else:
    return False


numeros = [6,9,16,21,26,54,72,218]
pertencem = []
for n in numeros:
  if M(n):
    pertencem.append(n)


print("Os numeros que pertencem ao conjunto são", pertencem)


#Questao 5
def caractere(n):
    if n == 'a' or n == 'b':
        return True
    elif n[0] == 'a':
        return caractere(n[1:])
    else:
        return False

sequencias = ["a","ab","aba","aaab","bbbbb"]
retorno = []
for n in sequencias:
    if caractere(n):
        retorno.append(n)

print(retorno)

#Questao 06
def pertence_a_W(cadeia):
  if len(cadeia) == 1 and cadeia in 'abc':
      return True
  elif cadeia[0] == 'a' and cadeia[-1] == 'c':
      return pertence_a_W(cadeia[1:-1])
  else:
      return False

cadeias = ['a(b)c', 'a(a(b)c)c', 'a(abc)c', 'a(a(a(a)c)c)c', 'a(aacc)c']

for cadeia in cadeias:
  if pertence_a_W(cadeia):
      print(f'A cadeia "{cadeia}" pertence a W.')
  else:
      print(f'A cadeia "{cadeia}" não pertence a W.')



# QUESTAO 08
#Letra A
def questao8_a(n):
  if n == 1:
    return 1
  else:
    return 3 * questao8_a(n-1)

parametro = int(input("Entre com o n: "))
teste = questao8_a(parametro)
print(teste)

#Letra B
def questao8_b(n):
  if n == 1:
    return 2
  else: 
    return questao8_b(n-1) / 2 

parametro = int(input("Entre com o n: "))
teste = questao8_b(parametro)
print(teste)

##Letra C
def questao8_c(n):
  if n == 1:
    return 'a'  
  if n == 2:
    return 'b'
  else: 
    return questao8_c(n-2) + questao8_c(n-1)

parametro = int(input("Entre com o n: "))
teste = questao8_c(parametro)
print(teste)

##Questao 9
def questao9(n):
  if n == 0:
      return 0
  else:
      return n + questao9(n-1)
parametro = int(input("Insira n-ésimo da recursão:"))
teste = questao9(parametro)
print("Resultado:", teste)

## Questao 10
## Letra A
def questao10(h):
  pop = 50000
  if h == 1:
    return pop * (h*3)
  else:
    return questao10(h-1) * 3

parametro = int(input("Entre com o número: "))
teste = questao10(parametro)
print(teste)

## Letra B
def questao10_b(h):
  pop = 50000
  if h == 1:
    return pop * (h*3)
  else:
    return questao10_b(h-1) * 3

teste = questao10_b(2)
print("Irá passar com duas horas, o resultado será de: ", teste, "bacterias")