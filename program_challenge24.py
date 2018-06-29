def inAnagram(first , new):
    if first == new[::-1]:
        return True
    else:
        return False
string1 = raw_input('Enter the first string :')
string2 = raw_input('Enter the second string :')

compare = inAnagram(string1, string2)
if compare is True:
    print( '"' + string1 +'" and "' + string2 +'" are anagrams')
else:
    print("They are not anagrams")

