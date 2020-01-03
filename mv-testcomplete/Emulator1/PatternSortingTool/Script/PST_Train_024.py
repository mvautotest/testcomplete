#Author: Ha Le
#The test verify error message display if info is empty or special chracters
#Note: The tool still allow to add label without information; Scpecial character will be same rule as lable include (<>?[]{}..)

import Setup
def PST_Train_024():
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

  Setup.Setup_PSTAddInfo("train", "@test!?")
 
  Setup.Setup_PSTAddButton()
  aqObject.CheckProperty(Aliases.javaw.Dialog6, "WndCaption", cmpEqual, "Setup Error")

  Aliases.javaw.Dialog6.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
  
  Setup.Setup_closeVPM()


