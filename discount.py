def apply_discount(total_people, total_cost):


    if total_people > 30:
        discount = total_cost * 0.10
        total_cost -= discount
    else:
        discount = 0

    return total_cost, discount