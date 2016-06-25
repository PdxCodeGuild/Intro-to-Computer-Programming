#!/usr/bin/env python3 

# Hang man game
# Enter the phrase
# Enter the characters

# ----------------------
# get the game phrase from the command line as user input
def set_phrase():
    phrase = input('What phrase would you like to hang? ')
    return phrase

# ----------------------
# build the template from the phrase 
def set_template(phrase):
    # split_phrase = list(phrase)
    template = [] # list 
    dash = '-' 
    
    for character in phrase:
        if (character.isalpha() == True):
            template.append(dash) 

        elif (character.isspace() == True):
            template.append(' ') 

    return template

# ----------------------
# get a character from the command line as user input
def get_character():
    letter = input ('Type character ?' )
    print('input character = ', letter)
    return letter

# ----------------------
# return list of index values of character in phrase
def get_index(char, phrase):
    indicies = [] 
    for index, character in enumerate(phrase):
        if (char == character):
            indicies.append(index) 
    
    return indicies

# ----------------------
# update the indicies of template with char, then return template
def update(char, indicies, template):
    for element in indicies:
        template[element] = char
    
    return template

# ----------------------
# do the phrase and template represent the same content?
def iscomplete(phrase, template):
    split_phrase = list(phrase)
    
    if (split_phrase == template): # compare phrase and template lists
        print("MATCH: split_phrase = ", split_phrase)
        print("MATCH: template = ", template)
        result = True
    else:
        print("NOT MATCH: split_phrase = ", split_phrase)
        print("NOT MATCH: template = ", template)
        result = False

    print(result) 
    return result

# ----------------------
def take_turn(phrase, template):
    ch = get_character()
    indicies = get_index(ch, phrase)
    print(indicies)
    template = update(ch, indicies, template)
    print(template)

# ----------------------

def main():
    win = False
    phrase = set_phrase()
    
    print("phrase = ", phrase)
    print("length of phrase = ", len(phrase))
    
    template = set_template(phrase)
    print(template)
        
    for turn in range(10):
        if iscomplete(phrase, template):
            win = True;
            break
        else:
            print("turn = ", turn)
            take_turn(phrase, template)

    if win:
        print("Hang Man WIN")
    else:
        print("Hang Man LOST")

        
if __name__ == '__main__':
    main()

