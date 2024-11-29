collector = []
with open("./output.txt", "r") as file:
    lines = file.readlines()

    dictionary = {}
    for line in lines:
        
        line = line.replace('\n', '')
        key_value = line.split(':')
        key = key_value[0]
        value = key_value[1]

        if key in dictionary.keys():
            collector.append(dictionary)
            dictionary = {}
            
        dictionary[key] = value
    collector.append(dictionary)

    name = input('Name: ')

    names = name.split()

    for info in collector:
        for name in names:
            if name == info.get('name').strip():
                for key, value in info.items():
                    print(key + ':' + value)
                print('\n')