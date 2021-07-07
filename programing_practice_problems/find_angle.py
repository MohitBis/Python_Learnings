"""
ABC is a right triangle at B

Point M is the midpoint of hypotenuse AC.
You are given the lengths AB and BC.
Your task is to find Angel MBC in degree

input:
The first line contains the length of side AB.
The second line contains the length of side BC.

output:
Angel MBC in degree

Examples:
If angle is 56.5000001°, then output 57°.
If angle is 56.5000000°, then output 57°.
If angle is 56.4999999°, then output 56°.

Sample Input
10
10

Sample output:
45
"""
import math

AB = int(input())
BC = int(input())
H = math.sqrt(AB**2 + BC**2)
H = H/2.0
adj = BC/2.0
Output = int(round(math.degrees(math.acos(adj/H))))
Output = str(Output)
print(f"{Output}\N{DEGREE SIGN}")