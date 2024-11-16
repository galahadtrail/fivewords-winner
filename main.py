import itertools

russian_letters = ["а", "б", "в", "г", "д", "е", "ж", "з", "и", "к", 
"л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ы", "ъ", "э", "ь", "ю", "я"]

words = []


with open("russian.utf-8", "r+") as file:
    temp = file.read()

words = temp.split("\n")
result = []

for word in words:
    if len(word) == 5:
        result.append(word)


black_list = []
white_list = []

print("Please type all letters that are exclude:\n")
print("For ending of input print the letter `q`\n")

letter = ""

while True:
    letter = str(input())
    if letter != "q":
        black_list.append(letter)
        continue
    else:
        break

for lett in russian_letters:
    if lett not in black_list:
        white_list.append(lett)

permutations = itertools.permutations(white_list, 5)

for perm in permutations:
    if perm in result:
        print("That's the results!\n")
        print(perm)
        break
