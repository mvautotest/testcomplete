#Author: Ha Le
#The test verify that load pattern database dialog appear when clicking on load button

import Setup
def PST_Train_094():
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  Setup.Setup_PSTLoadDBSet(None, None)
  aqObject.CheckProperty(Aliases.javaw.Dialog3, "WndCaption", cmpEqual, "Load Pattern Database")
  Setup.Setup_PSTLoadDBSet("", "cancel")
  Setup.Setup_closeVPM()
