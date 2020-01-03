#Author: Ha Le
#The test verify training points display on the pattern

import Setup

def PST_CPM_047():
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
  Delay(3000)
  Setup.Setup_PSTCPMPoint(True)
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternDisplay.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.roiList_.elementData_2.Items[2], "name_", cmpEqual, "PolypointROI")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternDisplay.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.roiList_.elementData_2.Items[2], "visible_", cmpEqual, True)

  Setup.Setup_DisableRunMode()

  Setup.Setup_closeCPM()
  Setup.Setup_closeVPM()

 
