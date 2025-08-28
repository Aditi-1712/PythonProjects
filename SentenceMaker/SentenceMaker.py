#Function for completing the sentences
def sentenceMaker (phrase):
    interrogatives = ("how", "when", "what", "why")         #Define the variables
    capitalized = phrase.capitalize()                       #Capitalize the first letter of each sentence

    if phrase.startswith(interrogatives):
        return"{}?".format(capitalized)                     #If a question, end with ?

    else:
        return"{}.".format(capitalized)                     #else, end with a .

results = []

while True:
    phrase = input("Say Something:")

    if phrase == '\end':
        break;
    
    else:
        results.append(sentenceMaker(phrase))
        

print(" ".join(results))

