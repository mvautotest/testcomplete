#Author: Ha Le
#The test verify user can delete all patterns by delete all button

import Setup

def PST_CPM_041():
  Setup.Setup_PSTCheck()
  
  Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  #Setup.VPM_CameraCheck()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()

  Setup.Setup_LoadCPM()
  Setup.Setup_PSTCPMDragDropPatternDBToPanel()
  Setup.Setup_EnableRunMode()
  Setup.Setup_PSTCPMLoadDB("test\\test.pdb", "load")
  Delay(1000)
  Setup.Setup_PSTCPMDeleteall()
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternValue, "text", cmpEqual, "<html>0</html>")
  Setup.Setup_DisableRunMode()
  Setup.Setup_PSTDeleteFoder("PST\\test")
  Setup.Setup_closeCPM()
  Setup.Setup_closeVPM()

 
