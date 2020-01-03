#Author: Ha Le
#The test verify input data in Advance dialog will be updated to properties tab

import Setup
def PST_Train_090():
  Setup.Setup_PSTCheck()
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  Setup.Setup_PSTLoadDB("test")

  Setup.Setup_PSTMode("Edge Match")
#  for i in range (0, 10):
#    Setup.Setup_VPMtriggerOne()
#  Setup.Setup_PSTPassFailPanel()
#  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingPassFailPanel.Panel.Panel.PassFailLabel, "text", cmpEqual, "Passed")
  Setup.Setup_PSTAddLabel("train", "testhale")
  Setup.Setup_PSTAddInfo("train", "test[Enter]")

  Setup.Setup_PSTAdvanceSet("train", "Edge Match", "[BS][BS]8", None, None, None, None, None, None, None, None)
  Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane3.Panel.Panel.Panel.Panel.Panel2.PatternSortingSetup1_AdvancedTrainDialog_PatchableEdgeSensitivitySlider.wPosition = 3
  Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane3.Panel.Panel.Panel.Panel.Panel2.PatternSortingSetup1_AdvancedTrainDialog_PatchableEdgeSensitivitySlider.wPosition = 5
  Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane3.Panel.Panel.Panel.Panel.Panel.PatchableRealSlider.wPosition = 200
  Setup.Setup_PSTAdvanceSet(None, "Edge Match", None, None, None, None, None, None, None, None, "ok")
  
  Setup.Setup_PSTRetrainAll("train", None)
  Setup.Setup_VPMPropertiesTab()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[16, "E"], "OleValue", cmpEqual, "Edge Match Algorithm")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[23, "E"], "OleValue", cmpEqual, "Fixed Threshold")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[24, "E"], "value_", cmpEqual, 20)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[19, "E"], "value_", cmpEqual, 8)

  Setup.Setup_closeVPM()
 


  
