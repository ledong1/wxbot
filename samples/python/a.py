# coding:utf-8
import random


def weight_choice(list, weight):

    new_list = []
    for i, val in enumerate(list):
        new_list.extend(val * weight[i])
    return random.choice(new_list)


if __name__ == "__main__":
    print(weight_choice(['A', 'B', 'C', 'D'], [5, 2, 2, 1]))
    a = "abc#hello"
    print(a[1:])