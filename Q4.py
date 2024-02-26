#Question 4
# Write a function that takes the name of the text file as parameter. print out the 3 letter words that starts with "b".

def words_b(filename):
    """
    Find 3 letter words in the file and print them
    :param filename: Name of the file
    :return: Nothing
    """
    punctuation = ",!?."
    #open the file
    with open(filename, "r") as file:
        # go over the file line by line
        for line in file:
            # replace each punctuation mark with nothing
            for p in punctuation:
                line = line.replace(p, "")
            # get the words in the line
            words = line.split(" ")
            for word in words:
                if len(word) == 3 and word.startswith("b"):
                    print(word)
    return

# call the function
words_b("text.txt")