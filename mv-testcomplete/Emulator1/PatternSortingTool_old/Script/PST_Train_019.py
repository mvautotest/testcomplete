#Author: Ha Le
#The test verify error message displays if label is duplicated

import Setup
def PST_Train_019():
  #Setup.Setup_InnitializeCPM()
  Setup.Setup_PSTCheck()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  Setup.Setup_PSTLoadDB("C:\\Datalogic\\IMPACT\\Applications\\Emulator\\EmulatorRoot\\PST\\test\\test.pdb")
  Setup.Setup_PSTAddLabel("train" ,"c[Enter]")

  Setup.Setup_PSTAddButton()
  aqObject.CheckProperty(Aliases.javaw.PatternSortDatabaseViewer_AddImagePromptDialog, "WndCaption", cmpEqual, "Duplicate Pattern Label")
  Aliases.javaw.PatternSortDatabaseViewer_AddImagePromptDialog.RootPane.null_layeredPane.null_contentPane.Panel.Panel.Button.ClickButton()


  Setup.Setup_closeVPM()


