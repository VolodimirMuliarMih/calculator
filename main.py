# calculator
class FoundException(Exception):
    def __init__(self, message='Это мое исключение, ноль возводить в ноль нельзя хотя говорят, что равно 1'):
        super().__init__(message)


print("Enter 1 for Addition ")
print("Enter 2 for Subtraction")
print("Enter 3 for Multiplication")
print("Enter 4 for Division")
print("Enter 5 for Exponentiation ")


def sub(A, B):
    result = None
    result = None
    try:
        result = int(A) - int(B)
    except ValueError:
        print('Dы ввели не цифры!')
    else:
        print(result)


class Calculator():

    def sum_1(self, A, B):
        result = None
        try:
            result = int(A) + int(B)
        except ValueError:
            print('Dы ввели не цифры!')
            print(result)

    def multiplication(self, A, B):
        result = None
        try:
            result = int(A) * int(B)
        except ValueError:
            print('Dы ввели не цифры!')
            print(result)

    def div(self, A, B):
        result = None
        try:
            result = int(A) / int(B)
        except ValueError:
            print('вы ввели не цифры!')
        except ZeroDivisionError:
            print('Делить на ноль нельзя!')
        print(result)

    def Exponentiation(self, A, B):
        result = None
        try:
            A = int(A)
            B = int(B)
            if A == 0 and B == 0:
                raise FoundException()
        except FoundException as err:
            print(err)
        except ValueError:
            print('вы ввели не цифры!')
        else:
            result = A ** B
        print(result)


C = Calculator()
while True:
    Input = int(input("Enter the choice:"))
    A = input("Enter A:")
    B = input("Enter B:")
    if Input == 1:
        C.sum_1(A, B)
    elif Input == 2:
        sub(A, B)
    elif Input == 3:
        C.multiplication(A, B)
    elif Input == 4:
        C.div(A, B)
    elif Input == 5:
        C.Exponentiation(A, B)