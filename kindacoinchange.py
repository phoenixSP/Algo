# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 14:21:32 2019

@author: shrey
"""

def ways(total, k):
    # Write your code here

    table=[[0 for x in range(k)] for x in range(total +1)]
    for i in range(k):
        table[0][i]=1

    for i in range(1,total+1):
        for j in range(k):
            x=table[i-j-1][j] if i-j-1>=0 else 0
            y=table[i][j-1] if j>=1 else 0
            table[i][j]=x+y

    return table[total][k-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    total = int(input().strip())

    k = int(input().strip())

    result = ways(total, k)

    fptr.write(str(result) + '\n')

    fptr.close()