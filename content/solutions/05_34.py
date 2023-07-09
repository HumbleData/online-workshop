def f(x):
    if x == 1:
        return "single"
    else:
        return "multiple"
    
print('def f(x):')
print('\tif x == 1:')
print('\t\treturn "single"')
print('\telse:')
print('\t\treturn "multiple"\n')

print('f(4) = ',f(4)) #x = 4