from typing import Dict, List, Tuple


def find_pizza_combination(combinations: List[Tuple[Dict[str, str], int]]) -> Dict[str, str]:
    ideal = {
        'crust': 'Pan',
        'seasoning': 'Yes',
        'sauce': 'Tomato',
        'veggies': 'Broccoli',
        'cheese': 'No',
    }
    pizza_points = {
        'crust': 5,
        'seasoning': 4,
        'sauce': 3,
        'veggies': 2,
        'cheese': 1,
    }

    # Saving the idex of the higest quantities of pizza in possibles
    # Starting with assuming the first pizza comb is best and will check later
    possibles = [0]
    cur_max = combinations[0][1]

    for i in range(1,len(combinations)):
        quantitie = combinations[i][1]
        if quantitie > cur_max:
            cur_max = quantitie
            possibles = [i]
        elif quantitie == cur_max:
            possibles.append(i)
    # if we got to this point and only one possibility for max ammout of pizzas then we are finished and just return it
    if len(possibles) == 1:
        return combinations[possibles[0]][0]

    # The ammount of similarities on the pizza pie!
    most_similar = 0

    # Pizzas that are cantidates for morty's order
    msp = {}
    # Since the list Possibles is a list of indexes we use them as such. IE pi means pizza index.
    for pi in possibles:
        cur = combinations[pi][0]
        cur_similar = 0 # counts similarities before there is a difference of ingredient
        total_diff = 0 # counts differences from ideal pizza
        any_diff = False
        pp_total = 0
        # Check to see if the pizza is the ideal pizza. If so then return and we are finished.
        if cur == ideal:
            return cur
        for item in cur:
            if cur[item] == ideal[item] and not any_diff:
                cur_similar += 1
                pp_total += pizza_points[item]
            elif cur[item] != ideal[item]:
                any_diff = True
                total_diff -= pizza_points[item]
            elif cur[item] == ideal[item] and any_diff:

                pp_total += pizza_points[item]
            else:
                total_diff -= pizza_points[item]
            
        if cur_similar > most_similar:
            msp = {}
            msp[pi] = {'similar': cur_similar, 'total_diff': total_diff, 'pp_total': pp_total}
            # print(f"remap: {msp}")
            most_similar = cur_similar
        elif cur_similar == most_similar:
            msp[pi] = {'similar': cur_similar, 'total_diff': total_diff, 'pp_total': pp_total}
            # print(f"adding: {msp}")
    # check to see if only one pizza has most similarities before a change.  if so we are finished.
    if len(msp) == 1:
        first = next(iter(msp))
        return combinations[first][0]
    else:
        best_pp = 0
        best_diff = float('-inf')
        best_possible = []
        for pizza in msp:
            cur_diff = msp[pizza]['total_diff']
            cur_pp = msp[pizza]['pp_total']
            if cur_pp > best_pp or cur_diff > best_diff:
                best_pp = cur_pp
                best_diff = cur_diff
                best_possible = []
                best_possible.append(pizza)
            elif cur_pp == best_pp and cur_diff == best_diff:
                best_possible.append(pizza)
    return combinations[best_possible[0]][0]


  
groups_1 = [
    ({'crust': 'Pan', 'seasoning': 'No', 'sauce': 'Mayo', 'veggies': 'Broccoli', 'cheese': 'No'}, 4),
    ({'crust': 'Thin-Crust', 'seasoning': 'No', 'sauce': 'Tomato', 'veggies': 'Broccoli', 'cheese': 'No'}, 2),
]
groups_2 = [
    ({'crust': 'Pan', 'seasoning': 'No', 'sauce': 'Tomato', 'veggies': 'Broccoli', 'cheese': 'No'}, 3),
    ({'crust': 'Pan', 'seasoning': 'Yes', 'sauce': 'Mayo', 'veggies': 'Broccoli', 'cheese': 'No'}, 3),
    ({'crust': 'Pan', 'seasoning': 'No', 'sauce': 'Mayo', 'veggies': 'Broccoli', 'cheese': 'Yes'}, 3),
]
groups_3 = [
    ({'crust': 'Thin-Crust', 'seasoning': 'No', 'sauce': 'Mayo', 'veggies': 'Broccoli', 'cheese': 'No'}, 3),
    ({'crust': 'Pan', 'seasoning': 'No', 'sauce': 'Tomato', 'veggies': 'Cucumber', 'cheese': 'Yes'}, 3),
    ({'crust': 'Pan', 'seasoning': 'No', 'sauce': 'Mayo', 'veggies': 'Broccoli', 'cheese': 'No'}, 3),
    ({'crust': 'Pan', 'seasoning': 'No', 'sauce': 'Tomato', 'veggies': 'Broccoli', 'cheese': 'Yes'}, 3),
]
groups_4 = [
    ({'crust': 'Thin-Crust', 'seasoning': 'No', 'sauce': 'Mayo', 'veggies': 'Broccoli', 'cheese': 'No'}, 3),
    ({'crust': 'Pan', 'seasoning': 'No', 'sauce': 'Tomato', 'veggies': 'Cucumber', 'cheese': 'Yes'}, 3),
    ({'crust': 'Pan', 'seasoning': 'No', 'sauce': 'Tomato', 'veggies': 'Broccoli', 'cheese': 'Yes'}, 3),
    ({'crust': 'Pan', 'seasoning': 'No', 'sauce': 'Tomato', 'veggies': 'Broccoli', 'cheese': 'Yes'}, 3),
]
groups_5 = [
    ({'crust': 'Thin-Crust', 'seasoning': 'No', 'sauce': 'Mayo', 'veggies': 'Broccoli', 'cheese': 'No'}, 3),
    ({'crust': 'Pan', 'seasoning': 'No', 'sauce': 'Tomato', 'veggies': 'Cucumber', 'cheese': 'Yes'}, 3),
    ({'crust': 'Pan', 'seasoning': 'No', 'sauce': 'Tomato', 'veggies': 'Broccoli', 'cheese': 'Yes'}, 3),
    ({'crust': 'Pan', 'seasoning': 'No', 'sauce': 'Tomato', 'veggies': 'Broccoli', 'cheese': 'No'}, 3),
]

assert find_pizza_combination(groups_1) == groups_1[0][0]
assert find_pizza_combination(groups_2) == groups_2[1][0]
assert find_pizza_combination(groups_3) == groups_3[3][0]
assert find_pizza_combination(groups_4) == groups_4[2][0] and id(find_pizza_combination(groups_4)) == id(groups_4[2][0])
assert find_pizza_combination(groups_5) == groups_5[3][0]