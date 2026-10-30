import itertools

#print("Hello")

#alphabet = ["a", "b"]

#forbidden = ["ab"]

def words_of_len(alphabet, forbidden, d):
    valid = []
    # generate all words 
    for guy in itertools.product(alphabet, repeat=d):
        word = ""
        #create flag for if word allowed
        is_allowed = True
        for i in guy:
            word += i
        for forbidden_word in forbidden:
            #trigger flag if forbidden substring detected
            if forbidden_word in word:
                is_allowed = False 
        #add word to valid list if allowed
        if is_allowed:
            valid.append(word)
    
    return valid

def data(alphabet, forbidden, d):
    print("\nTotal number of words: " + str(len(alphabet)**d))
    good_words = words_of_len(alphabet, forbidden, d)
    num_valid = len(good_words)
    num_invalid = len(list(itertools.product(alphabet, repeat=d))) - num_valid
    print("Alphabet: " + str(alphabet))
    print("Forbidden: " + str(forbidden))
    print("d = " + str(d) + "\n")
    print("Number of valid words: " + str(num_valid))
    print("Number of invalid words: " + str(num_invalid))
    print("Good words: " + str(good_words))
    print("-------------------------------------------------------------------------------------------------")
    
#words = words_of_len(2)

#for i in words:
#    print(i)

data(["a", "b"], ["aba"], 2)
data(["a", "b"], ["aba"], 3)
data(["a", "b"], ["aba"], 4)
data(["a", "b"], ["aba"], 5)
data(["a", "b"], ["aba"], 6)
data(["a", "b"], ["aba"], 7)
data(["a", "b"], ["aba"], 8)
