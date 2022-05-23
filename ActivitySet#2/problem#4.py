def get_cs():
    str=input("Enter the string : ")
    return str


def cs_to_lot(cs):
    l=[]
    for i in str.split(";"):
        k=i.split("=")
        t=tuple(k)
        l.append(t)

    return l


def lot_to_cs(lot):
    t=()
    for i in lot:
        print(i)


def main():
    cs=get_cs()

    lot=cs_to_lot(cs)  # convert connect string to list of tuples
    print(lot)

    cs=lot_to_cs(lot)  # convert list of strings to connect string
    print(cs)


if __name__ == '__main__':
    main()


