# 정답 판별

import random

def runQuiz(get_quiz, answers, num_questions=3):
    point = 0

    for i in random.sample(range(len(get_quiz)), num_questions):  # 문제 중복 회피
        print(get_quiz[i])
        user_input = input("정답을 입력하세요: ")

        if user_input.strip().lower() == answers[i].lower():
            print("정답입니다!")
            point += 1
        else:
            print(f"오답입니다. 정답은 '{answers[i]}' 입니다.")

    return point

