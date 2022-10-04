'''
Generators

'''


def word_gen(word):
    for i in word:
        yield(i)

if __name__ == '__main__':
    gen_word= word_gen("NAMES")
    print(next(gen_word))
    print(next(gen_word))
    print(next(gen_word))


def word_gen_sec(word):
    for i in range( 0,len(word),2) :
        yield (word[i])

if __name__ == '__main__':
            gen_word = word_gen_sec("NAMES")
            print(next(gen_word))
            print(next(gen_word))
            print(next(gen_word))



def word_gen_sec1(word):
    words=word.split()
    for i in range(0,len(words),1) :
        yield (words[i])


if __name__ == '__main__':
    gen_words1 = word_gen_sec1("NAMES and kotc")
    print(next(gen_words1))
    print(next(gen_words1))



def word_gen_sec2(word):
    words=word.split()
    for i in range(0,len(words),2) :
        yield (words[i])


if __name__ == '__main__':
    gen_words2 = word_gen_sec2("NAMES and kotc")
    print(next(gen_words2))
    print(next(gen_words2))
