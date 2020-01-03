﻿#Author: Ha Le
#The test verify user can zoom image

import Setup

def PST_CPM_046():
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
  Setup.Setup_PSTCPMZoom("in")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternSortDatabaseDisplay.PatternSortDatabaseViewer.Panel.ScrollPane.Viewport.PatternSortDatabaseViewer_DatabasePanel_.PatternSortDatabaseViewer_PatternModelPanel_2.Label3, "Height", cmpEqual, 121)
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternSortDatabaseDisplay.PatternSortDatabaseViewer.Panel.ScrollPane.Viewport.PatternSortDatabaseViewer_DatabasePanel_.PatternSortDatabaseViewer_PatternModelPanel_2.Label3, "Width", cmpEqual, 93)
  Setup.Setup_PSTCPMZoom("out")
  Setup.Setup_PSTCPMZoom("out")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternSortDatabaseDisplay.PatternSortDatabaseViewer.Panel.ScrollPane.Viewport.PatternSortDatabaseViewer_DatabasePanel_.PatternSortDatabaseViewer_PatternModelPanel_2, "Height", cmpEqual, 72)
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternSortDatabaseDisplay.PatternSortDatabaseViewer.Panel.ScrollPane.Viewport.PatternSortDatabaseViewer_DatabasePanel_.PatternSortDatabaseViewer_PatternModelPanel_2, "Width", cmpEqual, 86)
  Setup.Setup_PSTCPMZoom("100")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternSortDatabaseDisplay.PatternSortDatabaseViewer.Panel.ScrollPane.Viewport.PatternSortDatabaseViewer_DatabasePanel_.PatternSortDatabaseViewer_PatternModelPanel_2, "Height", cmpEqual, 113)
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternSortDatabaseDisplay.PatternSortDatabaseViewer.Panel.ScrollPane.Viewport.PatternSortDatabaseViewer_DatabasePanel_.PatternSortDatabaseViewer_PatternModelPanel_2, "Width", cmpEqual, 86)


  Setup.Setup_DisableRunMode()

  Setup.Setup_closeCPM()
  Setup.Setup_closeVPM()

 
