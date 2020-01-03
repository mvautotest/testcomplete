#Author: Ha Le
#The test verify tooltip of display segment ROI

import Setup
def AdvOCR_Train_028(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_DragAvdToTaskTree()
  Setup.Setup_VPMTrainPanel()

  a = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGTrainPanel.Panel.Panel.Panel.Button.getToolTipText()

  if a == "Click to display the Segmentation Region and start Auto Segmentation mode.":
    Log.Checkpoint(a, "passed")
  else:
    Log.Error(a, "failed")
 
  
  Setup.Setup_closeVPM()
  
