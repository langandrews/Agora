
###DEPRECIATED CODE. NONE OF THIS CODE IS WORKING OR PART OF THE FINAL PROGRAM. ORIGINAL CODE IS BELOW FOR DOCUMENTATION PURPOSES###

''' teststuff.py

a test using nested lists to recursively apply a random amount of variation to a linear graph.
@author: Quentin Baker
'''

def variate(init,list,index,min,max):
    print(index)
    list[index] = [init]
    for i in range(4):
        list[index].append(randint(min,max))
        
rofl = [2,3,4]

for i in range(len(rofl)):
    variate(rofl[i],rofl, i, 1, 3)
    
print(rofl)