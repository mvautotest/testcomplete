#Author: Ha Le
#The test verify user cannot delete train ROI

import Setup
def PST_Database_005():
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
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.PatternSortingSetup1_SortingDatabasePanel_2.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.Keys("[Del]")

  Setup.Setup_PSTDeletePattern()
  Setup.Setup_PSTRetrainAll("db", "ok")
  Setup.Setup_PSTPassFailPanel()
  #aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.PatternSortingSetup1_PatternSortingSetupPanel_1.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.activeROI_, "name_", cmpEqual, "ShapeListROI")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.PatternSortingSetup1_PatternSortingSetupPanel_1.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.activeROI_, "visible_", cmpEqual, False)

  Setup.Setup_closeVPM()

  

