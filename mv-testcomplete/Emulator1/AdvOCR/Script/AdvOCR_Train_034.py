#Author: Ha Le
#The test verify warning dialog appear if train chracter boxes are not labeled

import Setup
def AdvOCR_Train_034(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCREmpty()
  Setup.Setup_AdvSegmentNewLine()
  Setup.Setup_AdvAutoSegment()
  Setup.Setup_AdvTrainButton()
  aqObject.CheckProperty(Aliases.javaw.Dialog6, "WndCaption", cmpEqual, "Setup Error")
  Aliases.javaw.Dialog6.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
  Setup.Setup_closeVPM()
  
