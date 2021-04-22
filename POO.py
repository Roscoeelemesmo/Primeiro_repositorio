from random import randint, choice
from time import sleep

global mnv, mav, mnm, mam, mnc, mac

print('+=-=-=-=-=-=-=-= VAMOS CONFIGURAR A MESA =-=-=-=-=-=-=-=+')
while (True):
    try:
        op = input('Digite "1" caso vc queira definir o minimo e o maximo de vida, mana e carisma. Ou 2, caso vc queira usar o padrão (10 a 20)').replace(' ', '')
        if op == '1':
            mnv = int(input('Qual deve ser a vida minima?'))
            mav = int(input('Qual deve ser a vida maxima?'))
            print('+=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=+')
            mnm = int(input('Qual deve ser a mana minima?'))
            mam = int(input('Qual deve ser a mana maxima?'))
            print('+=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=+')
            mnc = int(input('Qual deve ser o carisma minimo?'))
            mac = int(input('Qual deve ser o carisma maximo?'))
        else:
            mnv = 10
            mav = 20
            mnm = 10
            mam = 20
            mnc = 10
            mac = 20

        break
    except:
        print('Digite apenas valores numericos')


class criando():

    def __init__ (self, jn):
        print(f'Seja bem vindo jogador {jn}')
        if (input('Você ja possui uma ficha?') == 'ss'):
            with open('fichas.txt', 'r') as fichas:
                pin = input('Insira seu PIN numerico:  ')
                coisas = fichas.readlines()
                lin = -1
                for line in coisas:
                    lin += 1
                    if pin in line:
                        tpin = lin
                        print('Pin encontrado')
                self.vida = int(coisas[tpin + 1])
                self.mana = int(coisas[tpin+ 2])
                self.carisma = int(coisas[tpin + 3])
                self.arquetipo = (coisas[tpin + 4])
                self.classe = (coisas[tpin + 5])
        else:
            self.vida = randint(mnv, mav)
            self.mana = randint(mnm, mam)
            self.carisma = randint(mnc, mac)
            arq = ['Fogo', 'Agua gelada hmmm', 'terra', 'ar']
            self.arquetipo = choice(arq)
            self.classe = input('Escolha uma classe, nossas sugestões são\n 1: Barbabro\n 2: Mago\n 3: Bardo :)\n')
            self.pin = randint(1, 10000000000)
            print(f'Seu pin numerico é \033[1;31m{self.pin}\033[0;0m')
            with open('fichas.txt', 'a') as fichas:
                fichas.write(f"{str(self.pin)}\n{self.vida}\n{self.mana}\n{self.carisma}\n{self.arquetipo}\n{self.classe}\n")

    def infos(self):
        return f'VIDA: {self.vida}\nMANA: {self.mana}\nCLASSE: {self.classe}\nCARISMA: {self.carisma}\nARQUETIPO: {self.arquetipo}'

#OBS: Caso isso fosse um aplicativo real, os jogadores receberiam um objeto e fariam sua própria ficha online (Caso fosse presencial o computador seria passado de jogador para jogador)

j1 = criando(1)
j2 = criando(2)
j3 = criando(3)
j4 = criando(4)
j5 = criando(5)
while (True):
    try:
        sen = int(input(('\nTudo certo para começar, por favor insira a senha para provar que é o mestre dessa sessão:  ')))
    except:
        print('Digite um valor numerico')
        continue
    #Pensa, é aquela senha, aquela sequencia de 4 numeros de sempre, a que vc sempre usa
    # esse if tem essa conta pra vc deixar de ser preguiçoso e pensar na senha, ou resolver a expressão, mas isso vai dar mais trabalho
    if sen == (8210 + 45.3 - 369.8) * 4 / 6 * (365 * 2 - 3 * 243 -1) + (375.5 * 14):
        print('Bem vindo senhor')
        while (True):
            print('Caso queira finalizar o progrma, digite "exit" na opção seguinte a esta')
            esco = input('Digite o numero que corresponde a ação que deseja realizar: 1: Visualizar todas as fichas / 2: Editar uma ficha ')
            if esco == 'exit' or esco == 'Exit' or esco == 'EXIT':
                print('\033[1;31mDesligando computador\033[0;0m')
                sleep(3)
                print('Brincadiera, \033[1;31mfinalizando\033[0;0m apenas o programa')
                exit()
            if esco == '1':
                print(f'\033[1;91mJOGADOR 1\033[0;0m: \n{j1.infos()}\n\033[1;91mJOGADOR 2\033[0;0m: \n{j2.infos()}\n\033[1;91mJOGADOR 3\033[0;0m: \n{j3.infos()}\n\033[1;91mJOGADOR 4\033[0;0m: \n{j4.infos()}\n\033[1;91mJOGADOR 5\033[0;0m: \n{j5.infos()}')
            else:
                jogalt = input('Qual jogador deve ter a ficha alterada? (ex: j1)  ')
                print('Digite a alteração a ser feita, como "-5" em vida caso o jogador tenha recebido 5 de dano, por exemplo')
                altvid = int(input('vida :'))
                altman =int(input('mana :'))
                altcar =int(input('carisma :'))
                if jogalt == 'j1':
                    j1.vida = j1.vida + altvid
                    j1.mana = j1.mana + altman
                    j1.carisma =j1.carisma + altcar
                if jogalt == 'j2':
                    j2.vida = j2.vida + altvid
                    j2.mana = j2.mana + altman
                    j2.carisma = j2.carisma + altcar
                if jogalt == 'j3':
                    j3.vida = j3.vida + altvid
                    j3.mana = j3.mana + altman
                    j3.carisma = j3.carisma + altcar
                if jogalt == 'j4':
                    j4.vida = j4.vida + altvid
                    j4.mana = j4.mana + altman
                    j4.carisma = j4.carisma + altcar
                if jogalt == 'j5':
                    j5.vida = j5.vida + altvid
                    j5.mana = j5.mana + altman
                    j5.carisma = j5.carisma + altcar
    else:
        print('Senha incorreta')
        continue