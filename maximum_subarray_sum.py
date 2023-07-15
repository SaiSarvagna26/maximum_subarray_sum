def maximum_subarray_sum(A,B,C):
    max_sum=0
    current_sum=0
    left=0

    for right in range(A):
        current_sum+=C[right]

        while current_sum > B:
            current_sum-=C[left]
            left+=1

        max_sum=max(max_sum, current_sum)

    return max_sum


A=int(input())
B=int(input())
C=list(map(int,input().split()))

result=maximum_subarray_sum(A,B,C)
print(result)
