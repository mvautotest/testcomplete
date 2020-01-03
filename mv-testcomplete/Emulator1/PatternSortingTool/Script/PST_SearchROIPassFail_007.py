﻿#Author: Ha Le
#The test verify actual value appear under deyect pattern correct on each image

import Setup

def PST_SearchROIPassFail_007():
  Setup.Setup_PSTCheck()
  
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.VPM_CameraCheck()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  aqTestCase.Begin("Start test ID: PST_SearchROIPassFail_007");
  Setup.Setup_PSTLoadDBSet("test", "load")
  Setup.Setup_PSTPassFailPanel()
  Setup.Setup_VPMtriggerOne()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingPassFailPanel.Panel2.Panel2.Panel.Panel.Label, "text", cmpEqual, "1")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingPassFailPanel.Panel2.Panel2.Panel.Panel.IntegerLabel, "text", cmpEqual, "1")
  panel = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingPassFailPanel.Panel2.Panel2.Panel.Panel
  panel.CheckBox.ClickButton(True)
  panel.CheckBox2.ClickButton(True)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingPassFailPanel.Panel2.Panel2.Panel.Panel.IntegerLabel2, "text", cmpEqual, "26")
  aqTestCase.End();
  
  
  
#SearchROIPassFail_010: Verify all info display correctly when run Online  
  aqTestCase.Begin("Start test ID: PST_SearchROIPassFail_010");
  Setup.Setup_PSTMatchScore(True, "[BS][BS]90")
  Setup.Setup_VPMRunOnline("16")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingPassFailPanel.Panel.Panel.PassFailLabel2, "text", cmpEqual, "Failed")
  aqTestCase.End();

#SearchROIPassFail_012: Verify that indepent Match Score is enabled when match score and enable failed match are selected
  aqTestCase.Begin("Start test ID: PST_SearchROIPassFail_012");
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingPassFailPanel.Panel.Panel.PassFailLabel, "text", cmpEqual, "Passed")
  #aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingPassFailPanel.Panel2.Panel.Panel.CheckBox, "Enabled", cmpEqual, False)
  Setup.Setup_PSTEnableFailedMatch(True)
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.PatternSortingSetup1_PatternSortingSetupPanel_1.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.Click(185, 130)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingPassFailPanel.Panel2.Panel.Panel.CheckBox, "Enabled", cmpEqual, True)
  aqTestCase.End(); 

#SearchROIPassFail_013: Verify that indepent Match Score value is enabled when indpendent match score is selected
  aqTestCase.Begin("Start test ID: PST_SearchROIPassFail_013");
  Setup.Setup_PSTIndependentMatchScore(True, None)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingPassFailPanel.Panel2.Panel.Panel.Label7, "text", cmpEqual, "82")
  #aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingPassFailPanel.Panel2.Panel.Panel.Label6, "text", cmpEqual, "78")
  #aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingPassFailPanel.Panel2.Panel.Panel.Label6, "Enabled", cmpEqual, True)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingPassFailPanel.Panel2.Panel.Panel.Label7, "Enabled", cmpEqual, True)
  aqTestCase.End(); 
  
#SearchROIPassFail_0014: Verify input independent match score value is saved to the selected patterns
  aqTestCase.Begin("Start test ID: PST_SearchROIPassFail_014");
  Setup.Setup_PSTIndependentMatchScore(True, "[BS][BS]50")
  Setup.Setup_VPMRunOnceCurrent()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingPassFailPanel.Panel.Panel.PassFailLabel, "text", cmpEqual, "Passed")
  aqTestCase.End(); 
  
#SearchROIPassFail_0015: Verify SHA1 hash of the selected pattern is written to Uid list of pattern with independent match score and independent match score value is written to independent minimum match score list after input value an press enter key
#Note: Uid List of Patterns with Independent Mini-mum Match Score: not use; Independent Minimum Match Score List: Not Used (The Independent Minimum Match Score is a sub-property of the Train Pattern property.)
  aqTestCase.Begin("Start test ID: PST_SearchROIPassFail_015");
  Setup.Setup_VPMPropertiesTab()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.ClickCell(7, "A")
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.ClickCell(25, "A")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[26, "E"], "stringValue_", cmpEqual, "09f61f60eaa57b14a5cb362162d607c11396823a")
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.ClickCell(43, "A")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[56, "E"], "value_", cmpEqual, 50)
  aqTestCase.End();
  
#SearchROIPassFail_0016: Verify the input value on Uid list of pattern with independent match score and independent match score are removeed when user unselected on independent match score
  aqTestCase.Begin("Start test ID: PST_SearchROIPassFail_016");
  Setup.Setup_VPMAdvSetupTab()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.PatternSortingSetup1_PatternSortingSetupPanel_1.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.Click(185, 130)
  
  Setup.Setup_PSTIndependentMatchScore(False, None)
  Setup.Setup_VPMPropertiesTab()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[56, "E"], "value_", cmpEqual, 0)
  aqTestCase.End();

  Setup.Setup_closeVPM()

  

