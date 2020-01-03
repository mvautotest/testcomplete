#Author: Ha Le
#The test verify all links in group are copied when links to group also copied


import Setup
def AdvOCR_CPM_021(): 
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
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.ClickTab("Link Summary")
  Regions.LinkingSummaryViewport.Check(Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Link_Summary.Panel.ScrollPane.LinkingSummaryViewport)
  #Regions.LinkingSummary.Check(Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Link_Summary.Panel.ScrollPane.LinkingSummaryViewport.LinkingSummary)
  Setup.Setup_closeCPM()
  Setup.Setup_closeVPM()
  
