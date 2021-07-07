"""
Dr. John Wesley has a spreadsheet containing a list of student's IDs, marks, class and name.
Your task is to help Dr. Wesley calculate the average marks of the students.

Average = Sum of all marks/Total Students

Note:
1. Columns can be in any order. IDs, marks, class and name can be written in any order in the spreadsheet.
2. Column names are ID, MARKS, CLASS and NAME. (The spelling and case type of these names won't change.)

Input Format

The first line contains an integer , the total number of students.
The second line contains the names of the columns in any order.
The next  lines contains the , ,  and , under their respective column names.

Constraints


Output Format

Print the average marks of the list corrected to 2 decimal places.

Sample Input

TESTCASE 01
-----------
5
ID         MARKS      NAME       CLASS
1          97         Raymond    7
2          50         Steven     4
3          91         Adrian     9
4          72         Stewart    5
5          80         Peter      6


Sample Output

78.00

"""
from collections import namedtuple
n = int(input())
column = input()
sum = 0
student = namedtuple("student", column)

for i in range(n):
    stud = student._make(input().split())
    sum += int(stud.MARKS)

print("{:.2f}" .format(sum/n))
