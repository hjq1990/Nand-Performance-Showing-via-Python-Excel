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

    fold_dict={'a':"//cvpfilip05//Dept_test",'b':"//cvpfilip03//SDSS_Prod_Data//MemoryTestData//magnum_summary_2"}

    Lot_Number=raw_input("lot number:")

    print "Currently, software will automatically search datalogs within below folders"
    print fold_dict

    print "Enter 'add' if you want to add another folder"
    print "Enter 'del' if you want to delete one folder"
    print "Enter 'search' if you want to start searching"
    inputs=raw_input("Enter your selection")
    # while not "search":
    #     if

    dst1 ='C:\Auto Uploading\Auto uploading\hjq\ort\AQL'
    dst=str(dst1).replace('\\','//')

    newpath = dst+'\\'+str(Lot_Number)
    print 'data logs will be copied to this folder:',newpath
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    files_found=0
    for folders in fold_dict.values():
        print 'searching within this folder:',folders
        for root, dirs, files in os.walk(folders):
            for name in files:
                fileName, fileExtension = os.path.splitext(name)
                if Lot_Number in name:
                    files_found=files_found+1
                    full_path=str(os.path.join(root,name)).replace('\\','//')
                    print 'data log',full_path,'will be copied to dist folder'
                    shutil.copy(full_path,newpath)
                    # print 'root=',root,'dirs=',dirs,'name=',name
                    # print root+'//'+name
                    # print os.path.join(root,name)
    return files_found

if __name__ == '__main__':

    a=main()
    print 'total files found: ',a
