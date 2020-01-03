#Author: Ha Le
#The test verify verification panel will display when run online or continious trigger

import Setup
def AdvOCR_Display_003(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCR()
  Setup.Setup_VPMOnlineButtonEnable()
#  Regions.Panel1.Check(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_2.DetailComponent_RuntimeTabbedPane_.Panel.Summary.SplitPane.ScrollPane.Viewport.Panel.Panel.Panel.Panel)
#  Regions.Panel2.Check(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_2.DetailComponent_RuntimeTabbedPane_.Panel.Summary.SplitPane.ScrollPane.Viewport.Panel.Panel.Panel.Panel2)
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_2.DetailComponent_RuntimeTabbedPane_.Panel.Summary.SplitPane.ScrollPane.Viewport.Panel.Panel.Panel.Panel3, "Enabled", cmpEqual, True)
  Setup.Setup_VPMOnlineButtonDisable()
  Setup.Setup_closeVPM()

