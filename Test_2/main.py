
def rev_bits(x):
    rev = 0
    while x:
        rev <<= 1
        rev += x & 1
        x >>= 1
    return rev


def main2(msg):
    a = msg
    a &= 0xFFFF
    a >>= 8

    b = int(msg)
    b &= 0b1000000
    b = ~b

    c = int(msg)
    c &= 0b11110000000000000000
    c >>= 16
    c = rev_bits(c)

    print('Второй байт:                   ', hex(a), ' ', a)
    print('Значение 7-го бита:            ', hex(b), ' ', b)
    print('Зеркальное отб. 17-20 го бита: ',  hex(c), '  ', c)


if __name__ == '__main__':
    main2(0x5FABFF01)
