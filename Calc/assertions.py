from expression_factory_ints import addition_evaluator,value_expressor,take_out_lst


stg = '1 + 2 + 3'
six = addition_evaluator(stg)

equation = value_expressor(stg)

sum_of_lst_ints = sum(take_out_lst(stg))

evaluation = eval(stg)

assert int(six) == int(equation[0]) == sum_of_lst_ints == evaluation

assert six == equation[0]

assert sum_of_lst_ints == evaluation

assert type(sum_of_lst_ints) == type(evaluation) == int

assert type(six) == type(equation[0]) == str