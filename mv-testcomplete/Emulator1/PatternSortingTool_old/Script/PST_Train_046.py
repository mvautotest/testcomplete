#Author: Ha Le
#The test verify run time will be affect according to DownSampling Ratio

import Setup
def PST_Train_046():
  Setup.Setup_PSTCheck()
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  Setup.Setup_PSTNewDB()
  Setup.Setup_PSTNameDB("test12345[Enter]")
  Setup.Setup_PSTAddLabel("train", "test new")
  Setup.Setup_PSTAddInfo("train", "test new 1")
  Setup.Setup_PSTAdvance("train")
  Setup.Setup_PSTDownSamplingRatio("Contour", "[BS]1")
  Setup.Setup_PSTAddButton()
  Setup.Setup_VPMtriggerOne()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.SummaryPanel.ScrollPane.Viewport.Summary_Table.wValue[2, "C"], "text", cmpLessOrEqual, "5000")
  Setup.Setup_PSTAdvance("train")
  Setup.Setup_PSTDownSamplingRatio("Contour", "[BS]5")
  Setup.Setup_VPMtriggerOne()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.SummaryPanel.ScrollPane.Viewport.Summary_Table.wValue[2, "C"], "text", cmpLessOrEqual, "600")
  Setup.Setup_PSTAdvance("train")
  Setup.Setup_PSTDownSamplingRatio("Contour", "[BS]10")
  Setup.Setup_VPMtriggerOne()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.SummaryPanel.ScrollPane.Viewport.Summary_Table.wValue[2, "C"], "text", cmpLessOrEqual, "293")


  Setup.Setup_PSTDeleteFoder("PST\\test12345")

  Setup.Setup_closeVPM()
