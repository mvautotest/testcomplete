#Author: Ha Le
#The test verify the point is increased when "Train Unsample Image" = True

import Setup
def PST_Train_065():
  Setup.Setup_PSTCheck()
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  Setup.Setup_PSTLoadDB("test")
  Setup.Setup_PSTResizeROI()
  for i in range(0, 3):
    Setup.Setup_VPMtriggerOne()
  Setup.Setup_PSTMode("Texture")
  Setup.Setup_PSTAddLabel("train", "testhale")
  Setup.Setup_PSTAddInfo("train", "test[Enter]")
  Setup.Setup_PSTAddButton()
  Setup.Setup_PSTAdvanceSet("train", "Texture", None, None, None, None, None, None, True, None, "ok")
  Setup.Setup_PSTRetrainAll("train", None)
  Setup.Setup_PSTDBPanel()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ToolBar.Panel.ToggleButton.ClickButton(True)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.Panel.Panel.Panel.Panel.Label6, "text", cmpEqual, "269")
  Setup.Setup_PSTAdvanceSet("db", "Texture", None, None, None, None, None, None, False, None, "ok")
  
  Setup.Setup_PSTRetrainAll("db", None)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.Panel.Panel.Panel.Panel.Label6, "text", cmpEqual, "9")
  #Setup.Setup_PSTDeleteFoder("PST\\test")
  Setup.Setup_PSTDeletePattern()
  Setup.Setup_PSTRetrainAll("db", None)
  Setup.Setup_closeVPM()


  
