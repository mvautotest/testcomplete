﻿#Author: Ha Le
#The test verify Adv OCR can work correctly with calibrated images


import Setup
def AdvOCR_CPM_022(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_Calibration()
  Setup.Setup_CaCalibratePanel()
  Setup.Setup_ApplyCalibration()
  Setup.Setup_CaLinkImage()


  Setup.Setup_DragAvdToTaskTree()
  Setup.Setup_CaLinkOutputImage()

  Setup.Setup_VPMSearchPanel()

  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_1.ROIEditor.Panel.ROIToolBar.Panel.ROIToolBar_4.ClickButton()


  
  Setup.Setup_LoadCPM()

  splitPane = Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane
  tasksTabbedPane_TaskTree_ = splitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.CPMPatchPanel.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.TasksTabbedPane_TaskTree_

  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.CPMPatchPanel.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.TasksTabbedPane_TaskTree_.wItems.Item["Root|Image In Task|Advanced OCR 1"].DblClick(True)
  Delay(400)
  tasksTabbedPane_TaskTree_.Drag(111, 229, 497, -92, skShift)
  Delay(500)
  Setup.Setup_EnableRunMode()
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.OCRSet.SwingObject("SegmentationFrame").SwingObject("AutoSegmentButton").ClickButton()
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.OCRSet.SwingObject("SearchImage").SwingObject("JPanel", "", 1).SwingObject("JPanel", "", 0).SwingObject("JScrollPane", "", 0).SwingObject("JViewport", "", 0).SwingObject("DisplayCanvas", "", 0).Click(106, 138)
  Delay(300)
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.OCRSet.SwingObject("SearchImage").SwingObject("JPanel", "", 1).SwingObject("JPanel", "", 0).SwingObject("JScrollPane", "", 0).SwingObject("JViewport", "", 0).SwingObject("DisplayCanvas", "", 0).Keys("lot2aw7")
  
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.OCRSet.SwingObject("TrainButton").ClickButton()
  aqObject.CheckProperty(Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.OCRSet.OCRSetFrame.OCRSetDisplay.OCRSetPanel.ScrollPane.Viewport.OCRSetPanel_LibraryPanel_, "ChildCount", cmpEqual, 7)

  Setup.Setup_closeCPM()
  Setup.Setup_closeVPM()
  