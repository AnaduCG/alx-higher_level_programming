#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """a function that divides element by element 2 lists

    Args:
        my_list_1 (list): list to be handled by the function
        my_list_2 (list): list to be handled by the function
        list_length (int): _description_

    Returns:
        list: a new list (length = list_length) with all divisions
    """
    i = 0
    len_of_ele = 0
    div = 0
    new_list = []
    for i in range(list_length):
        try:
            div = my_list_1[i]/my_list_2[i]
            len_of_ele += 1
        except (TypeError, ValueError):
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            new_list.append(div)
    return new_list
