import csv

def savefile(listgiven):

    #row = ['Action Name', ' Slow Emotion', ' Fast Emotion']
    lines = []
    row = ['alttopbottomslowhot','alttopbottomslowcold','alttopbottomslowneutral',
           'alttopbottomfasthot','alttopbottomfastcold','alttopbottomfastneutral',
           'altleftrightslowhot','altleftrightslowcold','altleftrightslowneutral',
           'altleftrightfasthot','altleftrightfastcold','altleftrightfastneutral',
           
           'wavelefttslowhot', 'waveleftslowcold',  'waveleftslowneutral',
           'wavelefttfasthot',   'waveleftfastcold',   'waveleftfastneutral',
           'wavetrightslowhot', 'wavetrightslowcold',  'wavetrightslowneutral',
           'waverightfasthot',   'waverightfastcold',   'waverightfastneutral',
           'wavedownslowhot',    'wavedownslowcold',    'wavedownslowneutral',
            'wavedownfasthot',    'wavedownfastcold',    'wavedownfastneutral',
            'waveupslowhot',      'waveupslowcold',      'waveupslowneutral',
            'waveupfasthot',      'waveupfastcold',      'waveupfastneutral',
            
            'nopatternhot',      'nopatterncold',      'nopatternneutral',
            
            'sixmotorslowhot',    'sixmotorslowcold',    'sixmotorslowneutral',
            'sixmotorfasthot',    'sixmotorfastcold',    'sixmotorfastneutral',
            'spineupslowhot',     'spineupslowcold',     'spineupslowneutral',
           'spineupfasthot',     'spineupfastcold',     'spineupfastneutral',
           'spinedownslowhot',   'spinedownslowcold',   'spinedownslowneutral',
           'spinedownfasthot',   'spinedownfastcold',   'spinedownfastneutral',
           'snkhorislowhot',     'snkhorislowcold',     'snkhorislowneutral',
           'snkhorifasthot',     'snkhorifastcold',     'snkhorifastneutral',
           'snkvertslowhot',     'snkvertslowcold',     'snkvertslowneutral',
           'snkvertfasthot',     'snkvertfastcold',     'snkvertfastneutral',
           'shoulertapslowhot',  'shoulertapslowcold',  'shoulertapslowneutral',
           'shoulertapfasthot',  'shoulertapfastcold',  'shoulertapfastneutral']
    lines.append(row)
    '''
    for i in range(0,len(listgiven)):
        rowtemplate = []
        for k in range(0,len(actionnames)):
            for j in range (0,3):
                if(j==0):
                    rowtemplate.insert(0,actionnames[k]) 
                if(i%2!=0):
                    rowtemplate.insert(1, listgiven[i])
                else:
                    rowtemplate.insert(2,listgiven[i])
            lines.append(rowtemplate)'''
    lines.append(listgiven)
    stringfilename = input("type in file name + .csv")
    try:
        with open(stringfilename, 'r') as readFile:
            '''reader = csv.reader(readFile)
            linesnext = list(reader)
            for i in lines:
                linesnext.append(i)
            lines = linesnext'''
            nextanswer = input("error: file with that name already exists. if you want to replace the file, type in yes, else type in whatever to cancel")
            if(nextanswer == 'yes'):
                with open(stringfilename, 'w', newline = ""  ) as writeFile:
                    writer = csv.writer(writeFile)
                    writer.writerows(lines)
                    readFile.close()
            else:
                print("you cancelled replacing the file named "+ stringfilename)
    except:
        print('file is being created')
    finally:   
        with open(stringfilename, 'w', newline = ""  ) as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
    
    try:
        readFile.close()
    except:
        #donothing
        print("readfile was never opened")
    finally:
        writeFile.close()
    
    
    
    
    
    