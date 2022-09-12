"""
    Napisz program, który pobiera od użytkownika słowo, a następnie wyświetla słowo złożone z co drugiego znaku pobranego.
    W drugiej kolejności program powinien wyświetlić słowo z pozostałych liter.

"""
def get_words():
  my_list=[]
  my_list2=[]
  sentence=str(input("Give the word:"))
  for i in range(0,len(sentence)):
    if i%2==0:
        my_list.append(sentence[i])
    else:
        my_list2.append(sentence[i])
  return my_list,my_list2

if __name__=="__main__":
    word1, word2=get_words()
    print("First words is:",(''.join(word1)))
    print("Second words is:", (''.join(word2)))
