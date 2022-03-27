def unpackage_file(file: str) -> list:
    with open(file, encoding='utf-8') as f:
        data = f.readlines()
        data.insert(0, len(data))
        data.insert(0, file)
    return data


def package_file(file: str, *datas):
    with open(file, 'w', encoding='utf-8') as f:
        for data in sorted(datas, key=lambda x: x[1]):
            f.write(f'{data.pop(0)}\n')
            f.write(f'{data.pop(0)}\n')
            for line in data:
                f.write(f'{line}')
            f.write('\n')

# package_file('e:/union.txt', unpackage_file('1.txt'), unpackage_file('2.txt'), unpackage_file('3.txt'))
