#Author: Ha Le
#The test verify user cannot create DB name with special characters

import Setup
def PST_Train_007():
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  Setup.Setup_PSTNewDBSet("*&test@[Enter]", None)

  aqObject.CheckProperty(Aliases.javaw.Dialog4, "Enabled", cmpEqual, True)
  Setup.Setup_PSTNewDBSet(None, "cancel")


  Setup.Setup_closeVPM()

