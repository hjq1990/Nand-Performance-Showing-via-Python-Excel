import csv
import os

def main():
    folder_paths={"Z:\Rel_Lab\CNE2\PC1\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_65279\Process_Event",
                  "Z:\Rel_Lab\CNE2\PC2\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_65280\Process_Event",
                  "Z:\Rel_Lab\CNE2\PC3\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_65281\Process",
                  "Z:\Rel_Lab\CNE3\PC1\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_65282\Process",
                  "Z:\Rel_Lab\CNE3\PC2\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_65283\Process",
                  "Z:\Rel_Lab\CNE3\PC3\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_65284\Process",
                  "Z:\Rel_Lab\CNE4\PC1\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_65273\Process",
                  "Z:\Rel_Lab\CNE4\PC2\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_65274\Process",
                  "Z:\Rel_Lab\CNE4\PC3\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_65275\Process",
                  "Z:\Rel_Lab\CNE5\PC1\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_65276\Process",
                  "Z:\Rel_Lab\CNE5\PC2\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_65277\Process",
                  "Z:\Rel_Lab\CNE5\PC3\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_65278\Process",
                  "Z:\Rel_Lab\CNE6\PC1\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_65257\Process",
                  "Z:\Rel_Lab\CNE6\PC2\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_65258\Process",
                  "Z:\Rel_Lab\CNE6\PC3\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_65259\Process"}

    print folder_paths
    for folders in folder_paths:
        folders.replace('\\','//')
        for root, dirs, files in os.walk(folders):
            for event_file in files:
                full_path=str(os.path.join(root,event_file)).replace('\\','//')
                with open (full_path,'r') as f:
                    for lines in f:
                        line=lines.replace(' ','').split(',')
                        if len(line)>2:
                            if((line[0]=='EventLog') and (int(line[2],10)<>4096)):
                                print line, full_path
if __name__ == '__main__':
    main()


