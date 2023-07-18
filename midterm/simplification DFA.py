states_primery = input()
states = states_primery[1:len(states_primery)-1].split(",")

language_primery = input()
language = language_primery[1:len(language_primery)-1].split(",")

final_states_primery = input()
final_states = final_states_primery[1:len(final_states_primery)-1].split(",")

transition_count = int(input())
DFA = {}

for i in range(transition_count):
    Transition_Rule = input().split(',')
    try:
        DFA[Transition_Rule[0]][Transition_Rule[1]].append(
            Transition_Rule[2])
    except:
        try:
            DFA[Transition_Rule[0]][Transition_Rule[1]] = Transition_Rule[2]
        except:
            DFA[Transition_Rule[0]] = {
                Transition_Rule[1]: Transition_Rule[2]}

# print(DFA)


def reach(DFA, reach_list, my_state):
    for state in DFA[my_state].values():
        if state == my_state:
            continue
        if not(state in reach_list):
            reach_list.append(state)
            reach(DFA, reach_list, state)


reachable_list = []
my_state = states[0]
reachable_list.append(my_state)
reach(DFA, reachable_list, my_state)
# print(reachable_list)
del_list = []
for state in states:
    if not(state in reachable_list):
        del DFA[state]
        del_list.append(state)
        if state in final_states:
            final_states.remove(state)
states = list(set(states) ^ set(del_list))

last_list = []
unfinal_list = []
last_list.append(final_states)
for state in states:
    if not(state in final_states):
        unfinal_list.append(state)
last_list.append(unfinal_list)
# print(last_list)


def checking_part(my_list, q0, q1):
    for list in my_list:
        if (q0 in list) and (q1 in list):
            return True
    return False


def one_part(my_list, q0, q1, dFA, language):
    count = 0
    for langu in language:
        if dFA[q0][langu] == dFA[q1][langu] or checking_part(my_list, dFA[q0][langu], dFA[q1][langu]):
            count += 1
    if count == len(language):
        return True
    return False


def stable_copy(L):
    if type(L[0]) != list:
        return [i for i in L]
    else:
        return [stable_copy(L[i]) for i in range(len(L))]


while True:
    list1temp = []
    list2temp = []

    list2temp = stable_copy(last_list)
    # for a in range(len(last_list)):
    #     list2temp.append(last_list[a])
    #     # print(len(last_list))
    #     # print(a)
    #     print(list2temp)
    for i in range(len(list2temp)):
        j = 0
        while j < len(list2temp[i]):
            list3temp = []
            list3temp.append(list2temp[i][j])
            k = j+1
            while k < len(list2temp[i]):
                if one_part(last_list, list2temp[i][j], list2temp[i][k], DFA, language):
                    list3temp.append(list2temp[i][k])
                    list2temp[i].remove(list2temp[i][k])
                    # print(list2temp,"777")
                    # print(last_list)
                else:
                    k += 1
            list2temp[i].remove(list2temp[i][j])
            list1temp.append(list3temp)
    # print(list1temp ,"11")
    # print(list2temp,"22")
    # print(last_list,"333")
    if last_list == list1temp:
        break
    last_list = list1temp

# print(last_list)
print(len(last_list))
