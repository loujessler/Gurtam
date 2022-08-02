from package import Package


def main():
    with open('file.txt', 'r') as f:
        result = [
            Package(x).write_to_file() and Package(x).write_to_console()
            for x in f.read().rstrip().split('\n')
        ]
    f.close()
    return result


if __name__ == '__main__':
    main()
