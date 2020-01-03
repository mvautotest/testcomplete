
import Setup
def test():
#  Driver = DDT.ExcelDriver("C:\\Users\\hale\\Documents\\TestComplete 14 Projects\\mv-testcomplete\\TestSteps.xlsx", "Sheet1")
#  Driver1 = DDT.ExcelDriver("C:\\Users\\hale\\Documents\\TestComplete 14 Projects\\mv-testcomplete\\TestSteps.xlsx", "Sheet2")
#  Driver2 = DDT.ExcelDriver("C:\\Users\\hale\\Documents\\TestComplete 14 Projects\\mv-testcomplete\\TestSteps.xlsx", "Sheet3")
  a= Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[12, "E"].getChildCount()
  Log.Message(a)