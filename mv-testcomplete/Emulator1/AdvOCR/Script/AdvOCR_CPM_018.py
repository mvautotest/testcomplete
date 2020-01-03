#Author: Ha Le
#The test verify at "Control Palette" can add over the group control, cannot add to the existing group
#Note: no message display ask to link in this case

import Setup
def AdvOCR_CPM_018(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCR()
  Setup.Setup_LoadCPM()
  Setup.Setup_DragOCRFontLibraryToCpFile()
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SwingObject("BeanPalette", "", 0).SwingObject("JScrollPane", "", 0).SwingObject("JViewport", "", 0).SwingObject("BeanPalette").ClickItem("|[0]|Input|Button")
  #Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.Item.Item.ScrollPane.Viewport.BeanPalette.Drag(34, 65, 779, 411)
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SwingObject("BeanPalette", "", 0).SwingObject("JScrollPane", "", 0).SwingObject("JViewport", "", 0).SwingObject("BeanPalette").Drag(34, 65, 779, 411)
  #Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.Item.Item.ScrollPane.Viewport.BeanPalette.Drag(34, 65, 779, 411)
  aqObject.CheckProperty(Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.ScrollPane.Viewport.ControlStatusPane.Panel.TextField, "wText", cmpEqual, "Button31")
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SwingObject("BeanPalette", "", 0).SwingObject("JScrollPane", "", 0).SwingObject("JViewport", "", 0).SwingObject("BeanPalette").ClickItem("|[0]|Input|Toggle Button")
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SwingObject("BeanPalette", "", 0).SwingObject("JScrollPane", "", 0).SwingObject("JViewport", "", 0).SwingObject("BeanPalette").Drag(45, 624, 1003, -134) 

  aqObject.CheckProperty(Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.wItems.Item["|[0]|Panel 1|Button31"], "Text", cmpEqual, "Button31")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.wItems.Item["|[0]|Panel 1|Toggle Button32"], "Text", cmpEqual, "Toggle Button32")
  
  Setup.Setup_closeCPM()
  Setup.Setup_closeVPM()
