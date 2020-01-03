import Setup
import PST_General_001
def test():
  Driver = DDT.ExcelDriver("../../PST_TestSteps.xlsx", "Sheet1")
  Driver1 = DDT.ExcelDriver("../../PST_TestSteps.xlsx", "Sheet2")
  Driver2 = DDT.ExcelDriver("../../PST_TestSteps.xlsx", "Sheet3")
  Log.Message(Driver1.Value[2])
  Log.Message(Driver1.Value[6])
  Setup.Setup_LoadImages(Driver1.Value[2], Driver1.Value[6])