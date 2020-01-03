#Author: Ha Le
#The test verify User Can zoom in/out and 100% OCR set

import Setup
def AdvOCR_Display_008(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCR()
  Setup.Setup_VPMPropertiesTab()
  Setup.Setup_ZoomButtonPropertiesTab()
  #Zoom out
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.ViewsTabbedPane.ROIEditor.Panel.ROIToolBar.SwingPopupMenu.Click("[0]")

  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.ViewsTabbedPane.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.Click(133, 177)
  #liases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.ViewsTabbedPane.ROIEditor.Panel.Panel.ScrollPane.VScroll.Pos = 0
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.ViewsTabbedPane.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.Click(127, 177)
  Regions.DisplayCanvas12.Check(Regions.CreateRegionInfo(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.ViewsTabbedPane.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas, 90, 172, 597, 259, False))
  #Zoom in
  #Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.ViewsTabbedPane.ROIEditor.Panel.Panel.ScrollPane.VScroll.Pos = 0

  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.ViewsTabbedPane.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.ClickR(393, 231)
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.ViewsTabbedPane.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.ClickR(393, 231)
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.ViewsTabbedPane.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.ClickR(234, 167)
  Regions.DisplayCanvas14.Check(Regions.CreateRegionInfo(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.ViewsTabbedPane.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas, 87, 142, 420, 177, False))
  #Zoom 100%
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.ViewsTabbedPane.ROIEditor.Panel.SwingObject("ROIToolBar", "", 0).SwingObject("JPanel", "", 0).SwingObject("ROIToolBar$PopupMenuToggleButton", "", 2).DblClick(True)
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.ViewsTabbedPane.ROIEditor.Panel.ROIToolBar.SwingPopupMenu.Click("[1]")
  Regions.DisplayCanvas13.Check(Regions.CreateRegionInfo(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.ViewsTabbedPane.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas, 114, 174, 445, 164, False))
  
  Setup.Setup_closeVPM()
 

