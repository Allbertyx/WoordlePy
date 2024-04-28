import random

print("THIS IS WORLDLE, YOU HAVE 5 TRY'S TO GET THE CORRECT ANSWER")

words = ["marvel", "batman", "superman", "spiderman", "green-goblin", "sandman", "electro", "joker", "robin", "spectrum", "gordon", "penguin", "cyclop", "flash", "wonder-woman", "conan", "dc", "batgirl", "rogue", "goku"]

num_word_selected = random.randrange(0, len(words))

word_selected = words[num_word_selected]

#print(word_selected)

word_list_splited = list(word_selected)

#print(word_list_splited)

ocult_word = []

while len(ocult_word) != len(word_list_splited):
    ocult_word.append("X")

print(ocult_word)

count = 0

for i in range(5):
    
    user_try = str(input("Select your word: "))

    word_user_spliterd = list(user_try)

    if len(word_user_spliterd) != len(word_list_splited):

        print("TRY AGAIN")
    else:

        for j in range(len(word_list_splited)):
            if word_list_splited[j] == word_user_spliterd[j]:
                ocult_word[j] = word_user_spliterd[j]
        
        if ocult_word == word_list_splited:
            print("Congratulations YOU WIN!!!!")
            break

        print(ocult_word)

        count += 1

        if count == 5:
            print("YOU LOSE!!!!")