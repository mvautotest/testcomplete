#Author: Ha Le
#The test verify blue ROIs appear and disappear on the pattern when click on display training mode ROI

import Setup
def PST_Database_070():
  Setup.Setup_PSTCheck()
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  Setup.Setup_PSTLoadDBSet("test", "load")
  Setup.Setup_PSTDBPanel()
  Setup.Setup_PSTDisplayTrainingModeROI(True)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.PatternSortingSetup1_SortingDatabasePanel_2.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.roiList_.elementData_2.Items[2], "visible_", cmpEqual, True)
  Setup.Setup_PSTDisplayTrainingModeROI(False)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.PatternSortingSetup1_SortingDatabasePanel_2.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.roiList_.elementData_2.Items[2], "visible_", cmpEqual, False)

 
  Setup.Setup_closeVPM()

  

