def addition_evaluator(stg):
    '''
    stg: string of ints with +'s between them, including whitespace. 
    
    note: only works with addition.
    
    returns: evaluation integer as fstring.
    '''
    lst = []
    for num in str(stg).split(' '):
        if num == '':
            continue
        try:
            if num == '+':
                continue
            adds = int(num)
            lst += [adds]
        except AttributeError as AE:
            
            print(AE)
            #given variable expressions:
            #      'a + b + c'
            #handle them as str representatives which can be quickly edited given constraints on the system they represent.
            return
    
    return f'{sum(lst)}'.format()
    
stg = '1 + 2 +  3'
six = addition_evaluator(stg)


print(six)

def value_expressor(stg):
    '''
    stg: stgs: string of ints with +'s between them, including whitespace. 
    
    returns: tuple of 'equation' filled with strings.
    '''
    lst_right=[]
    
    for num in str(stg).split(' '):
        lst_right+=[num]
    y = addition_evaluator(stg)
    return y,lst_right

equation = value_expressor(stg)

#given this output
#('6', ['1', '+', '2', '+', '3'])
#assert equality between left and right parts of the list.

assert six == equation[0]

def take_out_lst(stg):
    '''
    stg: a string of ints with +'s between them, whitespace included.
    note: only works with addition.
    returns: the list of ints.
    '''
    y,lst_right = value_expressor(stg)
    lst = []
    for adds in lst_right[:]:
        if adds == '+':
            continue
        else:
             lst += [int(adds)]
    return lst

str_demo = '3 + 5 + 7'
print(take_out_lst(str_demo))

def negative_evaluator(stg):
    '''
    stg: a string of ints with -'s between them, whitespace included.
    note: only works with subtraction.
    returns: evaluation of integers as fstring.
    '''
    
    lst = []
    for num in str(stg).split(' '):
        if num == '':
            continue
        try:
            if num == '-':
                continue
            else:
                if num.startswith('-'):
                    integer = int(num)
                else:
                    integer = -int(num)
                lst += [integer]
        except AttributeError as AE:
            print(AE)
            #given variable expressions:
            'a + b + c'
            #handle them as str representatives which can be quickly edited given constraints on the system they represent.
            return
    
    return f'{sum(lst)}'.format()

stg2 = '-4 - 4  -  4'
dash_twelve = negative_evaluator(stg2)
print(dash_twelve)

def negative_expressor(stg):
    '''
    stg: a string of ints with -'s between them, whitespace included.
    note: only works with subtraction.
    returns: tuple of evaluation and it's list representation.
    '''
    
    lst_right = []
    
    for num in str(stg).split(' '):
        if num == '':
            continue

        if num == '-':
            continue
        lst_right += [-abs(int(num))]
            
    y = sum(lst_right)
    return y,lst_right

negative_expression = negative_expressor(stg2)
print(negative_expression)
