#Author: Ha Le
#The test verify error displays if enter invalid chacter to downsample ratio with Edge Match

import Setup

def PST_CPM_016():
  Setup.Setup_PSTCheck()
  
  Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  #Setup.VPM_CameraCheck()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
#  for i in range(0, 3): 
#    Setup.Setup_VPMtriggerOne()
  Setup.Setup_LoadCPM()
  Setup.Setup_PSTCPMDragDropPatternDBToPanel()
  Setup.Setup_EnableRunMode()
  

  Setup.Setup_PSTCPMNewDb("testcpm", "create")
 
  Setup.Setup_PSTCPMAddLabelInfo(True, "test", "test", "Edge Match", "add")
  Delay(1000)
  Setup.Setup_PSTCPMUpdateMode("Edge Match")
  Delay(500)
  Setup.Setup_PSTCPMAdvanceSet("main", "Edge Match", None, None, None, None, None, None, None, None, None)
  Delay(300)
  Aliases.javaw.PatternSortDatabase_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane2.Panel.Panel.NumericEntry_2.Keys("[BS][BS][BS][BS]11[Enter]")
  aqObject.CheckProperty(Aliases.javaw.Dialog27, "WndCaption", cmpEqual, "Numeric Entry - Error")
  Aliases.javaw.Dialog27.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
  Delay(300)
  Aliases.javaw.PatternSortDatabase_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane2.Panel.Panel.NumericEntry_2.Keys("[BS][BS][BS][BS]-1[Enter]")
  aqObject.CheckProperty(Aliases.javaw.Dialog27, "WndCaption", cmpEqual, "Numeric Entry - Error")
  Aliases.javaw.Dialog27.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
  Delay(300)
  Setup.Setup_PSTCPMAdvanceSet(None, None, None, None, None, None, None, None, None, None, "ok")
 
  #PST_CPM_017: verify scale range type contains 3 types in dropdownlist
  Delay(300)
  Setup.Setup_PSTCPMAdvanceSet("main", "Edge Match", None, None, None, None, None, None, None, None, None)
  Delay(300)
  aqObject.CheckProperty(Aliases.javaw.PatternSortDatabase_AdvancedTrainDialog4.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane.Panel.Panel.ComboBox, "wItem[0]", cmpEqual, "No Scaling")
  aqObject.CheckProperty(Aliases.javaw.PatternSortDatabase_AdvancedTrainDialog4.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane.Panel.Panel.ComboBox, "wItemCount", cmpEqual, 3)
  aqObject.CheckProperty(Aliases.javaw.PatternSortDatabase_AdvancedTrainDialog4.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane.Panel.Panel.ComboBox, "wItem[1]", cmpEqual, "Slight Scaling 0.9 - 1.1")
  aqObject.CheckProperty(Aliases.javaw.PatternSortDatabase_AdvancedTrainDialog4.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane.Panel.Panel.ComboBox, "wItem[2]", cmpEqual, "Large Scaling 0.5 - 2.0")
  
  #PST_CPM_018: verify when train edge detecction - sensitivity is fixed, thrshold is enabled
  Aliases.javaw.PatternSortDatabase_AdvancedTrainDialog4.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane.Panel.Panel.Panel.Panel.Panel.PatternSortDatabase_AdvancedTrainDialog_EdgeSensitivitySlider.wPosition = 5
  aqObject.CheckProperty(Aliases.javaw.PatternSortDatabase_AdvancedTrainDialog4.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane.Panel.Panel.Panel.Panel.Panel2.Slider_2, "Enabled", cmpEqual, True)
  Setup.Setup_PSTCPMAdvanceSet(None, None, None, None, None, None, None, None, None, None, "ok")
  Delay(300)
 

  #PST_CPM_020: Verify user can create a pattern with Edge Match Algorithm
  Setup.Setup_PSTCPMAdvanceSet("main", "Edge Match", "[BS][BS]2", None, None, None, None, None, None, None, "ok")
  Delay(300)
  Setup.Setup_PSTCPMRetrainAll("")
  Delay(1000)
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternFrame.PointsValue, "text", cmpEqual, "<html>16</html>")
   

  Setup.Setup_DisableRunMode()
  Setup.Setup_closeCPM()
  Setup.Setup_closeVPM()
  Setup.Setup_PSTDeleteFoder("PST\\testcpm")

