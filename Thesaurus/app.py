import json
from difflib import get_close_matches

data = json.load (open ("data.json"))

def translate(word):

    word = word.lower()

    if word in data:
        return data[word]

    elif len(get_close_matches(word, data.keys())) > 0:

        yn =input ("Did you mean %s ? Enter Y for yes and N for no: " %get_close_matches(word, data.keys())[0])

        if yn == 'Y':
            return data[get_close_matches(word, data.keys())[0]]

        elif yn == 'N':
            return "The word doesn't exist. Please check your input."

        else:
            return "We didn't get that. Please try again later."

    else:
        return "The word doesn't exist. Please check your input."

word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print ("->" ,item, "\n")
else:
    print(output)

