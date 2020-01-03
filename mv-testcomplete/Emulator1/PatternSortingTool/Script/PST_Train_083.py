#Author: Ha Le
#The test verify the selected value "(E) Train Edge Detection Sensitivity" is updated successfully between setup tab and properties tab


import Setup
def PST_Train_083():
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
  Setup.Setup_PSTAddLabel("train", "test")
  Setup.Setup_PSTAddInfo("train", "test")
  Setup.Setup_PSTAddButton()
  Delay(500)
  Setup.Setup_VPMPropertiesTab()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.ClickCell(23, "E")
  
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.ComboBox.ClickItem("Fixed Threshold")


  Setup.Setup_VPMAdvSetupTab()
  Setup.Setup_PSTAdvanceSet("train", "Edge Match", None, None, None, None, None, None, None, None, None)
  aqObject.CheckProperty(Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane3.Panel.Panel.Panel.Panel.Panel2.PatternSortingSetup1_AdvancedTrainDialog_PatchableEdgeSensitivitySlider, "wPosition", cmpEqual, 5)
  Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane3.Panel.Panel.Panel.Panel.Panel2.PatternSortingSetup1_AdvancedTrainDialog_PatchableEdgeSensitivitySlider.wPosition = 0


  Setup.Setup_PSTAdvanceSet(None, "Edge Match", None, None, None, None, None, None, None, None, "ok")
  Setup.Setup_VPMPropertiesTab()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[23, "E"], "OleValue", cmpEqual, "High")
  Setup.Setup_VPMAdvSetupTab()
  Setup.Setup_PSTDBPanel()
  Setup.Setup_PSTDeletePattern()
  Setup.Setup_PSTRetrainAll("db", "ok")

  Setup.Setup_closeVPM()

 


  
