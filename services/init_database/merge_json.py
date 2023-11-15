import json

# TODO: Переработать в класс
# 1. Сделать класс
# 2. Переработать в несколько методов
# 3.
# 4. print в декоратор

print("Start merge json")

# Чтение json получение 2х переменных
with open("static/init_database/fixtures/question.json", "r") as raw_questions:
    questions = json.load(raw_questions)

with open("static/init_database/fixtures/answer.json", "r") as raw_answers:
    answers = json.load(raw_answers)

# Атрибут объекта
questions_answers = []

# Формирование обзего словаря questions_answers
# Посмотреть как будет выглядеть в генераторе списка все вместе
for question in questions["questions"]:
    answers_list = []

    # Переделать в генератор списка
    for answer in answers["answers"]:
        if question["id"] == answer["questions_id"]:
            answers_list.append(answer)

    questions_answers.append({"question": question, "answers": answers_list})

print("Complete merge json\n")
