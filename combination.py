def combination(a, b):
    #ans is (a+b)C(smaller value of a and b)
    if b > a:
        a,b= b,a
    count = 1
    l = [[0] for i in range(a+b)]
    head = b-2
    for i in range(b):
        l[i] = [1]
    i = b
    print(l)
    while i < len(l):
        
        l[i] = [1]
        l[i-1] = [0]
        i += 1
        count += 1
        print(l)
        #print(l, i, head)
        if i == len(l):
            if head != len(l)-b:
                l[head+1] = [1]
                head += 1
                l[head-1] = [0]
                
                l[i-1] = [0]
                i = head + 1
                l[i] = [1]
                i +=1
                print(l)
                count +=1
    return count
print(combination(2,5))
