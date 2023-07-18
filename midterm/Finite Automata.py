states_primery = input()
states = states_primery[1:len(states_primery)-1].split(",")

language_primery = input()
language = language_primery[1:len(language_primery)-1].split(",")

final_states_primery = input()
final_states = final_states_primery[1:len(final_states_primery)-1].split(",")

transition_count = int(input())
transition = {}

for i in range(transition_count):
    Transition_Rule = input().split(',')
    try:
        transition[Transition_Rule[0]][Transition_Rule[1]].append(
            Transition_Rule[2])
    except:
        try:
            transition[Transition_Rule[0]][Transition_Rule[1]] = [
                Transition_Rule[2]]
        except:
            transition[Transition_Rule[0]] = {
                Transition_Rule[1]: [Transition_Rule[2]]}

REGEX = input()


def Finite_Automata(final, i):
    if i == len(REGEX):
        if final in final_states:
            print("Accepted")
            exit()
        else:
            print("Rejected")
            exit()

    tras_final = transition[final].get(REGEX[i])
    #print(final, tras_final, i, transition[final])
    landa = transition[final].get('$')

    if tras_final != None:
        for item in tras_final:
            res = Finite_Automata(item, i+1)
            if res:
                print("Accepted")
                exit()

    if landa != None:
        for item in landa:
            res = Finite_Automata(item, i)
            if res:
                print("Accepted")
                exit()


i = 0
final = states[0]
Finite_Automata(final, i)
