#Author: Ha Le
#The test verify user can select the expected location for new created db

import Setup
def PST_Train_015():
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  Setup.Setup_PSTNewDB()

  #Aliases.javaw.Dialog4.RootPane.null_layeredPane.null_contentPane.PatternSortingSetup1_SortingTrainPanel_1_1.ToolBar.ClickItem("Up")
  Setup.Setup_PSTNameDB("test1\\test[Enter]")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel.PatchableStringTextField, "wText", cmpEqual, "test")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel.IntegerLabel3, "text", cmpEqual, "0")
  
  Setup.Setup_PSTDeleteFoder("test1\\test")

  Setup.Setup_closeVPM()


