print('********************************')
print('Bem-vindo ao jogo de Adivinhação')
print('********************************')

numero_secreto = 42

chute_str = input('Digite o seu numero:')

print('Voce digitou', chute_str)

chute = int(chute_str)

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

if(acertou):
  print('Voce acertou!')
else: 
  if(maior):
    print('Voce errou! O seu chute foi maior do que o numero secreto')
  elif(menor):
    print('Voce errou! O seu chute foi menor do que o numero secreto!')
