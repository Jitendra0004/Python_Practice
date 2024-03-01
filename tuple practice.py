def list_to_str(array):
    result = ''
    size =len(array)
    for i, item in enumerate(array):
        if size <=1:
            result = str(item)
        elif size == i+1:
            result = result[0:-2]+ ' and ' + item
        else:
            result += item + ', '
    return result
cars =['toyata','ford','audi','benz']
cars=[]
print(list_to_str(cars))