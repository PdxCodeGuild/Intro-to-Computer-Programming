def set_phrase():
    phrase = input('What phrase would you like to hang? ')
    template = ['_'] * len(phrase)

    space    = ' '
    indicies = get_index(space, phrase)
    template = update(space, indicies, template)

    return phrase, template


def get_index(char, phrase):
    # return list of index values of character in phrase
    ...


def update(char, indicies, template):
    # update the indicies of template with char, then return template
    ...


def iscomplete(phrase, template):
    # do the phrase and template represent the same content?
    ...


def get_character():
    # get a character from the command line as user input
    ...


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
            ...

        take_turn(phrase, template)

    if win:
        ...
    else:
        ...


if __name__ == '__main__':
    main()
