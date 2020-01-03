#Author: Ha Le
#The test verify the origin ROI (in red) display on panel in case "Tool Origin" input port is linked


import Setup
def AdvOCR_Verification_004(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_VPMOrigin()
  Setup.Setup_MethodPanel()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.SwingObject("JPanel", "", 0).SwingObject("JPanel", "", 0).SwingObject("JRadioButton", "One Direction", 0).Click(True)
  Setup.Setup_ROIPassFailPanel()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.Origin2Setup_OriginSetupPanel_1.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.Drag(218, 109, 10, 109)
  Setup.Setup_AdvOCREmpty()

  Setup.Setup_VPMVerificationPanel()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_1.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.roiList_.elementData_2.Items[3].origin_, "angle_", cmpEqual, -1.5707963267948966)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_1.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.roiList_.elementData_2.Items[3].origin_, "xLocation_", cmpEqual, 181)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_1.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.roiList_.elementData_2.Items[3].origin_, "yLocation_", cmpEqual, 241)

  Setup.Setup_closeVPM()


