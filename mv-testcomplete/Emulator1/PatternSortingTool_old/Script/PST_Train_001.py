#Author: Ha Le
#The test verify input images display in "Image Display" area

import Setup
def PST_Train_001():
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.PatternSortingSetup1_PatternSortingSetupPanel_1.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.calImage_, "height_", cmpEqual, 494)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.PatternSortingSetup1_PatternSortingSetupPanel_1.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.calImage_, "width_", cmpEqual, 650)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.PatternSortingSetup1_PatternSortingSetupPanel_1.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.calImage_.wtImage_.wt_.imageName, "OleValue", cmpEqual, "/cf/Images/Sample Pattern Sort - 01 Fail.png")


  Setup.Setup_closeVPM()

