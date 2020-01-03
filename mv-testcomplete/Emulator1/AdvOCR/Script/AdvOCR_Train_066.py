#Author: Ha Le
#The test verify Zoom 100% tooltip

import Setup
def AdvOCR_Train_066(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCR()
  a = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGTrainPanel.Panel3.Panel.Panel.OCRSetPanel.ToolBar.Panel.SwingObject("JButton", "", 2).getToolTipText()
  if a == "Click to zoom characters to 100%.":
    Log.Checkpoint(a, "test passed")
  else:
    Log.Error(a, "test failed")
  

  Setup.Setup_closeVPM()



