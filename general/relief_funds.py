if __name__ == "__main__":
    n = int(input()) 	
    vol = list(map(int, input().split(" ")))
    p = int(input())
    p_ = p
    gp_count = 0
    groups = []
    all_pair = []
    vol_dict = {}
    
    while(p_ > 0):
        pair = list(map(int, input().split(" ")))
        all_pair = all_pair + pair
        if groups == []:
            groups.append(pair)
            gp_count +=1
        else:
            for i in range(gp_count):
                if pair[0] in groups[i] or pair[1] in groups[i]:
                  	groups[i] = list(set(groups[i]+pair))
                else:
                    groups.append(pair)
                    gp_count +=1            
        p_-=1
        
    for i in range(n):
        if i+1 not in all_pair:
            groups.append([i+1])
            
    for group in groups:
        vol_dict[tuple(group)] = sum(group)

    flipped_vol_dict = {} 
  
    for key, value in vol_dict.items(): 
        if value not in flipped_vol_dict: 
            flipped_vol_dict[value] = [key] 
        else: 
            flipped_vol_dict[value].append(key)
    
    max_sum = max(flipped_vol_dict.keys())

    small = flipped_vol_dict[max_sum][0]
    for group in flipped_vol_dict[max_sum]:
        if len(group) <= len(small):
            small = group

    for i in range(len(small)):
        if i == len(small)-1:
            print(small[i])
        else:
            print(small[i], end=" ")
