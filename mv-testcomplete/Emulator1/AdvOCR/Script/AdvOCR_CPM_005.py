#Author: Ha Le
#The test verify user can hide/show the settings at "Visible"

import Setup
def AdvOCR_CPM_005():
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCR()
  Setup.Setup_LoadCPM()
  Setup.Setup_DragOCRFontLibraryToCpFile()
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.ExpandItem("[0]|Panel 1|OCR Font Library2")


 #Set False value
  Setup.Setup_DisableTypeOption()
  Setup.Setup_DisableTypeText()
  Setup.Setup_DisableSegmentNewLine()
  Setup.Setup_DisableTrainButton()
  Setup.Setup_DisableTrainPrompt()
  Setup.Setup_DisableAddCharacterBox()
  Setup.Setup_DisableAutoSegment()
  Setup.Setup_DisableSearchImage()
  Setup.Setup_DisableFontLibraryDisplay()
  #Setup.Setup_DisableTypeText()
  Setup.Setup_DisableOCRFontLibrary()
  Delay(500)
  Regions.Control_GlassPane.Check((Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.ScrollPane.Viewport.CpmFrame_25.Panel_1.OCR_Font_Library2.Control_GlassPane), False, False, 5000)

  #Set True value
  Setup.Setup_EnableTypeOption()
  Setup.Setup_EnableTypeText()
  Setup.Setup_EnableSegmentNewLine()
  Setup.Setup_EnableTrainButton()
  Setup.Setup_EnableTrainPrompt()
  Setup.Setup_EnableAddCharacterBox()
  Setup.Setup_EnableAutoSegment()
  Setup.Setup_EnableSearchImage()
  Setup.Setup_EnableOCRFontLibrary()
  Setup.Setup_EnableFontLibraryDisplay()
  Delay(500)
  Regions.Control_GlassPane1.Check((Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.ScrollPane.Viewport.CpmFrame_25.Panel_1.OCR_Font_Library2.Control_GlassPane), False, False, 5000)


  Setup.Setup_closeCPM()
  Setup.Setup_closeVPM()
 