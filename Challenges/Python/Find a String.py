def find_subtring(string, sub_string):
    start = 0
    end = start + len(sub_string)
    cont = 0
    while end != len(string)+1:
        if string[start:end] == sub_string:
            cont += 1
        start += 1
        end += 1

    return cont
if __name__ == '__main__':
    print(find_subtring('ABCDCDC', 'CDC'))