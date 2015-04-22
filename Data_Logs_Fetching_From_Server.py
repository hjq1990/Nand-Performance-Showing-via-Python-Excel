'''
*****************************************
Data Logs Fetch From Server
*****************************************
Purpose: this API is getting Test Datalogs from server and copy to assigned folder.

April 22, 2015
Jinqiang He

'''

import os
import shutil

def main():

    Dept_test="//cvpfilip05//Dept_test"
    magnum_summary_2="//cvpfilip03//SDSS_Prod_Data//MemoryTestData//magnum_summary_2"
    Magnum_Compressed="//cvpfilip05//Dept_test//Magnum_Compressed"

    Lot_Number=raw_input("lot number:")

    dst1 ='C:\Auto Uploading\Auto uploading\hjq\ort\AQL'
    dst=str(dst1).replace('\\','//')

    Log_folder=[Dept_test,magnum_summary_2]

    newpath = dst+'\\'+str(Lot_Number)
    print 'data logs will be copied to this folder:',newpath
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    files_found=0
    for folders in Log_folder:
        print 'searching within this folder:',folders
        for root, dirs, files in os.walk(Log_folder):
            for name in files:
                if (files_found>=3):
                    return files_found
                fileName, fileExtension = os.path.splitext(name)
                if Lot_Number in name:
                    files_found=files_found+1
                    full_path=str(os.path.join(root,name)).replace('\\','//')
                    print full_path
                    shutil.copy(full_path,newpath)
                    # print 'root=',root,'dirs=',dirs,'name=',name
                    # print root+'//'+name
                    # print os.path.join(root,name)
    return files_found

if __name__ == '__main__':

    a=main()
    print 'total files found: ',a
