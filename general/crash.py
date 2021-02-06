import math
def lcm(a, b):
    a,b = int(a), int(b)
    return abs(a*b) // math.gcd(a, b)

def get_first_common_element(x,y):
    ''' Fetches first element from x that is common for both lists
        or return None if no such an element is found.
    '''
    for i in x:
        if i in y:
            return i

    return -1

def first_crash(r1, r2, v1, v2, T, d):
    T1 = 2 * math.pi * r1 / abs(v1)
    T2 = 2 * math.pi * r2 / abs(v2)
    if r1 + r2 == d:
        print(int(lcm(T1, T2))," E&F")
        return
    x = (r2**2 - r1**2 + d**2)/(2*d)
    chord_length = 2 * math.sqrt(r2**2 - x**2)
    t_arc_12 = (2 * math.asin(chord_length/(2 * r1)) * r1 ) / v1
    t_arc_11 = T1 - t_arc_12
    t_arc_21 = (2 * math.asin(chord_length/(2 * r2)) * r2 ) / v2
    t_arc_22 = T2 - t_arc_21
    
    if v1 < 0:
      	t_arc_1 = t_arc_11
    else :
      	t_arc_1 = t_arc_12
    
    if v2 < 0:
      	t_arc_2 = t_arc_21
    else :
      	t_arc_2 = t_arc_22
    
    # for E
    ## for motor 1
    m1E = [int(i*T1) for i in range(1, int((T//T1)+1))]
    ## for motor 2
    m2E = [int(t_arc_2)]
    for i in range(1, int((T-t_arc_2)//T2)+1):
      	m2E.append(int(i*T2 + t_arc_2))

	# for F
    ## for motor 2
    m2F = [int(i*T2) for i in range(1, int((T//T2)+1))]
    ## for motor 1
    m1F = [int(t_arc_1)]
    for i in range(1, int((T-t_arc_1)//T1) + 1):
      	m1F.append(int(i*T1 + t_arc_1))

    t_E =  get_first_common_element(m1E, m2E)
    t_F =  get_first_common_element(m1F, m2F)

    if t_E == -1 and t_F != -1:
        print(t_F,"  F")
    elif t_F == -1 and t_E != -1:
        print(t_E," E")
    elif t_F != -1 and t_E != -1:
        print(min(t_E,t_F)," ", end = " ")
        if  min(t_E,t_F) == t_E:
            print("E")
        else:
            print("F")
    else:
        print("no crash")
   
    
if __name__ == "__main__":
    r1 = int(input())
    r2 = int(input())
    v1 = int(input())
    v2 = int(input())
    T = int(input())
    d = int(input())
    first_crash(r1, r2, v1, v2, T, d)
	