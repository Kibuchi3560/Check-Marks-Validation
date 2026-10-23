def check_datatypes(data):
    even = []
    odd = []
    floats = []
    booleans = []
    strings = []

    for i in data:
        if isinstance(i, bool):
            booleans.append(i)  
        elif isinstance(i, float):
            floats.append(i)
        elif isinstance(i, int):
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        elif isinstance(i, str):
            strings.append(i)
        else:
            raise ValueError("Invalid data type found in the list.")

    return even, odd, floats, booleans, strings       
