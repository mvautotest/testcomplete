#Author: Ha Le
#The test verify error displays if enter invalid chacter to max duplicate point with texture algoritnm

import Setup

def PST_CPM_009():
  Setup.Setup_PSTCheck()
  
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  #Setup.VPM_CameraCheck()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  for i in range(0, 3): 
    Setup.Setup_VPMtriggerOne()
  Setup.Setup_LoadCPM()
  Setup.Setup_PSTCPMDragDropPatternDBToPanel()
  Setup.Setup_EnableRunMode()
  

  Setup.Setup_PSTCPMNewDb("testcpm", "create")
 
  Setup.Setup_PSTCPMAddLabelInfo(True, "test", "test", "Texture", "add")
  Setup.Setup_PSTCPMAdvanceSet("main", "Contour", None, None, None, None, None, None, None, None, None)
  Aliases.javaw.PatternSortDatabase_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane3.Panel.Panel.NumericEntry_24.Keys("[BS][BS][BS]21474836348[Enter]")
  aqObject.CheckProperty(Aliases.javaw.Dialog27, "WndCaption", cmpEqual, "Numeric Entry - Error")
  Aliases.javaw.Dialog27.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
  Setup.Setup_PSTCPMAdvanceSet(None, None, None, None, None, None, None, None, None, None, "ok")
  Setup.Setup_PSTCPMAdvanceSet("main", "Texture", None, None, None, None, None, None, None, None, None)
  Aliases.javaw.PatternSortDatabase_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane3.Panel.Panel.NumericEntry_24.Keys("[BS][BS][BS]-1[Enter]")
  aqObject.CheckProperty(Aliases.javaw.Dialog27, "WndCaption", cmpEqual, "Numeric Entry - Error")
  Aliases.javaw.Dialog27.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
  Setup.Setup_PSTCPMAdvanceSet(None, None, None, None, None, None, None, None, None, None, "ok")
  
  #PST_CPM_010: Verify user can create a pattern with Texture Algorithm
  Setup.Setup_PSTCPMAdvanceSet("main", "Texture", "[BS][BS]1", None, None, None, "[BS][BS][BS][BS]2", "[BS][BS][BS][BS]2", None, None, "ok")
  

  Setup.Setup_PSTCPMRetrainAll()
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SwingObject("JScrollPane", "", 0).SwingObject("JViewport", "", 0).SwingObject("CpmFrame$25", "Panel 1", 0).SwingObject("Panel 1").SwingObject("PatternSortDatabase").SwingObject("PatternFrame").SwingObject("PointsValue"), "text", cmpEqual, "<html>39</html>")
  Setup.Setup_DisableRunMode()
  
  Setup.Setup_closeCPM()
 
  Setup.Setup_closeVPM()
  Setup.Setup_PSTDeleteFoder("PST\\testcpm")

