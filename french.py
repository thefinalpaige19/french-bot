import random

questions = []
for line in open('frencho.txt'):
    questions.append(line.rstrip())



key_words = []

temp_word_count = {}

for question in questions:
    listed_question = question.lower().split(' ')
    for word in listed_question:
        if '-' in word:
            word_index = listed_question.index(word)
            listed_question[word_index] = word.split('-')
        if "l'" in word:
            word_index = listed_question.index(word)
            listed_question[word_index] = word[2:]
    for word in listed_question:
        if len(word) > 5:
            if word not in temp_word_count:
                temp_word_count[word] = 1
            else:
                temp_word_count[word] += 1

word_count = {}

for word in temp_word_count:
    if word == "quel" or word == "quelle" or word == "quels" or word == "quelles" or word == "comment" or word == "seraient" or word == "decrivez":
        pass
    else:
        word_count[word] = temp_word_count[word]



highest_count = 0
for word in word_count:
    if word_count[word] > highest_count:
        highest_count = word_count[word]

while len(key_words) <10:
    for word in word_count:
        if word_count[word] == highest_count:
            key_words.append(word)
    if highest_count <= 0:
        break
    else:
        highest_count -=1

#################

def find_similar_question(current_question):
    if question_to_ask in questions:
        questions.remove(question_to_ask)
    question_key_words = []
    split_question = current_question.split(' ')
    for word in split_question:
        if '-' in word:
            word_index = split_question.index(word)
            split_question[word_index] = word.split('-')
        if "l'" in word:
            word_index = split_question.index(word)
            split_question[word_index] = word[2:]
        if word in key_words:
            question_key_words.append(word)

    list_of_similar_questions = []
    for question in questions:
        for word in question_key_words:
            if word in question:
                list_of_similar_questions.append(question)
    if list_of_similar_questions != []:
        return random.choice(list_of_similar_questions)
    else:
        if question_to_ask in questions:
            questions.remove(question_to_ask)
        return random.choice(questions)


question_to_ask = random.choice(questions)
print(question_to_ask)









next_question = input("Next question? ")
while next_question:
    question_to_ask = find_similar_question(question_to_ask)
    print(question_to_ask)
    next_question = input("Next question? ")
