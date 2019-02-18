import enchant
import itertools

d = enchant.Dict("en_US")


def amalgam(string_1, string_2):
    concat_string = string_1 + string_2
    ''' No of letters in the amalgamated word is set to 5 for now '''
    perm = itertools.permutations(concat_string, 5)

    word = ''
    tup_list = []
    for tup in perm:
        for letter in tup:
            word = word + letter
        if d.check(word) == True:
            tup_list.append(word)
        word = ''

    print(tup_list)


amalgam('abeer', 'ami')
