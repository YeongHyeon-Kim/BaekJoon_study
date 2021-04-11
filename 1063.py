
    
def move(moving,king_location,stone_location):
    king_location = list(king_location)
    king_location[1] = int(king_location[1])
    stone_location = list(stone_location)
    stone_location[1] = int(stone_location[1])
    
    if moving == 'B':
        if king_location[1] != 1:
            if ((king_location[1]-1) == (stone_location[1])) & ((king_location[0]) == (stone_location[0])):
                if stone_location[1] !=1:
                    king_location[1] -=1
                    stone_location[1] -=1
                    return ''.join(map(str,king_location)), ''.join(map(str,stone_location))
                else:
                    return ''.join(map(str,king_location)), ''.join(map(str,stone_location))
            else:
                king_location[1] -=1
                return ''.join(map(str,king_location)), ''.join(map(str,stone_location))
        else:    
            return ''.join(map(str,king_location)), ''.join(map(str,stone_location))
        
    
    elif moving == 'T':
        if king_location[1] != 8:
            if ((king_location[1]+1) == (stone_location[1])) & ((king_location[0]) == (stone_location[0])):
                if stone_location[1] !=8:
                    king_location[1] +=1
                    stone_location[1] +=1
                    return ''.join(map(str,king_location)), ''.join(map(str,stone_location))
                else:
                    return ''.join(map(str,king_location)), ''.join(map(str,stone_location))
            
            else:
                king_location[1] +=1
                return ''.join(map(str,king_location)), ''.join(map(str,stone_location))
        else:    
            return ''.join(map(str,king_location)), ''.join(map(str,stone_location))

    elif moving == 'L':
        if king_location[0] != 'A':
            if (chr(ord(king_location[0])-1) == (stone_location[0])) & ((king_location[1]) == (stone_location[1])):
                if stone_location[0] !='A':
                    king_location[0] = chr(ord(king_location[0])-1)
                    stone_location[0] = chr(ord(king_location[0])-1)
                    return ''.join(map(str,king_location)), ''.join(map(str,stone_location))
                else:
                    return ''.join(map(str,king_location)), ''.join(map(str,stone_location))
            else:
                king_location[0] = chr(ord(king_location[0])-1)
                return ''.join(map(str,king_location)), ''.join(map(str,stone_location))   
        else:    
            return ''.join(map(str,king_location)), ''.join(map(str,stone_location))
    
    elif moving == 'R':
        if king_location[0] != 'H':
            if (chr(ord(king_location[0])+1) == (stone_location[0])) & ((king_location[1]) == (stone_location[1])):
                if stone_location[0] !='H':
                    king_location[0] = chr(ord(king_location[0])+1)
                    stone_location[0] = chr(ord(king_location[0])+1)
                    return ''.join(map(str,king_location)), ''.join(map(str,stone_location))
                else:
                    return ''.join(map(str,king_location)), ''.join(map(str,stone_location))
            else:
                king_location[0] = chr(ord(king_location[0])+1)
                return ''.join(map(str,king_location)), ''.join(map(str,stone_location))   
        else:    
            return ''.join(map(str,king_location)), ''.join(map(str,stone_location))
    
    
    elif moving == 'RT':
        if (king_location[0] != 'H')&(king_location[1] != 8):
            if (chr(ord(king_location[0])+1) == (stone_location[0])) & ((king_location[1]+1) == (stone_location[1])):
                if (stone_location[0] != 'H')&(stone_location[1] != 8):
                    king_location[0] = chr(ord(king_location[0])+1)
                    king_location[1]+=1
                    
                    stone_location[0] = chr(ord(king_location[0])+1)
                    stone_location[1]+=1
                    
                    return ''.join(map(str,king_location)), ''.join(map(str,stone_location))
                
                else:
                    return ''.join(map(str,king_location)), ''.join(map(str,stone_location))
            
            else:
                king_location[0] = chr(ord(king_location[0])+1)
                king_location[1]+=1
                return ''.join(map(str,king_location)), ''.join(map(str,stone_location))   
        
        else:    
            return ''.join(map(str,king_location)), ''.join(map(str,stone_location))
    
    elif moving == 'LT':
        if (king_location[0] != 'A')&(king_location[1] != 8):
            if (chr(ord(king_location[0])-1) == (stone_location[0])) & ((king_location[1]+1) == (stone_location[1])):
                if (stone_location[0] != 'A')&(stone_location[1] != 8):
                    king_location[0] = chr(ord(king_location[0])-1)
                    king_location[1]+=1
                    
                    stone_location[0] = chr(ord(king_location[0])-1)
                    stone_location[1]+=1
                    
                    return ''.join(map(str,king_location)), ''.join(map(str,stone_location))
                
                else:
                    return ''.join(map(str,king_location)), ''.join(map(str,stone_location))
            
            else:
                king_location[0] = chr(ord(king_location[0])-1)
                king_location[1]+=1
                return ''.join(map(str,king_location)), ''.join(map(str,stone_location))   
        
        else:    
            return ''.join(map(str,king_location)), ''.join(map(str,stone_location))
    
    elif moving == 'LB':
        if (king_location[0] != 'A')&(king_location[1] != 1):
            if (chr(ord(king_location[0])-1) == (stone_location[0])) & ((king_location[1]-1) == (stone_location[1])):
                if (stone_location[0] != 'A')&(stone_location[1] != 1):
                    king_location[0] = chr(ord(king_location[0])-1)
                    king_location[1]-=1
                    
                    stone_location[0] = chr(ord(king_location[0])-1)
                    stone_location[1]-=1
                    
                    return ''.join(map(str,king_location)), ''.join(map(str,stone_location))
                
                else:
                    return ''.join(map(str,king_location)), ''.join(map(str,stone_location))
            
            else:
                king_location[0] = chr(ord(king_location[0])-1)
                king_location[1]-=1
                return ''.join(map(str,king_location)), ''.join(map(str,stone_location))   
        
        else:    
            return ''.join(map(str,king_location)), ''.join(map(str,stone_location))
    
    
    elif moving == 'RB':
        if (king_location[0] != 'H')&(king_location[1] != 1):
            if (chr(ord(king_location[0])+1) == (stone_location[0])) & ((king_location[1]-1) == (stone_location[1])):
                if (stone_location[0] != 'A')&(stone_location[1] != 1):
                    king_location[0] = chr(ord(king_location[0])+1)
                    king_location[1]-=1
                    
                    stone_location[0] = chr(ord(king_location[0])+1)
                    stone_location[1]-=1
                    
                    return ''.join(map(str,king_location)), ''.join(map(str,stone_location))
                
                else:
                    return ''.join(map(str,king_location)), ''.join(map(str,stone_location))
            
            else:
                king_location[0] = chr(ord(king_location[0])+1)
                king_location[1]-=1
                return ''.join(map(str,king_location)), ''.join(map(str,stone_location))   
        
        else:    
            return ''.join(map(str,king_location)), ''.join(map(str,stone_location))
    
    
    
    
king_location, stone_location, move_num = input().split(' ')
move_num = int(move_num)
for i in range(move_num):
    tmp = input()
    king_location, stone_location = move(tmp,king_location,stone_location)
    
print(king_location)
print(stone_location)