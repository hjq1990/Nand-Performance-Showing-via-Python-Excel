import csv
import os
import time

def get_path(wildcard):
    app = wx.App(None)
    style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    dialog = wx.FileDialog(None, 'Open', wildcard=wildcard, style=style)
    if dialog.ShowModal() == wx.ID_OK:
        path = dialog.GetPath()
    else:
        path = None
    dialog.Destroy()
    return path

def main():
    lin=0
    strr=[0 for x in xrange(1000000)]
    # folders_file=get_path()
    folder_paths={
"x:\REL_EFR\SATA_CNE\CNE2_PC1\Step4_DataDump_EFR_2FIM_4D_73867",
"x:\REL_EFR\SATA_CNE\CNE2_PC2\Step4_DataDump_EFR_2FIM_4D_73868",
"x:\REL_EFR\SATA_CNE\CNE2_PC3\Step4_DataDump_EFR_2FIM_4D_73869",
"x:\REL_EFR\SATA_CNE\CNE3_PC1\Step4_DataDump_EFR_2FIM_4D_73848",
"x:\REL_EFR\SATA_CNE\CNE3_PC2\Step4_DataDump_EFR_2FIM_4D_73849",
"x:\REL_EFR\SATA_CNE\CNE3_PC3\Step4_DataDump_EFR_2FIM_4D_73850",
"x:\REL_EFR\SATA_CNE\CNE4_PC1\Step4_DataDump_EFR_2FIM_4D_73864",
"x:\REL_EFR\SATA_CNE\CNE4_PC2\Step4_DataDump_EFR_2FIM_4D_73865",
"x:\REL_EFR\SATA_CNE\CNE4_PC3\Step4_DataDump_EFR_2FIM_4D_73866",
"x:\REL_EFR\SATA_CNE\CNE5_PC1\Step4_DataDump_EFR_2FIM_4D_73860",
"x:\REL_EFR\SATA_CNE\CNE5_PC2\Step4_DataDump_EFR_2FIM_4D_73861",
"x:\REL_EFR\SATA_CNE\CNE5_PC3\Step4_DataDump_EFR_2FIM_4D_73862",
"x:\REL_EFR\SATA_CNE\CNE6_PC1\Step4_DataDump_EFR_2FIM_4D_73853",
"x:\REL_EFR\SATA_CNE\CNE6_PC2\Step4_DataDump_EFR_2FIM_4D_73854",
"x:\REL_EFR\SATA_CNE\CNE6_PC3\Step4_DataDump_EFR_2FIM_4D_73855"

                }

    for folders in folder_paths:
        folders=folders+'\Process_Event'
        folders.replace('\\','//')

        for root, dirs, files in os.walk(folders):
            for event_file in files:
                full_path=str(os.path.join(root,event_file)).replace('\\','//')

                with open (full_path,'r') as f:
                    cur_cyc=0
                    for lines in f:
                        line=lines.replace(',',' ').split()

                        if (len(line)>19) and (line[0]=='EventLog'):


                            if((line[2]<>'4096')):

                                print full_path,line
                                lin=lin+1
                                strr[lin]=full_path+lines
        decode_log=folders+'\DecodeStatus.log'
        decode_log.replace('\\','//')
        with open(decode_log,'r') as decode:
            for line in decode:

                if line[-5:-1] <>'PASS':
                    print line
                    lin=lin+1
                    strr[lin]=lines

    # result_file='c:/'+str(time.localtime().tm_year)+'-'+str(time.localtime().tm_mon)+'-'+str(time.localtime().tm_mday)+'_Event.txt'
    # with open(result_file,'w') as result:
    #     for i in range(1,lin+1):
    #         a=str(strr[i])
    #         result.write(a+'\n')
    # print "the result is saved into as below file:",result_file


if __name__ == '__main__':
    main()


