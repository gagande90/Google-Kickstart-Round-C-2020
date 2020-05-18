num_cases_total = int(input())
m = 1
while(m <= num_cases_total):
    q = list(map(int, input().split(" ")))
    num_elements_list, num_operands_performed_on_list = q
    
    
    main_list = [0]
    main_list += list(map(int, input().split(" ")))
    
    list_of_operands = list()
    for i in range(num_operands_performed_on_list):
        w = list(input().split(" "))
        list_of_operands.append(w)
    
    query = 0
    for j in list_of_operands:
        if j[0] == "U":
            main_list[int(j[1])] = int(j[2])
        elif(j[0] == "Q"):
            making_sublist_of_main_list = [0]
            #for k in range(int(j[1]), int(j[2]) + 1):
            making_sublist_of_main_list += main_list[int(j[1]) : int(j[2]) + 1]
            for l in range(len(making_sublist_of_main_list)):
                query += ((-1)**(l + 1) * making_sublist_of_main_list[l]) * (l) 
    
    
    print("Case #" + str(m) + ": " + str(query))
    m = m + 1
