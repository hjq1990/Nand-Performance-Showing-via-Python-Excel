import xlsxwriter
import math
from functools import partial

def main():
    workbook=xlsxwriter.Workbook('EOL_RD1.xlsx')
    worksheet=workbook.add_worksheet('my sheet')
    Max_Cycle=101
    Max_Case=24
    col_offset=1
    row_offset=2
    col_div=29
    total=0
    first=1000
    D2 = [[0 for x in xrange(Max_Case)] for x in xrange(Max_Cycle)] 
    D3 = [[0 for x in xrange(Max_Case)] for x in xrange(Max_Cycle)] 
    
    # Set up structure of the tables
    bold = workbook.add_format({'bold': True})
           
    for cycle in range(1,Max_Cycle+1):
        worksheet.write(cycle+row_offset, col_offset, 'cycle  '+str(cycle*100-100)+'--'+str(cycle*100),bold) 
        worksheet.write(cycle+row_offset, col_offset+col_div, 'cycle  '+str(cycle*100-100)+'--'+str(cycle*100),bold) 
        
    for case in range(1,Max_Case):
        worksheet.write(row_offset,case+col_offset,'case  '+str(case),bold)
        worksheet.write(row_offset,case+col_offset+col_div,'case  '+str(case),bold)  
        
    worksheet.write(Max_Cycle+row_offset,col_offset,'Sum by case',bold)
    worksheet.write(Max_Cycle+row_offset,col_offset+col_div,'Sum by case',bold)
    
    worksheet.write(row_offset,Max_Case+col_offset,'Sum by cycle',bold)
    worksheet.write(row_offset,Max_Case+col_div+col_offset,'Sum by cycle',bold)
    
    # calculate the number of Dynamic Read event based on Cycle and Case
    bytes_per_line = 16
    sn=[0 for x in xrange(Max_Case)]
    sn1=[0 for x in xrange(Max_Case)]
    sn2=[0 for x in xrange(Max_Case)]
    s='WW06-EOL-FBC-LOTC1-HT-0'
    for i in range(1,4):
        sn[i]=str(i)+'.pat'
        with open(sn[i], 'rb') as binary_file:
            for block in iter(partial(binary_file.read, bytes_per_line), ''):
                s1=' '.join('{0:02x}'.format(ord(b)) for b in block)
                if s1[6:8]=='d2':
                    cycle=(int(s1[15:17],16)*256+int(s1[12:14],16)+0*int(s1[18:20],16)*256*256+0*int(s1[21:23],16)*256*256*256)/100+1
                    if cycle>100:
                        cycle=100
                    if (cycle<first):
                        first=cycle  
                    total=total+1       
                    case=int(s1[7],16)
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
                
    # write data into the 2D arrays      
    for cycle in range(1,Max_Cycle):
        for case in range(1,Max_Case):
            worksheet.write(cycle+row_offset,case+col_offset,D2[cycle][case])
            worksheet.write(cycle+row_offset,case+col_div+row_offset,D3[cycle][case])
        
            #for case in range(0,Max_Case):
    #    worksheet.write(Max_Cycle+1,case+1,'=sum(
         
    
        
    #for j in range(0,20):
    #    worksheet.write(row,j,s1[3*j:3*j+2])
    #    row=row+1    
    workbook.close()
    print 'total=',total
    print 'first cycle=',first 

if __name__ == '__main__':
    main()
