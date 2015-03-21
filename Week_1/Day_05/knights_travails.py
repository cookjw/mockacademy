from collections import deque

def on_board(square):
    return (square[0] in range(1,9)) and (square[1] in range(1,9))

def legal_moves(starting_square):
    if on_board(starting_square):
        x = starting_square[0]
        y = starting_square[1]
        preliminary_list = [
                (x+m, y+n) for m in (-2,-1,1,2) for n in (-2,-1,1,2)
                if abs(m) != abs(n)
            ]
        return filter(on_board, preliminary_list)
    else:
        raise Exception("{} not on board!".format(str(starting_square)))

def knight_path(origin, destination):
    ancestors = {}    
    queue = deque([origin])
    n = 1
    while queue:
        item = queue.popleft()
        n += 1
        if item == destination:
            path = [item]            
            while item != origin:
                path.append(ancestors[item])
                item = ancestors[item]
            return path[::-1]
        else:
            for child in legal_moves(item):
                if not child in ancestors:    
                    ancestors[child] = item
                    queue.append(child)
                
                    
    
        
                
    
    
    