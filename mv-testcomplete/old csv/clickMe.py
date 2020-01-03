import os
import csv
import re
def csv_test():
    with open ('TestCases.csv') as csv_file:
        csv_read = csv.reader(csv_file, delimiter = ',')
        line_count = 0
        for row in csv_read:
            if line_count == 0:
                #print(f'Setting: {", ".join(row)}')
                line_count +=1
            else:
                if row[0]== "TRUE" and row[1] == "" and row[2] == "FALSE":
                    print("Run_project_Suite")
                    #os.system('run TestComplete.exe "..\\mv-testcomplete\\Emulator1\\Emulator1.pjs" /run /el:"testlog\\log.html" /e /SilentMode')
                    #return 1
                    #os._exit(1)
                elif row[0]=="TRUE" and row[1]!= "" and row[2] == "FALSE":
                    print(row[1])
                    #print("Run project selected", row[1])
                    #os._exit(row[1])
                    #if row[1] == "AdvOCR":
                        #print(row[1])
                        
                        #os._exit(20)
                    #elif row[1] == "PatternSortingTool":
                       # print(row[1])
                        
                        #os._exit(21)
                    #elif row[1] == "PinpointPatternFind":
                        #print(row[1])
                        
                        #os._exit(22)
                    #else:
                        #os._exit(0)
                        #print(row[1])
                        #print("Project Name is not correct")
                elif row[0]=="TRUE" and row[1] != "" and row[2]== "TRUE":
                    print(row[1])
                    print(row[3])
                    #print(row[1] + ' /t:"Script|' + row[3] + "|" + row[3] +'" ') 
                    #return 3
                    #os._exit(1)
                else:
                    print("Setting was wrong. Please recheck")
                    os._exit(0)
                
                                
csv_test()

def test():
    print(os.getcwd())
#test()
