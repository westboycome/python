import random
import bisect

def create_student_scores(n):
    if n >= 0:
        scores = []
        for x in range(n):
            scores.append(random.randrange(0, 101, 1))
        return  scores
    else:
        print('the number should be greater than 0!')

def grade(score, breakpoints = [60, 70, 80, 90], grades = 'FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]

def main():
    student_scores = create_student_scores(10)
    student_results = [grade(score) for score in student_scores]
    print('学生成绩:{}\n评定结果:{}'.format(student_scores, student_results))

if __name__ == '__main__':
    main()