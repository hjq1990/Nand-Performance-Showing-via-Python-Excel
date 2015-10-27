
import os
import wx


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
    folder_path = get_path('*.txt')
    wrong_folder = []
    with open(folder_path, 'r') as fl:
        lines = fl.read().splitlines()

        for line in lines:

            for root, dirs, files in os.walk(line):

                for file in files:
                    if 'ffs_tmp' in file:
                        if not line in wrong_folder:
                            wrong_folder.append(line)
        print wrong_folder


if __name__ == '__main__':
    main()
