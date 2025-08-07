# def check(word):
#     for i in word:
#         if i.lower() in ("a","e","i","o","u"):
#             print(i, end='')

# w=input("enter a string: ")
# check(w)


# cnt={i: word.count(i) for i in vowels if i in word}



def check(word):
    vowels="aeiouAEIOU"
    cnt={i: word.count(i) for i in vowels if i in word}
    print(cnt)

w=input("enter a string: ")
check(w)