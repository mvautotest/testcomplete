import Setup
import CheckPoint
def main():
    #DDT.ExcelDriver()
    Driver = DDT.ExcelDriver("C:\\Users\\hale\\Documents\\TestComplete 14 Projects\\mv-testcomplete\\TestSteps.xlsx", "Sheet1")
    Driver1 = DDT.ExcelDriver("C:\\Users\\hale\\Documents\\TestComplete 14 Projects\\mv-testcomplete\\TestData.xlsx", "Sheet1")
#  while not Driver.EOF():
#    Setup.Setup_LoadApplication(Driver.Value[2])
#    Setup.Setup_LoadImage(Driver.Value[3])
#    #DDT.CurrentDriver.Next()
#    Setup.Setup_Action(Driver.Value[4], None)
#    #DDT.CurrentDriver.Next()
#    Setup.Setup_LoadTool(Driver.Value[5])
#    Setup.Setup_LEPanel(Driver.Value[6])
#    Setup.Setup_LEInput1(Driver.Value[7], Driver.Value[8], Driver.Value[9], Driver.Value[10])