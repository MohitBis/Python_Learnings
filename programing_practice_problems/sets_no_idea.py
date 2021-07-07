"""
There is an array of n integers. There are also 2 disjoint sets, A and B , each containing m integers.
You like all the integers in set A and dislike all the integers in set B. Your initial happiness is O.
For each i integer in the array, if i belong to A , you add 1 to your happiness. If i belong to B, you add -1 to your happiness.
Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since A and B are sets, they have no repeated elements. However, the array might contain duplicate elements.

Constraints:
1 <= n <= 10^5
1 <= m <= 10^5
1 <= Any integer in the input <= 10^9

Input Format:
The first line contains integers n and m separated by a space.
The second line contains n integers, the elements of the array.
he third and fourth lines contain m integers, A and B, respectively.\

Output Format:
Output a single integer, your total happiness.

Sample Input:
3 2
1 5 3
3 1
5 7

Sample Output:
1
"""

n,m = tuple(map(int,input().split()))
array = list(map(int,input().split()))
A = set(map(int,input().split()))
B = set(map(int,input().split()))
happiness = 0

for i in array:
    if i in A:
        happiness += 1
    elif i in B:
        happiness -= 1
print(happiness)