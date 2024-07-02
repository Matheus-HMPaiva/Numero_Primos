

def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number % i == 0:
      is_prime = False
  if is_prime:
    print("É um número primo.")
  else:
    print("Não é um número primo.")

n = int(input("Digite um número inteiro: ")) # Check this number

prime_checker(number=n)
