v = [1,2,3]
def g(a,b,m):
    return m(a,b)
print(g(1,1,lambda x,y:v[x:y+1]))