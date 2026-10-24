def recur_queens(n, row, queue, diag_prin, diag_secun, result):
    if n == row:
        result.append(queue.copy())
        return 
    
    for col in range(n):
        if col not in queue and col - row not in diag_prin and col + row not in diag_secun:
            queue.append(col)
            diag_prin.append(col - row)
            diag_secun.append(col + row)
            
            recur_queens(n, row + 1, queue, diag_prin, diag_secun, result)
        
            queue.pop()
            diag_prin.pop()
            diag_secun.pop()
    

  

def dfs_n_queens(n:int):
    if n < 1:
        return []

    result = []
    
    recur_queens(n, 0 , [], [], [], result)
                              
       
    return result



print(dfs_n_queens(5))
