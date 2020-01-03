#Author: Ha Le
#The test verify OCRSet Floating panel display when clicking on the pushpin icon

import Setup
def AdvOCR_Train_056(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCR()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGTrainPanel.Panel3.Panel.Panel.Panel.Panel2.Button.ClickButton()
  aqObject.CheckProperty(Aliases.javaw.FloatablePanel, "Enabled", cmpEqual, True)
  aqObject.CheckProperty(Aliases.javaw.FloatablePanel, "WndCaption", cmpEqual, "OCR Font Library")


  Setup.Setup_closeVPM()
#


