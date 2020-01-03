#Author: Ha Le
#The test verify the color of the character boxes

import Setup
def AdvOCR_CPM_015(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCREmpty()
  Setup.Setup_LoadCPM()
  Setup.Setup_DragOCRFontLibraryToCpFile()
  Setup.Setup_EnableRunMode()
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.OCRSet.SwingObject("SegmentationFrame").SwingObject("AddCharBoxButton").ClickButton()
  Regions.DisplayCanvas44.Check(Regions.CreateRegionInfo(Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.OCRSet.SearchImage.Panel.Panel.ScrollPane.Viewport.DisplayCanvas, 43, 36, 306, 214, False), False, False, 1000)
  #frame = Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.Item.Item.CpmFrame_25.Panel_1.OCRSet.SwingObject("SegmentationFrame")
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.OCRSet.SwingObject("SegmentationFrame").SwingObject("DisplaySegmentButton").ClickButton()
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.OCRSet.SwingObject("SegmentationFrame").SwingObject("TypeList").SwingObject("WindowsComboBoxUI$XPComboBoxButton", "", 0).ClickButton()
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.OCRSet.SwingObject("SegmentationFrame").SwingObject("TypeList").ClickItem("White Characters")
  Regions.DisplayCanvas45.Check(Regions.CreateRegionInfo(Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.OCRSet.SearchImage.Panel.Panel.ScrollPane.Viewport.DisplayCanvas, 52, 46, 275, 174, False), False, False, 1000)
  Setup.Setup_DisableRunMode()

  Setup.Setup_closeCPM()
  Setup.Setup_closeVPM()