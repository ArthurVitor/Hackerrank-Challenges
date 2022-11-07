if __name__ == '__main__':
    python_students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        python_students.append([name, score])
    sub = sorted(python_students, key=lambda x: x[1])
    for c in sorted(sub[1:3]):
        print(c[0])
