import json

print("Start merge json")

with open("database/init_database/fixtures/question.json", "r") as raw_questions:
    questions = json.load(raw_questions)


with open("database/init_database/fixtures/answer.json", "r") as raw_answers:
    answers = json.load(raw_answers)

questions_answers = []

for question in questions["questions"]:
    answers_list = []
    for answer in answers["answers"]:
        if question["id"] == answer["questions_id"]:
            answers_list.append(answer)
    questions_answers.append({"question": question, "answers": answers_list})

print("Complete merge json\n")
