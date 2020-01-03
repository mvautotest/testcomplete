#Author: Ha Le
#The test verify user can resize floating panel

import Setup
def AdvOCR_Train_059(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCR()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGTrainPanel.Panel3.Panel.Panel.Panel.Panel2.Button.ClickButton()
  floatablePanel = Aliases.javaw.FloatablePanel
  floatablePanel.Drag(533, 168, -118, -4)
  floatablePanel.Drag(210, 417, 36, -100)
  aqObject.CheckProperty(Aliases.javaw.FloatablePanel, "Width", cmpEqual, 418)

  Setup.Setup_closeVPM()



