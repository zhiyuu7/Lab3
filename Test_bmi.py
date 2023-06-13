import lab2.ex1_prac as bmi

def Test_bmi_normal_weight():
    input_weight = 51
    result = bmi.calculate_bmi(1.59, input_weight)
    test = 0

    assert(result == test)

def Test_bmi_over_weight():
    input_weight = 80
    result = bmi.calculate_bmi(1.59, input_weight)
    test = 1

    assert(result == test)

def Test_bmi_under_weight():
    input_weight = 40
    result = bmi.calculate_bmi(1.59, input_weight)
    test = -1

    assert(result == test)