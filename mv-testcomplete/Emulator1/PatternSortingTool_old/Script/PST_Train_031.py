#Author: Ha Le
#The test verify the trained pattern displays correctly with boundaries of all shapes

import Setup
def PST_Train_031():
  Setup.Setup_PSTCheck()
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  Setup.Setup_PSTNewDB()
  Setup.Setup_PSTNameDB("newdb[Enter]")
  Setup.Setup_PSTResizeROI()
  Setup.Setup_PSTAddROI()
  Setup.Setup_PSTAddButton()
  Setup.Setup_PSTAddLabel("train", "test")
  Setup.Setup_PSTAddInfo("train", "test")
  Setup.Setup_PSTDBPanel()
  
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ScrollPane.Viewport.PatternSortDatabaseViewer_DatabasePanel_.PatternSortDatabaseViewer_PatternModelPanel_2.Label, "Enabled", cmpEqual, True)
  Setup.Setup_PSTDeleteFoder("PST\\newdb")
  
  Setup.Setup_closeVPM()
