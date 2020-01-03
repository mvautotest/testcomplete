#Author: Ha Le
#The test verify user can modify subcontrol successfully
#Note: The CPM does not allow to paste in sub control

import Setup
def AdvOCR_CPM_010(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCR()
  Setup.Setup_LoadCPM()
  Setup.Setup_DragOCRFontLibraryToCpFile()
  
  Setup.Setup_CPM_ModifyItem("|[0]|Panel 1|OCR Font Library2|Segmentation|Add Character Box", 2, "Value", "30")
  Setup.Setup_CPM_ModifyItem("|[0]|Panel 1|OCR Font Library2|Segmentation|Add Character Box", 3, "Value", "150")
  Setup.Setup_CPM_ModifyItem("|[0]|Panel 1|OCR Font Library2|Segmentation|Add Character Box", 4, "Value", "370")
  Setup.Setup_CPM_ModifyItem("|[0]|Panel 1|OCR Font Library2|Segmentation|Add Character Box", 5, "Value", "10")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.ScrollPane.Viewport.CpmFrame_25.Panel_1.OCR_Font_Library2.Segmentation.Add_Character_Box.Control_GlassPane, "Height", cmpEqual, 30)
  aqObject.CheckProperty(Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.ScrollPane.Viewport.CpmFrame_25.Panel_1.OCR_Font_Library2.Segmentation.Add_Character_Box.Control_GlassPane, "ScreenLeft", cmpNotEqual, 0)
  aqObject.CheckProperty(Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.ScrollPane.Viewport.CpmFrame_25.Panel_1.OCR_Font_Library2.Segmentation.Add_Character_Box.Control_GlassPane, "ScreenTop", cmpNotEqual, 0)
  aqObject.CheckProperty(Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.ScrollPane.Viewport.CpmFrame_25.Panel_1.OCR_Font_Library2.Segmentation.Add_Character_Box.Control_GlassPane, "Width", cmpEqual, 150)
  
  Setup.Setup_CPMCopyItem("|[0]|Panel 1|OCR Font Library2|Segmentation|Add Character Box")
  Setup.Setup_CPMPasteItem("|[0]|Panel 1", "Paste Control(s)")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.ScrollPane.Viewport.ControlStatusPane.Panel.TextField, "wText", cmpEqual, "Add Character Box(2)")
  
  Setup.Setup_CPMDeleteItem("|[0]|Panel 1|Add Character Box(2)")  
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.ScrollPane.Viewport.ControlStatusPane.Panel.TextField, "wText", cmpEqual, "Panel 1")
  
#  Setup.Setup_closeCPM()
#  Setup.Setup_closeVPM()
