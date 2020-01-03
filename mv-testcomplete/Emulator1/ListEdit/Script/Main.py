import Setup
import CheckPoint
def main():
    Driver = DDT.CSVDriver("C:\\Users\\hale\\Documents\\TestComplete 14 Projects\\mv-testcomplete\\TestSteps.csv")
  #while not Driver.EOF():
    Setup.Setup_LoadApplication(Driver.Value[2])
    Setup.Setup_LoadImage(Driver.Value[3])
    #DDT.CurrentDriver.Next()
    Setup.Setup_Action(Driver.Value[4], None)
    #DDT.CurrentDriver.Next()
    Setup.Setup_LoadTool(Driver.Value[5])
    Setup.Setup_LEPanel(Driver.Value[6])
    Setup.Setup_LEInput1(Driver.Value[7], Driver.Value[8], Driver.Value[9], Driver.Value[10])
    Setup.Setup_Action(Driver.Value[19], None)
    Setup.Setup_LEInput2(Driver.Value[11], Driver.Value[12], Driver.Value[13])
    Setup.Setup_Action(Driver.Value[20], Driver.Value[25])
    #CheckPoint.
    CheckPoint.CheckInput1("text", "1")
    CheckPoint.CheckOutput1("text", "1")
    CheckPoint.CheckOutput2("text", "10")
    CheckPoint.CheckTextField1("Enabled", False)
    CheckPoint.CheckTextField2("Enabled", False)
     

  
    Setup.Setup_Action(Driver.Value[28], None)

    
    DDT.CurrentDriver.Next()
    
