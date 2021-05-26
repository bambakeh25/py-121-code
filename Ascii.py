# Goal: 
# 1. get user input 
# 2. convert each letter of input into ASCII
# 3. get sum of all numbers 

word = input('please give me ASCII> ')

def AsciiOutput(word):
    sum_of_words = 0

    for letter in word:
        print(letter)
        sum_of_words += ord(letter)
    
    print("sum of Ascii ", sum_of_words)

AsciiOutput(word)
