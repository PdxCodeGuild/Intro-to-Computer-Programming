def set_phrase():
    phrase = input('What phrase would you like to hang? ')
    template = ['_'] * len(phrase)

    space    = ' '
    indicies = get_index(space, phrase)
    template = update(space, indicies, template)

    return phrase, template


def get_index(char, phrase):
    # return list of index values of character in phrase
    acc = []
    for index, value in enumerate(phrase):
        if char == value:
            acc.append(index)
    return acc


def update(char, indicies, template):
    # update the indicies of template with char, then return template
    for index in indicies:
        template[index] = char
    return template

def iscomplete(phrase, template):
    # do the phrase and template represent the same content?
    for index, char in enumerate(phrase):
        a = phrase[index]
        b = template[index]
        if not a == b:
             return False
    return True

def get_character():
    # get a character from the command line as user input
    char = input('Type in a character')
    return char

def take_turn(phrase, template):
    ch = get_character()
    indicies = get_index(ch, phrase)
    template = update(ch, indicies, template)
    print(template)


def main():
    win = False
    phrase, template = set_phrase()

    for turn in range(10):
        if iscomplete(phrase, template):
            win = True
            break
        take_turn(phrase, template)

    if win:
        print('YOU WIN!')
        #restart the list
    else:
        print('You lose.')


if __name__ == '__main__':
    main()
