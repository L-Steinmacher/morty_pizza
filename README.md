"""The purpose of this exercise is to find how many Pizzas Morty can buy for a given combination of ingredients. 

A Pizza consists of the following ingredients: Crust, Seasoning, Sauce, Veggies, and Cheese

Morty's favourite combination and in this preference order(Crust is more important than Seasoning and so on):

Crust → Pan
Seasoning → Yes
Sauce → Tomato
Veggies → Broccoli
Cheese → No


It’s also possible that multiple Pizza combinations are available in the same quantity, in that case, we resolve it by picking the group
that’s "closest" to Morty's preference.

The definition of closest here being:
1. Count of Pizzas available with a given combination of ingredients. If a combination has a higher count even if it isn't Morty's preference, it will be picked.
2. The ingredients are matched in the preference order mentioned above(Crust → Seasoning → Sauce → Veggies → Cheese),
   and one that has the first mismatching item from Morty's preference is rejected.
3. If the items still match, pick the one that was seen first.


Let’s say we got:

A. (C: Pan,       Se: Yes, Sa: Tomato,  V: Broccoli, C: No)  → 3
B. (C: Thin-Crust Se: No,  Sa: Mayo,    V: Broccoli, C: No)  → 3
C. (C: Pan,       Se: Yes, Sa: Tomato,  V: Onion,    C: Yes) → 3

In the above example, A has the same count as B and C, but as A is also the same as Morty's preference, it’s picked over others.

Let’s take a more complicated example:

A. (C: Thin-Crust, Se: Yes, Sa: Mayo,   V: Broccoli, C: No)  → 3
B. (C: Pan,        Se: Yes, Sa: Tomato, V: Onion,    C: Yes) → 3
C. (C: Pan,        Se: Yes, Sa: Mayo,   V: Broccoli, C: No)  → 4
D. (C: Pan,        Se: Yes, Sa: Tomato, V: Broccoli, C: Yes) → 4 (winner)


Here A and B are already out of the race because of their lower counts(point 1 above),
the tiebreaker between C and D is broken by picking D as when Sauce(Se) is compared,
D has Tomato that matches Morty's preferred Sauce and C has Mayo, hence it’s rejected.

def find_pizza_combination(combinations: List[Tuple[Dict[str, str], int]]) →Dict[str, str]:
   ...
   
`groups` will be a List of tuples, where the first item in tuple will be the dictionary containing the group and the second item will be count.

[
    ({'crust': 'Pan', 'seasoning': 'No', 'sauce': 'Mayo', 'veggies': 'Broccoli', 'cheese': 'No'}, 4),
    ({'crust': 'Thin-Crust', 'seasoning': 'No', 'sauce': 'Tomato', 'veggies': 'Broccoli', 'cheese': 'No'}, 2),
]

For the above input the output should be:

{'crust': 'Pan', 'seasoning': 'No', 'sauce': 'Mayo', 'veggies': 'Broccoli', 'cheese': 'No'}

The solution will be evaluated for:

1. Correctness
2. Readability
3. Performance
"""