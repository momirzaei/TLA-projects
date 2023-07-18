states_primery = input()
states = states_primery[1:len(states_primery)-1].split(",")
# len_state=len(states)

language_primery = input()
language = language_primery[1:len(language_primery)-1].split(",")
len_language = len(language)

final_states_primery = input()
final_states = final_states_primery[1:len(final_states_primery)-1].split(",")

transition_count = int(input())
NFA = {}
count_eps = 0
list_lam1 = []
list_lam2 = []
for i in range(transition_count):
    Transition_Rule = input().split(',')
    if Transition_Rule[1] == "$":
        count_eps += 1
        list_lam1.append(Transition_Rule[0])
        list_lam2.append(Transition_Rule[2])
    try:
        NFA[Transition_Rule[0]][Transition_Rule[1]].append(Transition_Rule[2])
    except:
        try:
            NFA[Transition_Rule[0]][Transition_Rule[1]] = [Transition_Rule[2]]
        except:
            NFA[Transition_Rule[0]] = {
                Transition_Rule[1]: [Transition_Rule[2]]}

#len_NFA=len_language * len_state  - transition_count

for item in states:
    if not(item in NFA.keys()):
        for j in range(len_language):
            try:
                NFA[item][language[j]] = []
            except:
                NFA[item] = {language[j]: []}
    else:
        for t in language:
            if not(t in NFA[item].keys()):
                try:
                    NFA[item][t] = []
                except:
                    NFA[item] = {t: []}


# print(NFA)
new_nfa = {}
for i in range(count_eps):
    new_state = list_lam1[i]+list_lam2[i]
    new_state = "".join(new_state)
    for j in range(len_language):
        try:
            NFA[new_state][language[j]].append(
                "".join(NFA[list_lam1[i]][language[j]]))
        except:
            try:
                NFA[new_state][language[j]] = NFA[list_lam1[i]][language[j]]
            except:
                NFA[new_state] = {
                    language[j]: NFA[list_lam1[i]][language[j]]}
        if NFA[list_lam2[i]][language[j]]:
            NFA[new_state][language[j]].append(
                "".join(NFA[list_lam2[i]][language[j]]))
            # print(str(NFA[list_lam2[i]][language[j]]))
    # NFA.pop(list_lam1[i])
    # print(NFA)
    # for p in NFA.keys():
    #     for q in language:
    #         # print(NFA[p][q])
    #         if NFA[p][q] == [list_lam1[i]]:
    #             NFA[p][q] = [new_state]


# print(NFA)

new_states_list = []
# dfa = {}
# dfa[states[0]] = {}
keys_list = [list(NFA.keys())[0]]  # states
# path_list = list(NFA[keys_list[0]].keys())  #languages


# print(keys_list)
# print(path_list)
s = ""
landa_list = []
for i in range(len_language):
    temp = s.join(NFA[keys_list[0]][language[i]])
   #dfa[keys_list[0]][language[i]] = temp
    if not(temp in keys_list or not temp):
        new_states_list.append(temp)
        keys_list.append(temp)
# if not(NFA[keys_list[0]].get('$') is None):
#     temp1 = s.join(NFA[keys_list[0]].get('$'))
#     #dfa[keys_list[0]][language[i]] = temp1
#     if not(temp1 in keys_list):
#         new_states_list.append(temp1)
#         keys_list.append(temp1)
#         landa_list.append(new_states_list[0])


# print(keys_list)
# print(new_states_list)
while len(new_states_list) != 0:
    #dfa[new_states_list[0]] = {}
    # print(new_states_list[0])
    # print(keys_list)
    for _ in range(len(new_states_list[0])):
        for i in range(len(language)):
            temp = []
            # if any(map(str.isdigit, new_states_list[0])):
            for j in range(int(len(new_states_list[0])/2)):
                if new_states_list[0][2*j:2*j+2] in NFA.keys():
                    temp += ''.join(NFA[new_states_list[0]
                                    [2*j:2*j+2]][language[i]])

            # else:
            #     for j in range(len(new_states_list[0])):
            #         if new_states_list[0][j] in NFA.keys():
            #             temp += NFA[new_states_list[0][j]][language[i]]
                    # print(NFA[new_states_list[0][j]][language[i]])
            # print(temp)
            s = ""
            s = s.join(temp)
            if s not in keys_list:
                new_states_list.append(s)
                keys_list.append(s)
            #dfa[new_states_list[0]][language[i]] = s

    # print(NFA[new_states_list[0]])
    # if new_states_list[0] in states:
    #     if not(NFA[new_states_list[0]].get('$') is None):
    #         temp_landa = []
    #         if any(map(str.isdigit, new_states_list[0])):
    #             if not(NFA[new_states_list[0]].get('$') is None):
    #                 temp_landa += NFA[new_states_list[0]].get('$')

    #             temp_landa.insert(0, new_states_list[0])
    #             s = ""
    #             s = s.join(temp_landa)
    #             landa_list.append(new_states_list[0])
    #             if s not in keys_list:
    #                 new_states_list.append(s)
    #                 keys_list.append(s)
    new_states_list.remove(new_states_list[0])
print(len(keys_list))
# print(keys_list)
# print(landa_list)
