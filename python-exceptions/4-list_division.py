#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []

    try:
        for i in range(list_length):
            try:
                temp_list1 = my_list_1[i]
                temp_list2 = my_list_2[i]
                result = temp_list1 / temp_list2
                result_list.append(result)
            except ZeroDivisionError:
                print("division by 0")
                result_list.append(0)
            except (TypeError, ValueError):
                print("wrong type")
                result_list.append(0)
    except IndexError:
        print("out of range")

    finally:
        return result_list
