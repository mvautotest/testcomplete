#Author: Ha Le
#The test verify user can create a new db by modify name from exited files

import Setup
def PST_Train_013():
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  Setup.Setup_PSTNewDB()
  Aliases.javaw.Dialog4.RootPane.null_layeredPane.null_contentPane.PatternSortingSetup1_SortingTrainPanel_1_1.Panel.FilePane.Panel.ScrollPane.Viewport.FilePane_4.ClickItemXY("testPST", 25, 8)
  Setup.Setup_PSTNameDB("123456[Enter]")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel.PatchableStringTextField, "wText", cmpEqual, "testPST123456")
  
  Setup.Setup_PSTDeleteFoder("PST\\testPST123456")

  Setup.Setup_closeVPM()


