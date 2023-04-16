
#Escreva um programa que leia um número e exiba o dia correspondente da semana.
#(1-domingo, 2-segunda-feira, 3-terça-feira etc.), se digitar outro valor deve
#aparecer “valor inválido”.

def dia_semana(d):
    print('O dia que escolheu foi: ')
    if d == 1:
        print('domingo')
    else:
        if d == 2:
            print('segunda-feira')
        else:
            if d == 3:
                print('terça-feira')
            else:
                if d == 4:
                    print('quarta-feira')
                else:
                    if d == 5:
                        print('quinta-feira')
                    else:
                        if d == 6:
                            print('sexta-feira')
                        else:
                            if d == 7:
                                print('sábado')
                            else:
                                    print('valor inválido')

def main():
    dia = int(input('Digite um dia da semana.\n1-domingo\n2-segunda-feira\n3-terça-feira\n4-quarta-feira\n5-quinta-feira\n6-sexta-feita\n7-sábado\n:  '))
    dia_semana(dia)
if __name__ == '__main__':
    main()