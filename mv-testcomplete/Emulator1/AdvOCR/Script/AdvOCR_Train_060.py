#Author: Ha Le
#The test verify scroll bar will appear when floating window too small

import Setup
def AdvOCR_Train_060(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCR()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGTrainPanel.Panel3.Panel.Panel.Panel.Panel2.Button.ClickButton()
  Aliases.javaw.FloatablePanel.Drag(258, 415, 32, -140)
  aqObject.CheckProperty(Aliases.javaw.FloatablePanel.RootPane.null_layeredPane.null_contentPane.Panel.OCRSetPanel.ScrollPane.ScrollPane_ScrollBar, "Height", cmpGreater, 85)

  Setup.Setup_closeVPM()



