#Author: Ha Le
#The test verify import database dialog displays when clicking on import icon

import Setup
def PST_Database_0026():
  Setup.Setup_PSTCheck()
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  Setup.Setup_PSTLoadDBSet("test", "load")
  Setup.Setup_PSTResizeROI()
  Setup.Setup_PSTAddButton()
  Setup.Setup_PSTRetrainAll("train", "ok")
  Setup.Setup_PSTDBPanel()
  Setup.Setup_PSTImport("test", "")
  aqObject.CheckProperty(Aliases.javaw.Dialog21, "WndCaption", cmpEqual, "Import Database")
  Setup.Setup_PSTImport(None, "cancel")

  Setup.Setup_closeVPM()

  

