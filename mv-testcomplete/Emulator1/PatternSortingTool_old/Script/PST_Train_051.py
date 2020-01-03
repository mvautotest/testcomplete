#Author: Ha Le
#The test verify the performance is increased if values on Advance dialog is heigher

import Setup
def PST_Train_051():
  Setup.Setup_PSTCheck()
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.VPM_CameraCheck()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  Setup.Setup_PSTLoadDB("test")
  Setup.Setup_PSTAdvance("train")
  Setup.Setup_PSTDownSamplingRatio("Edge Match", "[BS]1")
  Setup.Setup_PSTRetrainAll("train", None)
  Setup.Setup_VPMRunOnline("10")
  a = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.SummaryPanel.ScrollPane.Viewport.Summary_Table.wValue[2,  "C"].text
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.SummaryPanel.ScrollPane.Viewport.Summary_Table.wValue[2, "C"], "text", cmpLessOrEqual, "67438")
  
  Setup.Setup_PSTAdvance("train")
  Setup.Setup_PSTDownSamplingRatio("Edge Match", "[BS]7")
  Setup.Setup_PSTRetrainAll("train", None)
  Setup.Setup_VPMResetButton()
  Setup.Setup_VPMRunOnline("10")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.SummaryPanel.ScrollPane.Viewport.Summary_Table.wValue[2, "C"], "text", cmpLess, a)

  Setup.Setup_closeVPM()
