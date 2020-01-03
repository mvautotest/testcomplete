#Author: Ha Le
#The test verify user can rename, resize, move "Pattern Database viewer"

import Setup

def PST_CPM_049():
  Setup.Setup_PSTCheck()
  
  Setup.Setup_InnitializeCPM()

  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_LoadPSTImages()
  #Setup.VPM_CameraCheck()
  Setup.Setup_VPMNewButton()
  
  Setup.Setup_DragPatternSortToTaskTree()

  Setup.Setup_LoadCPM()
  Setup.Setup_PSTCPMDragDropPatternDBToPanel()
  #rename
  Setup.Setup_CPMRenameItem("|[0]|Panel 1|Pattern Database2|Pattern Database Viewer", " test[Enter]")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.wItems.Item[0].Items.Item[1].Items.Item[1].Items.Item[0], "Text", cmpEqual, "Pattern Database Viewer test")
  #Resize
  Setup.Setup_CPM_ModifyItem(None, 0, "Value", "80")
  Setup.Setup_CPM_ModifyItem(None, 1, "Value", "400")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.ScrollPane.Viewport.CpmFrame_25.Panel_1.Pattern_Database2.Pattern_Database_Viewer_test.Control_GlassPane, "Height", cmpEqual, 80)
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.ScrollPane.Viewport.CpmFrame_25.Panel_1.Pattern_Database2.Pattern_Database_Viewer_test.Control_GlassPane, "Width", cmpEqual, 400)

#  #Move
  Setup.Setup_CPM_ModifyItem(None, 2, "Value", "50")
  Setup.Setup_CPM_ModifyItem(None, 3, "Value", "70")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.ScrollPane.Viewport.CpmFrame_25.Panel_1.Pattern_Database2.Pattern_Database_Viewer_test.Control_GlassPane, "ScreenLeft", cmpEqual, 879)
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.ScrollPane.Viewport.CpmFrame_25.Panel_1.Pattern_Database2.Pattern_Database_Viewer_test.Control_GlassPane, "ScreenTop", cmpEqual, 420)

  Setup.Setup_closeCPM()
  Setup.Setup_closeVPM()

 
