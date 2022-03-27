def unpackage_file(file: str) -> list:
    with open(file, encoding='utf-8') as f:
        data = f.readlines()
        data.insert(0, len(data))
        data.insert(0, file)
    return data

def package_file(*data: list) -> file:

#print(unpackage_file('1.txt'))
