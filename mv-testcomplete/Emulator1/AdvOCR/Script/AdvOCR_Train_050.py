#Author: Ha Le
#The test verify user can cut, coppy and paste cyan ROIS

import Setup
def AdvOCR_Train_050(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCR()
  #Setup.Setup_AdvSegmentNewLine()
  Setup.Setup_OCRClicktoTrain()
  displayCanvas = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_2.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas
  #displayCanvas.Click(117, 143)
  displayCanvas.Keys("^c")

  displayCanvas.Keys("^v")
  displayCanvas.Click(141, 127)
  Setup.Setup_OCRClicktoTrain()
  
  displayCanvas.Keys("^x")

  displayCanvas.Keys("^v")
  displayCanvas.Click(146, 127)


  Regions.DisplayCanvas38.Check(Regions.CreateRegionInfo(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_2.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas, 51, 59, 488, 311, False), False, False, 1000)

  Setup.Setup_closeVPM()
