#Author: Ha Le
#The test verify tool tip appears when hold mouse on the dropbox

import Setup
def AdvOCR_Train_023(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_DragAvdToTaskTree()
  Setup.Setup_VPMSearchPanel()
  Setup.Setup_DrawROI()
  Setup.Setup_VPMTrainPanel()
  Setup.Setup_AdvSegmentNewLine()
  a = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGTrainPanel.Panel.Panel.Panel.ComboBox.getToolTipText()
  if a == "Specify the type of character you want to segment.":
    Log.Checkpoint(a, "passed")
  else:
    Log.Error(a, "failed")


  Setup.Setup_closeVPM()


