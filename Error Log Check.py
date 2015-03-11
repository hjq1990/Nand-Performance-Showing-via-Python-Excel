'''
--IPython Code for Automatic Error log sorting------------

--By Jinqiang He,   March 11st, 2015

'''

from Tkinter import Tk
from tkFileDialog import askopenfilename
from tkFileDialog import asksaveasfilename
from functools import partial
import glob
import os
from openpyxl import Workbook



str=[]

def init():
    ws0.merge_cells('A1:D1')
    ws0.cell('A1').value='Error Log Stamp'
    ws0.merge_cells('E1:F1')
    ws0.cell('E1').value='Error Number'
    ws0.merge_cells('G1:H1')
    ws0.cell('G1').value='Error Type'
    ws0.merge_cells('I1:L1')
    ws0.cell('I1').value='Cycle'
    ws0.cell('M1').value='Error Code'
    ws0.cell('N1').value='FIM'
    ws0.cell('O1').value='CE'
    ws0.cell('P1').value='Die'
    ws0.merge_cells('Q1:R1')
    ws0.cell('Q1').value='Block'
    ws0.merge_cells('S1:T1')
    ws0.cell('S1').value='Page/WL'


def main(): 
    global excel_name,file,Max_Cycle

    bytes_per_line = 20
    line_num=0
    err_num=0
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

    print "Processing File",filename
    excel_name=os.path.dirname(filename)+'/'+os.path.basename(filename)[:-4]+'--error log.xlsx'
    with open(filename, 'rb') as binary_file:
        for block in iter(partial(binary_file.read, bytes_per_line), ''):
            s1=' '.join('{0:02x}'.format(ord(b)) for b in block)
            line_num=line_num+1
            ws.cell(row=line_num,column=1).value=s1

            if (s1[0:11]=='45 72 4c 67'):
                err_num=err_num+1
                row_offset=0
            elif(s1[0:11]=='52 64 45 72'):
                row_offset=22

            for i in range(20):
                ws0.cell(row=err_num+1,column=row_offset+i+1).value=s1[3*i:3*i+2]

            for item in s1:
                str.append(item)

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


    print "This API is for auto processing error-log data within pat files generated from CNE, and processed data will be saved in an excel file."
    
    print '****************************************************' 
    print "Please select the file for the error-log data to be processed."
    wb=Workbook()
    ws = wb.active

    ws.title="Raw Data"
    ws0 = wb.create_sheet()
    ws0.title="Error Log Items"
    init()
    main()
    wb.save(excel_name)
    print "The processed data is saved as",excel_name
