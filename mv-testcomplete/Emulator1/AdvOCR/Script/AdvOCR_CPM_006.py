#Author: Ha Le
#The test verify type dropdownbox auto enable or disable properly
import Setup
def AdvOCR_CPM_006():
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCR()
  Setup.Setup_LoadCPM()
  Setup.Setup_DragOCRFontLibraryToCpFile()
 
  Setup.Setup_DisableTypeText()
  #Not sure Type dropdownbox.. Skip this test
  Setup.Setup_EnableRunMode()
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.OCRSet.SwingObject("SegmentationFrame").SwingObject("AutoSegmentButton").ClickButton()
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.OCRSet.SwingObject("SegmentationFrame").SwingObject("DisplaySegmentButton").ClickButton()
  Setup.Setup_DisableRunMode()
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.ClickItem("|[0]|Panel 1|OCR Font Library2|Segmentation|Type")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.wValue[6, "Value"], "enabled", cmpEqual, True)
  Setup.Setup_closeCPM()
  Setup.Setup_closeVPM()
