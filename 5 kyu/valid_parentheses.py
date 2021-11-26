def valid_parentheses(string):
    par = ''.join(p for p in string if p in ['(',')'])    
    while '()' in par:
        par = par.replace('()', '')    
    return False if par else True


# string = '(())((()())())'
