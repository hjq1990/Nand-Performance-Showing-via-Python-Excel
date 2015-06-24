import csv
import os

def main():
    folder_paths={
"Z:\Rel_Lab\CNE2\PC1\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_65279",
"Z:\Rel_Lab\CNE2\PC2\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_65280",
"Z:\Rel_Lab\CNE2\PC3\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_65281",
"Z:\Rel_Lab\CNE3\PC1\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_65282",
"Z:\Rel_Lab\CNE3\PC2\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_65283",
"Z:\Rel_Lab\CNE3\PC3\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_65284",
"Z:\Rel_Lab\CNE4\PC1\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_65273",
"Z:\Rel_Lab\CNE4\PC2\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_65274",
"Z:\Rel_Lab\CNE4\PC3\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_65275",
"Z:\Rel_Lab\CNE5\PC1\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_65276",
"Z:\Rel_Lab\CNE5\PC2\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_65277",
"Z:\Rel_Lab\CNE5\PC3\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_65278",
"Z:\Rel_Lab\CNE6\PC1\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_65257",
"Z:\Rel_Lab\CNE6\PC2\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_65258",
"Z:\Rel_Lab\CNE6\PC3\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_65259"
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


if __name__ == '__main__':
    main()


