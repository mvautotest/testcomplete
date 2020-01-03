#Author: Ha Le
#The test verify that error dialog appears if create duplicate db name

import Setup
def PST_Train_014():
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  Setup.Setup_PSTNewDBSet("test", "create")
  #Setup.Setup_PSTNameDB("test[Enter]")
  
  aqObject.CheckProperty(Aliases.javaw.Dialog5, "WndCaption", cmpEqual, "Error")
  Aliases.javaw.Dialog5.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
  Aliases.javaw.Dialog4.RootPane.null_layeredPane.null_contentPane.PatternSortingSetup1_SortingTrainPanel_1_1.Panel.Panel.Panel2.WindowsFileChooserUI_10.ClickButton()

  Setup.Setup_closeVPM()


