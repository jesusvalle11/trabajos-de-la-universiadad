def vallida(solucion): 

    grupo= {'(':')','{':'}','[':']'}
    pila=[]
    
    for vall in solucion:
        if vall in grupo:
            pila.append(vall)
        elif vall in grupo.values():
            if not pila or vall != grupo[pila.pop()]:
                return False
        
    return not pila
            
print(vallida("{[()]}"))                 
print(vallida("{[(2+3)*5] - (6/3)}"))     
print(vallida("{[(()]}"))                 
print(vallida("((3+5]*2)"))               
print(vallida("[(4+2)*(7-3)]"))
