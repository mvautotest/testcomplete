#Author: Ha Le
#The test verify floating panel still open if navigate to another panel without close it

import Setup
def AdvOCR_Train_061(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCR()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGTrainPanel.Panel3.Panel.Panel.Panel.Panel2.Button.ClickButton()
  
  Aliases.javaw.FloatablePanel.Drag(263, 11, -458, -20)
  Setup.Setup_VPMVerificationPanel()
  Setup.Setup_VPMTrainPanel()
  aqObject.CheckProperty(Aliases.javaw.FloatablePanel, "Enabled", cmpEqual, True)
  aqObject.CheckProperty(Aliases.javaw.FloatablePanel, "WndCaption", cmpEqual, "OCR Font Library")
  
  Setup.Setup_closeVPM()



