class Student:
    def __init__(self, student_id, name, english_score, c_score, python_score):
        self.student_id = student_id
        self.name = name
        self.english_score = english_score
        self.c_score = c_score
        self.python_score = python_score
        self.total_score = self.english_score + self.c_score + self.python_score
        self.average_score = self.total_score / 3
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        if self.average_score >= 90:
            return 'A'
        elif 80 <= self.average_score < 90:
            return 'B'
        elif 70 <= self.average_score < 80:
            return 'C'
        elif 60 <= self.average_score < 70:
            return 'D'
        else:
            return 'F'

def input_student_data():
    students = []
    for i in range(5):
        student_id = input("학번을 입력하세요: ")
        name = input("이름을 입력하세요: ")
        english_score = int(input("영어 점수를 입력하세요: "))
        c_score = int(input("C-언어 점수를 입력하세요: "))
        python_score = int(input("파이썬 점수를 입력하세요: "))
        student = Student(student_id, name, english_score, c_score, python_score)
        students.append(student)
    return students

def calculate_total_average(students):
    total = sum(student.total_score for student in students)
    average = total / len(students)
    return total, average

def calculate_rank(students):
    students.sort(key=lambda x: x.total_score, reverse=True)
    for i, student in enumerate(students):
        student.rank = i + 1

def print_student_data(students):
    print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
        "학번", "이름", "영어점수", "C-언어점수", "파이썬점수", "총점", "등급"))
    for student in students:
        print("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
            student.student_id, student.name, student.english_score,
            student.c_score, student.python_score, student.total_score, student.grade))

def count_students_above_80(students):
    count = sum(1 for student in students if student.total_score >= 80)
    return count

def main():
    students = input_student_data()
    total, average = calculate_total_average(students)
    calculate_rank(students)
    print_student_data(students)
    print("전체 학생의 총점: {}, 평균: {}".format(total, average))
    print("80점 이상 학생 수:", count_students_above_80(students))

if __name__ == "__main__":
    main()


