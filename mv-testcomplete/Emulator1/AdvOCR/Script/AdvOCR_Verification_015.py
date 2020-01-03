#Author: Ha Le
#The test verify tooltip apprear on Line dropbox


import Setup
def AdvOCR_Verification_015(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCR()

  Setup.Setup_VPMVerificationPanel()
  a = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGVerifyPanel.Panel.Panel.Panel.Panel.Panel.ComboBox.WindowsComboBoxUI_XPComboBoxButton.getToolTipText()
  if a == "Selected line of characters to verify.":
    Log.Checkpoint(a, "Test passed")
  else:
    Log.Error(a, "test failed")
 

  Setup.Setup_closeVPM()

