#Author: Ha Le
#The test verify that message "Database needs to be trained" displays after add pattern successfully with Texture

import Setup
def PST_Train_068():
  Setup.Setup_PSTCheck()
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  Setup.Setup_PSTLoadDB("test")

  Setup.Setup_PSTMode("Texture")
  Setup.Setup_PSTAddLabel("train", "testhale")
  Setup.Setup_PSTAddInfo("train", "test[Enter]")
  Setup.Setup_PSTAddButton()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel2.Panel.Panel.TextField, "wText", cmpEqual, "Retrain database to optimize 1 change")
  


  Setup.Setup_PSTDBPanel()
  Setup.Setup_PSTDeletePattern()
  Setup.Setup_PSTRetrainAll("db", None)
  Setup.Setup_closeVPM()

 


  
