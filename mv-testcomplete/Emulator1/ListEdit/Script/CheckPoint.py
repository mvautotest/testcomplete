Driver = DDT.ExcelDriver("C:\\Users\\hale\\Documents\\TestComplete 14 Projects\\mv-testcomplete\\TestSteps.xlsx", "Sheet1")
Driver1 = DDT.ExcelDriver("C:\\Users\\hale\\Documents\\TestComplete 14 Projects\\mv-testcomplete\\TestSteps.xlsx", "Sheet2")
Driver2 = DDT.ExcelDriver("C:\\Users\\hale\\Documents\\TestComplete 14 Projects\\mv-testcomplete\\TestSteps.xlsx", "Sheet3")


def CheckInput1():
    aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel3.Panel.Panel.Panel.Panel.Label, str(Driver2.Value[3]).strip('""'), cmpEqual, str(Driver2.Value[2]).strip('""'))
#    aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel3.Panel.Panel.Panel.Panel2.Panel.ScrollPane.Viewport.ListEditSetup_PortDataTable, "wValue[0, 1]", cmpEqual, " 9")
#  for i in range(0,10):  
#    check = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel3.Panel.Panel.Panel.Panel.Label.text
#    j = i+2
#
#    if str(check) == str(Driver2.Value[j]):
#      
#      Log.Checkpoint("Check Input 1 for " + Driver2.Value[1] + " Pass")
#    else:
#      Log.Error("Check Input 1 for " + Driver2.Value[1] + " Fail with actual value" + str(check))

def CheckOutput1():
#  for i in range(11,20):
#    check = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel3.Panel.Panel.Panel2.Panel2.Panel.ScrollPane.Viewport.ListEditSetup_PortDataTable.wValue[0, 1]
#    j = i+2
#
#    if str(check) == str(Driver2.Value[j]):
#      
#      Log.Checkpoint("Check Output 1 for " + Driver2.Value[1] + " Pass")
#    else:
#      Log.Error("Check Output 1 for " + Driver2.Value[1] + " Fail with actual value" + str(check))
    aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel3.Panel.Panel.Panel2.Panel.Label, str(Driver2.Value[5]).strip('""'), cmpEqual, str(Driver2.Value[4]).strip('""'))

def CheckInput2():
  for i in range(21, 30):
    check =  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel3.Panel.Panel.Panel2.Panel2.Panel.ScrollPane.Viewport.ListEditSetup_PortDataTable.wValue[0, 1]
    j = i+2

    if str(check) == str(Driver2.Value[j]):
      
      Log.Checkpoint("Check Input 2 for " + Driver2.Value[1] + " Pass")
    else:
      Log.Error("Check Input 2 for " + Driver2.Value[1] + " Fail with actual value" + str(check))
    
def CheckOutput2():
  for i in range(0,10):  
    check = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel3.Panel.Panel.Panel3.Panel2.Panel.ScrollPane.Viewport.ListEditSetup_PortDataTable.wValue[i, 1]
    j = i+6
    a = Driver2.Value[j]
    Log.Message(Driver2.Value[j])
    if str(check.strip()) == str(a).strip('""'):
      
      Log.Checkpoint("Check Output 2 for " + Driver2.Value[1] + " Pass")
    else:
      Log.Error("Check Output 2 for " + Driver2.Value[1] + " Fail with actual value" + str(check))


def CheckTextField1():
    aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel.Panel2.Panel.PatchableIntegerTextField, "Enabled", cmpEqual, False, False)
def CheckTextField2():
    aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel.Panel2.Panel.PatchableIntegerTextField2, "Enabled", cmpEqual, False, False)
   