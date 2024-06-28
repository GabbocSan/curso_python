import random

def option():

    options = ('piedra', 'papel', 'tijera')
    user_option = input('Piedra, Papel o Tijera: ')
    user_option = user_option.lower()
    computer_option = random.choice(options)
    if not user_option in options:
      print('Opcion no valida, intente de nuevo')
      return None, None
  
    return (user_option, computer_option)   

def ruler (user_option, computer_option, count_vic, count_per):
      
    if user_option == computer_option:
        print('Empate')

    elif user_option == 'piedra' and computer_option == 'tijera':
      print('piedra gana a tijera')
      print('el usuario gana')
      count_vic += 1
    
    elif user_option == 'piedra' and computer_option == 'papel':
      print('papel gana a piedra')
      print('el usuario pierde')
      count_per += 1
    
    elif user_option == 'papel' and computer_option == 'tijera':
      print('tijera gana a papel')
      print('el usuario pierde')
      count_per += 1
    
    elif user_option == 'papel' and computer_option == 'piedra':
      print('papel gana a piedra')
      print('el usuario gana')
      count_vic += 1
    
    elif user_option == 'tijera' and computer_option == 'piedra':
      print('piedra gana a tijera')
      print('el usuario pierde')
      count_per += 1
    
    elif user_option == 'tijera' and computer_option == 'papel':
      print('tijera gana a papel')
      print('el usuario gana')
      count_vic += 1

    return (count_vic, count_per)

def victoria(count_vic, count_per):
  if count_vic>count_per:
    print('*' * 10)
    print('El usuario gana, Felicidades!')
    print('*' * 10)
  else :
    print('*' * 10)
    print('El usuario pierde')
    print('*' * 10)
  
def game():
  count_vic = 0
  count_per = 0
  rounds = 1
  
  while count_vic<2 and count_per<2:
    print('*' * 10)
    print('Round: ', rounds)
    print('*' * 10)
    user_option, computer_option = option()
    print('Usuario: ',user_option)
    print('Computadora: ',computer_option)
    count_vic, count_per = ruler(user_option, computer_option, count_vic, count_per)
    print('victorias: ',count_vic)
    print('derrotas: ',count_per)
    rounds +=1
  victoria(count_vic, count_per)

game()
