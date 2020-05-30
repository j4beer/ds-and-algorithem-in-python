
def factorial(num):
    if num == 0:
        return 1;
    else:
        return num * factorial(num - 1)


def main():
    num = int(input("enter the number to see it's factorial :"))

    print(num,' factorial is : ',factorial(num))


main()
