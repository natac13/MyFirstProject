'''
The problem was to calculate the amount of radiation expousre 
based off a given formula which is f(x)
'''

import math

def f(x):
    return 10 * math.e**(math.log(0.5)/5.27*x)
    
def radiationExposure(start, stop, step):
    '''
    Computes the amount of radiation exposure by calling function f
    
    start: integer, start of exposure
    stop: integer, end of exposure
    step: float, divide up the exposure time into equal partitions
    
    returns: float, which is the amount of radiation exposure
    '''
    
    x = int((stop - start) / step)
    y = []
    z = start
    w = []
    
    ## Make a list of the divided up values of the exposure, x-axis
    for i in range(x):
        y.append(z)
        z += step

    # test = [(f(a)*step) for a in y[:]]    
    # print 'testing total {0:.5f}'.format(sum(test)) 
    
    
    return sum([x * step for x in map(f, y)])
    
    ########     first attempt which I think is sloppy!      ############
    # Make list of the exposure amounts per division 
    ##for a in y[:]:
        ##w.append((f(a) * step))  # Take width:call function f(a) * height:step
        
    ##return 'total', sum(w)
    


print radiationExposure(0, 5, 1)
print radiationExposure(5, 11, 1)
print radiationExposure(0, 11, 1)
print radiationExposure(40, 100, 1.5)   