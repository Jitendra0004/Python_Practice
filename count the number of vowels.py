def count_vowels(name):
    vowels = "aeiouAEIOU" 
    count = 0
    for char in name:
        if char in vowels:
            count +=1
    return count

print(count_vowels(input("Enter name : ")))
print()
