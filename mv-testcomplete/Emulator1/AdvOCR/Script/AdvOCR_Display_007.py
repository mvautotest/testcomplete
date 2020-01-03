#Author: Ha Le
#The test verify OCR Set is presented at properties tab

import Setup
def AdvOCR_Display_007(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCR()
  Setup.Setup_VPMPropertiesTab()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.ViewsTabbedPane.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas, "ACTION_SIZING_ROI", cmpEqual, 3)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.ViewsTabbedPane.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas, "ScreenTop", cmpEqual, 85)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.ViewsTabbedPane.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas, "VisibleOnScreen", cmpEqual, True)

  Setup.Setup_VPMOCRFontLibraryTab()
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.ViewsTabbedPane2.OCRSetPanel.ScrollPane.Viewport.OCRSetPanel_LibraryPanel_, "Enabled", cmpEqual, True)
  Setup.Setup_closeVPM()
