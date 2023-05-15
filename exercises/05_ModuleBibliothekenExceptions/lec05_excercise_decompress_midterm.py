s_comp = "a4b3c2d1"

def decompress(s_comp):
    if len(s_comp) == 2:
        return s_comp[0]*int(s_comp[1])
    else:
        return decompress(s_comp[0:2]) + decompress(s_comp[2:])
    
print(decompress(s_comp))