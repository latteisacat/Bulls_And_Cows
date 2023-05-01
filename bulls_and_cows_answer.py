import random

def create_answer():
    answer_list = random.sample(range(0, 10), 4)
    return answer_list

if __name__ == '__main__':
    test_list = create_answer()
    print(test_list)

