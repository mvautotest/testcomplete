#Author: Ha Le
#The test verify user can check pattern correctly

import Setup

def PST_CPM_051():
  Setup.Setup_PSTCheck()
  
  Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.VPM_CameraCheck()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  
  Setup.Setup_LoadCPM()
  Setup.Setup_PSTCPMDragDropPatternDBToPanel()
  Setup.Setup_EnableRunMode()
  Setup.Setup_PSTCPMLoadDB("test\\test.pdb", "load")
  
  Setup.Setup_VPMOnlineButtonEnable()
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SwingObject("JScrollPane", "", 0).SwingObject("JViewport", "", 0).SwingObject("CpmFrame$25", "Panel 1", 0).SwingObject("Panel 1").SwingObject("Pattern Database2"), "Exists", cmpEqual, True)
  Setup.Setup_DisableRunMode()
  Setup.Setup_VPMOnlineButtonDisable()
  Setup.Setup_closeCPM()
  Setup.Setup_closeVPM()

 
