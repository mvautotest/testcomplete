#Author: Ha Le
#The test verify the drop list appears for the existing infor that match the tyoed string when typing at infor field

import Setup
def PST_Train_025():
  Setup.Setup_PSTCheck()
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  Setup.Setup_PSTLoadDB("test")
  Setup.Setup_PSTAddLabel("train", "s")

  Setup.Setup_PSTAddInfo("train", "s")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.Panel.ComboPopup_popup.ComboBox_scrollPane.Viewport.ComboBox_list, "wItemCount", cmpEqual, 2)
 
  Setup.Setup_PSTAddInfo("train", "[BS]")
  Setup.Setup_closeVPM()


