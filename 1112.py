with open("book.txt") as file:
    text = file.read()

# create a dictionnary of word frequencies
word_freq = {}
punctuation = ",.'!?;"
# remove punctuation
for p in punctuation:
    text = text.replace(p,"")

for line in file:
    words = line.split(" ")
    for word in words:
        # check and add into dictionnary
        if word in word_freq:
            #word in the dictionnary, increase the frequency by 1
        else:
            # not there, so we add it with initial value of 1
            word_freq[word]=1

print(word_freq)

file.close()

