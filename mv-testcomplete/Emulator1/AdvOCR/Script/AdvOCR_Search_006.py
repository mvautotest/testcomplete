#Author: Ha Le
#The test verify ROI off image watermark is displayed when the search ROI is off the image
import Setup
def AdvOCR_Search_006(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  #Setup.Setup_AdvOCRManual()
  
  Setup.Setup_DragAvdToTaskTree()
  Setup.Setup_VPMSearchPanel()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_1.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.Drag(111, 80, 331, 71)
  #aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_2.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.watermarkText_, "OleValue", cmpEqual, "ROI Off Image")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_1.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas, "watermarkText_", cmpEqual, "ROI Off Image")
  #aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_1.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.activeRectROI_.toolTipText_, "OleValue", cmpEqual, "Size and position ROI over the area you want to search for characters.")
  Setup.Setup_closeVPM()