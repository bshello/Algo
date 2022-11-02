from copy import deepcopy

def move(temp_arr, direction):

    if direction == 0:
        for c in range(N):
            pointer = 0
            for r in range(1, N):
                if temp_arr[r][c]:
                    tmp = temp_arr[r][c]
                    temp_arr[r][c] = 0
                    if temp_arr[pointer][c] == 0:
                        temp_arr[pointer][c] = tmp
                    elif temp_arr[pointer][c] == tmp:
                        temp_arr[pointer][c] += tmp
                        pointer += 1
                    else:
                        pointer += 1
                        temp_arr[pointer][c] = tmp
                        
        return temp_arr

    elif direction == 1:
        for c in range(N):
            pointer = N - 1
            for r in range(N - 2, -1, -1):
                if temp_arr[r][c]:
                    tmp = temp_arr[r][c]
                    temp_arr[r][c] = 0
                    if temp_arr[pointer][c] == 0:
                        temp_arr[pointer][c] = tmp
                    elif temp_arr[pointer][c] == tmp:
                        temp_arr[pointer][c] += tmp
                        pointer -= 1
                    else:
                        pointer -= 1
                        temp_arr[pointer][c] = tmp
                        
        return temp_arr
    
    elif direction == 2:
        for r in range(N):
            pointer = 0
            for c in range(1, N):
                if temp_arr[r][c]:
                    tmp = temp_arr[r][c]
                    temp_arr[r][c] = 0
                    if temp_arr[r][pointer] == 0:
                        temp_arr[r][pointer] = tmp
                    elif temp_arr[r][pointer] == tmp:
                        temp_arr[r][pointer] += tmp
                        pointer += 1
                    else:
                        pointer += 1
                        temp_arr[r][pointer] = tmp
                        
        return temp_arr
    
    else:
        for r in range(N):
            pointer = N - 1
            for c in range(N - 2, -1, -1):
                if temp_arr[r][c]:
                    tmp = temp_arr[r][c]
                    temp_arr[r][c] = 0
                    if temp_arr[r][pointer] == 0:
                        temp_arr[r][pointer] = tmp
                    elif temp_arr[r][pointer] == tmp:
                        temp_arr[r][pointer] += tmp
                        pointer -= 1
                    else:
                        pointer -= 1
                        temp_arr[r][pointer] = tmp
                        
        return temp_arr



def dfs(arr, depth):
    global res
    if depth == 5:
        ans = 0
        for r in range(N):
            for c in range(N):
                ans = max(arr[r][c], ans)
        res = max(ans, res)
        return

    for i in range(4):
        temp_arr = deepcopy(arr)
        move(temp_arr, i)
        dfs(temp_arr, depth + 1)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
res = 0
dfs(board, 0)
print(res)