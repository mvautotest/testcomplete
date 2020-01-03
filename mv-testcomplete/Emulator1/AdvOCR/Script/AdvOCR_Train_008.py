#Author: Ha Le
#The test verify Segmentation Region ROI only display in Auto Segment mode

import Setup
def AdvOCR_Train_008(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  #Setup.Setup_DragAvdToTaskTree()
  Setup.Setup_AdvOCREmpty()
  Setup.Setup_AdvSegmentNewLine()
  Setup.Setup_AdvAutoSegment()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_2.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.roiList_.elementData_2.Items[0], "visible_", cmpEqual, False)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_2.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.roiList_.elementData_2.Items[0], "xLocation_", cmpEqual, 32)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_2.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.roiList_.elementData_2.Items[0], "yLocation_", cmpEqual, 24)
  Setup.Setup_closeVPM()
