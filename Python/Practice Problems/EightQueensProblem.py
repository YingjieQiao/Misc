import random
import time 

points = []
queens = []

def make_a_plane(ps):
    for x in range(8):
        for y in range(8):
            ps.append((x,y))
    return ps

def diagonal_check(a,b):
    #a and b are two 2-D coordinates
    if a[0] == b[0]:
        return False
    elif abs((a[1]-b[1])/(a[0]-b[0])) == 1:
        return False
    else:
        return True

def possible_solutions(ps,qs):
    rej = []
    for p in ps:
        for q in qs:
            if p[0] == q[0] or p[1] == q[1] or diagonal_check(p,q)==False:
                rej.append(p)
    for a in rej:
        if a in ps:
            ps.remove(a)
    return ps,qs

def random_pick(ps,qs):
    #ps is the list of possible solutions, qs is the list of the queens.
    i = random.choice(ps)
    qs.append(i)
    ps.remove(i)
    return ps,qs

def find_solution():
    count = 0
    while count <= 7:
        if len(points) == 0 and len(queens) != 8:
            find_solution()
        random_pick(points,queens)
        possible_solutions(points,queens)
        count += 1
    return queens

start = time.time()

ans = []
m = True
while m:
    try:
        queens = []
        make_a_plane(points)
        a = find_solution()
    except RecursionError:
        pass
    else:
        ans.append(a)
        if len(ans) == 50: 
            #There are 92 solutions for 8 queens problem in total. 
            #However, there will be duplicates in the list, thus, even if I put a number greater than 92, it still outputs an answer.
            #I should figure out a way to edit a set in order to remove duplicates.
            m = False

for a in ans:
    print(a)
    
end = time.time()
print('Time used: ' + str(end-start))
