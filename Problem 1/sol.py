T = int(input())

m = 0
while(m < T):
    O = (input().split())
    N = int(O[0])
    K = int(O[1])
    
    
    Q = list(input().split(" "))
    L = list()
    for i in Q:
        L.append(int(i))
        
    filter_a = [L[i:i+j] for i in range(0,len(L)) for j in range(1,len(L)-i+1)]
    a = list()
    for i in filter_a:
        if i not in a:
            a.append(i)
    
    
    new = list()
    for i in a:
        new.append(sorted(i, reverse = True))
        
    def checking(arr):
        s = set()
        n = len(arr)
        if n == 1:
            if arr[0] == 1:
                s.add("True")
        elif(n == 2):
            if arr[1] ==  arr[0] - 1:
                s.add("True")
        else:
            d = arr[1] - arr[0] 
            for i in range(2, n): 
                if (arr[i] - arr[i-1] == d): 
                    s.add("True")
        
        return s


    num = 0      
    for p in new:
        if len(p) == p[0]: ##and len(p) == K and (if "True" in checking(p)):
            if len(p) == K:
                if (checking(p)):
                    num += 1
            
            
    print("Case #"+ str(m+1) + ": " + str(num))
    m = m + 1


  
