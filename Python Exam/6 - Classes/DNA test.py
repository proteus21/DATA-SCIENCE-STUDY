'''
Hamming distance

'''


person1 ="GAGCCTACTAACGGGAT"
person2 ="GAGCCTACTAACAAAT"
Child = "CATCGTAATGACGGCCT"


def is_father(person, child):
  result1 = 0
  j=0
  for i in person:



      if i!=child[j]:
        result1+=1
      j += 1
  return(result1)
print(is_father("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"), ":GAGCCTACTAACGGGAT")
#print(is_father("GTA", "GAS"))

# Second solution

def hamming(father_dna, child_dna):
    zipped_dnas = zip(father_dna, child_dna)
    return sum([1 if z[0] != z[1] else 0 for z in zipped_dnas])


def who_is_father(child_dna, *args, **kwargs):
   result= {father_dna: (hamming(child_dna, father_dna))for father_dna in args}
   return f"The father is {min(result.keys())}"
# zadanko domowe - zmienić who_is_father, tak, żeby zwracało DNA, które ma największą zgodność


print(who_is_father("CATCGTAATGACGGCCT","GAGCCTACTAACGGGAT","GAGCCTACTAACAAAT"))