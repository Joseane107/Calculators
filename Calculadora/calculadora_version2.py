import math
# comentário novo
# comentário novo de novo

class calculator:
    def __init__(self):
        pass

    def get_number1(self):
        self.num1 = float(input('Digite o primeiro número '))
        return self.num1

    def get_number2(self):
        self.num2 = float(input('Digite o segundo número '))
        return self.num2

    def get_operation(self):
        self.choice = int(input('''Esolha alguma das opções:
                        [1] Soma
                        [2] Subtração
                        [3] MUltiplicação
                        [4] Divisão \n
                        '''))
        return self.choice

    def calc_sum(self):
        self.result = self.num1 + self.num2
        self.is_int()

    def calc_sub(self):
        self.result = self.num1 - self.num2
        self.is_int()

    def calc_mult(self):
        self.result = self.num1 * self.num2
        self.is_int()

    def calc_div(self):
        self.result = self.num1 / self.num2
        self.is_int()

    def is_int(self):
        if math.modf(self.result)[0] == 0:
            print(int(self.result))
        else:
            print(f'{self.result:.4f}')

    def menu(self):

        self.get_number1()
        self.get_operation()
        self.get_number2()

        if self.choice == 1:
            self.calc_sum()
        elif self.choice == 2:
            self.calc_sub()
        elif self.choice == 3:
            self.calc_mult()
        elif self.choice == 4:
            self.calc_div()
        else:
            print('Escolha uma opção válida')


calc = calculator()

calc.menu()

