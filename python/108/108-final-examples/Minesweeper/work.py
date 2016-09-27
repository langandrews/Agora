'''
Opens spaces because of how the board is
Updated Fall 2015
@author: ajd74
'''
'''
Minesweepeer Program
Updated Fall 2015
@author: ajd74
'''
import copy
from random import randint
from datetime import datetime
from tkinter import *
from board_2_0 import *
from BoardPrinter import *
from Open_or_Flag_space_by_click import *
from Open_space_by_auto import *

class OpenSpaceByAuto:
    def __init__(self, time1, time2):
        self.hour_1=int(time1[0]+time1[1])
        self.min_1=int(time1[3]+time1[4])
        self.sec_1=int(time1[6]+time1[7])
        self.hour_2=int(time2[0]+time2[1])
        self.min_2=int(time2[3]+time2[4])
        self.sec_2=int(time2[6]+time2[7])
        self.hour_dif=(self.hour_2-self.hour_1)
        self.min_dif=(self.min_2-self.min_1)
        self.sec_dif=(self.sec_2-self.sec_1)
        self.result_int = (self.hour_dif*60+self.min_dif)*60+self.sec_dif
        self.result_sec=int(self.result_int%60*(self.result_int/abs(self.result_int)))
        self.result_min=int(abs(self.result_int)//60)*(self.result_int/abs(self.result_int))
        self.result_hour=int(abs(self.result_int)//3600*(self.result_int/abs(self.result_int))
#         if self.result_hour != int(0):
#             if self.result_min < 10:
#                 if self.result_sec<10:
#                     self.result_str = (str(self.result_hour)+':0'+str(self.result_min)+':0'+str(self.result_sec))
#                 else:
#                     self.result_str = (str(self.result_hour)+':0'+str(self.result_min)+':'+str(self.result_sec))
#             else:
#                 if self.result_sec<10:
#                     self.result_str = (str(self.result_hour)+':'+str(self.result_min)+':0'+str(self.result_sec))
#                 else:
#                     self.result_str = (str(self.result_hour)+':'+str(self.result_min)+':'+str(self.result_sec))
#         else:
#             if self.result_sec<10:
#                 self.result_str = (str(self.result_min)+':0'+str(self.result_sec))
#             else:
#                 self.result_str = (str(self.result_min)+':0'+str(self.result_sec))
     
#     def __str__(self):
#         return '/'+str(self.result_int)+'/'+str(self.result_hour)



class OpenSpaceByAuto:
    def __init__(self, time1, time2):
        self.hour_1=int(time1[0]+time1[1])
        self.min_1=int(time1[3]+time1[4])
        self.sec_1=int(time1[6]+time1[7])
        self.hour_2=int(time2[0]+time2[1])
        self.min_2=int(time2[3]+time2[4])
        self.sec_2=int(time2[6]+time2[7])
        self.hour_dif=(self.hour_2-self.hour_1)
        self.min_dif=(self.min_2-self.min_1)
        self.sec_dif=(self.sec_2-self.sec_1)
        self.result_int = (self.hour_dif*60+self.min_dif)*60+self.sec_dif
        self.result_sec=int(self.result_int%60*(self.result_int/abs(self.result_int)))
        self.result_min=int(abs(self.result_int)//60)*(self.result_int/abs(self.result_int))
        self.result_hour=int(abs(self.result_int)//3600*(self.result_int/abs(self.result_int))
#         if self.result_hour != int(0):
#             if self.result_min < 10:
#                 if self.result_sec<10:
#                     self.result_str = (str(self.result_hour)+':0'+str(self.result_min)+':0'+str(self.result_sec))
#                 else:
#                     self.result_str = (str(self.result_hour)+':0'+str(self.result_min)+':'+str(self.result_sec))
#             else:
#                 if self.result_sec<10:
#                     self.result_str = (str(self.result_hour)+':'+str(self.result_min)+':0'+str(self.result_sec))
#                 else:
#                     self.result_str = (str(self.result_hour)+':'+str(self.result_min)+':'+str(self.result_sec))
#         else:
#             if self.result_sec<10:
#                 self.result_str = (str(self.result_min)+':0'+str(self.result_sec))
#             else:
#                 self.result_str = (str(self.result_min)+':0'+str(self.result_sec))
     
#     def __str__(self):
#         return '/'+str(self.result_int)+'/'+str(self.result_hour)
                        
if __name__ == '__main__': 
    app = OpenSpaceByAuto('19:43:20','19:33:20')
    print(app)
