def min_shift_to_match(A, B):
  
    len_a = len(A)

    
    for n in range(1, len_a + 1):
      
        shifted_A = A[-n:] + A[:-n]
       
        if shifted_A == B:
            return n
    
    return -1

A = input().strip()
B = input().strip()

print(min_shift_to_match(A, B))