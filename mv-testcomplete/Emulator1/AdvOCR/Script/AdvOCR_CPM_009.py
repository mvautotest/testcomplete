#Author: Ha Le
#The test verify user can rename/resize and move OCRSet Display

import Setup
def AdvOCR_CPM_009(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCR()
  Setup.Setup_LoadCPM()
  Setup.Setup_DragOCRFontLibraryToCpFile()
  Setup.Setup_CPMRenameItem("|[0]|Panel 1|OCR Font Library2|OCR Font Library|OCR Font Library Display", "[BS][BS][BS][BS][BS][BS][BS][BS][BS][BS][BS][BS][BS][BS][BS][BS][BS][BS][BS][BS][BS][BS][BS][BS]OCR test[Enter]")
  Setup.Setup_CPM_ModifyItem("|[0]|Panel 1|OCR Font Library2|OCR Font Library|OCR test", 0, "Value", "140")
  Setup.Setup_CPM_ModifyItem("|[0]|Panel 1|OCR Font Library2|OCR Font Library|OCR test", 1, "Value", "500")
  Setup.Setup_CPM_ModifyItem("|[0]|Panel 1|OCR Font Library2|OCR Font Library|OCR test", 2, "Value", "20")
  Setup.Setup_CPM_ModifyItem("|[0]|Panel 1|OCR Font Library2|OCR Font Library|OCR test", 3, "Value", "90")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.ScrollPane.Viewport.CpmFrame_25.Panel_1.OCR_Font_Library2.OCR_Font_Library.OCR_test.Control_GlassPane, "Height", cmpEqual, 140)
  aqObject.CheckProperty(Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.ScrollPane.Viewport.CpmFrame_25.Panel_1.OCR_Font_Library2.OCR_Font_Library.OCR_test.Control_GlassPane, "ScreenLeft", cmpNotEqual, 0)
  aqObject.CheckProperty(Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.ScrollPane.Viewport.CpmFrame_25.Panel_1.OCR_Font_Library2.OCR_Font_Library.OCR_test.Control_GlassPane, "ScreenTop", cmpNotEqual, 0)
  aqObject.CheckProperty(Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.ScrollPane.Viewport.CpmFrame_25.Panel_1.OCR_Font_Library2.OCR_Font_Library.OCR_test.Control_GlassPane, "Width", cmpEqual, 500)


  Setup.Setup_closeCPM()
  Setup.Setup_closeVPM()
 


