'''
Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
'''

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

letter_number = int(input("Please enter letter number (1...26): "))

if 0 < letter_number < 27:
    alphabet_index = letter_number - 1
    print("Letter: ", alphabet[alphabet_index])
else:
    print("Invalid number. Please note that English alphabet consists of 26 letters.")