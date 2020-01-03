#Author: Ha Le
#The test verify validation on Noise level text field

import Setup
def AdvOCR_Train_075(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCR()
  #Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGTrainPanel.Panel3.Panel.Panel.Panel.Panel2.Panel.TextField2
  javaw = Aliases.javaw
  textField = javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGTrainPanel.Panel3.Panel.Panel.Panel.Panel2.Panel.TextField2
  textField.Click(True)
  textField.Keys("[BS]-1[Enter]")
  aqObject.CheckProperty(Aliases.javaw.Dialog10, "WndCaption", cmpEqual, "Setup Error - Error")
  button = javaw.Dialog10.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button
  button.ClickButton()
  textField.Keys("!![Enter]")
  aqObject.CheckProperty(Aliases.javaw.Dialog10, "WndCaption", cmpEqual, "Setup Error - Error")
  button.ClickButton()
  textField.Keys("[BS][Enter]")
  aqObject.CheckProperty(Aliases.javaw.Dialog10, "WndCaption", cmpEqual, "Setup Error - Error")
  button.ClickButton()
  textField.Keys("100[Enter]")
  aqObject.CheckProperty(Aliases.javaw.Dialog10, "WndCaption", cmpEqual, "Setup Error - Error")
  button.ClickButton()
  textField.Keys("98[Enter]")
  aqObject.CheckProperty(Aliases.javaw.Dialog10, "WndCaption", cmpEqual, "Setup Error - Error")
  Aliases.javaw.Dialog13.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
  textField.Keys("1[Enter][BS]47[Enter][BS][BS]99[Enter]")
  
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGTrainPanel.Panel3.Panel.Panel.Panel.Panel2.Panel.TextField2, "wText", cmpEqual, "99")
  Setup.Setup_VPMUnloadProgram()
  Aliases.javaw.Dialog11.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()


  Setup.Setup_closeVPM()
 



