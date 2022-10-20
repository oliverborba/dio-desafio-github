while True: 
    try: 
      perna = input()     
        # TODO:  Programe aqui dentro as condições necessárias para satisfazer o problema
        # e imprima a saída de acordo com a situação das pernas do papagaio
      if perna == 'esquerda':
        print('ingles\n')
      elif perna == 'direita':
        print('frances\n')
      elif perna == 'nenhuma':
        print('portugues\n')
      elif perna == 'ambas':
        print('caiu\n')
      
    except EOFError: 
        break