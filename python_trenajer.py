import random
import time

questions = {
    "Как создать переменную в Python?": "x = 5",
    "Что такое цикл в Python?": "Инструкция, которая выполняется несколько раз.",
    "Что такое список в Python?": "Упорядоченная изменяемая коллекция объектов.",
    "Что такое функция в Python?": "Блок кода, который выполняет определенную задачу.",
    "Чем отличается `list` от `tuple` в Python?": "`list` является изменяемым, а `tuple` - неизменяемым.",
    "Каким образом можно комментировать код в Python?": "С помощью символов `#` для однострочных комментариев и тройных кавычек для многострочных.",
    "Что такое индексация в списках Python?": "Нумерация элементов списка, начинающаяся с 0.",
    "Что такое метод `append()` в Python?": "Метод для добавления элемента в конец списка.",
    "Что такое условный оператор `if` в Python?": "Оператор, который выполняет код, если указанное условие истинно.",
    "Что такое `for` loop в Python?": "Цикл, который выполняет код для каждого элемента в последовательности.",
}

def generate_wrong_answers(correct_answer, num, questions):
    wrong_answers = []
    all_answers = list(questions.values())
    all_answers.remove(correct_answer)
    random.shuffle(all_answers)
    wrong_answers = all_answers[:num]
    return wrong_answers

def play_round(asked_questions, remaining_questions):
    if not remaining_questions:
        print("У вас закончились вопросы для тренировки.")
        return 0, "", ""

    question = random.choice(list(remaining_questions.keys()))
    correct_answer = remaining_questions[question]
    wrong_answers = generate_wrong_answers(correct_answer, 3, questions)
    all_answers = wrong_answers + [correct_answer]
    random.shuffle(all_answers)

    print(question)
    for i, answer in enumerate(all_answers):
        print(f"{i + 1}: {answer}")

    start_time = time.time()
    while True:
        user_answer = input("Введите номер правильного ответа: ")
        if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
            break
        else:
            print("Введите корректный номер ответа.")

    if time.time() - start_time > 10:
        print(f"Время истекло. Правильный ответ: {correct_answer}\n")
        return 0, question, correct_answer

    if int(user_answer) - 1 == all_answers.index(correct_answer):
        print("Правильно!\n")
        return 1, question, correct_answer
    else:
        print(f"Неправильно. Правильный ответ: {correct_answer}\n")
        return 0, question, correct_answer

def python_trainer():
    total_score = 0
    asked_questions = []
    remaining_questions = questions.copy()
    for _ in range(20):  # 20 вопросов для тренировки
        score, question, correct_answer = play_round(asked_questions, remaining_questions)
        total_score += score
        asked_questions.append(question)
        if question in remaining_questions:
            del remaining_questions[question]
        if not remaining_questions:
            asked_questions = []
            remaining_questions = questions.copy()

    print(f"Игра окончена. Ваш итоговый счет: {total_score} из 20.")

if __name__ == "__main__":
    python_trainer()
