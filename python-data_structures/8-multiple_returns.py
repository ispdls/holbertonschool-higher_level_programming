#!/usr/bin/python3
def multiple_returns(sentence):
    temp_list = list(sentence)

    if not temp_list:
        return 0, None

    return len(temp_list) , temp_list[0]
