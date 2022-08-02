# Инверсия двоичного числа
def reverse_bit(bit):
    return ''.join('0' if int(bit[x]) else '1' for x in range(0, len(bit)))


# Добавление недостоющего 0
def add_zero(bit):
    if len(bit) % 2 is 1:
        bit = '0' + bit
    return bit


def main(msg):
    a = add_zero(bin(int(msg, 0))[2:])
    first_par = add_zero(hex(int('0b' + a[16:24], 0))[2:])
    second_par = reverse_bit(a[::-1][6:7])
    third_par = hex(int('0b' + a[12:16][::-1], 0))[2:]

    print('Второй байт:                   ', first_par.upper())
    print('Значение 7-го бита:            ', second_par.upper())
    print('Зеркальное отб. 17-20 го бита: ', third_par.upper())
    print('Дополнительные параметры:      ', (first_par + second_par + third_par).upper())


if __name__ == '__main__':
    main('0x5FABFF01')
