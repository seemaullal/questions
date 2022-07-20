# Question from https://docs.google.com/document/d/1d0piZv7Hsog3IdOxvqZ569v1NSp6sHC76o_17gO0z5Q/edit

def menu_combinations(menu, target):
    result = []
    menu_items = list(menu.keys())
    # avoid floating point issues
    menu_item_costs = [cost * 100 for cost in menu.values()]

    def calculate(current, current_target, index):
        if current_target == 0:
            result.append(current[:])
        if current_target < 0:
            return
        for i in range(index, len(menu_items)):
            if menu_item_costs[i] <= current_target:
                current.append(menu_items[i])
                print(current, i)
                calculate(current, current_target - menu_item_costs[i], i)
                current.pop()
    calculate([], target*100, 0)
    return result


menu = {
    "mixed_fruit": 2.15,
    "french_fries": 2.75,
    "side_salad": 3.35,
    "hot_wings": 3.55,
    "mozz_sticks": 4.20,
    "sampler": 5.80,
}

# [['mixed_fruit','side_salad','side_salad','sampler'],['mixed_fruit','mixed_fruit','mixed_fruit','mixed_fruit','mixed_fruit','mixed_fruit','mixed_fruit']]


actual = menu_combinations(menu, 15.05)
