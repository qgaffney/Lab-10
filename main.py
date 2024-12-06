#Define isPalindromeRecursive as function
def isPalindromeRecursive(text):

    def clean_text(text):
        #Remove spaces, puctuations, and coverts to lowercase
        text = text.lower()
        text = ' '.join(ch for ch in text if ch.isalnum())
        return text

    if len(text) <= 1:
        return True
    
    text = clean_text(text)

    return text[0] == text[-1] and isPalindromeRecursive(text[1:-1])

#Define countVowelsConsonants as function
def countVowelsConsonants(text):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    consonants = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'}

    num_vowels = 0
    num_consonants = 0

    for char in text:
        if char in vowels:
            num_vowels += 1
        elif char in consonants:
            num_consonants += 1

        return num_vowels, num_consonants

#Print results
print(isPalindromeRecursive("Was it a cat I saw?"))
print(countVowelsConsonants("Was it a cat I saw?"))
print(isPalindromeRecursive("Was that a cat I saw?"))
print(countVowelsConsonants("Was that a cat I saw?"))
print(isPalindromeRecursive("Rotator"))
print(countVowelsConsonants("Rotator"))