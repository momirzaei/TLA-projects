turing_machine = input().split("00")
tur_list=[]
for i in range(0, len(turing_machine)):
    tur_list.append(turing_machine[i].split("0"))

# print(tur_list)

final_state=""

for i in range(0, len(turing_machine)):
    if len(tur_list[i][2])>len(final_state):
        final_state=tur_list[i][2]

# print(final_state)
num_inp=int(input())
for i in range(0, num_inp):
    current_state="1"
    inp_str=input().split("0")
    for q in range(0, 20):
        inp_str.insert(len(inp_str),"1")
    for q in range(0, 20):
        inp_str.insert(0,"1")


    if len(inp_str[20])==0:
        check0=True
        while check0 :
            check0=False
            for j in range(0, len(turing_machine)):
                if (current_state == tur_list[j][0] and tur_list[j][1]=="1"):
                    current_state =tur_list[j][2]
                    check0=True
                    
            if not check0 :              
                if current_state==final_state:
                    print("Accepted")
                else:
                    print("Rejected")
                    break
    else:
        index = 20
        while index < len(inp_str):
            check1=False
            for j in range(0, len(turing_machine)):
                if (inp_str[index]==tur_list[j][1] and current_state == tur_list[j][0]):
                    current_state =tur_list[j][2]
                    inp_str[index] = tur_list[j][3]
                    if tur_list[j][4] == "1" :
                        index = index-1
                    else: index = index+1
                    check1=True
                    break
            if not check1 :
                if current_state==final_state:
                    print("Accepted")
                else:
                    print("Rejected")
                break
            # print(current_state )
            # print(check)
            # print(index )
        
        # if check1 :
        #     if current_state==final_state:
        #         print("Accepted")
        #     else:
        #         for j in range(0, len(turing_machine)):
        #             check2=False
        #             if (current_state == tur_list[j][0] and tur_list[j][1]=="1"):
        #                 current_state =tur_list[j][2]
        #                 if current_state==final_state:
        #                     print("Accepted")
        #                 else:
        #                     print("Rejected")
        #                 check2=True
        #                 break

        #         if not check2 :
        #             print("Rejected")
        



    




