import os
import sys
import wx


# Get_path is refered from this site:
# http://stackoverflow.com/questions/9319317/quick-and-easy-file-dialog-in-python

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

# Bytes Change script from Puneet.Kori@sandisk.com

inputFileSize = 0
totalPageSize = 18000
pageSize = 17664
residueBytePadSize = 96  # pads 0xFF  residue bytes
additionalPadSize = 240  # pads 0x00  additional padding

rbPaddingByte = b'\xff'
aPaddingByte = b'\x00'


def updateNewPatternFile(inputFile, outputFile):
    ipPatternFile = open(inputFile, 'rb')
    opPatternFile = open(outputFile, 'wb')
    pageCount = 0

    while ipPatternFile.tell() < inputFileSize:
        opPatternFile.flush()
        ipPatternFile.seek(totalPageSize * pageCount)
        dataRead = ipPatternFile.read(pageSize)
        if totalPageSize * pageCount != inputFileSize:
            opPatternFile.write(dataRead)
            rbBytesCount = 0
            addBytesCount = 0
            while rbBytesCount < residueBytePadSize:
                opPatternFile.write(rbPaddingByte)
                rbBytesCount = rbBytesCount + 1
            while addBytesCount < additionalPadSize:
                opPatternFile.write(aPaddingByte)
                addBytesCount = addBytesCount + 1
            pageCount = pageCount + 1

    opPatternFile.close()
    ipPatternFile.close()


def updateOldPatternFile(inputFile, outputFile):
    ipPatternFile = open(inputFile, 'rb')
    opPatternFile = open(outputFile, 'wb')
    pageCount = 0

    while ipPatternFile.tell() < inputFileSize:
        ipPatternFile.seek(pageSize * pageCount)
        dataRead = ipPatternFile.read(pageSize)
        opPatternFile.write(dataRead)
        rbBytesCount = 0
        addBytesCount = 0
        while rbBytesCount < residueBytePadSize:
            opPatternFile.write(rbPaddingByte)
            rbBytesCount = rbBytesCount + 1
        while addBytesCount < additionalPadSize:
            opPatternFile.write(aPaddingByte)
            addBytesCount = addBytesCount + 1
        pageCount = pageCount + 1

    opPatternFile.flush()
    opPatternFile.close()
    ipPatternFile.close()

if __name__ == "__main__":
    RDG_input = get_path('*.pat')
    RDG_output = RDG_input[:-4] + "-output.pat"

    inputFileSize = os.path.getsize(RDG_input)

    if (inputFileSize % pageSize) == 0:
        updateOldPatternFile(RDG_input, RDG_output)
        print "Padding in Page mode file finish, input file: ", RDG_input, "  output file: ", RDG_output

    elif (inputFileSize % totalPageSize) == 0:
        updateNewPatternFile(RDG_input, RDG_output)
        print "Padding in Block mode file finish, input file: ", RDG_input, "  output file: ", RDG_output
