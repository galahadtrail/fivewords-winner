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

