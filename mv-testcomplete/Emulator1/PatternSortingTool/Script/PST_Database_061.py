#Author: Ha Le
#The test verify a menu list will popup allowing the user to select sort the patterns by name or creation date

import Setup
def PST_Database_061():
  Setup.Setup_PSTCheck()
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  aqTestCase.Begin("Start test ID: PST_Database_061");
  Setup.Setup_PSTLoadDBSet("test", "load")
  Setup.Setup_PSTDBPanel()
  Setup.Setup_PSTSort()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.Panel.PopupMenu, "Enabled", cmpEqual, True)
  aqTestCase.End()
  
  #Database_063: verify patterns are sorted by ascending correctly via label
  aqTestCase.Begin("Start test ID: PST_Database_063");
  Aliases.javaw.VpmFrame.SwingPopupMenu.Click("Label Ascending")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ScrollPane.Viewport.PatternSortDatabaseViewer_DatabasePanel_.PatternSortDatabaseViewer_PatternModelPanel_2.Label2, "text", cmpEqual, "b")
  aqTestCase.End()
  
  #Database_064: verify patterns are sorted by decending correctly via label
  aqTestCase.Begin("Start test ID: PST_Database_064");
  Setup.Setup_PSTSort()
  Aliases.javaw.VpmFrame.SwingPopupMenu.Click("Label Descending")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ScrollPane.Viewport.PatternSortDatabaseViewer_DatabasePanel_.PatternSortDatabaseViewer_PatternModelPanel_2.Label3, "text", cmpEqual, "Sample Pattern Sort - 05 Pass")
  aqTestCase.End()
  
  #Database_065: verify patterns are sorted by decending correctly via creation time
  aqTestCase.Begin("Start test ID: PST_Database_065");
  Setup.Setup_PSTSort()
  Aliases.javaw.VpmFrame.SwingPopupMenu.Click("Date Descending")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ScrollPane.Viewport.PatternSortDatabaseViewer_DatabasePanel_.PatternSortDatabaseViewer_PatternModelPanel_2.Label4, "text", cmpEqual, "Sample Pattern Sort - 01 Fail")
  aqTestCase.End()
  
  #Database_066: verify patterns are sorted by Ascending correctly via creation time
  aqTestCase.Begin("Start test ID: PST_Database_066");
  Setup.Setup_PSTSort()
  Aliases.javaw.VpmFrame.SwingPopupMenu.Click("Date Ascending")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ScrollPane.Viewport.PatternSortDatabaseViewer_DatabasePanel_.PatternSortDatabaseViewer_PatternModelPanel_2.Label3, "text", cmpEqual, "Sample Pattern Sort - 05 Pass")
  aqTestCase.End()
 
  
  Setup.Setup_closeVPM()

  

