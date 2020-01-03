#Author: Ha Le
#The test verify a drop down list appears for exitsing labels that match the typed string when typing at label field

import Setup
def PST_Train_021():
  Setup.Setup_PSTCheck()
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  Setup.Setup_PSTLoadDB("test")
  Setup.Setup_PSTAddLabel("train", "c")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.Panel.ComboPopup_popup.ComboBox_scrollPane.Viewport.ComboBox_list, "wItemCount", cmpEqual, 1)
  Setup.Setup_PSTAddLabel("train", "[Enter]")
  Setup.Setup_closeVPM()


