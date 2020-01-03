#Author: Ha Le
#The test verify algorithm is not assigned if it is not trained

import Setup

def PST_CPM_021():
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
  

  Setup.Setup_PSTCPMNewDb("testcpm", "create")
 
  Setup.Setup_PSTCPMAddLabelInfo(True, "test", "test", "Auto-Selected", "add")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.ModesUsedButton, "Enabled", cmpEqual, False)

 #PST_CPM_017: verify the correct algorithm is assigned when mode is Auto-Selected
  Setup.Setup_PSTCPMRetrainAll("")
  Delay(1000)
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.ModesUsedButton, "Enabled", cmpEqual, True)

  Setup.Setup_DisableRunMode()
  Setup.Setup_closeCPM()
  Setup.Setup_closeVPM()
  Setup.Setup_PSTDeleteFoder("PST\\testcpm")

