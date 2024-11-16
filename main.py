
def  is_letter_in_word(black, word):
    for letter in word:
        if letter in black:
            return True
    return False

def is_letter_in_forbidden(letter, dct):
    for let in dct:
        if letter == let:
            return True
    return False

russian_letters = ["а", "б", "в", "г", "д", "е", "ж", "з", "и", "к", 
"л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ы", "ъ", "э", "ь", "ю", "я"]

words = []


with open("russian.utf-8", "r+") as file:
    temp = file.read()

words = set(temp.split("\n"))
result = []

for word in words:
    if len(word) == 5:
        result.append(word.lower())

result = set(sorted(result))

black_list = []
white_list = []

print("Please type all letters that are exclude, divided by comma:\n")

letter = str(input())
black_list = letter.split(",")

black_list = set(sorted(black_list))

finally_black_result = []

for word in result:
    if not is_letter_in_word(black_list, word):
        finally_black_result.append(word)

finally_black_result = set(finally_black_result)

print("Please type all letters that are include, divided by comma:\n")
letter = str(input())
white_list = letter.split(",")

white_list = set(sorted(white_list))
finally_result = []

for word in finally_black_result:
    if is_letter_in_word(white_list, word):
        finally_result.append(word)

finally_result = set(finally_result)

print("Please type which letters can not be at some places. Type q to interrupt the string\n")

first_letter = []
letter = str(input())
first_letter = letter.split(",")
    
first_letter = []
letter = str(input())
second_letter = letter.split(",")

first_letter = []
letter = str(input())
third_letter = letter.split(",")

first_letter = []
letter = str(input())
forth_letter = letter.split(",")

first_letter = []
letter = str(input())
fifth_letter = letter.split(",")


res = []

for word in finally_result:
    if not is_letter_in_forbidden(word[0], first_letter) and not is_letter_in_forbidden(word[1], second_letter) and not is_letter_in_forbidden(word[2], third_letter) and not is_letter_in_forbidden(word[3], forth_letter) and not is_letter_in_forbidden(word[4], fifth_letter):
        res.append(word)
print(res)
print(len(res))
