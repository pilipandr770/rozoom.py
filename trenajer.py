import random
import time
import operator

# Функция для генерации неправильных ответов
def generate_wrong_answers(correct, min_value, max_value):
    wrong_answers = set()
    while len(wrong_answers) < 3:
        wrong = round(random.uniform(min_value, max_value), 2)
        if wrong != correct:
            wrong_answers.add(wrong)
    return list(wrong_answers)

# Функция для проведения одного раунда игры
def play_round():
    operations = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    num1 = random.randint(10, 99)
    num2 = random.randint(10, 99)
    op = random.choice(list(operations.keys()))
    correct_answer = round(operations[op](num1, num2), 2)

    # Генерация неправильных ответов
    wrong_answers = generate_wrong_answers(correct_answer, -100, 100)
    all_answers = wrong_answers + [correct_answer]
    random.shuffle(all_answers)

    print(f"Сколько будет {num1} {op} {num2}?")
    start_time = time.time()

    # Вывод вариантов ответов
    for i, answer in enumerate(all_answers):
        print(f"{i + 1}: {answer}")

    # Получение ответа пользователя
    user_answer = input("Введите номер правильного ответа: ")
    end_time = time.time()
    time_taken = end_time - start_time

    # Проверка ответа и начисление очков
    if time_taken > 5:
        return -50, 5
    elif int(user_answer) - 1 == all_answers.index(correct_answer):
        score = 100 * (1 - (0.2 * time_taken))
        return round(score), time_taken
    else:
        return -50, time_taken

# Основная функция игры
def math_trainer():
    total_score = 0
    for _ in range(20):
        score, time_taken = play_round()
        total_score += score
        print(f"Ваш ответ {'правильный' if score > 0 else 'неправильный'}. Время: {time_taken:.2f} сек. Ваш счет: {score}.\n")

    print(f"Игра окончена. Ваш итоговый счет: {total_score}.")

if __name__ == "__main__":
    math_trainer()
