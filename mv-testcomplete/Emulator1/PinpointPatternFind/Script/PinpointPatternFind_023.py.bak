#Author: Ha Le
#The test verify search image for Pattern matches between (Inclusive) the max and min value



import Setup
def PinpointPatternFind_023():
    Setup.Setup_loadVPM()
    Setup.Setup_PinpointPatternFindImages()
    Delay(500)
    Setup.VPM_CameraCheck()   
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.Panel.Main_Toolbar.SwingObject("LoadProgramButton").ClickButton()

    Aliases.javaw.ToolBar_LoadProgramAction_LoadProgramDialog.RootPane.null_layeredPane.null_contentPane.Panel.Panel.VisionProgramsPanel.ScrollPane.Viewport.Table.ClickCell(0, "Program Name")
 
    Delay(1144)

    Aliases.javaw.ToolBar_LoadProgramAction_LoadProgramDialog.RootPane.null_layeredPane.null_contentPane.Panel.SwingObject("JPanel", "", 1).SwingObject("JButton", "OK", 0).ClickButton()
    for i in range(0, 10):
      Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.Panel.TaskToolbar.SwingObject("TaskAdvanceButton").ClickButton()
  
      Delay(1000)
    
    
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.Panel.Main_Toolbar.SwingObject("OnlineButton").doClick()
  
    Delay(200)
    


      
    while True:
     

      k = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.SummaryPanel.ScrollPane.Viewport.Summary_Table.wValue[1, "A"].AWTComponentAccessibleName
  
      if k != "22":
        Log.Message (" value : " + k)
        #for i in range(0, 10):
        a = Aliases.javaw.Dialog2
        if not a.Exists:
            Log.Checkpoint("pass ans continue run")
        else:
            Log.Error("failed")
          #Delay(300) 
      else:  
        Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.Panel.Main_Toolbar.SwingObject("OnlineButton").doClick()  
        Log.Message (" value a: " + k)
        #Delay(300)
        break  
    
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.ClickItem("Root|Image In Task|Pinpoint Pattern Find")

    Setup.Setup_PinpointPatternFindPropertyTab()
    aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel2.PropertiesScrollPane.Viewport.PropertyTable.wValue[30, "E"].end_, "max_", cmpEqual, 6)
    aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel2.PropertiesScrollPane.Viewport.PropertyTable.wValue[30, "E"].end_, "min_", cmpEqual, 1)
    Setup.Setup_PinpointPatternSetupTab()
    Delay(500)
    aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane3.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternFindSetup_PatternFindPassFailPanel.Panel.Panel.Panel.PassFailLabel, "AWTComponentAccessibleName", cmpEqual, "Passed")
        #Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane3.ClickTab("Properties")
    aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane3.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternFindSetup_PatternFindPassFailPanel.Panel.Panel2.Panel.Panel.TextField, "wText", cmpEqual, "1")

    aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane3.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternFindSetup_PatternFindPassFailPanel.Panel.Panel2.Panel.Panel.TextField2, "wText", cmpEqual, "6")

    Setup.Setup_closeVPM()
 