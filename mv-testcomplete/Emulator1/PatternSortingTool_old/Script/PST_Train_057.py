#Author: Ha Le
#The test verify label, info and mode will appear correctly after train

import Setup
def PST_Train_057():
  Setup.Setup_PSTCheck()
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  Setup.Setup_PSTLoadDB("test")

  Setup.Setup_PSTMode("Contour")
  Setup.Setup_PSTAddLabel("train", "testhale")
  Setup.Setup_PSTAddInfo("train", "test[Enter]")

  Setup.Setup_PSTAdvanceSet("train", "Contour", "[BS]1", "[BS]1", "[BS]3", "[BS]7", None, None, None, None, "ok")
  Setup.Setup_PSTAddButton()
  Delay(500)
  Setup.Setup_PSTRetrainAll("train", None)
  Setup.Setup_PSTDBPanel()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.Panel.Panel.Panel.PatternSortModelDropdown2.BasicComboBoxEditor_BorderlessTextField, "wText", cmpEqual, "testhale")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.Panel.Panel.Panel.PatternSortModelDropdown.BasicComboBoxEditor_BorderlessTextField, "wText", cmpEqual, "test")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.Panel.Panel.Panel.ComboBox, "wText", cmpEqual, "Contour")
  Setup.Setup_PSTDeletePattern()
  Delay(500)
  Setup.Setup_PSTRetrainAll("db", None)

  Setup.Setup_closeVPM()
