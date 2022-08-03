from datetime import datetime


class Package:
    """Класс функций для обработки пакета"""

    def __init__(self, pack):
        self.pack = pack

    # Функция разделения на тип и данные
    def split_pack(self):
        return self.pack[1:].split('#')

    def get_dict(self):
        dic_pack = {}
        lst = self.split_pack()
        # Проверка на тип пакета
        if lst[0] == 'SD':
            # Обработка строки и сортировака от лишних значений
            lst = [x for x in lst[1].split(';') if not x.isalpha()]
            # Создание словаря с соотвествующими переменными
            dic_pack['datetime'] = datetime.strptime(lst[0] + lst[1], '%d%m%Y%H%M%S')
            dic_pack['lat'] = float(lst[2])
            dic_pack['lon'] = float(lst[3])
            dic_pack['speed'] = int(lst[4])
            dic_pack['course'] = int(lst[5])
            dic_pack['height'] = int(lst[6])
            dic_pack['sats'] = int(''.join(x for x in lst[7] if x.isdigit()))
        elif lst[0] == 'M':
            dic_pack = lst[1]
        else:
            dic_pack = 'Error'
        return dic_pack

    # Запись данных в файл
    def write_to_file(self):
        dict_pack = self.get_dict()
        if type(dict_pack) is not str:
            f = open("result.txt", "a")
            f.write(dict_pack['datetime'].strftime('Дата: %Y-%m-%d Время: %H:%M:%S'))
            f.write('\nШирота: ' + str(dict_pack['lat']))
            f.write(' Долгота: ' + str(dict_pack['lon']))
            f.write('\nСкорость: ' + str(dict_pack['speed']))
            f.write(' Курс: ' + str(dict_pack['course']))
            f.write(' Высота: ' + str(dict_pack['height']))
            f.write('\nКоличество спутников: ' + str(dict_pack['sats']))
            f.write('\n################################################\n')
            f.close()
        else:
            f = open("result.txt", "a")
            f.write(dict_pack)
            f.write('\n################################################\n')
            f.close()
        return f

    # Запись данных в консоль
    def write_to_console(self):
        dict_pack = self.get_dict()
        if type(dict_pack) is not str:
            print('################################################')
            print('|  ' + dict_pack['datetime'].strftime('Дата: %d.%m.%Y Время: %H:%M:%S'))
            print('|  ' + 'Широта: ' + str(dict_pack['lat'])[0:2] + '° ' + str(dict_pack['lat'])[2:] + "'")
            print('|  ' + 'Долгота: ' + str(dict_pack['lon'])[0:2] + '° ' + str(dict_pack['lon'])[2:] + "'")
            print('|  ' + 'Скорость: ' + str(dict_pack['speed']) + ' км/ч')
            print('|  ' + 'Курс: ' + str(dict_pack['course']) + '°')
            print('|  ' + 'Высота: ' + str(dict_pack['height']) + ' м')
            print('|  ' + 'Количество спутников: ' + str(dict_pack['sats']))
            print('|  ' + str(dict_pack))
            print('################################################\n')
        else:
            print('################################################')
            print('|  ')
            print('|  ' + str(dict_pack))
            print('|  ')
            print('################################################\n')
