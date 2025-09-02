def palindrome(word):
    cleaned = ""  
    for char in word:
        if char.isalnum():            
            cleaned += char.lower()   
    reversed_word = ""  
    for char in cleaned:
        reversed_word = char + reversed_word
    if cleaned == reversed_word:
        return True
    else:
        return False
print(palindrome("racecar"))                      # True
print(palindrome("Nurses Run"))                   # True
print(palindrome("Sit on a potato pan, Otis."))   # True
print(palindrome("Hello"))                        # False


def parentheses(sequence):
    balance = 0
    for char in sequence:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
            if balance < 0:
                return False
    return balance == 0
print(parentheses("((blah)()()())"))     # True
print(parentheses("(((())blee))"))       # True
print(parentheses("(()hello((())()))"))  # True
print(parentheses("((((((())"))           # False
print(parentheses("()))"))                # False


