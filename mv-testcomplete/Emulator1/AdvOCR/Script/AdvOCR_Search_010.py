#Author: Ha Le
#The test verify there is a blue message on the panel

import Setup
def AdvOCR_Search_010(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()

  
  Setup.Setup_DragAvdToTaskTree()
 
  Setup.Setup_VPMSearchPanel()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGSearchPanel.Panel.Label, "text", cmpEqual, "Select and resize the displayed ROI to define the Search region.")
 
  Setup.Setup_closeVPM()
  
