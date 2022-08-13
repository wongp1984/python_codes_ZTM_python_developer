def highest_even(alist):
    '''
    Info: This function will print out the highest even number from the given list
    ''' 
    blist = []
    for i in alist:
        if type(i) == int and i % 2 == 0 :
            blist.append(i)
        
    blist.sort(reverse=True)
    if len(blist) > 0: 
        return blist[0]
    else:
        return None
