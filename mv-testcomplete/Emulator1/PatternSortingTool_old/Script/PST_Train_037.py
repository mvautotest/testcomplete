#Author: Ha Le
#The test verify tooltip displays correctly on Mode used button

import Setup
def PST_Train_037():
  Setup.Setup_PSTCheck()
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  Setup.Setup_PSTLoadDB("test")
 

  a =  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel.Button3.getToolTipText()
  if a == "Press to view all pattern modes used in loaded database.":
    Log.Checkpoint("Pass", a)
  else:
    Log.Error("Fail", a)
  

  Setup.Setup_closeVPM()
