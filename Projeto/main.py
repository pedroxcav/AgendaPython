'''
Projeto Final | SENAI
Participantes: Beatriz Vieceli e Pedro Cavalcanti
início: 09/08/2023
término: 10/08/2023
'''

def showMonth(numberMonth):
  calendario = calendar.month(currentYear, numberMonth)
  return calendario

from datetime import date
currentYear = date.today().year
import calendar
fullYear = {}

while True:
  print('\n=== AGENDA PESSOAL ===')
  #MENU DO USUÁRIO.
  while True:
    op = int(input('\nO que deseja?\n1 - Consultar Agenda.\n2 - Marcar Eventos.\n3 - Desmarcar Eventos.\n4 - Sair.\nOpção: '))
    if op >= 1 and op <= 4:
      break
    else:
      print('\nOpção inválida. Digite novamente.')
  if op == 1:
    while True:
      #CONSULTA DE DADOS NA AGENDA.
      while True:
        numberMonth = int(input('\nInforme o mês que deseja consultar!\n1 - Janeiro.     7 - Julho.\n2 - Fevereiro.   8 - Agosto.\n3 - Março.       9 - Setembro.\n4 - Abril.      10 - Outubro.\n5 - Maio.       11 - Novembro.\n6 - Junho.      12 - Dezembro.\nOpção: '))
        if numberMonth >= 1 and numberMonth <=12:
          break
        else:
          print('\nMês incorreto. Digite novamente.')
      print('\n',showMonth(numberMonth))
      if numberMonth==4 or numberMonth==6 or numberMonth==9 or numberMonth==11:
        totalMonth = 30
      elif numberMonth==1 or numberMonth==3 or numberMonth==5 or numberMonth==7 or numberMonth==8 or numberMonth==10 or numberMonth==12:
        totalMonth = 31
      else:
        totalMonth = 28
      while True:
        numberDay = int(input(f'\nInforme o dia que deseja consultar!\nDia: '))
        if numberDay >= 1 and numberDay <= totalMonth:
          break
        else:
          print('\nDia inválido. Digite novamente.')
      #EXIBIÇÃO DE EVENTOS
      if numberMonth in fullYear:
        if numberDay in fullYear[numberMonth]:
          if numberMonth == 1:
            print('\nMês: Janeiro, dia:',numberDay)
          elif numberMonth == 2:
            print('\nMês Fevereiro, dia:',numberDay)
          elif numberMonth == 3:
            print('\nMês Março, dia:',numberDay)
          elif numberMonth == 4:
            print('\nMês Abril, dia:',numberDay)
          elif numberMonth == 5:
            print('\nMês Maio, dia:',numberDay)
          elif numberMonth == 6:
            print('\nMês Junho, dia:',numberDay)
          elif numberMonth == 7:
            print('\nMês Julho, dia:',numberDay)
          elif numberMonth == 8:
            print('\nMês Agosto, dia:',numberDay)
          elif numberMonth == 9:
            print('\nMês Setembro, dia:',numberDay)
          elif numberMonth == 10:
            print('\nMês Outubro, dia:',numberDay)
          elif numberMonth == 11:
            print('\nMês Novembro, dia:',numberDay)
          else:
            print('\nMês Dezembro, dia:',numberDay)
          for i in range(len((fullYear[numberMonth])[numberDay])):
            print(f'Evento: {((fullYear[numberMonth])[numberDay])[i]}')
        else:
          print('\nNão há eventos para essa data!')
      else:
        print('\nNão há eventos para essa data!')
      op = int(input('\nDeseja consultar outra data?\n1 - Sim.\n2 - Não.\nOpção: '))
      if op == 2:
        break
  elif op == 2:
    while True:
      #INSERÇÃO DE DADOS NA AGENDA | SELEÇÃO DO LOCAL.
      while True:
        numberMonth = int(input('\nInforme o mês que deseja marcar!\n1 - Janeiro.     7 - Julho.\n2 - Fevereiro.   8 - Agosto.\n3 - Março.       9 - Setembro.\n4 - Abril.      10 - Outubro.\n5 - Maio.       11 - Novembro.\n6 - Junho.      12 - Dezembro.\nOpção: '))
        if numberMonth >= 1 and numberMonth <=12:
          break
        else:
          print('\nMês incorreto. Digite novamente.')
      print('\n',showMonth(numberMonth))
      if numberMonth==4 or numberMonth==6 or numberMonth==9 or numberMonth==11:
        totalMonth = 30
      elif numberMonth==1 or numberMonth==3 or numberMonth==5 or numberMonth==7 or numberMonth==8 or numberMonth==10 or numberMonth==12:
        totalMonth = 31
      else:
        totalMonth = 28
      #INSERÇÃO DE DADOS NA AGENDA | INFORMANDO DADOS.
      month = {}
      day = []
      while True:
        numberDay = int(input(f'\nInforme o dia que deseja marcar! '))
        if numberDay >= 1 and numberDay <= totalMonth:
          break
        else:
          print('\nDia inválido. Digite novamente.')
      while True:
        evento = input('\n[Digite (0) para terminar]\nInforme sua ocasião: ')
        if evento == '0':
          break
        day.append(evento)
      month[numberDay] = day
      if numberMonth == 1:
        if 1 in fullYear:
          fullYear[1].update(month)
        else:
          fullYear[1] = month
      elif numberMonth == 2:
        if 2 in fullYear:
          fullYear[2].update(month)
        else:
          fullYear[2] = month
      elif numberMonth == 3:
        if 3 in fullYear:
          fullYear[3].update(month)
        else:
          fullYear[3] = month
      elif numberMonth == 4:
        if 4 in fullYear:
          fullYear[4].update(month)
        else:
          fullYear[4] = month
      elif numberMonth == 5:
        if 5 in fullYear:
          fullYear[5].update(month)
        else:
          fullYear[5] = month
      elif numberMonth == 6:
        if 6 in fullYear:
          fullYear[6].update(month)
        else:
          fullYear[6] = month
      elif numberMonth == 7:
        if 7 in fullYear:
          fullYear[7].update(month)
        else:
          fullYear[7] = month
      elif numberMonth == 8:
        if 8 in fullYear:
          fullYear[8].update(month)
        else:
          fullYear[8] = month
      elif numberMonth == 9:
        if 9 in fullYear:
          fullYear[9].update(month)
        else:
          fullYear[9] = month
      elif numberMonth == 10:
        if 10 in fullYear:
          fullYear[10].update(month)
        else:
          fullYear[10] = month
      elif numberMonth == 11:
        if 11 in fullYear:
          fullYear[11].update(month)
        else:
          fullYear[11] = month
      else:
        if 12 in fullYear:
          fullYear[12].update(month)
        else:
          fullYear[12] = month
      op = int(input('\nDeseja marcar algum outro evento?\n1 - Sim.\n2 - Não.\nOpção: '))
      if op == 2:
        break
    '''
    for key, val in fullYear.items():
      print(f'\nMês {key}: {val}')
    '''
  elif op == 3:
    while True:
      #REMOÇÃO DE DADOS NA AGENDA | SELEÇÃO DO LOCAL.
      while True:
        numberMonth = int(input('\nInforme o mês que deseja desmarcar!\n1 - Janeiro.     7 - Julho.\n2 - Fevereiro.   8 - Agosto.\n3 - Março.       9 - Setembro.\n4 - Abril.      10 - Outubro.\n5 - Maio.       11 - Novembro.\n6 - Junho.      12 - Dezembro.\nOpção: '))
        if numberMonth >= 1 and numberMonth <=12:
          break
        else:
          print('\nMês incorreto. Digite novamente.')
      print('\n',showMonth(numberMonth))
      if numberMonth==4 or numberMonth==6 or numberMonth==9 or numberMonth==11:
        totalMonth = 30
      elif numberMonth==1 or numberMonth==3 or numberMonth==5 or numberMonth==7 or numberMonth==8 or numberMonth==10 or numberMonth==12:
        totalMonth = 31
      else:
        totalMonth = 28
      #REMOÇÃO DE DADOS NA AGENDA | INFORMANDO DADOS.
      month = {}
      day = []
      while True:
        numberDay = int(input(f'\nInforme o dia que deseja desmarcar! '))
        if numberDay >= 1 and numberDay <= totalMonth:
          break
        else:
          print('\nDia inválido. Digite novamente.')
      if numberMonth in fullYear:
        if numberDay in fullYear[numberMonth]:
          if numberMonth == 1:
            print('\nMês: Janeiro, dia:',numberDay)
          elif numberMonth == 2:
            print('\nMês Fevereiro, dia:',numberDay)
          elif numberMonth == 3:
            print('\nMês Março, dia:',numberDay)
          elif numberMonth == 4:
            print('\nMês Abril, dia:',numberDay)
          elif numberMonth == 5:
            print('\nMês Maio, dia:',numberDay)
          elif numberMonth == 6:
            print('\nMês Junho, dia:',numberDay)
          elif numberMonth == 7:
            print('\nMês Julho, dia:',numberDay)
          elif numberMonth == 8:
            print('\nMês Agosto, dia:',numberDay)
          elif numberMonth == 9:
            print('\nMês Setembro, dia:',numberDay)
          elif numberMonth == 10:
            print('\nMês Outubro, dia:',numberDay)
          elif numberMonth == 11:
            print('\nMês Novembro, dia:',numberDay)
          else:
            print('\nMês Dezembro, dia:',numberDay)
          for i in range(len((fullYear[numberMonth])[numberDay])):
            print(f'Evento: {((fullYear[numberMonth])[numberDay])[i]}')
        else:
          print('\nNão há eventos para desmarcar!')
      else:
        print('\nNão há eventos para desmarcar!')
      while True:
        if numberMonth not in fullYear or numberDay not in fullYear[numberMonth]:
          break
        else:
          while True:
            evento = input('\n[Digite (0) para terminar]\nQual evento você deseja desmarcar?\nData: ')
            if evento in (fullYear[numberMonth])[numberDay]:
              (fullYear[numberMonth])[numberDay].remove(evento)
              for i in range(len((fullYear[numberMonth])[numberDay])):
                  print(f'Evento: {((fullYear[numberMonth])[numberDay])[i]}')
              if len((fullYear[numberMonth])[numberDay]) == 0:
                fullYear[numberMonth].pop(numberDay)
                break
            elif evento == '0':
              break
            else:
              print('\nData incorreta. Digite novamente.')
        break
      op = int(input('\nDeseja desmarcar algum outro evento?\n1 - Sim.\n2 - Não.\nOpção: '))
      if op == 2:
        break
  else:
    break