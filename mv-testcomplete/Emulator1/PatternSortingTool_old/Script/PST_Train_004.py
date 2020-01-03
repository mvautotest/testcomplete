#Author: Ha Le
#The test verify user can position the train ROI

import Setup
def PST_Train_004():
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()

  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  Setup.Setup_PSTResizeROI()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.PatternSortingSetup1_PatternSortingSetupPanel_1.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.activeROI_.specificROI_, "xLocation_", cmpEqual, 266.08064516129036)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.PatternSortingSetup1_PatternSortingSetupPanel_1.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.activeROI_.specificROI_, "yLocation_", cmpEqual, 192.93317972350226)

  Setup.Setup_closeVPM()

