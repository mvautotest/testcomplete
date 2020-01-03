#Author: Ha Le
#The test verify train ROI display in cyan

import Setup
def PST_Database_002():
  Setup.Setup_PSTCheck()
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  Setup.Setup_PSTLoadDBSet("test", "load")
  Delay(1000)
  Setup.Setup_PSTResizeROI()
  Setup.Setup_PSTAddButton()
  Setup.Setup_PSTRetrainAll("train", "ok")
  Setup.Setup_PSTDBPanel()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.PatternSortingSetup1_SortingDatabasePanel_2.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.calImage_, "height_", cmpGreaterOrEqual, 94)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.PatternSortingSetup1_SortingDatabasePanel_2.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.calImage_, "width_", cmpGreaterOrEqual, 98)
  Setup.Setup_PSTDeletePattern()
  Setup.Setup_PSTRetrainAll("db", "ok")
  Setup.Setup_closeVPM()

