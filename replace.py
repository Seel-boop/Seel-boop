#replace will replace all vowels and duplicate letters except for the first instance of those letters.



import time
# Removes the vowels
def word_no_voul():
    sentence = input("words: ")
    # By cycling through a list of the vowels
    remove = ["a", "e", "e", "i", "o", "u"]
    length = len(remove)
    global new_sentence
    new_sentence = sentence
    for i in range(6):
        # And replacing them
        new_sentence = new_sentence.replace(remove[i], "")
# Removes duplicate letters except for the first instance of the letters.
def word_no_dupe():
    final = new_sentence
    final1 = len(final)
    for i in range(final1):
        for v in range(final1):
            if new_sentence[v] == new_sentence[i]:
                final = final.replace(new_sentence[i], "@")
                final = final.replace("@", new_sentence[i], 1)
                final = final.replace("@", "")
                break
    print(final)
    time.sleep(5)
word_no_voul()
word_no_dupe()
