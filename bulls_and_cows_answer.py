import random

def create_answer():
    answer_list = list();
    for _ in range(4):
        answer_list.append(random.randrange(0,10))
    return answer_list

if __name__ == '__main__':
    test_list = create_answer()
    print(test_list)
