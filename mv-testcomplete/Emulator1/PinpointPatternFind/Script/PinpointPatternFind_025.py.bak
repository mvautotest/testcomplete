import Setup
def PinpointPatternFind_025():
    Setup.Setup_loadVPM()
    Setup.Setup_PinpointPatternFindImages()
    Delay(500)
     #Clicks at point (278, 0) of the 'HideableTabbedPane' object.
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.Panel.Main_Toolbar.SwingObject("LoadProgramButton").ClickButton()
    #Delays the test execution for the specified time period.
    Delay(1310)
    #Clicks the 'Table' grid cell at row 6, column 'Program Name'.
    Aliases.javaw.ToolBar_LoadProgramAction_LoadProgramDialog.RootPane.null_layeredPane.null_contentPane.Panel.Panel.VisionProgramsPanel.ScrollPane.Viewport.Table.ClickCell(2, "Program Name")
    #Delays the test execution for the specified time period.
    Delay(300)
    #Clicks at point (394, 611) of the 'ToolBar_LoadProgramAction_LoadProgramDialog' object.
    Aliases.javaw.ToolBar_LoadProgramAction_LoadProgramDialog.RootPane.null_layeredPane.null_contentPane.Panel.SwingObject("JPanel", "", 1).SwingObject("JButton", "OK", 0).ClickButton()
    #Delays the test execution for the specified time period.
    Delay(1000)
    #Sets the 'HScroll' scroll bar thumb to position 0.
    #Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.HScroll.Pos = 0
    #Clicks at point (35, 0) of the 'TaskTree' object.
    
    for i in range(0, 10):
      Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.Panel.TaskToolbar.TaskAdvanceButton.ClickButton()
    #Delays the test execution for the specified time period.
      Delay(1000)
      
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.Panel.Main_Toolbar.SwingObject("OnlineButton").doClick()
    #Delays the test execution for the specified time period.
    Delay(20000)
    
#Check if the error message exits while running online

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
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane3.ClickTab("Properties")
    Setup.Setup_closeVPM()






