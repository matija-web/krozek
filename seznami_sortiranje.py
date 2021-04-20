seznam = [1, 2, 4, 5, 15, 21, 63]
seznam2 = [1, 2, 3]

def je_sortiran (seznam):
    index = 1
    while index < len(seznam):
        if seznam[index] < seznam[index-1]:
            return False
        index += 1
    return True
    
print(je_sortiran(seznam))



def insert_sorted(originalni_seznam, seznam_ki_ga_vstavimo):
    mesto = 1
    for i in range(len(seznam_ki_ga_vstavimo)):
        originalni_seznam.insert(i + mesto, seznam_ki_ga_vstavimo[i])  
    return sorted(originalni_seznam)  
            
print(insert_sorted(seznam, seznam2))

