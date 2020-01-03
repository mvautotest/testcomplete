#Author: Ha Le
#The test verify tooltip apprear for Pass/Fail


import Setup
def AdvOCR_Verification_010(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCR()

  Setup.Setup_VPMVerificationPanel()
  a = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGVerifyPanel.Panel2.Panel.PassFailLabel.getToolTipText()
  if a == "Indicates if the read of the characters was successful.":
    Log.Checkpoint(a, "Test passed")
  else:
    Log.Error(a, "test failed")
 

  Setup.Setup_closeVPM()

