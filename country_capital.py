#program to display country capital. If not available , add it to dictionary.

capitals = {'India':'New Delhi','United States':'Washingthon DC','Poland':'Warsaw'}

while True:
    country = input('Enter a country : ')
    if country == '':
        break
    if country in capitals:
        print(f'capital city of {country} is {capitals[country]}')
    else:
        caps = input('country not found , add the country : ')
        if caps == '':
            break
        else:
            capitals[country] == caps
            print('country added!')