def spiral(m):
    return m and list(m.pop(0)) + spiral(list(zip(*m))[::-1])
print(spiral([[1,2,3],[4,5,6],[7,8,9]]))
