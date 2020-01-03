#Author: Ha Le
#The test verify Search Image output displays properly after user adjust out of search ROI at search panel

import Setup
def AdvOCR_Train_017(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_DragAvdToTaskTree()
  Setup.Setup_VPMSearchPanel()
  Setup.Setup_OCROutOfImage()
#  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_1.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.Drag(103, 78, 307, 41)
  Setup.Setup_VPMTrainPanel()
  Aliases.javaw.Dialog8.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button2.ClickButton()
  Setup.Setup_VPMSearchPanel()
  Setup.Setup_CorrectROI()
  Setup.Setup_VPMTrainPanel()
  Setup.Setup_VPMPropertiesTab()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[9, "E"].origin_.point_.x_, "value_", cmpEqual, 113.54838709677422)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[9, "E"].origin_.point_.y_, "value_", cmpEqual, 120)

  Setup.Setup_closeVPM()


