import csv
import os
import time

def main():
    wafer_ID()
def wafer_ID():
    roots="Z:\Rel_Lab"
    line=0
    strr=[0 for x in xrange(1000000)]
    roots.replace('\\','//')
    for path1 in os.listdir(roots):
        if (path1[0:3]=='CNE'):
            path2=str(os.path.join(roots,path1)).replace('\\','//')
            if os.path.isdir(path2):
                for path3 in os.listdir(path2):
                    if path3[0:2]=='PC':
                        full_path3=os.path.join(path2,path3).replace('\\','//')
                        for path4 in os.listdir(full_path3):
                            full_path4=os.path.join(full_path3,path4).replace('\\','//')
                            if (len(full_path4)==64) and (full_path4[-10:-5]=='_EFR_'):
                                full_path5=os.path.join(full_path4,'Process_TLV').replace('\\','//')
                                if os.path.isdir(full_path5):
                                    file_lists=os.listdir(full_path5)
                                    for file in file_lists:

                                         if (file[5:10]=='_TLV_'):
                                            full_path=str(os.path.join(full_path5,file)).replace('\\','//')

                                            with open (full_path,'r') as f:
                                                f.readline()
                                                wrong_info=0
                                                wafer_info=f.readline()
                                                chars=wafer_info.replace(',','').replace(' ','')[8:]
                                                wafer_info=wafer_info.replace(',',' ')
                                                line=line+1
                                                for i in chars:
                                                    if ord(i)>64:
                                                        wrong_info=1

                                                        print full_path,"wrong info",chars
                                                        strr[line]=full_path+'wrong info'+ chars

                                                if (wrong_info==0):
                                                    wafer_info=wafer_info.split(' ')[4:]
                                                    if len(wafer_info)>=16:
                                                        wafer_lot=chr(int(wafer_info[1],16))+chr(int(wafer_info[2],16))+chr(int(wafer_info[6],16))+chr(int(wafer_info[7],16))+chr(int(wafer_info[11],16))+chr(int(wafer_info[12],16))+chr(int(wafer_info[13],16))+chr(int(wafer_info[14],16))+chr(int(wafer_info[15],16))
                                                        wafer_num=int(wafer_info[3],10)
                                                        wafer_x=int(wafer_info[4],10)
                                                        wafer_y=int(wafer_info[5],10)
                                                        print full_path,wafer_lot,wafer_num,wafer_x,wafer_y
                                                        strr[line]=full_path+' '+wafer_lot+' '+str(wafer_num)+' '+str(wafer_x)+' '+str(wafer_y)
                                                    else:
                                                        print full_path,"wrong info",wafer_info
                                                        strr[line]=full_path+'wrong info'+ chars
                                else:
                                    line=line+1
                                    print full_path4, 'TLV data is not processed yet'
                                    strr[line]=full_path4+ 'is TLV data is not processed yet'

    result_file='c:/'+str(time.localtime().tm_year)+'-'+str(time.localtime().tm_mon)+'-'+str(time.localtime().tm_mday)+'_wafer_id.txt'
    with open(result_file,'w') as result:
        for i in range(1,line+1):
            a=str(strr[i])
            result.write(a+'\n')
    print "the result is saved into as below file:",result_file

if __name__ == '__main__':
    main()


