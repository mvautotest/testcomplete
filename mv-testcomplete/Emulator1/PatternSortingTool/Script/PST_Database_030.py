#Author: Ha Le
#The test verify that import patterns are loaded automatically into database panel
# Note: This script will include PST_Database_030, 031, 032, 033
import Setup
def PST_Database_030():
  Setup.Setup_PSTCheck()
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  Setup.Setup_PSTLoadDBSet("test", "load")
  Delay(500)
  Setup.Setup_PSTDBPanel()
 
  Setup.Setup_PSTImport("\\test123.pdpkg[Enter]", "ok")
  if Aliases.javaw.Dialog22.Exists:
    
    Aliases.javaw.Dialog22.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
  else:
    Log.Message("do nothing")   
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ScrollPane.Viewport.PatternSortDatabaseViewer_DatabasePanel_, "ChildCount", cmpEqual, 42) 
  
  #Database_033: Verify advance info of the imported db display correctly
  Setup.Setup_PSTAdvanceSet("db", None, None, None, None, None, None, None, None, None, None)
  aqObject.CheckProperty(Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane.Panel2.Panel.PatchableRealTextField, "wText", cmpEqual, "1")
  aqObject.CheckProperty(Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane.Panel2.Panel.PatchableRealTextField3, "wText", cmpEqual, "5")
  aqObject.CheckProperty(Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane.Panel2.Panel.PatchableRealTextField2, "wText", cmpEqual, "10")
  aqObject.CheckProperty(Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane.Panel2.Panel.PatchableIntegerTextField, "wText", cmpEqual, "1")
  Setup.Setup_PSTAdvanceSet(None, None, None, None, None, None, None, None, None, None, "cancel")
  
  #Database_031: Verify import db name and number of pattern displays correctly
  Setup.Setup_PSTTrainPanel()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel.PatchableStringTextField, "wText", cmpEqual, "test123")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel.IntegerLabel4, "text", cmpEqual, "42")
  
  #Database_032: Verifu import db name displays in "pattern database name"
  Setup.Setup_VPMPropertiesTab()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[11, "E"], "stringValue_", cmpEqual, "test123")
  Setup.Setup_closeVPM()

  

