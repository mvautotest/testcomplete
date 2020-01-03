#Author: Ha Le
#The test verify the selected options are display on run mode if user selected at display panel

import Setup
def AdvOCR_Display_005(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCR()
  Setup.Setup_VPMDisplayPanel()
  #Enable OCR font library
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGDisplayPanel.Panel.Panel.ScrollPane.Viewport.BaseDisplayPane_DisplayTable.wValue[0, "A"]
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGDisplayPanel.Panel.Panel.ScrollPane.Viewport.BaseDisplayPane_DisplayTable.ClickCell(0, "A")
  #Enbale Train Segment
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGDisplayPanel.Panel.Panel.ScrollPane.Viewport.BaseDisplayPane_DisplayTable.wValue[8, "A"]
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGDisplayPanel.Panel.Panel.ScrollPane.Viewport.BaseDisplayPane_DisplayTable.ClickCell(8, "A")
  #Enable minimum Score
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGDisplayPanel.Panel.Panel.ScrollPane.Viewport.BaseDisplayPane_DisplayTable.wValue[14, "A"]
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGDisplayPanel.Panel.Panel.ScrollPane.Viewport.BaseDisplayPane_DisplayTable.ClickCell(14, "A")
  
  Setup.Setup_VPMRunModeEnable()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane2.DisplayPanel.SplitPane.DisplayPanel_DisplayPanelLeftPanel_.DisplayPanel_TablePane.ScrollPane.Viewport.DisplayPanel_RuntimeTable, "wRowCount", cmpEqual, 7)
#  Regions.DisplayPanel_RuntimeTable.Check(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane2.DisplayPanel.SplitPane.DisplayPanel_DisplayPanelLeftPanel_.DisplayPanel_TablePane.ScrollPane.Viewport.DisplayPanel_RuntimeTable)
  Setup.Setup_VPMRunModeDisable()
  Setup.Setup_closeVPM()
