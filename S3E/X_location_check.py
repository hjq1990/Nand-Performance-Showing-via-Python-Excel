import csv
import os
import time


def main():
    line = 0
    strr = [0 for x in xrange(1000000)]
    folder_paths = {

        "Z:\Rel_Lab\CNE2\PC1\Bonafire_UID_EFR_Algo_2FIM_SEQ_62643\DUT150",
        "Z:\Rel_Lab\CNE2\PC1\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_63360\DUT150",
        "Z:\Rel_Lab\CNE2\PC3\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_63362\DUT310",
        "Z:\Rel_Lab\CNE2\PC3\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_63362\DUT412",
        "Z:\Rel_Lab\CNE4\PC1\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_63348\DUT032",
        "Z:\Rel_Lab\CNE6\PC1\Bonafire_UID_EFR_Algo_2FIM_SEQ_62641\DUT162",
        "Z:\Rel_Lab\CNE6\PC1\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_63355\DUT162",
        "Z:\Rel_Lab\CNE6\PC1\Bonafire_UID_EFR_Algo_2FIM_SEQ_62641\DUT020",
        "Z:\Rel_Lab\CNE6\PC1\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_63355\DUT020",
        "Z:\Rel_Lab\CNE6\PC2\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_63356\DUT270",
        "Z:\Rel_Lab\CNE2\PC1\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_64183\DUT212",
        "Z:\Rel_Lab\CNE3\PC1\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_64388\DUT092",
        "Z:\Rel_Lab\CNE5\PC1\Bonafire_UID_EFR_Algo_2FIM_SEQ_RQ_64202\DUT230",
        "Z:\Rel_Lab\CNE2\PC1\Bonafire_UID_EFR_Algo_2FIM_SEQ_RQ_64545\DUT160",
        "Z:\Rel_Lab\CNE2\PC1\Bonafire_UID_EFR_Algo_2FIM_SEQ_RQ_64545\DUT162",
        "Z:\Rel_Lab\CNE3\PC2\Bonafire_UID_EFR_Algo_2FIM_SEQ_RQ_64539\DUT250",
        "Z:\Rel_Lab\CNE3\PC2\Bonafire_UID_EFR_Algo_2FIM_SEQ_RQ_64539\DUT252",
        "Z:\Rel_Lab\CNE6\PC1\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_65257\DUT032",
        "Z:\Rel_Lab\CNE2\PC3\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_66036\DUT252",
        "Z:\Rel_Lab\CNE2\PC3\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_66036\DUT272",
        "Z:\Rel_Lab\CNE2\PC3\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_66036\DUT290",
        "Z:\Rel_Lab\CNE2\PC3\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_66036\DUT310",
        "Z:\Rel_Lab\CNE2\PC3\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_66036\DUT312",
        "Z:\Rel_Lab\CNE2\PC3\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_66036\DUT330",
        "Z:\Rel_Lab\CNE2\PC3\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_66036\DUT350",
        "Z:\Rel_Lab\CNE2\PC3\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_66036\DUT412",
        "Z:\Rel_Lab\CNE2\PC3\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_66036\DUT450",
        "Z:\Rel_Lab\CNE4\PC1\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_66746\DUT190",
        "Z:\Rel_Lab\CNE6\PC1\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_66755\DUT120",
        "Z:\Rel_Lab\CNE6\PC1\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_66755\DUT162",
        "Z:\Rel_Lab\CNE6\PC2\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_66756\DUT272",
        "Z:\Rel_Lab\CNE6\PC2\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_66756\DUT330",
        "Z:\Rel_Lab\CNE6\PC2\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_66756\DUT352",
        "Z:\Rel_Lab\CNE3\PC3\Bonafire_UID_EFR_Algo_2FIM_SEQ_EFR_67182\DUT250"

    }

    for folders in folder_paths:
        target_fim = int(folders[-1:])
        folders = folders[:-1].replace('\\', '//')
        fim = 0
        for event_file in os.listdir(folders):
            if event_file[-3:] == 'csv':
                full_path = str(
                    os.path.join(folders, event_file)).replace('\\', '//')
                X_CRC = [0 for x in xrange(10)]
                X_mask = [0 for x in xrange(10)]
                with open(full_path, 'r') as f:

                    for lines in f:

                        if lines[0:10] == 'X Computed':
                            if lines[11:14] == 'out':

                                X_CRC[fim] = lines.replace(
                                    '-', '').split(' ')[9]

                            if lines[11:16] == 'after':

                                X_mask[fim] = lines.replace(
                                    '-', '').split(' ')[-1]

                                fim = 2

                    line = line + 1
                    print full_path, (X_CRC[target_fim]), type(X_mask[target_fim])
                    strr[line] = full_path + ' FIM ' + str(target_fim) + '  ' + str(
                        X_CRC[target_fim]) + '  ' + str(X_mask[target_fim])

    result_file = 'c:/' + str(time.localtime().tm_year) + '-' + str(
        time.localtime().tm_mon) + '-' + str(time.localtime().tm_mday) + '_UID.txt'
    with open(result_file, 'w') as result:
        for i in range(1, line + 1):
            a = str(strr[i])
            result.write(a + '\n')
    print "the result is saved into as below file:", result_file


if __name__ == '__main__':
    main()
