
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "Ss":
            translation = translation + "5"
        elif letter in "Aa":
            translation = translation + "4"
        elif letter in "Ee":
            translation = translation + "3"
        elif letter in "Ii":
            translation = translation + "1"
        elif letter in "Zz":
            translation = translation + "2"
        elif letter in "Vv":
            translation = translation + "7"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))