'''Initializes the coordinates of squares
Created on Dec 9, 2014
Final Project
@author: Hannah Ludema (hel7)
'''
class Squares:
    def __init__(self):
        #Initializes the x and y coordinates of 5 squares
        self.squares_x_list = [280, 260, 240, 220, 200]
        self.squares_y_list = [260, 260, 260, 260, 260]
        
   
   
if __name__ == '__main__': 
    #Calls the Squares class
    s = Squares()
    
    #Checks that the lists are initialized properly     
    assert s.squares_x_list == [280, 260, 240, 220, 200]
    assert s.squares_y_list == [260, 260, 260, 260, 260]
    
    print("All Squares tests passed!")