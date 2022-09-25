"""
    Napisz prosta funkcje "szyfrujaca". Jej zadaniem jest zamiana
    co trzeciego znaku w hasle na znak gwiazdki (*).
    Przyklad:
    >> x = hide_password("moje_super_tajne_haslo123")
    >> print(x)
    "mo*e_*up*r_*aj*e_*as*o1*3"
    Pamietaj, ze dlugosc napisu nie musi byc podzielna przez 3.
"""


def hide_password(password):
    """Ukrywa co trzecia litere w hasle password.

    :param password: haslo z gwiazdkami co trzecia litere.
    :return: napis z czesciowo ukrytym haslem.

    """
    password_tmp=''
    n=0
    for i in range(0,len(password)):

        if n==3:
          password_tmp+="*"
          n=0
        else:
            password_tmp+=password[i]
            print(password_tmp, "s")
            n+=1
    return password_tmp


if __name__== "__main__":
    pass_name=str(input("Encrypt password:"))
    encrypt_pass=hide_password(pass_name)
    print(encrypt_pass)