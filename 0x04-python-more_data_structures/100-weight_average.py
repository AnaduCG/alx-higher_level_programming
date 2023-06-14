#!/usr/bin/python3
def weight_average(my_list=[]):
        s = 0
        for i in my_list:
                s += sum(i)
        return (s / len(my_list))