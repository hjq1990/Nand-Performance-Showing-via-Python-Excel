__author__ = '20093'

import wx
import os
import shutil
import itertools
from multiprocessing.dummy import Pool as ThreadPool


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


def get_dir():
    app = wx.PySimpleApp()
    dialog = wx.DirDialog(
        None, "Choose a directory:", style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
    if dialog.ShowModal() == wx.ID_OK:
        mydir = dialog.GetPath()
    else:
        mydir = None
    dialog.Destroy()
    return mydir


def main():

    func_hint()
    func = raw_input("Please select the function you would like to use:")
    func_num = int(func, 10)

    if func_num==0:
        S3E_Processing_Status()
    elif func_num==1:
        FBC_Results_Outliers()


def FBC_Results_Outliers():
    file_name=get_path('*.csv')
    with open(file_name,'r')as f:
        lines=f.read().splitlines()
    head=lines[0]
    BitFlip_col=head.index('BitFlip')
    Outliers=set()
    for line in lines[1:]:
        if line.split(',')[BitFlip_col]>255:
            Outliers.add(line)
    for i in Outliers:
        print i



def S3E_Processing_Status():
    print "Please select the txt file containing folder lists:"
    file_name = get_path('*.txt')
    print 'You have selected function: ', func, 'on this file', file_name
    with open(file_name, 'r') as f:
        folders = f.read().splitlines()

    Rake = filter(lambda s: os.path.exists(
        s.split()[2]+ '\\Process_TLV\\rake.parse.log'), folders)
    Rake_No = filter(lambda s: os.path.exists(
        s.split()[2]+ '\\Process_TLV\\rake.parse.log') == 0, folders)
    print '***************************************************'
    print 'Below folder is not completely decoded:'
    for i in Rake_No:
        print i, 'Not completed decoding'
    print '***************************************************'
    for folder_full in Rake:
        folder=folder_full.split()[2]
        decode_status = 'Pending'
        analysis_status = 'Finish'
        with open(folder + '\\Process_TLV\\rake.parse.log', 'r') as f:
            lines = f.read().splitlines()
        Pass = filter(lambda s: s[-4:] == 'PASS', lines)
        print folder_full, 'decoded, passed, failed DUT number', len(lines), len(Pass), len(lines) - len(Pass),
        if len(lines) - len(Pass) == 0:
            decode_status = 'Finish'
            maps_folder = folder + '/maps'
            if os.path.isdir(maps_folder):
                Maps_log = filter(
                    lambda s: s[-4:] == '.log', os.listdir(maps_folder))
                for dut_log in Maps_log:
                    with open(maps_folder + '/' + dut_log, 'r') as f:
                        log_lines = f.read().splitlines()
                        load = filter(lambda s: '[LOAD]' in s, log_lines)
                        finish = filter(
                            lambda s: 'Project Finalized, Happy Ending!' in s, log_lines)
                    if len(finish)== 0:
                        analysis_status = 'Ongoing'
                        # print 'status 1:  ', maps_folder, dut_log[:5],
                        # 'did not finish analysis'
            else:
                analysis_status = 'Pending'
        print ' decoding_status: ', decode_status, ' Analysis_status: ', analysis_status


def func_hint():
    print "This is a combined tool for S3E//LGA related data processing status check"
    print "**************************************************************************************************"
    print "0: S3E CNE 16D decoding & analysis check"
    print "1: S3E Analysis FBC result check and outlier sorting"
    print "**************************************************************************************************"
    print ' '

if __name__ == '__main__':
    main()
