#Author: Ha Le
#The test verify user can hide the existed label by click the left mouse button on an item or clicking "Escape" key or backpacing in the text entry until no match are found

import Setup
def PST_Train_023():
  Setup.Setup_PSTCheck()
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  Setup.Setup_PSTLoadDB("test")
  Setup.Setup_PSTAddLabel("train", "s [Down][Enter]")

  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel2.Panel.PatternSortModelDropdown.BasicComboBoxEditor_BorderlessTextField, "wText", cmpEqual, "s ")
  Setup.Setup_PSTAddLabel("train", "[BS][Esc][Down][Enter]")

  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel2.Panel.PatternSortModelDropdown.BasicComboBoxEditor_BorderlessTextField, "wText", cmpEqual, "s")

  Setup.Setup_closeVPM()


