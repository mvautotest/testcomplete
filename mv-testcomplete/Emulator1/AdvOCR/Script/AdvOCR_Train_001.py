#Author: Ha Le
#The test verify there is a blue message displays at the first time user enter this panel

import Setup
def AdvOCR_Train_001(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()

  Setup.Setup_DragAvdToTaskTree()
 
  Setup.Setup_VPMTrainPanel()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGTrainPanel.Panel2.Label, "text", cmpEqual, "Before training the tool, first define row segments then type a label for each box.")
  Setup.Setup_closeVPM()
  
