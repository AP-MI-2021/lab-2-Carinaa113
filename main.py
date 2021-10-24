#problemele 3 si 4 si 5
def is_prime(n):
    '''
    input-n este numarul dat
    :param n:
    :return: True-daca n este un numar prim
            False -daca nu e numar prim
    '''
    if n < 2 :
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
        return True

def get_goldbach(n):
    '''

    :param n: numarul pentru care generam p1 si p2,suma lor sa fie egala cu n
    :return: [p1,p2]-daca exista 2 astfel de numere
              -1--->daca nu satisface conditia data
    '''

    for i in range(2,n):
        for j in range(2,n):
            if(i+j== n) and is_prime(i) and is_prime(j):
                return [i,j]
            return -1

def test_get_goldbach():
    print("1.Pentru numarul : 1")
    assert get_goldbach(1)== -1

    print("2.Pentru numarul 20")
    assert get_goldbach(20)==[7,13]


def get_newton_sqrt(n,pasi):
    '''

    :param n: numarul pentru care calculam radicalul
    :param pasi:aproximarile numarului de calcule
    :return:radicalul lui n
    '''

    if n<0:
        return None
    x1=2
    while pasi>0:
        x1=0.5*(x1+n/x1)
        pasi=pasi-1
    return x1


def test_get_newton_sqrt():
    print("Testarea lui -1 radical din el")
    assert get_newton_sqrt(-1,3)==None
    print("Testarea lui 9 radical din el ")
    assert round(get_newton_sqrt(9,1),1)==3.0


def get_leap_years(start,end):
    '''
    afiseaza toti anii biecti dintre 2 ani dati
    :param start: primul an
    :param end: al doilea an
    :return: anii bisecti aflati intre cei 2 ani
    '''

    rez=[]
    for i in range(start,end+1):
        if i%4 ==0:
            rez.append(i)
    return rez

def test_get_leap_years():
    assert get_leap_years(2011,2021)==[2012,2016,2020]
    assert get_leap_years(2005,2007)==[]

def main():
    test_get_goldbach()
    test_get_newton_sqrt()
    test_get_leap_years()

    while True:
        print("1.Afiseaza toate numerele prime care indeplinesc conditia")
        print("2.Afiseaza radicalul numarului")
        print("3.Afiseaza anii bisecti dintre 2 numere date")
        print("4.Iesire")

        command=int(input("Introduceti optiunea: "))
        if command ==1:
            start=int(input("Numarul este :"))
            print("Numerele prime sunt", get_goldbach(start))

        elif command==2:
            start=int(input("Numarul este: "))
            end=int(input("Numarul de aproximari: "))
            print("Radicalul numarului este ",get_newton_sqrt(start,end))

        elif command==3:
            start=int(input("Primul an este:"))
            end=int(input("Al doilea an este:"))
            print("Anii bisecti sunt",get_leap_years(start,end))
        elif command==4:
            break
            '_main_' == if_name
main()