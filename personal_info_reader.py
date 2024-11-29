
collector = []
    #stream txt file into list of dictionaries
with open("./output.txt", "r") as f:
    lines = f.readlines()
    
    dictionary = {}
    for line in lines:
        
        line = line.replace('\n', '')
        key_val = line.split(':')
        key = key_val[0]
        value = key_val[1]

        if key in dictionary.keys():
            collector.append(dictionary)
            dictionary = {}
            
        dictionary[key] = value
    collector.append(dictionary)

input_name = input("Input your name here: ")


for info in collector:
    if input_name == info.get("Full name").strip():
        for key, value in info.items():
            print(key + ':' + value)
        print('\n')
    else:
        for name in info.get("Full name").strip().split():
            if name == input_name:

                for key, value in info.items():
                    print(key + ':' + value)
                print('\n')