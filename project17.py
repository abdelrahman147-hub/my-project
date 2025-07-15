sen=input("enter a sentence: ")
words= sen.split()
reversed_words=words[::-1]
reversed_sen=" ".join(reversed_words)
print(reversed_sen)