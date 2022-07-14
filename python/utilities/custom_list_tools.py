def sort_list_by_count_keyword(keyword=None, input_list=[]):
    '''

    :param keyword: 需要计数的关键字
    :param input_list: 输入列表
    :return: 列表
    '''
    if not keyword:
        input_list
    i = 1
    while i<len(input_list):
        j=0
        while j< len(input_list) - 1:
            if input_list[j].count(keyword) > input_list[j + 1].count(keyword):
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
            j += 1
        i += 1
    return input_list