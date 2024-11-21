#### Fonction secondaire
"""jjjj"""
import string
def ispalindrome(mot):
    """palindrome"""
    mot = mot.lower()
    mot=mot.replace(" ","")
    table=str.maketrans("éàëêûâèôç","eaeeuaeoc")
    mot=mot.translate(table)
    table1=str.maketrans("", "", string.punctuation)
    mot = mot.translate(table1)
    palindrome = mot[::-1]
    if palindrome == mot:
        print(mot+""+" est un palindrome")
        return True
    return False
#### Fonction principale


def main():
    """jjjj"""

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
