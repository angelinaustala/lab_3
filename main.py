def ypr1():
    n = int(input("введите кол-во слов"))
    a = ' '
    for i in range(n):
        x = str(input("введите слово"))
        a = a + x + " "
    print(a)



def ypr2():
    a = ' '
    x = str(input("введите слово"))
    while x!='stop':
       a = a + x + " "
       x = str(input("введите слово"))
    print(a)



def ypr3():
        x = str(input("введите слово"))
        if x.count("ф")>0:
            print('вау редкое слово')
        else:
            print('слово не редкое')



def ypr4():
    from random import randint

    x=0
    while x<3:
        a=int(randint(0,20))
        b=int(randint(0,20))
        print(a,"+",b,"=")
        y=int(input("введите ответ"))
        if a+b!=y:
            x=x+1
    if x==3:
        print('игра окончена')

ypr4()