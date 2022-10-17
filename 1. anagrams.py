from collections import Counter

s1= "nameless"
s2= "salesman"

if len(s1) == len(s2):
    if sorted(s1) == sorted(s2):
        print('True')
    else:
        print('False')
else:
    print('Not Even Close')

# def anagrams(s1, s2):
#     if len(s1) != len(s2):
#         print('False')
#     return sorted(s1) == sorted(s2)

# def anagrams(s1, s2):
#     if len(s1) != len(s2):
#         return False
#     return Counter(s1) == Counter(s2)