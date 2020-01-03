#Author: Ha Le
#The test verify that a default folder display on new pattern database dialog when clicking on new button

import Setup
def PST_Train_012():
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  Setup.Setup_PSTNewDBSet("new", None)
  aqObject.CheckProperty(Aliases.javaw.Dialog4.RootPane.null_layeredPane.null_contentPane.PatternSortingSetup1_SortingTrainPanel_1_1.ToolBar.WindowsFileChooserUI_2, "wText", cmpEqual, "PST")
  Setup.Setup_PSTNewDBSet(None, "cancel")
  Setup.Setup_closeVPM()


