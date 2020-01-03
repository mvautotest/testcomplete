#Author: Ha Le
#The test verify user can sort pattens correctly

import Setup

def PST_CPM_045():
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
 
  Setup.Setup_PSTCPMSort("Label Descending")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternSortDatabaseDisplay.PatternSortDatabaseViewer.Panel.ScrollPane.Viewport.PatternSortDatabaseViewer_DatabasePanel_.PatternSortDatabaseViewer_PatternModelPanel_2.Label, "text", cmpEqual, "Sample Pattern Sort - 05 Pass")
  Setup.Setup_PSTCPMSort("Date Descending")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternSortDatabaseDisplay.PatternSortDatabaseViewer.Panel.ScrollPane.Viewport.PatternSortDatabaseViewer_DatabasePanel_.PatternSortDatabaseViewer_PatternModelPanel_3.Label, "text", cmpEqual, "b")
  Setup.Setup_PSTCPMSort("Date Ascending")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternSortDatabaseDisplay.PatternSortDatabaseViewer.Panel.ScrollPane.Viewport.PatternSortDatabaseViewer_DatabasePanel_.PatternSortDatabaseViewer_PatternModelPanel_3.Label2, "text", cmpEqual, "c")
  Setup.Setup_PSTCPMSort("Label Ascending")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternSortDatabaseDisplay.PatternSortDatabaseViewer.Panel.ScrollPane.Viewport.PatternSortDatabaseViewer_DatabasePanel_.PatternSortDatabaseViewer_PatternModelPanel_2.Label2, "text", cmpEqual, "b")
  

  Setup.Setup_DisableRunMode()

  Setup.Setup_closeCPM()
  Setup.Setup_closeVPM()

 
