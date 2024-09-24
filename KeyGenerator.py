def getMinIndex(phone_number:list[int]):
    min_number_index = getFirstNumber(phone_number)
    min_number = phone_number[min_number_index]
    for idx, i in enumerate(phone_number):
        if i < min_number:
            min_number_index = idx
            min_number = i
    return min_number_index

def getFirstNumber(phone_number:list[int]):
    for idx, i in enumerate(phone_number):
        if i != 10:
            max_number_index = idx
            break
    return max_number_index

def createKey(phone:str):
    if type(phone) != str:
        phone = str(phone)
    key = ['*' for letter in phone]
    phone_number = [int(i) for i in phone]
    counter = 1
    for l in range(len(phone_number)):
        # find index to replace
        current_min_index = getMinIndex(phone_number)
        # assign counter to key
        key[current_min_index] = str(counter)
        # marked as visited
        phone_number[current_min_index] = 10
        # increment counter
        counter += 1
    return "".join(key)
