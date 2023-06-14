#!/usr/bin/python3
def weight_average(my_list=[]):
    if not list:
        return 0
    weight = sum(score * weight for score, weight in my_list)
    total = sum(weight for _, weight in my_list)
    return weight / total
