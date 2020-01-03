#Author: Ha Le
#The test verify Segmentation Region ROI cannot modify if it linked

import Setup
def AdvOCR_Train_009(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCR()
  Setup.Setup_DragAvdToTaskTree()
  Setup.Setup_VPMPropertiesTab()
  Setup.Setup_LinkSegmentation()
    #tasksTabbedPane_TaskTree_.ClickItem("Root|Image In Task|Advanced OCR|Segmentation Region = (((32,24),0°),(576,432),)")
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.ViewsTabbedPane.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.Click(375, 288)
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.ViewsTabbedPane.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.Keys("[Del]")

  Regions.DisplayCanvas27.Check(Regions.CreateRegionInfo(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.ViewsTabbedPane.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas, 41, 47, 572, 408, False), False, False, 1000)

#  Setup.Setup_VPMPropertiesTab()
##  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.ViewsTabbedPane.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.roiList_.elementData_2.Items[0], "xLocation_", cmpEqual, 32)
##  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.ViewsTabbedPane.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.roiList_.elementData_2.Items[0], "yLocation_", cmpEqual, 24)
#
##  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[9, "E"].origin_.angle_, "value_", cmpEqual, 0)
##  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[9, "E"].origin_.reference_.element_.point_.x_, "value_", cmpEqual, 32)
##  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[9, "E"].origin_.reference_.element_.point_.y_, "value_", cmpEqual, 24)
#
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[8, "E"].point_.x_, "value_", cmpEqual, 331.5)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[8, "E"].point_.y_, "value_", cmpEqual, 255.5)

  Setup.Setup_closeVPM()
  

