#Author: Ha Le
#The test verify user can drag and drog OCR Font Library to cp file by "Shift" key and drag the tool

import Setup
def AdvOCR_CPM_001():
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCR()
  #Setup.Setup_closeVPM()

  Setup.Setup_LoadCPM()
  Delay(1000)
  Setup.Setup_DragOCRFontLibraryToCpFile()
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.MainToolBar.Panel.DesignRunModeButton.ClickButton(True)
  Regions.OCRSet.Check(Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SwingObject("JScrollPane", "", 0).SwingObject("JViewport", "", 0).SwingObject("CpmFrame$25", "Panel 1", 0).SwingObject("Panel 1").SwingObject("OCRSet", "OCR Font Library2", 0))
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.MainToolBar.Panel.DesignRunModeButton.ClickButton(False)
  

  Setup.Setup_closeCPM()
  Setup.Setup_closeVPM()
