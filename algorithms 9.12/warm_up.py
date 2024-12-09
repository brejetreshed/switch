def count_vowels(str):
    vowels = set("aeiouAEIOU")  
    vowel_count = 0
    consonants_count = 0
    
    for char in str:
        if char.isalpha():  # Check if the character is a letter
            if char in vowels:
                vowel_count += 1
            else:
                consonants_count += 1
    return vowel_count, consonants_count

str = "Hello, World!"
vowels, consonants = count_vowels(str)
print(f"Vowels: {vowels}, Consonants: {consonants}")


def median_char(str):
    alphabetic_chars = sorted([char.lower() for char in str if char.isalpha()])
    if not alphabetic_chars:
        return None  
    
    n = len(alphabetic_chars)
    median_char = alphabetic_chars[(n-1) // 2]  
    return median_char

print(median_char("question"))


def word_score(str):
    return sum(ord(char) - ord('a') + 1 for char in str)

def highest_score(sentence):
    words = sentence.split()  
    max_score = 0
    highest_word = ""
    
    for word in words:
        score = word_score(word)  
        if score > max_score:
            max_score = score
            highest_word = word
    
    return highest_word


def largest_of_3(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    else:
        return c

print(largest_of_3(10,7,15))

