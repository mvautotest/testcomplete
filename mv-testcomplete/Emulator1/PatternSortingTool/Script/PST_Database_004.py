#Author: Ha Le
#The test verify user can move ROI position or resize train ROI on the image

import Setup
def PST_Database_003():
  Setup.Setup_PSTCheck()
  #Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()
  Setup.Setup_PSTTrainPanel()
  Setup.Setup_PSTLoadDBSet("test", "load")
  Setup.Setup_PSTResizeROI()
  Setup.Setup_PSTAddButton()
  Setup.Setup_PSTRetrainAll("train", "ok")
  Setup.Setup_PSTDBPanel()
  panel = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.PatternSortingSetup1_SortingDatabasePanel_2.ROIEditor.Panel
  ROIToolBar = panel.ROIToolBar
  ROIToolBar.Panel.ROIToolBar_ROITypeToggleButton.ClickButton(True)
  ROIToolBar.SwingPopupMenu.Click("[0]")
  displayCanvas = panel.Panel.ScrollPane.Viewport.DisplayCanvas
  displayCanvas.Drag(61, 73, 172, 295)
  displayCanvas.Drag(81, 89, 259, 325)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.PatternSortingSetup1_SortingDatabasePanel_2.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.activeROI_.specificROI_, "height_", cmpGreaterOrEqual, 73.857142857142861)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.PatternSortingSetup1_SortingDatabasePanel_2.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.activeROI_.specificROI_, "width_", cmpGreaterOrEqual, 59.562211981566819)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.PatternSortingSetup1_SortingDatabasePanel_2.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.activeROI_.specificROI_, "xLocation_", cmpGreaterOrEqual, 13.211981566820278)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.PatternSortingSetup1_SortingDatabasePanel_2.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.activeROI_.specificROI_, "yLocation_", cmpGreaterOrEqual, 15.811059907834101)
  Setup.Setup_PSTDBPanel()
  Setup.Setup_PSTDeletePattern()
  Setup.Setup_PSTRetrainAll("db", "ok")
  Setup.Setup_closeVPM()

  

