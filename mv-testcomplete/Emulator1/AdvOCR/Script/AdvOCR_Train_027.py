#Author: Ha Le
#The test verify tooltip of auto segment button

import Setup
def AdvOCR_Train_027(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_DragAvdToTaskTree()
  Setup.Setup_VPMTrainPanel()
  Setup.Setup_AdvSegmentNewLine()
  Setup.Setup_AdvAutoSegment()
  a = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGTrainPanel.Panel.Panel.Panel.Button2.getToolTipText()

  if a == "Click to segment the characters within the Segmentation Region into boxes.":
    Log.Checkpoint(a, "passed")
  else:
    Log.Error(a, "failed")
 
#Train_028: verify tooltip of display segment ROI
  b = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGTrainPanel.Panel.Panel.Panel.Button.getToolTipText()

  if b == "Click to display the Segmentation Region and start Auto Segmentation mode.":
    Log.Checkpoint(b, "passed")
  else:
    Log.Error(b, "failed")  
  Setup.Setup_closeVPM()
  
