#Author: Ha Le
#The test verify error displays if enter invalid chacter to max dip with texture algoritnm

import Setup

def PST_CPM_008():
  Setup.Setup_PSTCheck()
  
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  #Setup.VPM_CameraCheck()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_LoadCPM()
  Setup.Setup_PSTCPMDragDropPatternDBToPanel()
  Setup.Setup_EnableRunMode()
  

  Setup.Setup_PSTCPMNewDb("testcpm", "create")
 
  Setup.Setup_PSTCPMAddLabelInfo(True, "test", "test", "Texture", "add")
  Setup.Setup_PSTCPMAdvanceSet("main", "Texture", None, None, None, None, None, None, None, None, None)


  Aliases.javaw.PatternSortDatabase_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane3.Panel.Panel.NumericEntry_22.Keys("[BS][BS][BS]101[Enter]")


  aqObject.CheckProperty(Aliases.javaw.Dialog27, "WndCaption", cmpEqual, "Numeric Entry - Error")
  Aliases.javaw.Dialog27.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
  Setup.Setup_PSTCPMAdvanceSet(None, None, None, None, None, None, None, None, None, None, "ok")
  Setup.Setup_DisableRunMode()
  
  Setup.Setup_closeCPM()
 
  Setup.Setup_closeVPM()
  Setup.Setup_PSTDeleteFoder("PST\\testcpm")

