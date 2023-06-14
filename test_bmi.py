import lab2.bmi_prac as bmi

def test_bmi_normal_weight():
    input_weight = 51
    result = bmi.calculate_bmi(1.59, input_weight)
    test = 0

    assert(result == test)

def test_bmi_over_weight():
    input_weight = 80
    result = bmi.calculate_bmi(1.59, input_weight)
    test = 1

    assert(result == test)

def test_bmi_under_weight():
    input_weight = 40
    result = bmi.calculate_bmi(1.59, input_weight)
    test = -1

    assert(result == test)
