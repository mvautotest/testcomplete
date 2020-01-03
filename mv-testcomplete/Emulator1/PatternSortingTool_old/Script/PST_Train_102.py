#Author: Ha Le
#The test verify training processing works properly

import Setup
def PST_Train_102():
  Setup.Setup_PSTCheck()
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()

  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  Setup.Setup_PSTLoadDBSet("BigDbhalf", "load")
  Delay(9000)
  Setup.Setup_PSTResizeROI()
  Setup.Setup_PSTMode("Texture")
  Delay(10000)
  Setup.Setup_PSTAddButton()

  Setup.Setup_PSTRetrainAll("train", "ok")
  Delay(90000)
  Setup.Setup_PSTDBPanel()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.Panel.Panel.Panel.PatternSortModelDropdown2.BasicComboBoxEditor_BorderlessTextField, "wText", cmpEqual, "Sample Pattern Sort - 01 Fail")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.Panel.Panel.Panel.PatternSortModelDropdown.BasicComboBoxEditor_BorderlessTextField, "wText", cmpEqual, "Sample Pattern Sort - 01 Fail")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ScrollPane.Viewport.PatternSortDatabaseViewer_DatabasePanel_, "ChildCount", cmpEqual, 187)
  Setup.Setup_PSTDeletePattern()
  Delay(5000)
  Setup.Setup_PSTRetrainAll("db", "ok")
#  Delay(90000)
#  Setup.Setup_PSTTrainPanel()
#  Setup.Setup_PSTNewDBSet("imagetest", "create")
#  Setup.Setup_PSTDBPanel()
#  Setup.Setup_PSTAddPatternImage("Image004.JPG")
#  Setup.Setup_PSTAddPatternImage("Image005.BMP")
#  Delay(5000)
#  Setup.Setup_PSTRetrainAll("db", "ok")
#  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ScrollPane.Viewport.PatternSortDatabaseViewer_DatabasePanel_, "ChildCount", cmpEqual, 2)
#  Setup.Setup_PSTDeleteFoder("PST\\imagetest")
  Delay(5000)
  Setup.Setup_closeVPM()

