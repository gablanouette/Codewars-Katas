'''
Simple Pig Latin
Move the first letter of each word to the end of it, then add 'ay' to the end of 
the word.
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
'''


def pig_it(text):
    new_text = text.split(' ')
    
    pig_latin = []
    
    for words in new_text:
        if words[:-2] + words[:-1] != 'ay' and words[0].isalpha():
            word = words[1:] + words[0] + 'ay'
            pig_latin.append(word)
        else:
            pig_latin.append(words)
            
    return ' '.join(pig_latin)
    
