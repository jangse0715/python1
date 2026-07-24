import quiz02
from quiz01 import Quiz, Answer


def getGrade(point):
    if point == 3:
        return 'A'
    elif point == 2:
        return 'B'
    elif point == 1:
        return 'C'
    else:
        return 'F'

while True:
    get_quiz = Quiz()
    answer = Answer()

    point = quiz02.runQuiz(get_quiz, answer, num_questions=3)

    print(f"\n총 3문제 중 '{point}' 문제를 맞췄습니다.")
    print(f" 최종 등급: ' {getGrade(point)} '")

    retry = input("\n재도전 하시겠습니까? (y/n): ")
    if retry.strip().lower() != "y":
        print("게임을 종료합니다.")
        break
