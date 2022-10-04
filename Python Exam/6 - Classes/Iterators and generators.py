# iterators

l= list(range(11))
r= reversed(l)

print(next(r))
print(next(r))
print(list(r))

# generators

def  generate_integers(n):
    for i in range(n):
        yield (i)

if __name__ == '__main__':
    gen= generate_integers(5)
    print(len(list(gen)))
    print(next(gen))
    print(next(gen))
    print(next(gen))
    print(list(gen))


string="Names"

