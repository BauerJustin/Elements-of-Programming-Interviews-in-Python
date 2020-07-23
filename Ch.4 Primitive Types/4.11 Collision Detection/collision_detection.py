# code
def collision(x1,y1,w1,h1,x2,y2,w2,h2):
    if x1 <= x2 + w2 and x1 + w1 >= x2 and y1 <= y2 + h2 and y1 + h1 >= y2:
        return (max(x1,x2),max(y1,y2),min(x1 + w1, x2 + w2)-max(x1,x2),min(y1 + h1, y2 + h2)-max(y1,y2))
    return None