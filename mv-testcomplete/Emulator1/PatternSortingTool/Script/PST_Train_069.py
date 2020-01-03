#Author: Ha Le
#The test verify that user can cancel during training without error with Texture

import Setup
def PST_Train_069():
  Setup.Setup_PSTCheck()
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  Setup.Setup_PSTLoadDB("test")

  Setup.Setup_PSTMode("Texture")
  Setup.Setup_PSTAddLabel("train", "testhale")
  Setup.Setup_PSTAddInfo("train", "test")
  Setup.Setup_PSTAddButton()
  #Setup.Setup_PSTAdvanceSet("train", "Texture", "[BS]1", "[BS]1", "[BS]3", "[BS]7", None, None, None, None, "ok")
  Delay(500)
  Setup.Setup_PSTRetrainAll("train", "cancel")
 
  Aliases.javaw.Dialog6.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
  Setup.Setup_PSTDBPanel()
  Setup.Setup_PSTDeletePattern()
  Setup.Setup_PSTRetrainAll("db", None)

  Setup.Setup_closeVPM()

 


  
