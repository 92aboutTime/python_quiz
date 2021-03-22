import numpy as np

def solution(board, moves):
    board = np.array(board)
    
    N_size = board.shape[0] - 1
    board_height_list = [0 for _ in range(N_size + 1)]
    tong_list = []
    
    answer = 0
    
    # board_height_list에 값을 채우기
    for column in range(N_size + 1):
        for row in range(N_size + 1):
            if board[row][column] != 0:
                board_height_list[column] = row
                break
                
    print(board_height_list)
    
    # 실제로 moves에 있는 값들을 실행시키는 과정
    for move in moves:
        move = move -1
        
        # 밑바닥인데, 0이 아닌 경우
        if ((board_height_list[move] == N_size) and (board[board_height_list[move]][move] != 0)):         
            tong_list.append(board[board_height_list[move]][move])
            
            if len(tong_list) > 1:
                if tong_list[-1] == tong_list[-2]:
                    
                    
                    answer = answer + 2
                    del tong_list[-1 : -2]
                    # print(tong_list)
            
            board[board_height_list[move]][move] = 0
            board_height_list[move] = N_size
            
            
        elif  board_height_list[move] != N_size: # 밑바닥이 아닌 경우 
            
            print(tong_list)
            tong_list.append(board[board_height_list[move]][move])

            
            if len(tong_list) > 1:
                if tong_list[-1] == tong_list[-2]:
                    answer = answer + 2
                    del tong_list[-1 : -2]
                    
                    
            print("a")
            board[board_height_list[move]][move] = 0
            board_height_list[move] = board_height_list[move] + 1
            
            
        else : # 밑바닥이고 0인 경우
            continue
            
    return answer