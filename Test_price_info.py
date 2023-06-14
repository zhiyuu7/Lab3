import price_info as price_info

def test_total_cost_shopping():
    result = price_info.total_cost_shopping()
    test = 46.75

    assert(test == result)

def test_cost_of_fruits():
    input_fruit = 'orange'
    input_quantity = 5
    result = price_info.cost_of_fruits(input_fruit, input_quantity)
    test = 7

    assert(test == result)