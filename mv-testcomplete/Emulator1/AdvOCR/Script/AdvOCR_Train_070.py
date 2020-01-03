#Author: Ha Le
#The test verify user can train multi row sucessfully without error

import Setup
def AdvOCR_Train_070(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImageMultiText()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCREmpty()
  Setup.Setup_AdvSegmentNewLine()
  displayCanvas = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_2.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas
  displayCanvas.Drag(198, 414, 3, -305)
  Setup.Setup_AdvAutoSegment()
  displayCanvas.Click(28, 40)
 
  displayCanvas.Keys("abcd%$#")
  
  Setup.Setup_AdvSegmentNewLine()
  displayCanvas.Drag(27, 28, -5, 106)
  Setup.Setup_AdvAutoSegment()
  displayCanvas.Click(24, 143)
  displayCanvas.Keys("&*><>?/}")
  Setup.Setup_AdvSegmentNewLine()
  displayCanvas.Drag(19, 131, -3, 108)
  Setup.Setup_AdvAutoSegment()
  displayCanvas.Click(20, 246)
  
  displayCanvas.Keys("{|\+@!~`(")

  Setup.Setup_AdvTrainButton()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGTrainPanel.Panel4.ScrollPane.Viewport2.HOG_OCRSetup_OCRSpaceModelTable, "wRowCount", cmpEqual, 3)
 # aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGTrainPanel.Panel4.ScrollPane.Viewport2.HOG_OCRSetup_OCRSpaceModelTable.wValue[2, "A"], "OleValue", cmpEqual, 2)


  Setup.Setup_closeVPM()


