#Author: Ha Le
#The test verify user can adjust Segmentation region ROI to define each row of character to segment

import Setup
def AdvOCR_Train_005(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  #Setup.Setup_AdvOCR()
  Setup.Setup_DragAvdToTaskTree()
  #Setup.Setup_AdvNotTrain()
  Setup.Setup_VPMSearchPanel()
  Setup.Setup_DrawROISmall()

  Setup.Setup_VPMTrainPanel()
  Setup.Setup_AdvSegmentNewLine()
  Setup.Setup_AdjustROI()
  Setup.Setup_AdvAutoSegment()
  Setup.Setup_OCRClicktoTrain()
#  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGTrainPanel.Panel.Panel.Panel.Button.ClickButton()
  baseSetupPanel_1 = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1
  displayCanvas = baseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_2.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas

  displayCanvas.Keys("lot2a")
  Setup.Setup_AdvTrainButton()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGTrainPanel.Panel3.Panel.Panel.OCRSetPanel.ScrollPane.Viewport.OCRSetPanel_LibraryPanel_, "ChildCount", cmpEqual, 5)
  Setup.Setup_closeVPM()
 

