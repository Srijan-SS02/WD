def word_frequency(sentence):
    words=sentence.split()
    
    frequency={}
    
    for word in words:
        
        word = word.strip()
        
        frequency[word]= frequency.get(word, 0)+1

    return frequency

sentence=input("Enter a sentence:")
result=word_frequency(sentence)
print(result)
# print(word_frequency(sentence))