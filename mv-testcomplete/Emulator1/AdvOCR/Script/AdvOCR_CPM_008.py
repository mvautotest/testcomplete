#Author: Ha Le
#The test verify a properly error message appear prevent user delete subcontrol

import Setup
def AdvOCR_CPM_008():
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM()  
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCR()
  Setup.Setup_LoadCPM()
  Setup.Setup_DragOCRFontLibraryToCpFile()
  Setup.Setup_CPMDeleteItem("|[0]|Panel 1|OCR Font Library2|OCR Font Library|OCR Font Library Display")  
  aqObject.CheckProperty(Aliases.javaw.Dialog5, "WndCaption", cmpEqual, "Error")
  Aliases.javaw.Dialog5.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
  Setup.Setup_CPMDeleteItem("|[0]|Panel 1|OCR Font Library2|Segmentation|Segment New Line")
  aqObject.CheckProperty(Aliases.javaw.Dialog5, "WndCaption", cmpEqual, "Error")
  Aliases.javaw.Dialog5.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()  

  Setup.Setup_closeCPM()
  Setup.Setup_closeVPM()
 
