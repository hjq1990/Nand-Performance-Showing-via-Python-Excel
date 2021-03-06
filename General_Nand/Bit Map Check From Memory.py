'''
*****************************************
Bitmap check for Bad Blocks
*****************************************
Purpose: this API is for checking the bitmap for Bad Blocks for each dies

Jan 10, 2015
Jinqiang He

'''
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

    HDB=16
    Base=8  # hex is 8, bin is 1
    Bytes_Per_line=32
    BB = [0 for x in xrange(50)]
    strr=[0 for x in xrange(10000)]

    TYPE=0  #  0----1Y Ex2 2P 8K,  1----1Y Ex3 1P,  2-------1Y Ex3 2P,  4---------1Y Ex2 4P 16K

    print '''
    *****************************************
    Bitmap check for Bad Blocks
    *****************************************
    Purpose: this API is for checking the bitmap for Bad Blocks for each dies

    Jan 10, 2015
    Jinqiang He

    '''
    print "The bit map file should be in below format:"
    print "1: number in Hex mode, each line contains 32 number, and number in Byte form"

    print "please select the config of product you are testing"
    print '''Product Config Type: 0----1Y Ex2 2P 8K,  1----1Y Ex3 1P,  2-------1Y Ex3 2P,  3---------1Y Ex2 4P 16K
    if (TYPE==0)://
        BLOCK_BIT_MAP_START='0x8007830c'
        BB_MAP_BLOCK_BYTES='0x10c '
    elif(TYPE==1):
        BLOCK_BIT_MAP_START='0x8007830c'
        BB_MAP_BLOCK_BYTES='0x214'
    elif(TYPE==2):
        BLOCK_BIT_MAP_START='0x8007830c'
        BB_MAP_BLOCK_BYTES='0x220 '
    elif(TYPE==3):
        BLOCK_BIT_MAP_START='0x8007830c'
        BB_MAP_BLOCK_BYTES='0x218
        '''
    print "********************************************"

    TYPE=input("Product Config Type: ")
    filename=get_path('*.txt')

    index=filename.find('.')
    result_name=filename[:index]+"-BB"+filename[index:]

    #Product Config Type: 0----1Y Ex2 2P 8K,  1----1Y Ex3 1P,  2-------1Y Ex3 2P,  3---------1Y Ex2 4P 16K
    if (TYPE==0):
        BLOCK_BIT_MAP_START='0x8007830c'
        BB_MAP_BLOCK_BYTES='0x10c '
    elif(TYPE==1):
        BLOCK_BIT_MAP_START='0x8007830c'
        BB_MAP_BLOCK_BYTES='0x214'
    elif(TYPE==2):
        BLOCK_BIT_MAP_START='0x8007830c'
        BB_MAP_BLOCK_BYTES='0x220 '
    elif(TYPE==3):
        BLOCK_BIT_MAP_START='0x8007830c'
        BB_MAP_BLOCK_BYTES='0x218 '

    line_pre=-1
    die=0
    bb_count=0

    with open(filename) as f:
      for lines in f:

          if (len(lines)>20):
            start="0x"+lines[0:8]
            line=(int(start, 16)-int(BLOCK_BIT_MAP_START,16))/32
            if (line - line_pre!=1):
              print "warning, missing data here at "+line[0:8]

            line_hex=str(lines[10:-37].replace(' ','').replace('_',''))
            line_bin=bin(int(line_hex, HDB)).zfill(Bytes_Per_line*Base)
            print line,line_pre
            line_pre=line

          for i in range(0,32):
              for j in range(0,8):
                  if(line_bin[8*i+8-j-1]=='1'):

                      BB[die]=BB[die]+1
                      die=(line*Bytes_Per_line*Base+i*8+j)/(int(BB_MAP_BLOCK_BYTES,base=16)*8)
                      strr[bb_count]='Die--'+str(die)+',  BB Number--'+str(BB[die])+', block '+str(hex((line*Bytes_Per_line*Base+i*8+j) % (int(BB_MAP_BLOCK_BYTES,base=16)*8)))
                      bb_count=bb_count+1
    with open(result_name,'w') as result:
      for i in range(0,bb_count):
        result.write(strr[i]+'\n')
    print bb_count

    print "BB list is generated and saved to below file: ", result_name


if __name__ == '__main__':
    main()

