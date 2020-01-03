#Author: Ha Le
#The test verify user can broswer to another place on the load pattern database dialog

import Setup
def PST_Train_095():
  Setup.Setup_PSTCheck()
  #Setup.Setup_InnitializeCPM()
  
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  Setup.Setup_PSTLoadDBSet(None, None)
  Aliases.javaw.Dialog3.RootPane.null_layeredPane.null_contentPane.PatternSortingSetup1_SortingTrainPanel_2_1.ToolBar.ClickItem("Up")
  aqObject.CheckProperty(Aliases.javaw.Dialog3, "WndCaption", cmpEqual, "Load Pattern Database")
  Setup.Setup_PSTLoadDBSet("", "cancel")

  Setup.Setup_closeVPM()


