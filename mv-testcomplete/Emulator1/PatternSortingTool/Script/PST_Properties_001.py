#Author: Ha Le
#The test verify database roo directory displays "%INSSTALL_DIR%\Application\Root\PST" as default

import Setup

def PST_Properties_001():
  Setup.Setup_PSTCheck()
  
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  #Setup.VPM_CameraCheck()
  Setup.Setup_VPMNewButton()
  aqTestCase.Begin("Start test ID: PST_Properties_001");
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_VPMPropertiesTab()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[102, "E"], "stringValue_", cmpEqual, "C:\\Datalogic\\IMPACT\\Applications\\Emulator\\EmulatorRoot\\PST\\")
  aqTestCase.End();
  
#PST_Properties_015: Verify user can train successfully without train progress percentage dialog appears during train pattern
  aqTestCase.Begin("Start test ID: PST_Properties_015");
  Setup.Setup_VPMAdvSetupTab()
  Setup.Setup_PSTTrainPanel()
  Setup.Setup_PSTLoadDB("dbnottrain")
  Setup.Setup_VPMPropertiesTab()
  Setup.Setup_PSTTrainProperties()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.ClickCell(7, "A")
  Setup.Setup_PSTTrainProperties()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[23, "E"].wtBase_.wt_, "yearDay", cmpNotEqual, 0)
  aqTestCase.End();
  
#PST_Properties_027: Verify that between PST tool do not upddate each other after user unlink
  aqTestCase.Begin("Start test ID: PST_Properties_027");
  Setup.Setup_DragPatternSortToTaskTree()
  #Setup.Setup_VPMPropertiesTab()
  Setup.Setup_PSTLinkPatternDB()
  Setup.Setup_VPMPropertiesTab()
  Setup.Setup_PSTRunButton()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.ClickCell(7, "D")
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.ClickItem("Root|Image In Task|Pattern Sort 1")
  Setup.Setup_VPMAdvSetupTab()
  Setup.Setup_PSTLoadDBSet("test", "load")
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.ClickItem("Root|Image In Task|Pattern Sort 1")
  Setup.Setup_PSTTrainPanel()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel.PatchableStringTextField, "wText", cmpEqual, "")
  aqTestCase.End();
  
  Setup.Setup_PSTDeleteFoder("PST\\test")
  Setup.Setup_closeVPM()
