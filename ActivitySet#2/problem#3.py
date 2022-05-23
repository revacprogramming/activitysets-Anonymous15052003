def get_cs():
    str=input("Enter the string : ")
    return str


def cs_to_lot(str):
    l=[]
    for i in str.split(";"):
        k=i.split("=")
        t=tuple(k)
        l.append(t)

    return l


def main():
    cs = get_cs()

    lot = cs_to_lot(cs)
    print(lot)


if __name__ == '__main__':
    main()

# str=input("Enter the string : ")
# l=[]
# for i in str.split(";"):
#     k=i.split("=")
#     t=tuple(k)
#     l.append(t)

# print(l)