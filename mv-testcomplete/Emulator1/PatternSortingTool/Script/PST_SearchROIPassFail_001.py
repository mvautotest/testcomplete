#Author: Ha Le
#The test verify the selected pattern's name and number of matched points are displayed at filters area when click on ROI

import Setup

def PST_SearchROIPassFail_001():
  Setup.Setup_PSTCheck()
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  aqTestCase.Begin("Start test ID: " + PST_SearchROIPassFail_001);
  Setup.Setup_PSTTrainPanel()
  Setup.Setup_PSTLoadDBSet("test", "load")
  Setup.Setup_PSTPassFailPanel()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingPassFailPanel.Panel2.Panel.Panel.Panel.TextField, "wText", cmpEqual, "Sample Pattern Sort - 01 Fail")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingPassFailPanel.Panel.Panel.PassFailLabel, "text", cmpEqual, "Passed")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingPassFailPanel.Panel2.Panel.Panel.Label, "text", cmpEqual, "11")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingPassFailPanel.Panel2.Panel.Panel.Label2, "text", cmpEqual, "89")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingPassFailPanel.Panel2.Panel.Panel.PatchableRealTextField, "wText", cmpEqual, "50")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingPassFailPanel.Panel2.Panel.Panel.Label3, "text", cmpEqual, "89")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingPassFailPanel.Panel2.Panel.Panel.Label4, "text", cmpEqual, "89")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingPassFailPanel.Panel2.Panel.Panel.Label5, "text", cmpEqual, "89")
  aqTestCase.End(); 
  
  #SearchROIPassFail_002: Verify result return correctly when match score is enabled
  aqTestCase.Begin("Start test ID: " + PST_SearchROIPassFail_002);
  Setup.Setup_PSTMatchScore(True, "[BS][BS]90")
  Setup.Setup_VPMRunOnceCurrent()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingPassFailPanel.Panel.Panel.PassFailLabel, "text", cmpEqual, "Failed")
  Setup.Setup_PSTMatchScore(False, None)
  Delay(900)
  aqTestCase.End(); 
  
  #SearchROIPassFail_003: Verify result return correctly when match Fraction is enabled
  aqTestCase.Begin("Start test ID: " + PST_SearchROIPassFail_003);
  Setup.Setup_PSTMatchFraction(True, "[BS][BS]90")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingPassFailPanel.Panel.Panel.PassFailLabel, "text", cmpEqual, "Passed")
  Setup.Setup_VPMRunOnceCurrent()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingPassFailPanel.Panel.Panel.PassFailLabel, "text", cmpEqual, "Failed")
  Setup.Setup_PSTMatchFraction(False, None)
  aqTestCase.End(); 
  
  #SearchROIPassFail_004: Verify result return correctly when match Confident is enabled
  aqTestCase.Begin("Start test ID: " + PST_SearchROIPassFail_004);
  Setup.Setup_PSTMatchConfidence(True, "[BS][BS]90")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingPassFailPanel.Panel.Panel.PassFailLabel, "text", cmpEqual, "Passed")
  Setup.Setup_VPMRunOnceCurrent()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingPassFailPanel.Panel.Panel.PassFailLabel, "text", cmpEqual, "Failed")
  Setup.Setup_PSTMatchConfidence(False, None)
  aqTestCase.End();
  
  Setup.Setup_closeVPM()

  

