#Author: Ha Le
#The test verify user can copy a group control by select only control or select all sub-controls are selected along with the group control


import Setup
def AdvOCR_CPM_019(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCR()
  Setup.Setup_LoadCPM()
  Setup.Setup_DragOCRFontLibraryToCpFile()
  Setup.Setup_CopyPasteOCRFontLibrary()
  Regions.OCR_Font_Library2_2_1.Check(Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.ScrollPane.Viewport.CpmFrame_25.Panel_1.OCR_Font_Library2_2_)
  aqObject.CheckProperty(Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.ScrollPane.Viewport.ControlStatusPane.Panel.TextField, "wText", cmpEqual, "OCR Font Library2(2)")
  Setup.Setup_CopyPasteTrainButton()
  aqObject.CheckProperty(Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.ScrollPane.Viewport.ControlStatusPane.Panel.TextField, "wText", cmpEqual, "Train(3)")
  Regions.Control_GlassPane7.Check(Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.ScrollPane.Viewport.CpmFrame_25.Panel_1.Train_3_.Control_GlassPane)
  Setup.Setup_closeCPM()
  Setup.Setup_closeVPM()