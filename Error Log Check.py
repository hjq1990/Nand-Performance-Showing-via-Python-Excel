'''
--IPython Code for Automatic Error log sorting------------

--By Jinqiang He,   Nov 26th, 2014

'''

from Tkinter import *
import tkSimpleDialog
from tkFileDialog import *
import glob
import os
from openpyxl import Workbook
from functools import partial

def init():
    global Max_Cycle,FBC_event,  row_offset,col_offset

           
    for cycle in range(1,Max_Cycle+1):
        print cycle+row_offset, col_offset
        ws0.cell(row=cycle+row_offset, column =col_offset).value= 'cycle '+str(cycle*100-100)+'--cycle'+str(cycle*100)
        ws0.cell(row=cycle+row_offset, column=col_offset+col_div).value= 'cycle  '+str(cycle*100-100)+'--'+str(cycle*100) 
        
    for case in range(1,Max_Case):
        ws0.cell(row=row_offset,column=case+col_offset).value='case  '+str(case)
        ws0.cell(row=row_offset,column=case+col_offset+col_div).value='case  '+str(case)
        
    ws0.cell(row=Max_Cycle+row_offset,column=col_offset).value='Sum by case'
    ws0.cell(row=Max_Cycle+row_offset,column=col_offset+col_div).value='Sum by case'
    
    ws0.cell(row=row_offset,column=Max_Case+col_offset).value='Sum by cycle'
    ws0.cell(row=row_offset,column=Max_Case+col_div+col_offset).value='Sum by cycle'

def main(): 
    global excel_name,file,Max_Cycle
    D2 = [[0 for x in xrange(Max_Case)] for x in xrange(Max_Cycle)] 
    D3 = [[0 for x in xrange(Max_Case)] for x in xrange(Max_Cycle)] 
    bytes_per_line = 20
    sector=8  # 8 for 16K mode, 4 for 8K mode
    Type=0   # 0 :error log, 1: failure bit 
    total=0
    first=1000
    root = Tk()
    root.wm_title("Dynamic Read data")
    
    w = Label(root, text="Please select the folder for the Dynamic-Read data to be processed.") 
   
    dirname = askdirectory()
    print "Selecting folder:",dirname
    
    fold=dirname.replace('/',' ').split()
    excel_name=fold[len(fold)-1]+' Dynamic Read data.xlsx'
    print "Please close this dialog by clicking X on the right-top"
    
    w.pack()
    root.mainloop()
    os.chdir(dirname)
    for file in glob.glob("*.pat"):
        print "Processing File",file              
        with open(file, 'rb') as binary_file:
            for block in iter(partial(binary_file.read, bytes_per_line), ''):
                s1=' '.join('{0:02x}'.format(ord(b)) for b in block)
                if (s1=='45 72 4c 67'):
                    print 






                if s1[6:8]=='d2':
                    cycle=(int(s1[15:17],16)*256+int(s1[12:14],16)+0*int(s1[18:20],16)*256*256+0*int(s1[21:23],16)*256*256*256)/100+1
                    if cycle>100:
                        cycle=100
                    if (cycle<first):
                        first=cycle  
                    total=total+1       
                    case=int(s1[7],16)
                    #print case
                    D2[cycle][case]=D2[cycle][case]+1
    
                if s1[6:8]=='d3':
                    cycle=(int(s1[15:17],16)*256+int(s1[12:14],16)+0*int(s1[18:20],16)*256*256+0*int(s1[21:23],16)*256*256*256)/100+1
                    case=int(s1[7],16)
                    if cycle>100:
                        cycle=100
                    if (cycle<first):
                        first=cycle  
                    total=total+1 
                    D3[cycle][case]=D2[cycle][case]+1
   
    # Set up structure of the table                
    # write data into the 2D arrays      
    for cycle in range(1,Max_Cycle):
        for case in range(1,Max_Case):
            ws0.cell(row=cycle+row_offset,column=case+col_offset).value=D2[cycle][case]
            ws0.cell(row=cycle+row_offset,column=case+col_div+row_offset).value=D3[cycle][case]
   
    print 'total=',total
    print 'first cycle=',first 

if __name__ == '__main__':
    error_num=0
    Max_Case=36
    col_offset=1
    row_offset=2
    col_div=40
    total=0
    first=1000
    RL=0
    RU=0
    Erase_num=0
    FBC_event=0;
    Row_offset=4
    PL=0
    PU=0
    excel_name=' '
    file=' '
    erase_time=0
    
#------------------Excel WorkBook Initiation----------------------------------    
    wb=Workbook()
    ws = wb.active
    ws.title="Summary"
    ws0 = wb.create_sheet()
    ws0.title="Error Log"

    init()
    print "This API is for auto processing error-log data within pat files generated from CNE, and processed data will be saved in an excel file."
    
    print '****************************************************' 
    print "Please select the file for the error-log data to be processed."
    main()
    
    wb.save(excel_name)
    #Summarize()
    
