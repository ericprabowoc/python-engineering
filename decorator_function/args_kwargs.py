def makeSentence(**words):
    sentence=''
    for word in words.values():
        sentence+=word
    return sentence
 
print('Sentence:', makeSentence(a='Kwargs ',b='are ', c='awesome!'))

def multiplyNumbers(*numbers):
    product=1
    for n in numbers:
        product*=n
    return product
 
print("product:",multiplyNumbers(4,4,4,4,4,4)) 
