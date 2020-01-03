#Author: Ha Le
#The test verify error displays if enter invalid chacter to downsample ratio with Contour algoritnm

import Setup

def PST_CPM_011():
  Setup.Setup_PSTCheck()
  
  Setup.Setup_InnitializeCPM()

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
  Delay(500)
  Setup.Setup_PSTCPMAddLabelInfo(True, "test", "test", "Contour", "add")
  Delay(500)
  Setup.Setup_PSTCPMUpdateMode("Contour")
  Delay(500)
  Setup.Setup_PSTCPMAdvanceSet("main", "Contour", None, None, None, None, None, None, None, None, None)
  Delay(300)
  Aliases.javaw.PatternSortDatabase_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane.Panel.Panel.NumericEntry_2.Keys("[BS][BS][BS][BS]11[Enter]")
  aqObject.CheckProperty(Aliases.javaw.Dialog27, "WndCaption", cmpEqual, "Numeric Entry - Error")
  Aliases.javaw.Dialog27.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
  Delay(300)
  Aliases.javaw.PatternSortDatabase_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane.Panel.Panel.NumericEntry_2.Keys("[BS][BS][BS][BS]-1[Enter]")
  aqObject.CheckProperty(Aliases.javaw.Dialog27, "WndCaption", cmpEqual, "Numeric Entry - Error")
  Aliases.javaw.Dialog27.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
  Setup.Setup_PSTCPMAdvanceSet(None, None, None, None, None, None, None, None, None, None, "ok")
  Delay(300)  
  #PST_CPM_012: verify error displays if enter invalid chacter to number of Scale level
  
  Setup.Setup_PSTCPMAdvanceSet("main", "Contour", None, None, None, None, None, None, None, None, None)
  Delay(300)
  Aliases.javaw.PatternSortDatabase_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane.Panel.Panel.NumericEntry_22.Keys("[BS][BS][BS]8[Enter]")
  aqObject.CheckProperty(Aliases.javaw.Dialog27, "WndCaption", cmpEqual, "Numeric Entry - Error")
  Aliases.javaw.Dialog27.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
  Delay(300)
  Aliases.javaw.PatternSortDatabase_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane.Panel.Panel.NumericEntry_22.Keys("[BS][BS][BS]-1[Enter]")
  aqObject.CheckProperty(Aliases.javaw.Dialog27, "WndCaption", cmpEqual, "Numeric Entry - Error")
  Aliases.javaw.Dialog27.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
  Setup.Setup_PSTCPMAdvanceSet(None, None, None, None, None, None, None, None, None, None, "ok")
  Delay(300)
  #PST_CPM_013: verify error displays if enter invalid chacter to number of Clusters Per Keypoint
  Setup.Setup_PSTCPMAdvanceSet("main", "Contour", None, None, None, None, None, None, None, None, None)
  Delay(300)
  Aliases.javaw.PatternSortDatabase_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane.Panel.Panel.NumericEntry_23.Keys("[BS][BS][BS]5[Enter]")
  aqObject.CheckProperty(Aliases.javaw.Dialog27, "WndCaption", cmpEqual, "Numeric Entry - Error")
  Aliases.javaw.Dialog27.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
  Delay(300)
  Aliases.javaw.PatternSortDatabase_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane.Panel.Panel.NumericEntry_23.Keys("[BS][BS][BS]1[Enter]")
  aqObject.CheckProperty(Aliases.javaw.Dialog27, "WndCaption", cmpEqual, "Numeric Entry - Error")
  Aliases.javaw.Dialog27.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
  Setup.Setup_PSTCPMAdvanceSet(None, None, None, None, None, None, None, None, None, None, "ok")
  Delay(300)  
  #PST_CPM_014: verify error displays if enter invalid chacter to number of Max Number of Keypoint
  Setup.Setup_PSTCPMAdvanceSet("main", "Contour", None, None, None, None, None, None, None, None, None)
  Delay(300)
  Aliases.javaw.PatternSortDatabase_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane.Panel.Panel.NumericEntry_24.Keys("[BS][BS][BS]21474836348[Enter]")
  aqObject.CheckProperty(Aliases.javaw.Dialog27, "WndCaption", cmpEqual, "Numeric Entry - Error")
  Aliases.javaw.Dialog27.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
  Delay(300)
  Aliases.javaw.PatternSortDatabase_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane.Panel.Panel.NumericEntry_24.Keys("[BS][BS][BS]-1[Enter]")
  aqObject.CheckProperty(Aliases.javaw.Dialog27, "WndCaption", cmpEqual, "Numeric Entry - Error")
  Aliases.javaw.Dialog27.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
  Setup.Setup_PSTCPMAdvanceSet(None, None, None, None, None, None, None, None, None, None, "ok")
  Delay(300)  
  #PST_CPM_015: verify user can create a pattern with contour algorithm
  Setup.Setup_PSTCPMAdvanceSet("main", "Contour", "[BS][BS][BS][BS][BS]1", "[BS][BS][BS][BS]2", "[BS][BS][BS]4", "[BS]0", None, None, None, None, "ok")
  Delay(500)
  Setup.Setup_PSTCPMRetrainAll("")
  Delay(1000)
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternFrame.PointsValue, "text", cmpEqual, "<html>540</html>")
  

  Setup.Setup_DisableRunMode()
  Setup.Setup_closeCPM()
  Setup.Setup_closeVPM()
  Setup.Setup_PSTDeleteFoder("PST\\testcpm")
