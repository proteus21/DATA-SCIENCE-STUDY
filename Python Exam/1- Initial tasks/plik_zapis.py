"""
    Stwórz pusty plik tekstowy.
    Napisz program, który pobiera od użytkownika listę słów i zapisuje je w pliku i potem odczytuje cos tam napisał.
    Create empty file text.
    Write the program, which recive list of the words from user and save it.
"""
# Insert some text
sentence=str(input("Write any text:"))

f = open("demofile.txt", "w")
f.write('\n'.join(sentence))
f.close()

#open and read the file after the appending:
f = open("demofile.txt", "r")
print(f.read())