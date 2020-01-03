#Author: Ha Le
#The test verify user can cancel druing training without error with Edge Match
#Note: there is an error setup message to notify if user click cancel sucessfully

import Setup
def PST_Train_085():
  Setup.Setup_PSTCheck()
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  Setup.Setup_PSTLoadDB("test")

  Setup.Setup_PSTMode("Edge Match")
  Setup.Setup_PSTAddLabel("train", "testhale")
  Setup.Setup_PSTAddInfo("train", "test")
  Setup.Setup_PSTAddButton()
  Setup.Setup_PSTAdvanceSet("train", "Edge Match", "[BS]1", None, None, None, None, None, None, None, "ok")
  Delay(500)
  Setup.Setup_PSTRetrainAll("train", "cancel")
 
  Aliases.javaw.Dialog6.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
  Setup.Setup_PSTDBPanel()
  Setup.Setup_PSTDeletePattern()
  Setup.Setup_PSTRetrainAll("db", None)

  Setup.Setup_closeVPM()
