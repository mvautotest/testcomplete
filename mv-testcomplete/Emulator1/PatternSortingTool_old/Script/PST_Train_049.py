#Author: Ha Le
#The test verify train points are more when max number of keypoint = 0

import Setup
def PST_Train_049():
  Setup.Setup_PSTCheck()
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  for i in range(0, 3):
    Setup.Setup_VPMtriggerOne()
  Setup.Setup_PSTNewDB()
  Setup.Setup_PSTNameDB("test12345[Enter]")
  Setup.Setup_PSTResizeROI()
  Setup.Setup_PSTAddLabel("train", "test new")
  Setup.Setup_PSTAddInfo("train", "test new 1")

  Setup.Setup_PSTAdvance("train")
  Setup.Setup_PSTMaxNumberOfKeypoint("[BS]0")
  Setup.Setup_PSTAddButton()
  Setup.Setup_PSTMode("Contour")
  Setup.Setup_PSTRetrainAll("train", None)
  Setup.Setup_PSTDBPanel()
  Setup.Setup_PSTModeDB("Contour")
  Setup.Setup_PSTRetrainAll("db", None)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.Panel.Panel.Panel.Panel.Label, "text", cmpEqual, "29")
  Setup.Setup_PSTAdvanceSet("db", "Contour", None, None, None, "[BS]5", None, None, None, None, "ok")
#  Setup.Setup_PSTAdvance("db")
#  Setup.Setup_PSTMaxNumberOfKeypoint("5")
  Setup.Setup_PSTRetrainAll("db", None)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.Panel.Panel.Panel.Panel.Label2, "text", cmpEqual, "0")
  Delay(1000)
  Setup.Setup_PSTDeleteFoder("PST\\test12345")
 
  
  Setup.Setup_closeVPM()
