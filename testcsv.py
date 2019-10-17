import csv

def savefile(listgiven):

    #row = ['Action Name', ' Slow Emotion', ' Fast Emotion']
    lines = []
    row = ['emotion', 'audio file', 'user response']
    lines.append(row)
    for listwithin in listgiven:
        lines.append(listwithin)
    stringfilename = input("type in file name + .csv: ")
    try:
        with open(stringfilename, 'r') as readFile:
            '''reader = csv.reader(readFile)
            linesnext = list(reader)
            for i in lines:
                linesnext.append(i)
            lines = linesnext'''
            nextanswer = input("error: file with that name already exists. if you want to replace the file, type in yes, else type in whatever to cancel\n")
            if(nextanswer == 'yes'):
                with open(stringfilename, 'w', newline = ""  ) as writeFile:
                    writer = csv.writer(writeFile)
                    writer.writerows(lines)
                    readFile.close()
            else:
                print("you cancelled replacing the file named "+ stringfilename)
                stringfilename = input("type in another file name + .csv: ")
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
    
    
    
    
    
    