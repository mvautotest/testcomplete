﻿#Author: Ha Le
#The test verify each chracter box display in dash outlines if they are in the currently selected verification line


import Setup
def AdvOCR_Verification_007(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImageMultiText()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCREmpty()
  Setup.Setup_AdvSegmentNewLine()
  displayCanvas = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_2.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas
  displayCanvas.Drag(198, 414, 3, -305)
  Setup.Setup_AdvAutoSegment()
  displayCanvas.Click(28, 40)
 
  displayCanvas.Keys("abcd%$#")
  
  Setup.Setup_AdvSegmentNewLine()
  displayCanvas.Drag(27, 28, -5, 106)
  Setup.Setup_AdvAutoSegment()
  displayCanvas.Click(24, 143)
  displayCanvas.Keys("&*><>?/}")
  Setup.Setup_AdvSegmentNewLine()
  displayCanvas.Drag(19, 131, -3, 108)
  Setup.Setup_AdvAutoSegment()
  displayCanvas.Click(20, 246)
  
  displayCanvas.Keys("{|\+@!~`(")
  Setup.Setup_AdvTrainButton()
  Setup.Setup_VPMVerificationPanel()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGVerifyPanel.Panel.Panel.Panel.Panel.Panel.PatchableStringTextField, "wText", cmpEqual, "\"abcd%$#\"")
  comboBox = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGVerifyPanel.Panel.Panel.Panel.Panel.Panel.ComboBox
  comboBox.WindowsComboBoxUI_XPComboBoxButton.ClickButton()
  comboBox.ClickItem("2")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGVerifyPanel.Panel.Panel.Panel.Panel.Panel.PatchableStringTextField, "wText", cmpEqual, "\"&*><>?/}\"")
  comboBox.WindowsComboBoxUI_XPComboBoxButton.ClickButton()
  comboBox.ClickItem("3")
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGVerifyPanel.Panel.Panel.Panel.Panel.Panel.PatchableStringTextField, "wText", cmpEqual, "\"{|\\+@~(\"")

  Setup.Setup_closeVPM()