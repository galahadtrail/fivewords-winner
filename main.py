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



