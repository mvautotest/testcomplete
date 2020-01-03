#Author: Ha Le
#The test verify OCR Font Library also display on Run mode if OCR Font Library is selected

import Setup
def AdvOCR_Display_010(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCR()

  Setup.Setup_VPMDisplayPanel()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGDisplayPanel.Panel.Panel.ScrollPane.Viewport.BaseDisplayPane_DisplayTable.wValue[0, "A"]
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGDisplayPanel.Panel.Panel.ScrollPane.Viewport.BaseDisplayPane_DisplayTable.ClickCell(0, "A")
  
  Setup.Setup_VPMRunModeEnable()
  Setup.Setup_VPMOCRFontLibraryTabRunMode()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane2.DisplayPanel.DisplayPanel_DisplayPanelRightPanel_.SplitPane.DisplayPanel_ImagePane2.OCRSetPanel.ScrollPane.Viewport.OCRSetPanel_LibraryPanel_, "ChildCount", cmpEqual, 7)
  #Regions.OCRSetPanel1.Check(Regions.CreateRegionInfo(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane2.DisplayPanel.DisplayPanel_DisplayPanelRightPanel_.SplitPane.DisplayPanel_ImagePane2.OCRSetPanel, 27, 1, 585, 117, False))
  Setup.Setup_VPMRunModeDisable()
  Setup.Setup_closeVPM()
  
