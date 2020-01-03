#Author: Ha Le
#The test verify user can rename, colappesed/expended, delete, copy and paste under pattern database group and pattern group

import Setup

def PST_CPM_048():
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
  Setup.Setup_CPMRename("test[Enter]")
  Setup.Setup_CPMCopyItem("|[0]|Panel 1|Pattern Database2test")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.ScrollPane.Viewport.ControlStatusPane.Panel.TextField, "wText", cmpEqual, "Pattern Database2test")

  Setup.Setup_CPMPasteItem("|[0]|Panel 1", "Paste Control(s)")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.ScrollPane.Viewport.ControlStatusPane.Panel.TextField, "wText", cmpEqual, "Pattern Database2test(2)")
  Setup.Setup_CPMDeleteItem("|[0]|Panel 1|Pattern Database2test")
  aqObject.CheckProperty(Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane, "wTabCount", cmpEqual, 1)
  Setup.Setup_CPMCollaspItem("[0]|Panel 1|Pattern Database2test(2)")
  if Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.SwingObject("PanelContentsEditor", "", 0).SwingObject("PanelContentsEditor$CPTreeView", "", 0).SwingObject("JScrollPane", "", 0).SwingObject("JViewport", "", 0).SwingObject("ControlPanelTree").wItems.Item[0].Items.Item[1].Items.Item[0].Expanded == False:
    Log.Checkpoint("test pass")
  else:
    Log.Error("test fail")
    

  Setup.Setup_closeCPM()
  Setup.Setup_closeVPM()

 
