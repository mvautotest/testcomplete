import Setup
def EnviromentCheck():
#  TestedApps.Xmx_Setup.Run(1, True)
#
#  Delay(16000)

  if Aliases.javaw.DeviceSelector.Exists:
   #Choose device to connect
     #name  = 'IMPACT Emulator 1   (127.0.0.1:10010) - Local Emulator'
     F = aqFile.OpenTextFile(aqFileSystem.GetCurrentFolder() + "\\Setting1.txt", aqFile.faRead, aqFile.ctANSI)
     F.Cursor = 0
     #Log.Message("File by line")
     while not F.IsEndOfFile():
       s = F.ReadLine()
       if not ";" in s:
         #Log.Message(s)
         name = s
         Log.Message(name)
     
     F.Close()
     
     if Aliases.javaw.SwingObject("DeviceSelector", "Select a Vision Device to Connect to:", -1, 1).SwingObject("JRootPane", "", 0).SwingObject("null.layeredPane").SwingObject("null.contentPane").SwingObject("DeviceSelectorPanel", "", 0).SwingObject("JScrollPane", "", 0).SwingObject("JViewport", "", 0).SwingObject("JList", "", 0).wSelected[name] == True:
       Log.Message("Emulator/Device has been selected")
       Aliases.javaw.DeviceSelector.RootPane.null_layeredPane.null_contentPane.Panel.Box.Button.ClickButton()
     else:
      Aliases.javaw.SwingObject("DeviceSelector", "Select a Vision Device to Connect to:", -1, 1).SwingObject("JRootPane", "", 0).SwingObject("null.layeredPane").SwingObject("null.contentPane").SwingObject("DeviceSelectorPanel", "", 0).SwingObject("JScrollPane", "", 0).SwingObject("JViewport", "", 0).SwingObject("JList", "", 0).ClickItem(name)
      Aliases.javaw.DeviceSelector.RootPane.null_layeredPane.null_contentPane.Panel.Box.Button.ClickButton()
  
      
  else:
    Log.Message("do nothing")
  
def VPMCheck():
    if aqFileSystem.FindFiles("C:\\Datalogic\\IMPACT\\Applications\\VPM\\", "*.jar") != None:
      TestedApps.Xmx_Setup.Run(1, True)
      EnviromentCheck()
      Delay(16000)
      Setup.Setup_VPMNewButton()
      h = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.BaseImagePanel.ROIEditor.SwingObject("JPanel", "", 1).SwingObject("JPanel", "", 0).SwingObject("JScrollPane", "", 0).SwingObject("JViewport", "", 0).SwingObject("DisplayCanvas", "", 0).Height  
      w = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.BaseImagePanel.ROIEditor.SwingObject("JPanel", "", 1).SwingObject("JPanel", "", 0).SwingObject("JScrollPane", "", 0).SwingObject("JViewport", "", 0).SwingObject("DisplayCanvas", "", 0).Width 
      if h == 436 and w == 1084:
        Log.Message("device is ready to test")
        Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane_ToolPalettePanelSplitPane_.ConnectedDevicesPanel.ScrollPane.Viewport.ConnectedDevicesPanel_DeviceTree_.ClickItem("top|127.0.0.1 IMPACT Emulator 1")
        Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_SystemComponent_.ScrollPane.Viewport.Panel.TaskTree.ClickItem("Root|[0]|Camera")
        Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.Panel2.ToolSetupCardPanel.CameraSetup_OptionsSetupPanel.TabbedPane2.ClickTab("Frame Trigger")
        if Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.Panel2.ToolSetupCardPanel.CameraSetup_OptionsSetupPanel.TabbedPane.Panel.Panel.Panel.RadioButton.wState == 0:
          Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.Panel2.ToolSetupCardPanel.CameraSetup_OptionsSetupPanel.TabbedPane.Panel.Panel.Panel.RadioButton.ClickButton(True)
        else:
          Log.Message("do nothing")  
        if Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.Panel2.ToolSetupCardPanel.CameraSetup_OptionsSetupPanel.TabbedPane.Panel.Panel.Panel.CheckBox.JCheckBoxControl.wState == 0:
          Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.Panel2.ToolSetupCardPanel.CameraSetup_OptionsSetupPanel.TabbedPane.Panel.Panel.Panel.CheckBox.ClickButton(True)
        else:
          Log.Message("do nothing")  
      else:
        Log.Message("Please adjust VPM as default: Height = 436 and width = 1084")
      Setup.Setup_closeVPM()
      Aliases.javaw.Dialog.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button2.ClickButton()
    else:
     Log.Message("please Install Impact in your device")
  

     
      
      