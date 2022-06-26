# return a list of all combination possible to replace letter in the word with number like:
# hello = [hello, h3llo, hell0, h3ll0]

# I thank a friend of mine who, during the development of this small script, after asking him for help
# in checking all the possible combinations, tried to use the binary numbers to help control them. From there,
# I came up with the idea of exploiting binary numbers to facilitate everything.

def replace_number(word):
    dic = {"o": "0",
           "a": "4",
           "e": "3",
           "i": "1",
           "t": "7",
           "g": "9",
           "b": "8",
           "l": "2",
           "s": "5"
           }
    
    list_words = [word]
    # I will replace this two list/array with a dictionary, but right now I'm too bored
    list_comp = []
    list_replace = []
    num = 0
    word_old = word
    for x in range(len(word)):
        for i in dic:
            if i == word[x]:
                num += 1
                list_comp.append(x)
                list_replace.append(dic[i])

    num = 2 ** num
    for n in range(num):
        counter = 0
        for x in str(bin(n))[:1:-1]:
            if int(x):
                word = word[:list_comp[counter]] + list_replace[counter] + word[(int(list_comp[counter]) + 1):]
                if not (word in list_words):
                    list_words.append(word)
                counter += 1
            if not int(x):
                counter += 1
        word = word_old
    return list_words

print(replace_number("aiuole"))
