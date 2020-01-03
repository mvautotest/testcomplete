#Author: Ha Le
#The test verify error dialog appear if user delete any tool in group

import Setup

def PST_CPM_050():
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
#  Setup.Setup_CPMExpandItem("|[0]|Panel 1|Pattern Database2")
  Setup.Setup_CPMDeleteItem("|[0]|Panel 1|Pattern Database2|Pattern Database Viewer")
  aqObject.CheckProperty(Aliases.javaw.Dialog5, "WndCaption", cmpEqual, "Error")
  Aliases.javaw.Dialog5.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.Keys("[Enter]")
  Setup.Setup_closeCPM()
  Setup.Setup_closeVPM()

 
