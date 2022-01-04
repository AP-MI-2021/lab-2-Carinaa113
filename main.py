def get_largest_prime_below(n):
    for i in range(2, n):
        k = 1
        for d in range(2, n // 2):
            if(i % d == 0):
                k = 0
        if (k == 1):
            a = i
    return a


def test_get_largest_prime_below():
    assert get_largest_prime_below(20) == 19
    assert get_largest_prime_below(100) == 97
    assert get_largest_prime_below(54) == 53


test_get_largest_prime_below()


def is_palindrome(n) -> bool:

    inv = 0
    x = n
    while (x != 0):
        inv = inv * 10
        inv = inv + (x % 10)
        x = x // 10
    if (inv == n):
        return True
    return False


def test_is_palindrome():
    assert is_palindrome(121) == True
    assert is_palindrome(23432) == True
    assert is_palindrome(123) == False


def show_menu():
    print('''
        1. Largest prime
        2. Palindrome
        x. Iesire
        ''')


def main():
    while True:
        show_menu()
        cmd = input("Comanda:")
        if cmd == '1':
            n = int(input("Introduceti n="))
            print(get_largest_prime_below(n))
        else:
            if cmd == '2':
                n = int(input("Introduceti n="))
                print(is_palindrome(n))
            elif cmd == 'x':
                break
            else:
                print("Comanda invalida")


main()
