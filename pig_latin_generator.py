sentence = input("Type your sentance: ").lower()
words = sentence.split()

#makes iterable to run through loop
for i, word in enumerate(words):

    #if first letter is a vowel
    if word[0] in 'aeiou' :
        words[i] = words[i]+"ay"

    #else get vowel position and postfix all the consonants present before that vowel to the end of the word with 'ay'
    else:
        has_vowel = False

        for j, letter in enumerate(word):
            if letter in 'aeiou': 
                words[i] = word[j:] + word[:j] +"ay"
                has_vowel = True
                break


        #if the word doesn't have a vowel, put postfix 'ay'
        if(has_vowel == False):
            words[i] = words[i]+"ay"

pig_latin = ' '.join(words)
print("Pig Latin: ",pig_latin)
