'''
ISOGRAM
'''
def is_isogram(word):
    return len(word)==len(set(word.lower()))

if __name__ == '__main__':
      print(is_isogram(input("provide the word:")))
