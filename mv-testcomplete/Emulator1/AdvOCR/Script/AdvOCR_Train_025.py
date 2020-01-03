#Author: Ha Le
#The test verify the previous cyan ROI will be preplaced after clicking on auto segment button


import Setup
def AdvOCR_Train_025(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCR()

  Setup.Setup_AdvSegmentNewLine()
  displayCanvas = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_2.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas
  displayCanvas.Drag(28, 71, -14, 9)
  displayCanvas.Drag(547, 206, 16, 2)
  displayCanvas.Drag(327, 20, 0, -8)
  displayCanvas.Drag(322, 410, 0, 9)

  Setup.Setup_AdvAutoSegment()
  Setup.Setup_VPMPropertiesTab()


  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[24, "E"].rectangleList_.elementData_2.Items[0].origin_.point_.x_, "value_", cmpEqual, 167.11612903225807)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[24, "E"].rectangleList_.elementData_2.Items[0].origin_.point_.y_, "value_", cmpEqual, 222.50207373271888)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[24, "E"].rectangleList_.elementData_2.Items[1].origin_.point_.x_, "value_", cmpEqual, 214.01612903225805)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[24, "E"].rectangleList_.elementData_2.Items[1].origin_.point_.y_, "value_", cmpEqual, 222.50207373271888)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[24, "E"].rectangleList_.elementData_2.Items[2].origin_.point_.x_, "value_", cmpEqual, 261.11612903225807)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[24, "E"].rectangleList_.elementData_2.Items[2].origin_.point_.y_, "value_", cmpEqual, 221.50207373271888)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[24, "E"].rectangleList_.elementData_2.Items[3].origin_.point_.x_, "value_", cmpEqual, 308.01612903225805)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[24, "E"].rectangleList_.elementData_2.Items[3].origin_.point_.y_, "value_", cmpEqual, 223.50207373271888)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[24, "E"].rectangleList_.elementData_2.Items[4].origin_.point_.x_, "value_", cmpEqual, 355.21612903225804)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[24, "E"].rectangleList_.elementData_2.Items[4].origin_.point_.y_, "value_", cmpEqual, 224.50207373271888)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[24, "E"].rectangleList_.elementData_2.Items[5].origin_.point_.x_, "value_", cmpEqual, 401.01612903225805)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[24, "E"].rectangleList_.elementData_2.Items[5].origin_.point_.y_, "value_", cmpEqual, 224.50207373271888)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[24, "E"].rectangleList_.elementData_2.Items[6].origin_.point_.x_, "value_", cmpEqual, 449.11612903225807)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[24, "E"].rectangleList_.elementData_2.Items[6].origin_.point_.y_, "value_", cmpEqual, 223.50207373271888)



 
  Setup.Setup_closeVPM()
