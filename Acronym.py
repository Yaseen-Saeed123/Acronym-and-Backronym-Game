# This is a program For Designing Acronyms and Backronyms
funny_easy_words = {
    'A': 'Alien',
    'B': 'Banana',
    'C': 'Clown',
    'D': 'Donut',
    'E': 'Elbow',
    'F': 'Fart',
    'G': 'Gorilla',
    'H': 'Hippo',
    'I': 'Igloo',
    'J': 'Jelly',
    'K': 'Ketchup',
    'L': 'Llama',
    'M': 'Monkey',
    'N': 'Noodle',
    'O': 'Onion',
    'P': 'Pickle',
    'Q': 'Quack',
    'R': 'Robot',
    'S': 'Socks',
    'T': 'Taco',
    'U': 'Ufo',
    'V': 'Vampire',
    'W': 'Waffle',
    'X': 'X-ray',
    'Y': 'Yawn',
    'Z': 'Zombie'
}
def acronym(phrase):
    my_phrase = phrase.split()
    my_acronym = []
    if len(my_phrase) < 2:
        return False, "Can not make an acronym from less than two words"
    for word in my_phrase:
        char = word[0].upper()
        my_acronym.append(char)
    # Make it as a string
    new_acronym = "".join(my_acronym)
    return new_acronym
def backronym(word):
    if word == "":
        return False, "Can't Make A Backronym"
    my_backronym = []
    for char in word:
        my_char = char.upper()
        if my_char == " ":
            backword = " "
        elif my_char in funny_easy_words.keys():
            backword = funny_easy_words[my_char]
        else:
            backword = "[Special Character]"
        string = f"{my_char}: {backword}"
        my_backronym.append(string)
    # Make it as a string
    new_backronym = "\n".join(my_backronym)
    return new_backronym
print("-"*30+"\nWelcome to designing Acronyms and Backronyms\n"+"-"*30)
print("Choose Your Mode:- ")
for i, val in enumerate(["Acronym", "Backronym"], start=1):
    print(f"{i}. {val}    ", end="")
print("\n"+"-"*30)
while True:
    mode = input("=> ").strip()
    print("-"*30)
    if mode not in ["1", "2"]:
        print("Not A Valid input\n"+"-"*30)
        continue
    break
phrase = input("Enter Your Phrase: ").strip()
print("-"*30)
match mode:
    case "1":
        result = acronym(phrase)
    case "2":
        result = backronym(phrase)
if isinstance(result, tuple):
    print(result[1])
else:
    if mode == "1":
       response = f"Your Acronym is {result}"
    else:
        response = f"Your Backronym is {result}"
    print(response)
print("-"*30)