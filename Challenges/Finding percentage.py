if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        student_marks[name] = [int(x) for x in line]
    query_name = input()
    print(format(sum(student_marks[query_name]) / len(student_marks[query_name]), '.2f'))