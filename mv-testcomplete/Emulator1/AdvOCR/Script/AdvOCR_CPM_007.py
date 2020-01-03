#Author: Ha Le
#The test verify user can modify OCR Set group control

import Setup
def AdvOCR_CPM_007(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCR()
  Setup.Setup_LoadCPM()
  Setup.Setup_DragOCRFontLibraryToCpFile()
  Setup.Setup_CPMRenameItem("|[0]|Panel 1|OCR Font Library2", "[BS][BS][BS][BS][BS][BS][BS][BS][BS][BS][BS][BS][BS][BS][BS][BS][BS][BS][BS]OCR test[Enter]")
  Setup.Setup_CPM_ModifyItem("|[0]|Panel 1|OCR test|OCR Font Library|OCR Font Library Display", 0, "Value", "60")
  Setup.Setup_CPM_ModifyItem("|[0]|Panel 1|OCR test|OCR Font Library|OCR Font Library Display", 1, "Value", "60")
  Setup.Setup_CPM_ModifyItem("|[0]|Panel 1|OCR test|OCR Font Library|OCR Font Library Display", 2, "Value", "1030")
  Setup.Setup_CPM_ModifyItem("|[0]|Panel 1|OCR test|OCR Font Library|OCR Font Library Display", 3, "Value", "490")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.ScrollPane.Viewport.CpmFrame_25.Panel_1.OCR_test.OCR_Font_Library.Control_GlassPane, "Height", cmpEqual, 280)
  aqObject.CheckProperty(Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.ScrollPane.Viewport.CpmFrame_25.Panel_1.OCR_test.OCR_Font_Library.Control_GlassPane, "ScreenLeft", cmpEqual, 719)
  aqObject.CheckProperty(Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.ScrollPane.Viewport.CpmFrame_25.Panel_1.OCR_test.OCR_Font_Library.Control_GlassPane, "ScreenTop", cmpGreaterOrEqual, 180)
  aqObject.CheckProperty(Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.ScrollPane.Viewport.CpmFrame_25.Panel_1.OCR_test.OCR_Font_Library.Control_GlassPane, "Width", cmpEqual, 510)

  Setup.Setup_CPMCollaspItem("|[0]|Panel 1|OCR test")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.wItems.Item[0].Items.Item[1].Items.Item[1], "Expanded", cmpEqual, False)

  Setup.Setup_CPMExpandItem("|[0]|Panel 1|OCR test") 
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.wItems.Item[0].Items.Item[1].Items.Item[1], "Expanded", cmpEqual, True)
 
  Setup.Setup_CPMCopyItem("|[0]|Panel 1|OCR test")
  Setup.Setup_CPMPasteItem("|[0]|Panel 1", "Paste Control(s)")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.ScrollPane.Viewport.ControlStatusPane.Panel.TextField, "wText", cmpEqual, "OCR test(2)")
  
  Setup.Setup_CPMDeleteItem("|[0]|Panel 1|OCR test(2)")  
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.wItems.Item[0].Items.Item[1].Items, "Count", cmpEqual, 2)
 

  Setup.Setup_closeCPM()
  Setup.Setup_closeVPM()
  
 
