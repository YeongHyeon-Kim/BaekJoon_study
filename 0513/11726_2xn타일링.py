n = int(input())

co = {1:1, 2:2, 3:3, 4:5, 5:8, 6:13}

def count(n):
    if n in co:
        return co[n]
    else:
        co[n] = count(n-1) + count(n-2)
        return co[n]

print(count(n)%10007)