def input_two_numbers():
    a=int(input("Enter a : "))
    b=int(input("Enter b : "))
    return a, b


def add(a, b):
    c=a+b
    return c


def output(a, b, sum):
    print("The addition of ",a," + ",b,"=",sum)



def main():
    a, b = input_two_numbers()
    sum = add(a, b)

    output(a, b, sum)


if __name__ == '__main__':
    main()
