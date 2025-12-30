def merge_count(A):
    n = len(A)
    if n <= 1:
        return A, 0
    
    mid = n // 2
    left, cnt_left = merge_count(A[:mid])
    right, cnt_right = merge_count(A[mid:])
    
    merged = []
    cnt = cnt_left + cnt_right
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            cnt += len(left) - i
            j += 1
    
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged, cnt

N = int(input())
A = list(map(int, input().split()))

_, ans = merge_count(A)
print(ans)
