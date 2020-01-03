#Author: Ha Le
#The test verify Mode displays full algorithm which added and trained

import Setup

def PST_CPM_022():
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
  Setup.Setup_PSTCPMLoadDB("acb\\acb.pdb", "load")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.ModesUsedButton, "Enabled", cmpEqual, True)
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternFrame.ModeValue, "wText", cmpEqual, "Edge Match")
  Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternSortDatabaseDisplay.PatternSortDatabaseViewer.Panel.ScrollPane.Viewport.PatternSortDatabaseViewer_DatabasePanel_.PatternSortDatabaseViewer_PatternModelPanel_.Label.Click(33, 59)
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternFrame.ModeValue, "wText", cmpEqual, "Contour")

 #PST_CPM_024: verify the warming message disappear after trained
  Setup.Setup_PSTCPMAddLabelInfo(True, "test", "test", "Edge Match", "add")
  Delay(2000)
  Setup.Setup_PSTCPMRetrainAll("")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.RetrainPrompt, "text", cmpEqual, "")

 #PST_CPM_025: verify the correct algorithm is selected if user select "Edged Match"
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternFrame.ModeValue, "wText", cmpEqual, "Edge Match")

  Setup.Setup_PSTCPMDeletePattern()
  Setup.Setup_PSTCPMRetrainAll("")

  Setup.Setup_DisableRunMode()
  Setup.Setup_closeCPM()
  Setup.Setup_closeVPM()
  Setup.Setup_PSTDeleteFoder("PST\\testcpm")
#  
