__author__ = '20093'

import seaborn as sns
import pandas as pd
import wx
import matplotlib.pyplot as plt

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
    file_path=get_path('*.csv')
    if '(BitFlips' in file_path:
        print 'Will generate Histogram chart'

        Histo = pd.read_csv(file_path)
        sns.set()  # use seaborn styles
        Histo.pivot_table('Count', index=['BitFlip'], columns=['Lot','Level'], aggfunc='sum').plot()
        plt.title('Histogram by Lot')
        plt.xlabel('Bitflip')
        plt.ylabel('Number of MU')
        plt.yscale('log')
        plt.show()
    elif 'Grade' in file_path:
        print 'Will generate Cr or Tr grade chart'
        Grade=pd.read_csv(file_path)
        sns.set()  # use seaborn styles
        Grade.pivot_table('Count', index=['CrGrade'], columns=['Level'], aggfunc='max').plot()
        plt.title('Cr Grade by Lot')
        plt.xlabel('Bitflip')
        plt.ylabel('Number of MU')
        plt.yscale('log')
        plt.show()

if __name__ == '__main__':
    main()