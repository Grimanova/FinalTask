def check_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


if __name__ == '__main__':
    print(check_prime(int(input('Введите число: '))))
