#Author: Ha Le
#The test verify output1, ouput2 display correctly when read an element from image and insert to list

import Setup
def ListEdit_Usecase15_186(): 
  #Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadImage("Sample Pattern Sort")
  Setup.Setup_VPMNewButton()
  Setup.Setup_LoadTool("List Edit")
  Setup.Setup_LEPanel("Setup")
  Setup.Setup_LEInput1("Image", "Read", None, None)
  Setup.Setup_LELinkImage()
  Setup.Setup_LEInput2("Image List", "Insert", None)
  for i in range(0, 10):
    Setup.Setup_VPMtriggerOne()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel3.Panel.Panel.Panel.Panel.Label, "text", cmpEqual, "1")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel3.Panel.Panel.Panel2.Panel.Label, "text", cmpEqual, "1")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel.Panel2.Panel.PatchableIntegerTextField, "Enabled", cmpEqual, False)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel.Panel2.Panel.PatchableIntegerTextField2, "Enabled", cmpEqual, False)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel3.Panel.Panel.Panel3.Panel.Label, "text", cmpEqual, "10")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel3.Panel.Panel.Panel3.Panel.Label2, "text", cmpEqual, "10")
  
  Setup.Setup_closeVPM()
