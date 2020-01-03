#Author: Ha Le
#The test verify user can delete each trained or delete all trained characterbox

import Setup
def AdvOCR_CPM_017(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCR()

  Setup.Setup_LoadCPM()
  Setup.Setup_DragOCRFontLibraryToCpFile()
  Setup.Setup_EnableRunMode()
  Delay(500)
  Setup.Setup_OCRCPMDeletePattern()
  aqObject.CheckProperty(Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.OCRSet.OCRSetFrame.OCRSetDisplay.OCRSetPanel.ScrollPane.Viewport.OCRSetPanel_LibraryPanel_, "ChildCount", cmpEqual, 6)
  Setup.Setup_OCRCPMDeleteAllPattern()
  aqObject.CheckProperty(Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.OCRSet.OCRSetFrame.OCRSetDisplay.OCRSetPanel.ScrollPane.Viewport.OCRSetPanel_LibraryPanel_, "ChildCount", cmpEqual, 0)
    
   
  Setup.Setup_DisableRunMode()
  Setup.Setup_closeCPM()
  Setup.Setup_closeVPM()
 

 