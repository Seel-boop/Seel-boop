import time

def word_no_voul():
    sentence = input("words: ")
    remove = ["a", "e", "e", "i", "o", "u"]
    length = len(remove)
    global new_sentence
    new_sentence = sentence
    for i in range(6):
        new_sentence = new_sentence.replace(remove[i], "")

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
