#Author: Ha Le
#The test verify a new db is created with pattern is allway zero

import Setup
def PST_Train_044():
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
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel.IntegerLabel3, "text", cmpEqual, "0")
  Setup.Setup_PSTDeleteFoder("PST\\test12345")


  Setup.Setup_closeVPM()
