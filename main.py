def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n//2 + 1):
            if n % i == 0:
                return False
    return True


def get_goldbach(n):
    for i in range(2, n//2):
        if isPrime(i) and isPrime(n-i):
            return i, n-i

def test_get_goldbach():
    assert get_goldbach(32) == (3, 29)
    assert get_goldbach(30) == (7, 23)
    assert get_goldbach(20) == (3,17)


def get_largest_prime_below(n):
    for i in range(n, 0, -1):
        if isPrime(i):
            return i
    return -1

def test_get_largest_prime_below():
    assert get_largest_prime_below(74) == 73
    assert get_largest_prime_below(5) == 3


def is_palindrome(n):
    copien = n
    inv = 0
    while copien > 0:
        inv = inv * 10 + copien % 10
        copien = copien//10
    if n == inv:
        return True
    else:
        return False


if __name__ == '__main__':
    while True:
        test_get_goldbach()
        #test_get_largest_prime_below()
        print("1.verificarea conjecturii lui Goldbach")
        print("2.determina ulimul nr prim mai mic decat un nr citit")
        print("3.verifcare daca un nr e palindrom")
        print("4.iesire")
        optiune = input("dati optiune:")
        if optiune == "1":
            numar1 = int(input("dati nr:"))
            print(get_goldbach(numar1))
        elif optiune == "2":
            numar2 = int(input("dati nr:"))
            print(get_largest_prime_below(numar2))
        elif optiune == "3":
            numar3 = int(input("dati nr:"))
            print(is_palindrome(numar3))
        elif optiune == "4":
            break

        else:
            print("optiune gresita")
