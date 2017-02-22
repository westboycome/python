#!/usr/bin/python
STUDENT_number = 100
SCHOOL_NAME = 'Guangzhou University'
"""\
获取全局变量：学生人数STUDENT_NUMBER的值
"""
def getStudentNumber():
    return STUDENT_number

def setStudentNumber(num):
    global STUDENT_number
    STUDENT_number = num

def getSchoolName():
    return SCHOOL_NAME

def setSchoolName(name):
    global SCHOOL_NAME
    SCHOOL_NAME = name

def changeValue():
    name = '广州大学'
    number = 1000
    print('全局变量STUDENT_NUMBER =',getStudentNumber())
    print('SCHOOL_NAME=',getSchoolName())
    print('#######################################')
    print('局部变量namber = ', number)
    print('局部变量name = ', name)
    print('#######################################')
    print('改变全局变量值...')
    print('#######################################')
    setStudentNumber(number)
    setSchoolName(name)
    print('全局变量STUDENT_NUMBER = ', getStudentNumber())
    print('全局变量SCHOOL_NAME = ', getSchoolName())

changeValue()