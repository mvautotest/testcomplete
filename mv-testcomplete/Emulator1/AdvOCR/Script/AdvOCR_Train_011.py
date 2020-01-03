#Author: Ha Le
#The test verify the link Segmentation Region ROI is not updated if unlinked
#Skip
import Setup
def AdvOCR_Train_011(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCR()
  Setup.Setup_DragAvdToTaskTree()
  Setup.Setup_VPMPropertiesTab()
  Setup.Setup_LinkSegmentation()
  splitPane = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane
  scrollPane = splitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane
  tasksTabbedPane_TaskTree_ = scrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[8, "D"]
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.ClickCell(8, "D")
  splitPane = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane
  tasksTabbedPane_TaskTree_ = splitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree
  tasksTabbedPane_TaskTree_.ClickItem("Root|Image In Task|Advanced OCR 1")
  detailComponent_1 = splitPane.DetailComponent.DetailComponent_1
  displayCanvas = detailComponent_1.ViewsTabbedPane.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas
  displayCanvas.Drag(122, 20, 34, 90)
  displayCanvas.Drag(242, 455, 2, -90)
  displayCanvas.Drag(29, 223, 72, 9)
  displayCanvas.Drag(604, 220, -58, -1)
  tasksTabbedPane_TaskTree_.ClickItem("Root|Image In Task|Advanced OCR 1")
  detailComponent_BottomComponent_ = detailComponent_1.DetailComponent_BottomComponent_
  detailComponent_BottomComponent_.PropertiesTabbedPane2.ClickTab("Setup")
  detailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.BaseSetupPanel_ButtonBar_.ToolSetupCardPanel_HashcodeRadioButton.ClickButton(True)
  
  Setup.Setup_VPMPropertiesTab()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[8, "E"].origin_.angle_, "value_", cmpEqual, 0)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[8, "E"].origin_.reference_.element_.point_.x_, "value_", cmpEqual, -163.5)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[8, "E"].origin_.reference_.element_.point_.y_, "value_", cmpEqual, -129.5)

  Setup.Setup_closeVPM()

