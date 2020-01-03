#Author: Ha Le
#The test verify user can view input chracter on properties tab at train chracter box

import Setup
def AdvOCR_Train_048(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCREmpty()
  Setup.Setup_AdvNotTrain()
  Setup.Setup_OCRClicktoTrain()
  vpm = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM
  #vpm.Panel.Main_Toolbar.Button.Keys("[BS][BS]")
  displayCanvas = vpm.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_2.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas
  #displayCanvas.Click(111, 145)
  displayCanvas.Keys("[BS][BS]")
  Setup.Setup_VPMPropertiesTab()

  
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[24, "E"].rectangleList_.elementData_2.Items[0].annotation_, "stringValue_", cmpEqual, "l")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[24, "E"].rectangleList_.elementData_2.Items[1].annotation_, "stringValue_", cmpEqual, "o")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[24, "E"].rectangleList_.elementData_2.Items[2].annotation_, "stringValue_", cmpEqual, "t")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[24, "E"].rectangleList_.elementData_2.Items[3].annotation_, "stringValue_", cmpEqual, "2")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[24, "E"].rectangleList_.elementData_2.Items[4].annotation_, "stringValue_", cmpEqual, "a")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[24, "E"].rectangleList_.elementData_2.Items[5].annotation_, "stringValue_", cmpEqual, "")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[24, "E"].rectangleList_.elementData_2.Items[6].annotation_, "stringValue_", cmpEqual, "")



  Setup.Setup_closeVPM()
