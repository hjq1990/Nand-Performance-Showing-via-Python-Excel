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
                            if(path4[0:16]=='LUA_BURN_EXECUTE'):
                                full_path4=os.path.join(full_path3,path4).replace('\\','//')
                                for path5 in os.listdir(full_path4):
                                    if (path5[0:3]=='DUT'):
                                        full_path5=os.path.join(full_path4,path5).replace('\\','//')
                                        for path6 in os.listdir(full_path5):
                                            # if (path6[-3:]=='csv'):
                                            #     full_path6=os.path.join(full_path5,path6).replace('\\','//')
                                            #     with open (full_path6,'r') as f:
                                            #         for lines in f:
                                            #             if len(lines)==18:
                                            #                 if lines[:11]== 'Test_Status' and int(lines[-2:],16)>3:
                                            #                     print full_path6,lines
                                            #                     line=line+1
                                            #                     strr[line]=full_path6+lines
                                            if path6[:10]== 'S3E_SysErr':

                                                line=line+1
                                                strr[line]=os.path.join(full_path5,path6).replace('\\','//')
                                                print strr[line]


    result_file='c:/'+str(time.localtime().tm_year)+'-'+str(time.localtime().tm_mon)+'-'+str(time.localtime().tm_mday)+'_Lua_Execuate.txt'
    with open(result_file,'w') as result:
        for i in range(1,line+1):
            a=str(strr[i])
            result.write(a+'\n')
    print "the result is saved into as below file:",result_file

if __name__ == '__main__':
    main()


