#Author: Ha Le
#The test verify an error prompt display if enter the invalid line


import Setup
def AdvOCR_Verification_013(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCR()
  
  Setup.Setup_VPMVerificationPanel()
  javaw = Aliases.javaw
  basicComboBoxEditor_BorderlessTextField = javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGVerifyPanel.Panel.Panel.Panel.Panel.Panel.ComboBox.BasicComboBoxEditor_BorderlessTextField
  basicComboBoxEditor_BorderlessTextField.Click(True)
  basicComboBoxEditor_BorderlessTextField.Keys("[BS]5[Enter]")
  aqObject.CheckProperty(Aliases.javaw.Dialog5, "WndCaption", cmpEqual, "Error")
  javaw.Dialog5.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()


  Setup.Setup_closeVPM()

