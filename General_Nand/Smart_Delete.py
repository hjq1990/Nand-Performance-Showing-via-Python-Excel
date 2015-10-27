__author__ = '20093'

import os
import shutil
import time
import itertools
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from os.path import join, getsize


def main():
    dest_folder = 'X:\SATA_old'

    CNE = map(lambda s: os.path.join(dest_folder, s), os.listdir(dest_folder))

    CNE_dir = filter(lambda s: os.path.isdir(s), CNE)

    for CNE_list in CNE_dir:
        PC = map(lambda s: os.path.join(CNE_list, s), os.listdir(CNE_list))

        PC_dir = filter(lambda s: os.path.isdir(s) == 1, PC)
        for PC_list in PC_dir:

            Test_folder = map(lambda s: os.path.join(
                PC_list, s), os.listdir(PC_list))
            Test_dir = filter(lambda s: os.path.isdir(s) == 1, Test_folder)
            TLV_CSV = map(lambda s: s + '/Process_TLV', Test_dir)
            TLV_folder = filter(lambda s: (os.path.isdir(s) == 1), TLV_CSV)
            for TLV in TLV_folder:

                csv_file = map(lambda s: os.path.join(TLV, s), os.listdir(TLV))
                csv_list = filter(lambda s: '.csv' in s, csv_file)
                print csv_list
                pool = ThreadPool(20)
                pool.map(os.remove, csv_list)
                pool.close()
            for Test in Test_dir:
                Test_DUT = map(lambda s: os.path.join(
                    Test, s), os.listdir(Test))
                DUT_list = filter(
                    lambda s: 'DUT' in s[-6:] and os.path.isdir(s), Test_DUT)
                for DUT in DUT_list:

                    DAT_files = map(lambda s: os.path.join(
                        DUT, s), os.listdir(DUT))
                    DAT_list = filter(lambda s: '.dat' in s[-5:], DAT_files)
                    pool = ThreadPool(20)
                    pool.map(os.remove, DAT_list)
                    pool.close()
                    print DAT_list

if __name__ == '__main__':
    dest_folder = ''
    main()
