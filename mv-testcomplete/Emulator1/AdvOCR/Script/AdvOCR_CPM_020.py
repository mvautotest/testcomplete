#Author: Ha Le
#The test verify user can delete the copied group control


import Setup
def AdvOCR_CPM_020(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCR()
  Setup.Setup_LoadCPM()
  Setup.Setup_DragOCRFontLibraryToCpFile()
  Setup.Setup_CopyPasteOCRFontLibrary()
  Setup.Setup_CopyPasteTrainButton()
  Setup.Setup_CPMDeleteItem("[0]|Panel 1|OCR Font Library2")
 
  aqObject.CheckProperty(Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.cellRenderer, "text", cmpEqual, "Hidden Run(2)")
  Setup.Setup_closeCPM()
  Setup.Setup_closeVPM()
 
