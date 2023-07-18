def get_child(lstring):
    global grammer_dict
    res = []
    for string in lstring:
        for char in string:
            if char.isupper():
                for p in grammer_dict[char]:
                    res.append(string.replace(char, p))
    return res


num = int(input())
grammar_input = []

for i in range(num):
    inp =input()
    inp1=inp.replace(" ","")
    inp2=inp1.replace("<","")
    inp3=inp2.replace(">","")
    grammar_input.append(inp3)

# print (grammar_input)
temp_gr=[]
temp_add=""
null_rem=[]
# for i in range(num):
#     if "#" in grammar_input[i] :
#         start_gr=grammar_input[i].split("-")[0]
#         for j in range(num): 
#             temp_gr=grammar_input[j].split('-','|')
#             for q in range(len(temp_gr)):
#                 if start_gr in  temp_gr[q]:

for i in range(num):
    if "#" in grammar_input[i] :
        start_gr=grammar_input[i].split("-")[0]
        # print(start_gr)
        for j in range(num): 
            if start_gr in grammar_input[j]:
                start_g1=grammar_input[j].split("-")[0]
                temp_gr = grammar_input[j].replace(start_gr,"").replace("-","|")
                temp_gr = temp_gr.split("|")
                str_gr=grammar_input[j].replace("-","|").split("|")
                temp_gr.extend(str_gr)
                if start_gr==start_g1:
                    temp_gr.pop(0)
                    temp_gr.insert(0,start_gr)
                temp_gr = list(dict.fromkeys(temp_gr))

                for q in range(len(temp_gr)):
                    if q == 0 :
                        temp_add = temp_gr[0] + "-"
                    else :
                        temp_add += temp_gr[q] + "|"
                
                temp_add=temp_add.replace("|#","")
                temp_add=temp_add[:-1]
                null_rem.append(temp_add) 
       



# print(null_rem) 
grammer_dict = {}   

for i in range(len(null_rem)):
    str_dic=null_rem[i].replace("-","|").split("|")
    if str_dic[0] in grammer_dict.keys() :
        for j in range(len(str_dic[1:])):
            if j == 0 :
                continue
            if str_dic[j] not in grammer_dict[str_dic[0]] :
                grammer_dict[str_dic[0]].append(
                str_dic[j])

    else:
        try:
            grammer_dict[str_dic[0]].append(
                str_dic[1:])
        except:
            try:
                grammer_dict[str_dic[0]] =str_dic[1:]
            except:
                grammer_dict[str_dic[0]] =str_dic[1:]

# print(grammer_dict)
# # Changing and adding Dictionary Elements


str_want = input()

try:
    fin_string = [grammer_dict[tuple(grammer_dict.keys())[0]]]
    for i in range(20):
        res = []
        for string in fin_string:
            for char in string:
                if char.isupper():
                    for q in grammer_dict[char]:
                        res.append(string.replace(char, q))
        if str_want in res:
            print('Accepted')
            break
    else:
        print('Rejected')
except:
    print('Rejected')
