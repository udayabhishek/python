def mutate_string(string, position, character):
    res = string[:position] + character + string[position+1:]
    return res


"""Using List"""
def mutate_string_using_list(string, position, character):
    charList = list(string)
    charList[position] = character
    res = ''.join(charList)
    return res

print(mutate_string("hellk world", 4,'XXXX'))
print(mutate_string_using_list("I am mac book pro", 8,'Apple'))