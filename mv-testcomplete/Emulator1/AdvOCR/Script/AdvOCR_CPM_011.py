#Author: Ha Le
#The test verify Zoom function is updated and work properly between run mode and design mode

import Setup
def AdvOCR_CPM_011(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCR()
  Setup.Setup_LoadCPM()
  Setup.Setup_DragOCRFontLibraryToCpFile()


  scrollPane = Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane
  scrollPane.VScroll.Pos = 229
  Regions.ControlPropertiesPane_ControlPropertiesInnerPane2.Check((Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane), False, False, 11000)
  panel = Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane
  splitPane = panel.Panel.SplitPane.SplitPane
  scrollPane = splitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane
  scrollPane.VScroll.Pos = 229
  propertyText = scrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.PropertyText
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.Click(224, 182)
  propertyText.Keys("[BS]2")
  Setup.Setup_EnableRunMode()
  
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SwingObject("JScrollPane", "", 0).SwingObject("JViewport", "", 0).SwingObject("CpmFrame$25", "Panel 1", 0).SwingObject("Panel 1").SwingObject("OCRSet", "OCR Font Library2", 0).SwingObject("OCRSetFrame").SwingObject("OCRSetDisplay").SwingObject("OCRSetPanel", "", 0).SwingObject("JToolBar", "", 0).SwingObject("JPanel", "", 0).SwingObject("JToggleButton", "", 0).ClickButton(True)
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SwingObject("JScrollPane", "", 0).SwingObject("JViewport", "", 0).SwingObject("CpmFrame$25", "Panel 1", 0).SwingObject("Panel 1").SwingObject("OCRSet", "OCR Font Library2", 0).SwingObject("OCRSetFrame").SwingObject("OCRSetDisplay").SwingObject("OCRSetPanel", "", 0).SwingObject("JScrollPane", "", 0).SwingObject("JViewport", "", 0).SwingObject("OCRSetPanel$LibraryPanel_", "", 0).SwingObject("OCRSetPanel$CharTemplatePanel_", "", 0).Click(True)
  Setup.Setup_DisableRunMode()
  scrollPane.VScroll.Pos = 229
  Regions.ControlPropertiesPane_ControlPropertiesInnerPane3.Check(Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane)

  Setup.Setup_closeCPM()
  Setup.Setup_closeVPM()

