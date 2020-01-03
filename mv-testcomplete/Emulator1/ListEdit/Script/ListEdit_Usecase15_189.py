
#Author: Ha Le
#Verify Output1, Output 2 display correctly when Read an element from Integer and Insert to list

import Setup
def ListEdit_Usecase15_188(): 
  #Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadImage("Sample Pattern Sort")
  Setup.Setup_VPMNewButton()
  Setup.Setup_LoadTool("Origin")  
  Setup.Setup_LoadTool("List Edit")
  Setup.Setup_LEPanel("Setup")
  Setup.Setup_LEInput1("Origin", "Read", "None", "None")
  Setup.Setup_LELinkItem("Output Origin Relative To RWC")

  Setup.Setup_LEInput2("Origin List", "Insert", "None")
  for i in range(0, 10):
    Setup.Setup_VPMtriggerOne()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel3.Panel.Panel.Panel.Panel.Label, "text", cmpEqual, "1")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel3.Panel.Panel.Panel2.Panel.Label, "text", cmpEqual, "1")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel.Panel2.Panel.PatchableIntegerTextField, "Enabled", cmpEqual, False)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel.Panel2.Panel.PatchableIntegerTextField2, "Enabled", cmpEqual, False)
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.VScroll.Pos = 186
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel3.Panel.Panel.Panel3.Panel.Label, "text", cmpEqual, "10")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel3.Panel.Panel.Panel3.Panel.Label2, "text", cmpEqual, "10")
  
  Setup.Setup_closeVPM()

