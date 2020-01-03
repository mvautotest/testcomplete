#Author: Ha Le
#The test verify tooltip on Noise Level field

import Setup
def AdvOCR_Train_077(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCR()
  a = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGTrainPanel.Panel3.Panel.Panel.Panel.Panel2.Panel.TextField2.getToolTipText()
  if a == "Value must be odd and kept as low as possible. Increase for higher noise images.":
    Log.Checkpoint(a, "test passed")
  else:
    Log.Error(a, "test failed")


  Setup.Setup_closeVPM()




