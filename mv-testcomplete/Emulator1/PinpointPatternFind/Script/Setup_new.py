#Author: Ha Le
#Set up steps

import re
import math

#Choose mapped drive to connect
 #name  = "\\\\192.168.0.13\\c\\Users\\hale\\Documents\\PST\\"
global name1

F = aqFile.OpenTextFile(aqFileSystem.GetCurrentFolder() + "\\MappedDriveSetting.txt", aqFile.faRead, aqFile.ctANSI)
F.Cursor = 0
 #Log.Message("File by line")
while not F.IsEndOfFile():
   s = F.ReadLine()
   if not ";" in s:
     #Log.Message(s)
     name1 = s
     #name2 = aqString.Remove(name1, 0, 2) + aqString.Remove(name1, 16, 1) + aqString.Remove(name1 + 19, 1) + aqString.Remove(name1, 26, 1) + aqString.Remove(name1, 32, 1) + aqString.Remove(name1, 43, 1) + aqString.Remove(name1, 48, 1)
     Log.Message(name1)
     
F.Close()
 
def Setup_OCRValue():
  x = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[24, "E"].rectangleList_.elementData_2.Items[0].origin_.point_.x_.value_
  #Segmentation Roi point 
  y = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[24, "E"].rectangleList_.elementData_2.Items[0].origin_.point_.y_.value_
  #Segmentation Roi point 
  b = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[24, "E"].rectangleList_.elementData_2.Items[0].size_.width_.value_
  #Character box legth
  a = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[24, "E"].rectangleList_.elementData_2.Items[0].size_.height_.value_
  #Character box width
  z = int(x) - math.sqrt(math.pow((math.sqrt((a*a) + (b*b))/2), 2)-math.pow((a/2), 2))
  #Point on Character box

#===================================Set up for VPM=====================================
def EnviromentCheck():
  #obj = Aliases.javaw.Find("DeviceSelector")
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
  



#Check if Camera setting for runonline mode is enabled or not
def VPM_CameraCheck():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_SystemComponent_.ScrollPane.Viewport.Panel.TaskTree.ClickItem("Root|[0]|Camera")
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.Panel2.ToolSetupCardPanel.CameraSetup_OptionsSetupPanel.TabbedPane2.ClickTab("Frame Trigger")
  if Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.Panel2.ToolSetupCardPanel.CameraSetup_OptionsSetupPanel.TabbedPane.Panel.Panel.Panel.RadioButton.wState == 1 and Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.Panel2.ToolSetupCardPanel.CameraSetup_OptionsSetupPanel.TabbedPane.Panel.Panel.Panel.CheckBox.Enabled == True:
    Log.Message("do nothing")
  else:
    panel = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.Panel2.ToolSetupCardPanel.CameraSetup_OptionsSetupPanel.TabbedPane.Panel.Panel.Panel
    panel.RadioButton.ClickButton(True)
    panel.CheckBox.ClickButton(True)


#Check if CPM Frame still existing on Desktop and close it before run the test
def Setup_InnitializeCPM():
  if Aliases.javaw.CpmFrame2.Exists:

    Setup_closeCPM()
  else:
      Log.Message("do nothing")
  

#Check if VPM Frame still existing on Desktop and close it before run the test
def Setup_InnitializeVPM():
  if Aliases.javaw.VpmFrame.Exists:
    Log.Message("VPM till open")
    Setup_closeVPM()

  else:
      Log.Message("do nothing")
    
def Setup_loadVPM():
  if Aliases.javaw.VpmFrame.Exists:
    Log.Message("do nothing")
  else:      
    TestedApps.Xmx_Setup.Run(1, True)
    if Aliases.javaw.DeviceSelector.Exists:
      Delay(3000)
      EnviromentCheck()
    else:
      Log.Message("do nothing")
    Delay(10000)
    if Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.Panel.TaskToolbar.CameraModeButton.Enabled == False:
      Log.Message("Device is ready to test")
    else:
      Delay(1000)
      Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.Panel.TaskToolbar.CameraModeButton.ClickButton(True)
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_SystemComponent_.ScrollPane.Viewport.Panel.TaskTree.ClickItem("Root|[0]|File Camera")
    Setup_VPMSizeCheck()

def Setup_VPMSizeCheck():
  h = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.BaseImagePanel.ROIEditor.SwingObject("JPanel", "", 1).SwingObject("JPanel", "", 0).SwingObject("JScrollPane", "", 0).SwingObject("JViewport", "", 0).SwingObject("DisplayCanvas", "", 0).Height  
  w = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.BaseImagePanel.ROIEditor.SwingObject("JPanel", "", 1).SwingObject("JPanel", "", 0).SwingObject("JScrollPane", "", 0).SwingObject("JViewport", "", 0).SwingObject("DisplayCanvas", "", 0).Width 
  if h == 436 and w == 1084:
    Log.Message("device is ready to test")
  else:
    Log.Message("Please adjust VPM as default: Height = 436 and width = 1084")

def Setup_closeVPM():
  if Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.Panel.Main_Toolbar.CloseProgramButton.isEnabled() == True:
    Setup_VPMUnloadProgram()
    Aliases.javaw.Dialog.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
  else:
    Log.Message("do nothing")
 
  Aliases.javaw.VpmFrame.Close()
  if Aliases.javaw.Dialog.Exists:
    #Aliases.javaw.Dialog.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button2.ClickButton()
    Aliases.javaw.Dialog.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
  else:
    Log.Message("do nothing")
  


# this function to let VPM run as time we want. Count = run count
def Setup_VPMRunOnline(count):
  Setup_VPMOnlineButtonEnable()
  while True:
      k = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.SummaryPanel.ScrollPane.Viewport.Summary_Table.wValue[2, "A"].AWTComponentAccessibleName
  
      if k != count:    
        Log.Message (" running online mode " + k )
         
      else:  
        Setup_VPMOnlineButtonDisable()
        Log.Message (" count: " + k)
        
        break  
#===========================================VPM buttons=========================================

def Setup_VPMNewButton():
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.Panel.Main_Toolbar.NewProgramButton.ClickButton()
    #RestartDevice()
    Aliases.javaw.NewProgramPrompt.RootPane.null_layeredPane.null_contentPane.Panel.Panel.Button.ClickButton()
    if Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.SwingObject("BaseImagePanel", "", 0).SwingObject("ROIEditor", "", 0).SwingObject("JPanel", "", 0).Exists:
      a= Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.SwingObject("BaseImagePanel", "", 0).SwingObject("ROIEditor", "", 0).SwingObject("JPanel", "", 0).component.elementData_2.Items[0].getText()
    else:
      a= Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane3.Panel.Setup.BaseSetupPanel_1.Panel.Panel.SwingObject("BaseImagePanel", "", 0).SwingObject("ROIEditor", "", 0).SwingObject("JPanel", "", 0).component.elementData_2.Items[0].getText()
 
    b = str(a)
    if b =="   /cf/Images/Capture.PNG":
      Log.Message("do nothing")
    else:
      x = int(re.search(r'\d+', b).group())
      if x == 1: 
        Log.Message("do nothing")
    
      else:
       
        for i in range(0, 11-x):
          Setup.Setup_VPMtriggerOne()
        Setup_VPMResetButton()

def Setup_VPMResetButton():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.Panel.TaskToolbar.ResetSummaryButton.ClickButton()

def Setup_VPMRunOnceCurrent():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.Panel.TaskToolbar.TaskRunOnceButton.ClickButton()

def Setup_VPMOnlineButtonEnable():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.Panel.Main_Toolbar.OnlineButton.ClickButton(True)

def Setup_VPMOnlineButtonDisable():  
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.Panel.Main_Toolbar.OnlineButton.ClickButton(False)

def Setup_VPMContinousButtonEnable():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.Panel.TaskToolbar.TaskPlayButton.ClickButton(True)

def Setup_VPMContinousButtonDisable():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.Panel.TaskToolbar.TaskPlayButton.ClickButton(False)

def Setup_VPMtriggerOne():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.Panel.TaskToolbar.TaskAdvanceButton.ClickButton()

def Setup_VPMRunModeEnable():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.Panel.Main_Toolbar.RunButton.ClickButton(True)
  
def Setup_VPMRunModeDisable():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.Panel.Main_Toolbar.RunButton.ClickButton(False)

def Setup_VPMSaveButton():
   Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.Panel.Main_Toolbar.SaveProgramButton.ClickButton()

def Setup_VPMSaveAsButton():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.Panel.Main_Toolbar.SaveProgramAsButton.ClickButton()

def Setup_VPMDisconectReconectDevice():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.Panel.Main_Toolbar.Button.ClickButton()
  Delay(2000)
  Aliases.javaw.DeviceSelector.RootPane.null_layeredPane.null_contentPane.Panel.Box.Button.ClickButton()

def Setup_VPMUnloadProgram():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.Panel.Main_Toolbar.CloseProgramButton.ClickButton()

def Setup_ZoomButtonPropertiesTab():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.ViewsTabbedPane.ROIEditor.Panel.SwingObject("ROIToolBar", "", 0).SwingObject("JPanel", "", 0).SwingObject("ROIToolBar$PopupMenuToggleButton", "", 2).ClickButton(True)

def Setup_TrainButtonPropertiesTab():
   Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.VPMMethodBar.Button.ClickButton()

def Setup_LinkButtonGeneralPanel():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.General.Panel.Panel.Panel.ToggleButton.ClickButton(True)

def Setup_TrainROIPinpointPatternFind():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane3.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.BaseSetupPanel_ButtonBar_.ToolSetupCardPanel_HashcodeRadioButton.ClickButton(True)

def Setup_AdvSegmentNewLine(): 
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGTrainPanel.Panel.Panel.Panel.Button.ClickButton()   
  
def Setup_AdvAutoSegment():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGTrainPanel.Panel.Panel.Panel.Button2.ClickButton()

def Setup_AdvAddChacterBox():
   Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGTrainPanel.Panel.Panel.Panel.Button3.ClickButton()

def Setup_AdvTrainButton():
   Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGTrainPanel.Panel2.Panel.Button.ClickButton()

  
#================================================VPM tabs=================================================  
def Setup_VPMPropertiesTab():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.ClickTab("Properties")

def Setup_VPMLinkSumaryTab():
   Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.ClickTab("Link Summary")

def Setup_VPMInfoTab():
   Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane3.ClickTab("Info")

def Setup_VPMOCRFontLibraryTab():
   Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.ViewsTabbedPane.ClickTab("OCR Font Library")

def Setup_VPMOCRFontLibraryTabRunMode():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane2.DisplayPanel.DisplayPanel_DisplayPanelRightPanel_.SplitPane.DisplayPanel_ImagePane.ClickTab("Advanced OCR 1: OCR Font Library")
def Setup_VPMAdvSetupTab():
   Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.ClickTab("Setup")


#================================================VPM panels==============================================
#Display panel
def Setup_VPMDisplayPanel():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.BaseSetupPanel_ButtonBar_.ToolSetupCardPanel_HashcodeRadioButton3.ClickButton(True)
def Setup_VPMVerificationPanel():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.BaseSetupPanel_ButtonBar_.ToolSetupCardPanel_HashcodeRadioButton4.ClickButton(True)
def Setup_VPMTrainPanel():
   Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.BaseSetupPanel_ButtonBar_.ToolSetupCardPanel_HashcodeRadioButton.ClickButton(True)
def Setup_VPMSearchPanel():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.BaseSetupPanel_ButtonBar_.ToolSetupCardPanel_HashcodeRadioButton2.ClickButton(True)
def Setup_GeneralPanel():
   Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.BaseSetupPanel_ButtonBar_.ToolSetupCardPanel_HashcodeRadioButton5.ClickButton(True)
def Setup_MethodPanel():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.BaseSetupPanel_ButtonBar_.ToggleButton.ClickButton(True)      

def Setup_ROIPassFailPanel():
   Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.BaseSetupPanel_ButtonBar_.ToggleButton2.ClickButton(True)


#===================================================Set up for CPM====================================
def Setup_closeCPM():
  javaw = Aliases.javaw
  
  javaw.CpmFrame2.Close()
  if javaw.Dialog26.Exists:
    
    Aliases.javaw.Dialog26.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
  else:
    Log.Message("do nothing")
  

def Setup_LoadCPM():
    TestedApps.Xmx_Setup1.Run(1, True)
    Delay(15000)
    if Aliases.javaw.CpmFrame.Exists:
      Aliases.javaw.CpmFrame.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.Panel.ViewOptionsButton.ClickButton()
      
      if Aliases.javaw.CpmFrame.RootPane.null_layeredPane.SwingObject("JPanel", "", 0).SwingObject("JPopupMenu", "", 0).SwingObject("JCheckBoxMenuItem", "Control Panel Tree", 2).getState() == True:
        Aliases.javaw.CpmFrame.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.Panel.ViewOptionsButton.ClickButton()
        #Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.MainToolBar.Panel.NewButton.ClickButton()
      else:
        #Aliases.javaw.CpmFrame.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.Panel.ViewOptionsButton.SwingPopupMenu.Check("Control Panel Tree", True)
        Aliases.javaw.CpmFrame.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.Panel.ViewOptionsButton.SwingPopupMenu.Check("Control Panel Tree", True)
        #Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.MainToolBar.Panel.NewButton.ClickButton()
      
      if Aliases.javaw.CpmFrame.RootPane.null_layeredPane.null_contentPane.MainToolBar.Panel.ConnectButton.wState == 0:
        
        Aliases.javaw.CpmFrame.RootPane.null_layeredPane.null_contentPane.MainToolBar.Panel.ConnectButton.DblClick()
        Delay(7000)
        panel = Aliases.javaw.DeviceSelector.RootPane.null_layeredPane.null_contentPane
        panel.Panel.CheckBox.ClickButton(True)
      
        Aliases.javaw.DeviceSelector.RootPane.null_layeredPane.null_contentPane.Panel2.Box.Button.ClickButton()
      else:
        if Aliases.javaw.DeviceSelector.Exists:
          panel = Aliases.javaw.DeviceSelector.RootPane.null_layeredPane.null_contentPane
          panel.Panel.CheckBox.ClickButton(True)
    
          Aliases.javaw.DeviceSelector.RootPane.null_layeredPane.null_contentPane.Panel2.Box.Button.ClickButton()
      Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.MainToolBar.Panel.NewButton.ClickButton()
      Aliases.javaw.OpenTemplateDialog_TemplateDialog.RootPane.null_layeredPane.null_contentPane.OpenTemplateDialog_TemplateChooser.FileChooser.Panel.Panel.Panel.WindowsFileChooserUI_7.Keys("new[Enter]")
        
    else:
      Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.MainToolBar.Panel.NewButton.ClickButton()
      Aliases.javaw.OpenTemplateDialog_TemplateDialog.RootPane.null_layeredPane.null_contentPane.OpenTemplateDialog_TemplateChooser.FileChooser.Panel.Panel.Panel.WindowsFileChooserUI_7.Keys("new[Enter]")
  

   


 


#======================================================Setup for other tool====================================

 
def Setup_VPMOrigin():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane_ToolPalettePanelSplitPane_.ScrollPane.Viewport.Panel.ToolTree.ClickItemR("|[0]|Locating|Origin")
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane_ToolPalettePanelSplitPane_.ScrollPane.SwingPopupMenu.Click("Copy Origin")
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.ClickR(True)
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.SwingPopupMenu.Click("Paste Origin")


  
def Setup_Calibration():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane_ToolPalettePanelSplitPane_.ScrollPane.Viewport.Panel.ToolTree.ClickItemR("|[0]|Calibration|Calibration")
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane_ToolPalettePanelSplitPane_.ScrollPane.SwingPopupMenu.Click("Copy Calibration")
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.ClickR(True)
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.SwingPopupMenu.Click("Paste Calibration")
  
def Setup_ImageArchive():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane_ToolPalettePanelSplitPane_.ScrollPane.Viewport.Panel.ToolTree.ClickItemR("|[0]|Communication|Image Archive")
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane_ToolPalettePanelSplitPane_.ScrollPane.SwingPopupMenu.Click("Copy Image Archive")
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.ClickR(True)
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.SwingPopupMenu.Click("Paste Image Archive")

def Setup_IMADestinationPanel():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.BaseSetupPanel_ButtonBar_.ToolSetupCardPanel_HashcodeRadioButton4.ClickButton(True)

def Setup_IMALinkImage():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ImageArchivingSetup_ImageArchiveSetupPanel_MainSetupPanel.Panel.Panel.Panel.ToggleButton.ClickButton(True)
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.ClickItem("Root|Image In Task|Image Archive")
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.Panel.PopupMenu.Click(0, 0)
  Aliases.javaw.VpmFrame.SwingPopupMenu.Click("Destination File Name")
  patchableComboBox = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ImageArchivingSetup_ImageArchiveSetupPanel_MainSetupPanel.Panel.Panel.Panel.PatchableComboBox
  patchableComboBox.WindowsComboBoxUI_XPComboBoxButton.ClickButton()
  patchableComboBox.ClickItem("JPG")


#=====================================================Set up for Pinpoint Pattern Find Tool===============================================        
def Setup_PPCheck():
  if aqFileSystem.Exists("C:\\Datalogic\\IMPACT\\Applications\\Emulator"):
  
    folder = aqFileSystem.FindFiles("C:\\Datalogic\\IMPACT\\Applications\\Emulator\\IMPACTEmulator\\cf\\VisionPrograms", "PinpointPatternFind_023.vp")
    if folder == None:
      currentfolder = aqFileSystem.GetCurrentFolder()
      path = currentfolder + "\\testdata\\" + "*.vp"
      aqFileSystem.CopyFile(path, "C:\\Datalogic\\IMPACT\\Applications\\Emulator\\IMPACTEmulator\\cf\\VisionPrograms")
      #aqFileSystem.RenameFolder("C:\\Datalogic\\IMPACT\\Applications\\Emulator\\EmulatorRoot\\Copy of PST", "C:\\Datalogic\\IMPACT\\Applications\\Emulator\\EmulatorRoot\\PST")
    else:
      Log.Message("Folder exist")
      
  else:
    folder = aqFileSystem.FindFolders("C:\\Datalogic\\IMPACT\\Applications\\Device\\IMPACTDevice\\cf\\VisionPrograms", "PinpointPatternFind_023.vp")
    if folder == None:
      currentfolder = aqFileSystem.GetCurrentFolder()
      path = currentfolder + "\\testdata\\" + "*.vp"
      aqFileSystem.CopyFile(path, "C:\\Datalogic\\IMPACT\\Applications\\Device\\IMPACTDevice\\cf\\VisionPrograms")
      #aqFileSystem.RenameFolder("C:\\Datalogic\\IMPACT\\Applications\\Device\\DeviceRoot\\Copy of PST", "C:\\Datalogic\\IMPACT\\Applications\\Device\\DeviceRoot\\PST")
    else:
      Log.Message("Folder exist")


def Setup_PinpointPatternFindImages():
  if Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel.ScrollPane.Viewport.List.wItemCount==10 and Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel.ScrollPane.Viewport.List.wItem[0] =="Sample Pinpoint PickPlace 2 - 01 Pass":
    Log.Message("PP Image existed - do nothing")
  elif Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel.ScrollPane.Viewport.List.wItemCount==0:
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel3.ScrollPane.Viewport.List.ClickItem("Sample Pinpoint PickPlace 2 - 01 Pass")
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel3.ScrollPane.Viewport.List.ClickItem("Sample Pinpoint PickPlace 2 - 10 Pass", skShift | skCtrl)
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel2.Panel.Button.ClickButton()
  
  else:
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel.ScrollPane.Viewport.List.Keys("^a")
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel2.Panel.Button.ClickButton()
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel3.ScrollPane.Viewport.List.ClickItem("Sample Pinpoint PickPlace 2 - 01 Pass")
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel3.ScrollPane.Viewport.List.ClickItem("Sample Pinpoint PickPlace 2 - 10 Pass", skShift | skCtrl)
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel2.Panel.Button.ClickButton()


def Setup_LoadPinpointPatternFind():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane_ToolPalettePanelSplitPane_.ScrollPane.Viewport.Panel.ToolTree.ClickItemR("[0]|Locating|Pinpoint Pattern Find")
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane_ToolPalettePanelSplitPane_.ScrollPane.SwingPopupMenu.Click("Copy Pinpoint Pattern Find")
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.ClickR(True)
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.SwingPopupMenu.Click("Paste Pinpoint Pattern Find")


def Setup_DrawROIPinpointPatternFind():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane3.Panel.Setup.BaseSetupPanel_1.Panel.Panel.PatternFindSetup_PatternFindSetupPanel_1.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.Drag(204, 117, 88, 4)
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane3.Panel.Setup.BaseSetupPanel_1.Panel.Panel.PatternFindSetup_PatternFindSetupPanel_1.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.Drag(218, 148, 1, 26)

def Setup_PinpointPatternFindPropertyTab():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane3.ClickTab("Properties")

def Setup_PinpointPatternSetupTab():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane3.ClickTab("Setup")


#============================================Set up for AvdOCR tool========================================
def Setup_OCRClicktoTrain():
  
  x = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_2.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.roiList_.elementData_2.Items[1].contents_.elementData_2.Items[0].xLocation_
  #Segmentation Roi point 
  y = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_2.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.roiList_.elementData_2.Items[1].contents_.elementData_2.Items[0].yLocation_
  #Segmentation Roi point 
  a = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_2.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.roiList_.elementData_2.Items[1].contents_.elementData_2.Items[0].height_
  #Character box length
  b = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_2.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.roiList_.elementData_2.Items[1].contents_.elementData_2.Items[0].width_
  #Character box width
  z = int(x) - math.sqrt(math.pow((math.sqrt((a*a) + (b*b))/2), 2)-math.pow((a/2), 2))
    
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_2.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.Click(z, y)

def Setup_AdjustROI():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_2.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.Drag(636, 277, -167, 4)
  
 
def Setup_OCRDeleteRegionROI():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_2.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.Click(44, 380)
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_2.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.Keys("[Del]")


def Setup_OCRImages():
  if Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel.ScrollPane.Viewport.List.wItemCount==10 and Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel.ScrollPane.Viewport.List.wItem[0] =="Sample OCR - 01 Pass":
    Log.Message("OCR Image existed - do nothing")
  elif Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel.ScrollPane.Viewport.List.wItemCount==0:
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel3.ScrollPane.Viewport.List.ClickItem("Sample OCR - 01 Pass")
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel3.ScrollPane.Viewport.List.ClickItem("Sample OCR - 10 Fail", skShift | skCtrl)
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel2.Panel.Button.ClickButton()
  
  else:
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel.ScrollPane.Viewport.List.Keys("^a")
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel2.Panel.Button.ClickButton()
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel3.ScrollPane.Viewport.List.ClickItem("Sample OCR - 01 Pass")
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel3.ScrollPane.Viewport.List.ClickItem("Sample OCR - 10 Fail", skShift | skCtrl)
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel2.Panel.Button.ClickButton()

def Setup_OCRImageMultiText():
  a = aqFileSystem.GetCurrentFolder()
  path = a + "\\Image\\"
  if aqFileSystem.Exists("C:\\Datalogic\\IMPACT\\Applications\\Emulator"):
    if aqFileSystem.Exists("C:\\Datalogic\\IMPACT\\Applications\\Emulator\\IMPACTEmulator\\cf\\Images\\Capture.PNG"):
      Log.Message("File exist and ready to test")
    else:
      aqFileSystem.CopyFile(path + "Capture.PNG", "C:\\Datalogic\\IMPACT\\Applications\\Emulator\\IMPACTEmulator\\cf\\Images")
  else:
    if aqFileSystem.Exists("C:\\Datalogic\\IMPACT\\Applications\\Device\\IMPACTDevice\\cf\\Images\\Capture.PNG"):
      Log.Message("File exist and ready to test")
    else:
      aqFileSystem.CopyFile(path + "Capture.PNG", "C:\\Datalogic\\IMPACT\\Applications\\Device\\IMPACTDevice\\cf\\Images")  
      
  if Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel.ScrollPane.Viewport.List.wItemCount==1 and Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel.ScrollPane.Viewport.List.wItem[0] =="Capture":
    Log.Message("OCR Image existed - do nothing")
  elif Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel.ScrollPane.Viewport.List.wItemCount==0:
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel3.ScrollPane.Viewport.List.ClickItem("Capture")
    #Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel3.ScrollPane.Viewport.List.ClickItem("Sample OCR - 10 Fail", skShift | skCtrl)
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel2.Panel.Button.ClickButton()
  else:
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel.ScrollPane.Viewport.List.Keys("^a")
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel2.Panel.Button.ClickButton()
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel3.ScrollPane.Viewport.List.ClickItem("Capture")
    #Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel3.ScrollPane.Viewport.List.ClickItem("Sample OCR - 10 Fail", skShift | skCtrl)
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel2.Panel.Button.ClickButton()


#  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel.ScrollPane.Viewport.List.Keys("^a")
#  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel2.Panel.Button.ClickButton()
#  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel3.ScrollPane.Viewport.List.ClickItem("Capture")
#  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel2.Panel.Button.ClickButton()

#Train OCR without Search ROI
def Setup_AdvOCR():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane_ToolPalettePanelSplitPane_.ScrollPane.Viewport.Panel.ToolTree.ClickItemR("|[0]|Readers|Advanced OCR")
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane_ToolPalettePanelSplitPane_.ScrollPane.SwingPopupMenu.Click("Copy Advanced OCR")
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.ClickR(True)
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.SwingPopupMenu.Click("Paste Advanced OCR")

##  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane_ToolPalettePanelSplitPane_.ScrollPane.Viewport.Panel.ToolTree.ClickItem("|[0]|Readers")
##  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane_ToolPalettePanelSplitPane_.ScrollPane.Viewport.Panel.ToolTree.ClickItem("|[0]|Readers|Advanced OCR")
#  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane_ToolPalettePanelSplitPane_.ScrollPane.Viewport.Panel.ToolTree.Drag(39, 231, 213, -515)
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.BaseSetupPanel_ButtonBar_.ToolSetupCardPanel_HashcodeRadioButton2.ClickButton(True)
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_1.ROIEditor.Panel.ROIToolBar.Panel.ROIToolBar_4.ClickButton()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_1.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.Keys("[Del]")
  Setup_VPMTrainPanel()
  Delay(500)
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGTrainPanel.Panel.Panel.Panel.Button.ClickButton()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGTrainPanel.Panel.Panel.Panel.Button2.ClickButton()
  Setup_OCRClicktoTrain()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_2.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.Keys("lot2aw7")
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGTrainPanel.Panel2.Panel.Button.ClickButton()
 


def Setup_AdvOCREmpty():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane_ToolPalettePanelSplitPane_.ScrollPane.Viewport.Panel.ToolTree.ClickItemR("|[0]|Readers|Advanced OCR")
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane_ToolPalettePanelSplitPane_.ScrollPane.SwingPopupMenu.Click("Copy Advanced OCR")
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.ClickR(True)
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.SwingPopupMenu.Click("Paste Advanced OCR")
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.BaseSetupPanel_ButtonBar_.ToolSetupCardPanel_HashcodeRadioButton2.ClickButton(True)
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_1.ROIEditor.Panel.ROIToolBar.Panel.ROIToolBar_4.ClickButton()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_1.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.Keys("[Del]")
  Setup_VPMTrainPanel()

def Setup_AdvNotTrain():

  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGTrainPanel.Panel.Panel.Panel.Button.ClickButton()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGTrainPanel.Panel.Panel.Panel.Button2.ClickButton()
  Setup_OCRClicktoTrain()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_2.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.Keys("lot2aw7")

#Train OCR with Search ROI
def Setup_AdvOCRManual():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane_ToolPalettePanelSplitPane_.ScrollPane.Viewport.Panel.ToolTree.ClickItemR("|[0]|Readers|Advanced OCR")
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane_ToolPalettePanelSplitPane_.ScrollPane.SwingPopupMenu.Click("Copy Advanced OCR")
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.ClickR(True)
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.SwingPopupMenu.Click("Paste Advanced OCR")

  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.BaseSetupPanel_ButtonBar_.ToolSetupCardPanel_HashcodeRadioButton2.ClickButton(True)
  Setup_DrawROI()
  Setup_VPMTrainPanel()
  Setup_AdvSegmentNewLine()
  Setup_AdvAutoSegment()
  Setup_OCRClicktoTrain()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_2.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.Keys("lot2aw7")
  Setup_AdvTrainButton()
 

def Setup_DrawROI():
  displayCanvas = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_1.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas
  displayCanvas.Drag(290, 162, 286, 33)
  displayCanvas.Drag(320, 215, -44, 211)
  displayCanvas.Drag(150, 245, -138, 8)
  displayCanvas.Drag(349, 110, 17, -103)

def Setup_DrawROISmall():

  displayCanvas = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_1.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas
  displayCanvas.Drag(288, 150, 207, 11)
  displayCanvas.Drag(446, 215, -7, 119)
  displayCanvas.Drag(147, 114, -30, -1)

def Setup_RotateROI():
  displayCanvas = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_1.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas
  displayCanvas.Drag(464, 111, -33, 159)
  displayCanvas.Drag(107, 103, 68, -67)


def Setup_DragAvdToTaskTree():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane_ToolPalettePanelSplitPane_.ScrollPane.Viewport.Panel.ToolTree.ClickItemR("|[0]|Readers|Advanced OCR")
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane_ToolPalettePanelSplitPane_.ScrollPane.SwingPopupMenu.Click("Copy Advanced OCR")
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.ClickR(True)
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.SwingPopupMenu.Click("Paste Advanced OCR")


def Setup_DragOCRSetFronInputDrawer():
  tree = Aliases.javaw.CpmFrame4.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.BeanPalette.ScrollPane.Viewport.BeanPalette
  tree.ClickItem("|[0]|Input")
  tree.Drag(40, 297, 920, -97)

def Setup_ExpandAdvOCR():
  Aliases.javaw.CpmFrame.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.CPMPatchPanel.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.TasksTabbedPane_TaskTree_.Click(26, 122)

def Setup_DragOCRFontLibraryToCpFile():
  Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.CPMPatchPanel.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.TasksTabbedPane_TaskTree_.DblClickItem("Root|Image In Task|Advanced OCR 1")
  Delay(1000)
  Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.CPMPatchPanel.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.TasksTabbedPane_TaskTree_.ClickItemR("Root|Image In Task|Advanced OCR 1|OCR Font Library")

  Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.CPMPatchPanel.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.TasksTabbedPane_TaskTree_.SwingPopupMenu.Click("Set link to here")
  #Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.ScrollPane.Viewport.CpmFrame_252.P30.ClickR(173, 259)
  Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.ScrollPane.Viewport.CpmFrame_25.Panel_1.ClickR(173, 259)
  Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.ScrollPane.Viewport.CpmFrame_25.Panel_1.SwingPopupMenu.Click("Create OCR Font Library")
  Delay(5000)

  

  
def Setup_LinkOCRFontLibrary():
  ImageRepository.Propertytab.LinkOCRFLB.Click()
  ImageRepository.TreeView.ExpandOCR.Click()
  #Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.ClickItem("Root|Image In Task|Advanced OCR|OCR Font Library")
  scrollPane = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane
  #scrollPane.VScroll.Pos = 0
  scrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.ClickItem("Root|Image In Task|Advanced OCR 1|OCR Font Library")

def Setup_LinkOCRFontLibrarySetupTab():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGTrainPanel.Panel2.LinkPanel.ToggleButton.ClickButton(True)
  ImageRepository.TreeView.ExpandOCR.Click()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.ClickItem("Root|Image In Task|Advanced OCR 1|OCR Font Library")

def Setup_LinkSegmentation():
  ImageRepository.Propertytab.LinkSegmentaion.Click()
  ImageRepository.TreeView.ExpandOCR.Click()
  ImageRepository.TreeView.SegmentaionOCR.Click()

  
def Setup_LinkTrainCharacterBox():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[24, "B"]
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.ClickCell(24, "B") 
  ImageRepository.Propertytab.LinkCharacterBox.Click()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.ClickItem("Root|Image In Task|Advanced OCR 1")
  Aliases.javaw.VpmFrame.SwingPopupMenu.Click("Character Boxes")

def Setup_OCROutOfImage():
   Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_1.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.Drag(147, 111, 468, 123)

def Setup_CorrectROI():
   Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_1.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.Drag(617, 233, -510, -123)
   displayCanvas = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_1.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas
   displayCanvas.Drag(251, 177, 237, 11)
   displayCanvas.Drag(302, 215, 20, 89)
   
def Setup_OCRClickGreenROI():
   Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_2.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.Click(33, 24)

def Setup_OCRReset():
   Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.HOG_OCRSetup_HOGTrainPanel.Panel3.Panel.Panel.Panel.Panel2.Panel.Button.ClickButton()

#=================================================================CPM Setting===================================================================================
def Setup_DisableTypeOption():
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.ClickItem("|[0]|Panel 1|OCR Font Library2|Segmentation|Type:")
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.VScroll.Pos = 134
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.wValue[16, 3]
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.ClickCell(16, 3)
  Delay(200)
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.PropertySelector.ClickItem("False")

def Setup_DisableTypeText(): 
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.ClickItem("|[0]|Panel 1|OCR Font Library2|Segmentation|Type")
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.VScroll.Pos = 83
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.wValue[7, 3]
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.ClickCell(7, 3)
  Delay(200)
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.PropertySelector.ClickItem("False")

def Setup_DisableSegmentNewLine():
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.ClickItem("|[0]|Panel 1|OCR Font Library2|Segmentation|Segment New Line")
 
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.VScroll.Pos = 267
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.wValue[23, 3]
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.ClickCell(23, 3)
  Delay(200)
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.PropertySelector.ClickItem("False")

def Setup_DisableAutoSegment():
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.ClickItem("|[0]|Panel 1|OCR Font Library2|Segmentation|Auto Segment")
  
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.VScroll.Pos = 267
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.wValue[23, 3]
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.ClickCell(23, 3)
  Delay(200)
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.PropertySelector.ClickItem("False")

def Setup_DisableAddCharacterBox():  
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.ClickItem("|[0]|Panel 1|OCR Font Library2|Segmentation|Add Character Box")
 
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.VScroll.Pos = 267
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.wValue[23, 3]
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.ClickCell(23, 3)
  Delay(200)
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.PropertySelector.ClickItem("False")

def Setup_DisableTrainPrompt():  
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.ClickItem("|[0]|Panel 1|OCR Font Library2|Train Prompt")
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.VScroll.Pos = 134
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.wValue[16, 3]
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.ClickCell(16, 3)
  Delay(200)
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.PropertySelector.ClickItem("False")

def Setup_DisableTrainButton():  
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.ClickItem("|[0]|Panel 1|OCR Font Library2|Train")
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.VScroll.Pos = 267
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.wValue[23, 3]
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.ClickCell(23, 3)
  Delay(200)
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.PropertySelector.ClickItem("False")

def Setup_DisableOCRFontLibrary():
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.ClickItem("|[0]|Panel 1|OCR Font Library2|OCR Font Library")
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.VScroll.Pos = 77
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.wValue[12, 3]
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.ClickCell(12, 3)
  Delay(200)
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.PropertySelector.ClickItem("False")

def Setup_DisableFontLibraryDisplay():  
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.ClickItem("|[0]|Panel 1|OCR Font Library2|OCR Font Library|OCR Font Library Display")
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.wValue[6, 3]
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.ClickCell(6, 3)
  Delay(200)
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.PropertySelector.ClickItem("False")

def Setup_DisableSegmentation():
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.ClickItem("|[0]|Panel 1|OCR Font Library2|Segmentation")
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.VScroll.Pos = 77
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.wValue[12, 3]
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.ClickCell(12, 3)
  Delay(200)
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.PropertySelector.ClickItem("False")

def Setup_DisableSearchImage():  
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.ClickItem("|[0]|Panel 1|OCR Font Library2|Search Image")
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.VScroll.Pos = 533
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.wValue[29, 3]
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.ClickCell(29, 3)
  Delay(200)
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.PropertySelector.ClickItem("False")

def Setup_EnableTypeOption():  
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.ClickItem("|[0]|Panel 1|OCR Font Library2|Segmentation|Type:")
  
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.VScroll.Pos = 134
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.wValue[16, 3]
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.ClickCell(16, 3)
  Delay(200)
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.PropertySelector.ClickItem("True")
 

def Setup_EnableTypeText(): 
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.ClickItem("|[0]|Panel 1|OCR Font Library2|Segmentation|Type")
  
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.VScroll.Pos = 83
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.wValue[7, 3]
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.ClickCell(7, 3)
  Delay(200)
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.PropertySelector.ClickItem("True")


def Setup_EnableSegmentNewLine(): 
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.ClickItem("|[0]|Panel 1|OCR Font Library2|Segmentation|Segment New Line")
 
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.VScroll.Pos = 267
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.wValue[23, 3]
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.ClickCell(23, 3)
  Delay(200)
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.PropertySelector.ClickItem("True")

def Setup_EnableAutoSegment():
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.ClickItem("|[0]|Panel 1|OCR Font Library2|Segmentation|Auto Segment")
  
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.VScroll.Pos = 267
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.wValue[23, 3]
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.ClickCell(23, 3)
  Delay(200)
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.PropertySelector.ClickItem("True")

def Setup_EnableAddCharacterBox():    
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.ClickItem("|[0]|Panel 1|OCR Font Library2|Segmentation|Add Character Box")

  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.VScroll.Pos = 267
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.wValue[23, 3]
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.ClickCell(23, 3)
  Delay(200)
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.PropertySelector.ClickItem("True")

def Setup_EnableTrainPrompt():    
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.ClickItem("|[0]|Panel 1|OCR Font Library2|Train Prompt")
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.VScroll.Pos = 134
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.wValue[16, 3]
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.ClickCell(16, 3)
  Delay(200)
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.PropertySelector.ClickItem("True")

def Setup_EnableTrainButton():  
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.ClickItem("|[0]|Panel 1|OCR Font Library2|Train")
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.VScroll.Pos = 267
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.wValue[23, 3]
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.ClickCell(23, 3)
  Delay(200)
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.PropertySelector.ClickItem("True")

def Setup_EnableOCRFontLibrary():
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.ClickItem("|[0]|Panel 1|OCR Font Library2|OCR Font Library")
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.VScroll.Pos = 77
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.wValue[12, 3]
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.ClickCell(12, 3)
  Delay(200)
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.PropertySelector.ClickItem("True")

def Setup_EnableFontLibraryDisplay():    
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.ClickItem("|[0]|Panel 1|OCR Font Library2|OCR Font Library|OCR Font Library Display")
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.wValue[6, 3]
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.ClickCell(6, 3)
  Delay(200)
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.PropertySelector.ClickItem("True")

def Setup_EnableSegmentation():
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.ClickItem("|[0]|Panel 1|OCR Font Library2|Segmentation")
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.VScroll.Pos = 77
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.wValue[13, 3]
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.ClickCell(13, 3)
  Delay(200)
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.PropertySelector.ClickItem("True")
def Setup_EnableSearchImage():    
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.ClickItem("|[0]|Panel 1|OCR Font Library2|Search Image")
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.VScroll.Pos = 533
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.wValue[29, 3]
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.ClickCell(29, 3)
  Delay(200)
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.PropertySelector.ClickItem("True")

def Setup_EnableRunMode(): 
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.MainToolBar.Panel.DesignRunModeButton.ClickButton(True)

def Setup_DisableRunMode(): 
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.MainToolBar.Panel.DesignRunModeButton.ClickButton(False)
  


def Setup_CopyPasteOCRFontLibrary():
  splitPane = Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane
  tree = splitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree
  splitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.ClickItem("|[0]|Panel 1|OCR Font Library2")
  splitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.ClickItemR("|[0]|Panel 1|OCR Font Library2")
  splitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.SwingPopupMenu.Click("Copy")
  scrollPane = splitPane.SplitPane.ScrollPane
  scrollPane.VScroll.Pos = 0
  scrollPane.HScroll.Pos = 0
  controlPanel = scrollPane.Viewport.CpmFrame_25.Panel_1
  controlPanel.Click(174, 455)
  controlPanel.ClickR(174, 455)
  controlPanel.SwingPopupMenu.Click("Paste Control(s)")
  controlPanel.Click(217, 441)
  scrollPane.VScroll.Pos = 287
  
def Setup_CopyPasteTrainButton():

  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.ClickItem("|[0]|Panel 1|OCR Font Library2|Train")
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.ClickItemR("|[0]|Panel 1|OCR Font Library2|Train")
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.SwingPopupMenu.Click("Copy")
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.ScrollPane.Viewport.CpmFrame_25.Panel_1.Click(149, 645)
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.ScrollPane.Viewport.CpmFrame_25.Panel_1.ClickR(149, 645)
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.ScrollPane.Viewport.CpmFrame_25.Panel_1.SwingPopupMenu.Click("Paste Control(s)")
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.ScrollPane.Viewport.CpmFrame_25.Panel_1.Click(88, 644)

def Setup_OCRCPMDeletePattern():
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.OCRSet.OCRSetFrame.OCRSetDisplay.OCRSetPanel.ToolBar.Panel.Button.ClickButton()

def Setup_OCRCPMDeleteAllPattern():  
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.OCRSet.OCRSetFrame.OCRSetDisplay.OCRSetPanel.ToolBar.Panel.Button2.ClickButton()
  Aliases.javaw.Dialog30.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button2.ClickButton()

def Setup_CPMSaveAs(name):
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.MainToolBar.Panel.SaveAsButton.ClickButton()
  Aliases.javaw.SecurityFileChooser.RootPane.null_layeredPane.null_contentPane.SecurityFileChooser_FileChooserPanel.FileChooser.Panel.Panel.Panel2.WindowsFileChooserUI_7.Keys(name)  
  
def Setup_CPMLoadFile(name):
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.MainToolBar.Panel.OpenButton.ClickButton()
  Aliases.javaw.Dialog7.RootPane.null_layeredPane.null_contentPane.FileChooser.Panel.Panel.Panel2.WindowsFileChooserUI_7.Keys(name)
    
def Setup_DeleteFile(path):
  aqFileSystem.DeleteFile(path)  
################################################################Set up Pattern Sort Tool###################################################################
def Setup_LoadPSTImages():

  if Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel.ScrollPane.Viewport.List.wItemCount==10 and Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel.ScrollPane.Viewport.List.wItem[0] =="Sample Pattern Sort - 01 Fail":
    Log.Message("PSI Image existed - do nothing")
  elif Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel.ScrollPane.Viewport.List.wItemCount==0:
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel3.ScrollPane.Viewport.List.ClickItem("Sample Pattern Sort - 01 Fail")
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel3.ScrollPane.Viewport.List.ClickItem("Sample Pattern Sort - 10 Fail", skShift | skCtrl)
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel2.Panel.Button.ClickButton()
  
  else:
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel.ScrollPane.Viewport.List.Keys("^a")
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel2.Panel.Button.ClickButton()
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel3.ScrollPane.Viewport.List.ClickItem("Sample Pattern Sort - 01 Fail")
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel3.ScrollPane.Viewport.List.ClickItem("Sample Pattern Sort - 10 Fail", skShift | skCtrl)
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.FileCameraSetup_GeneralPanel.Panel.Panel.Panel2.Panel.Button.ClickButton()


def Setup_DragPatternSortToTaskTree():
 
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane_ToolPalettePanelSplitPane_.ScrollPane.Viewport.Panel.ToolTree.ClickItemR("|[0]|Feature Finding|Pattern Sort")
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane_ToolPalettePanelSplitPane_.ScrollPane.SwingPopupMenu.Click("Copy Pattern Sort")
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.ClickR(True)
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.SwingPopupMenu.Click("Paste Pattern Sort")

def Setup_PSTTrainPanel():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.BaseSetupPanel_ButtonBar_.ToolSetupCardPanel_HashcodeRadioButton.ClickButton(True)

  #Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.BaseSetupPanel_ButtonBar_.ToolSetupCardPanel_HashcodeRadioButton10.ClickButton(True)

def Setup_PSTLoadDB(foldername):
  
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel.Button.ClickButton()
  Aliases.javaw.Dialog3.RootPane.null_layeredPane.null_contentPane.PatternSortingSetup1_SortingTrainPanel_2_1.Panel.Panel.Panel.WindowsFileChooserUI_7.Keys(name1 + foldername + "\\" +foldername+".pdb")
  #Aliases.javaw.Dialog3.RootPane.null_layeredPane.null_contentPane.PatternSortingSetup1_SortingTrainPanel_2_1.Panel.FilePane.Panel.ScrollPane.Viewport.FilePane_4.ClickItemXY("test.pdb", 48, 12)
  Aliases.javaw.Dialog3.RootPane.null_layeredPane.null_contentPane.PatternSortingSetup1_SortingTrainPanel_2_1.Panel.Panel.Panel2.WindowsFileChooserUI_9.ClickButton()
  Delay(2000)
def Setup_PSTLoadDBSet(foldername, option):
  if foldername == None:
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel.Button.ClickButton()
  elif foldername == "":
    Log.Message("do nothing")
  else:
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel.Button.ClickButton()  
    Aliases.javaw.Dialog3.RootPane.null_layeredPane.null_contentPane.PatternSortingSetup1_SortingTrainPanel_2_1.Panel.Panel.Panel.WindowsFileChooserUI_7.Keys(name1 + foldername + "\\" +foldername+".pdb")
    #Aliases.javaw.Dialog3.RootPane.null_layeredPane.null_contentPane.PatternSortingSetup1_SortingTrainPanel_2_1.Panel.FilePane.Panel.ScrollPane.Viewport.FilePane_4.ClickItemXY("test.pdb", 48, 12)
    
    Delay(2000)
  if option == "load":
    Aliases.javaw.Dialog3.RootPane.null_layeredPane.null_contentPane.PatternSortingSetup1_SortingTrainPanel_2_1.Panel.Panel.Panel2.WindowsFileChooserUI_9.ClickButton()
  elif option == "cancel":
    Aliases.javaw.Dialog3.RootPane.null_layeredPane.null_contentPane.PatternSortingSetup1_SortingTrainPanel_2_1.Panel.Panel.Panel2.WindowsFileChooserUI_10.ClickButton()
  else:
    Log.Message("do nothing")
def Setup_PSTNewDBSet(name, option):
  
  #name = "\\\\192.168.0.13\\c\\Users\\hale\\Documents\\PST" + name
  if name != None:
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel.Button2.ClickButton()
    #def Setup_PSTNameDB(name):
    Aliases.javaw.Dialog4.RootPane.null_layeredPane.null_contentPane.PatternSortingSetup1_SortingTrainPanel_1_1.Panel.Panel.Panel.WindowsFileChooserUI_7.Keys(name1 +name)
#def Setup_PSTCancelNameDB():
    if option == "cancel":
      Aliases.javaw.Dialog4.RootPane.null_layeredPane.null_contentPane.PatternSortingSetup1_SortingTrainPanel_1_1.Panel.Panel.Panel2.WindowsFileChooserUI_10.ClickButton()
    elif option == "create":
      Aliases.javaw.Dialog4.RootPane.null_layeredPane.null_contentPane.PatternSortingSetup1_SortingTrainPanel_1_1.Panel.Panel.Panel2.WindowsFileChooserUI_9.ClickButton()
    else:
      Log.Message("BD has been created")
  else:
    if option == "cancel":
      Aliases.javaw.Dialog4.RootPane.null_layeredPane.null_contentPane.PatternSortingSetup1_SortingTrainPanel_1_1.Panel.Panel.Panel2.WindowsFileChooserUI_10.ClickButton()
    elif option == "create":
      Aliases.javaw.Dialog4.RootPane.null_layeredPane.null_contentPane.PatternSortingSetup1_SortingTrainPanel_1_1.Panel.Panel.Panel2.WindowsFileChooserUI_9.ClickButton()
    else:
      Log.Message("BD has been created")
    #Log.Message("do nothing")

def Setup_PSTNewDB():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel.Button2.ClickButton()

def Setup_PSTNameDB(name):
  Aliases.javaw.Dialog4.RootPane.null_layeredPane.null_contentPane.PatternSortingSetup1_SortingTrainPanel_1_1.Panel.Panel.Panel.WindowsFileChooserUI_7.Keys(name1+name)

def Setup_PSTCancelNameDB():       
  Aliases.javaw.Dialog4.RootPane.null_layeredPane.null_contentPane.PatternSortingSetup1_SortingTrainPanel_1_1.Panel.Panel.Panel2.WindowsFileChooserUI_10.ClickButton()
  
def Setup_PSTAddButton():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel2.Panel.Panel.Button.ClickButton()

def Setup_PSTCoppyPatternSort1():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.ClickItemR("Root|Image In Task|Pattern Sort 1")
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.SwingPopupMenu.Click("Copy")

def Setup_PSTPasteToTaskTree():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.ClickR(True)
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.SwingPopupMenu.Click("Paste Tool(s)")

def Setup_PSTOriginSetting():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.BaseSetupPanel_ButtonBar_.ToggleButton2.Click(True)
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.SwingObject("JPanel", "", 0).SwingObject("JPanel", "", 0).SwingObject("JRadioButton", "One Direction", 0).Click(True)
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.BaseSetupPanel_ButtonBar_.ToggleButton.ClickButton(True)
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.Origin2Setup_OriginSetupPanel_1.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.Drag(214, 109, -23, -17)

def Setup_PSTResizeROI():
  displayCanvas = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.PatternSortingSetup1_PatternSortingSetupPanel_1.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas
  displayCanvas.Drag(144, 111, 59, 52)
  displayCanvas.Drag(349, 227, -30, 3)
  displayCanvas.Drag(201, 219, 22, -1)
 
def PST_ProClick():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.ClickCell(7, "A")
def PST_ProClick1():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.ClickCell(7, "D")
def PST_ClickItem():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.ClickItem("Root|Image In Task|Pattern Sort 1")  
def Setup_PSTAddROI():
  panel = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.PatternSortingSetup1_PatternSortingSetupPanel_1.ROIEditor.Panel
  ROIToolBar = panel.ROIToolBar
  ROIToolBar.Panel.ROIToolBar_ROITypeToggleButton.ClickButton(True)
  ROIToolBar.SwingPopupMenu.Click("[0]")
  displayCanvas = panel.Panel.ScrollPane.Viewport.DisplayCanvas
  displayCanvas.Drag(160, 70, 37, 78)
  displayCanvas.Drag(181, 88, 34, 57)
  
def Setup_PSTDeleteROI():
  displayCanvas = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.PatternSortingSetup1_PatternSortingSetupPanel_1.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas
  #displayCanvas.Click(145, 112)
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.PatternSortingSetup1_PatternSortingSetupPanel_1.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.Click(132, 100)

  displayCanvas.Keys("[Del]")
  
def Setup_PSTDBPanel():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.BaseSetupPanel_ButtonBar_.ToolSetupCardPanel_HashcodeRadioButton2.ClickButton(True)

def Setup_PSTDeletePattern():
   Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ToolBar.Panel.Button.ClickButton()

def Setup_PSTAddLabel(panel, label):
  if panel != "db":
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel2.Panel.PatternSortModelDropdown.BasicComboBoxEditor_BorderlessTextField.Keys(label)
  else:
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.Panel.Panel.Panel.PatternSortModelDropdown2.BasicComboBoxEditor_BorderlessTextField.Keys(label)
 

def Setup_PSTAddInfo(panel, info):
  if panel != "db":
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel2.Panel.PatternSortModelDropdown2.BasicComboBoxEditor_BorderlessTextField.Click(True)
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel2.Panel.PatternSortModelDropdown2.BasicComboBoxEditor_BorderlessTextField.Keys(info)
  else:
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.Panel.Panel.Panel.PatternSortModelDropdown.BasicComboBoxEditor_BorderlessTextField.Click()  
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.Panel.Panel.Panel.PatternSortModelDropdown.BasicComboBoxEditor_BorderlessTextField.Keys(info)



    

  
def Setup_PSTCheck():
  if aqFileSystem.Exists("C:\\Datalogic\\IMPACT\\Applications\\Emulator\\EmulatorRoot\\PST"):
    if aqFileSystem.Exists("\\\\192.168.0.13\\c\\Users\\hale"):
      Log.Message("exist mapped folder")
      folder = aqFileSystem.FindFolders("\\\\192.168.0.13\\c\\Users\\hale\\Documents\\PST", "*PST")
      currentfolder = aqFileSystem.GetCurrentFolder()
      path = currentfolder + "\\PST"
      if folder == None:

        Log.Message(path)
        #aqFileSystem.DeleteFolder("\\\\192.168.0.13\\c\\Users\\hale\\Documents", True)
        aqFileSystem.CopyFolder(path, "\\\\192.168.0.13\\c\\Users\\hale\\Documents")
        #aqFileSystem.RenameFolder("\\\\192.168.0.13\\c\\Users\\hale\\Documents\\Copy of PST", "\\\\192.168.0.13\\c\\Users\\hale\\Documents\\PST")
        Log.Message("coppy datat test")
      else:
        
        #aqFileSystem.DeleteFolder("\\\\192.168.0.13\\c\\Users\\hale\\Documents", True)
        aqFileSystem.CopyFolder(path, "\\\\192.168.0.13\\c\\Users\\hale\\Documents")
        aqFileSystem.RenameFolder("\\\\192.168.0.13\\c\\Users\\hale\\Documents\\Copy of PST", "\\\\192.168.0.13\\c\\Users\\hale\\Documents\\PST")
         

    else:
      folder = aqFileSystem.FindFolders("C:\\Datalogic\\IMPACT\\Applications\\Emulator\\EmulatorRoot\\PST", "*Test")
      currentfolder = aqFileSystem.GetCurrentFolder()
      path = currentfolder + "\\PST"
      if folder == None:

        aqFileSystem.CopyFolder(path, "C:\\Datalogic\\IMPACT\\Applications\\Emulator\\EmulatorRoot")
        aqFileSystem.RenameFolder("C:\\Datalogic\\IMPACT\\Applications\\Emulator\\EmulatorRoot\\Copy of PST", "C:\\Datalogic\\IMPACT\\Applications\\Emulator\\EmulatorRoot\\PST")
        Log.Message("coppy datat test")
      else:
        Log.Message("Folder exist")
      
  else:
    folder = aqFileSystem.FindFolders("C:\\Datalogic\\IMPACT\\Applications\\Device\\DeviceRoot\\PST", "*Test")
    if folder == None:
      currentfolder = aqFileSystem.GetCurrentFolder()
      path = currentfolder + "\\PST"
      aqFileSystem.CopyFolder(path, "C:\\Datalogic\\IMPACT\\Applications\\Device\\DeviceRoot")
      aqFileSystem.RenameFolder("C:\\Datalogic\\IMPACT\\Applications\\Device\\DeviceRoot\\Copy of PST", "C:\\Datalogic\\IMPACT\\Applications\\Device\\DeviceRoot\\PST")
    else:
      Log.Message("Folder exist")

def Setup_PSTDeleteFoder(foldername):
  if aqFileSystem.Exists("C:\\Datalogic\\IMPACT\\Applications\\Emulator\\EmulatorRoot\\PST"):
    path = "\\\\192.168.0.13\\c\\Users\\hale\\Documents\\PST\\"+ foldername
    Log.Message(path)
    aqFileSystem.DeleteFolder(path, True)
    
  else:
     aqFileSystem.DeleteFolder("C:\\Datalogic\\IMPACT\\Applications\\Device\\DeviceRoot\\"+ foldername, True)

 

def Setup_PSTAdjustROI():
  b = ImageRepository.DrawROI.ROI1.FindPosition()
  c = ImageRepository.DrawROI.ROI3.FindPosition()
  if b !=None and c!=None:
    x = b.Width/2
    y = b.Height/2
    dx = c.Width/2
    dy = c.Height/2
    ImageRepository.DrawROI.ROI1.Drag(x, y, dx, dy)
  else:
    Log.Message("point not found")
 
def Setup_PSTAdvance(panel):
  if panel == "db":
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.Panel.Panel.Panel.Panel.Button.ClickButton()
  else:
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel2.Panel.Panel.Button2.ClickButton()

def Setup_PSTMaxNumberOfKeypoint(numberofkeypoint):

  Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane.ClickTab("Contour")
  Delay(200)
  Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane.Panel.Panel.PatchableIntegerTextField.Keys(numberofkeypoint)
  Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.Panel.Button2.ClickButton()
  
def Setup_PSTDownSamplingRatio(tab, numberofdownsampling): 
  if tab== "Countour":
    Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane.ClickTab("Contour")
    Delay(200) 
    Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane2.Panel.Panel.PatchableRealTextField.Keys(numberofdownsampling)
    Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.Panel.Button2.ClickButton()
  elif tab == "Edge Match":
    Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane.ClickTab("Edge Match")
    Delay(200) 
    Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane3.Panel.Panel.PatchableRealTextField.Keys(numberofdownsampling)
    Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.Panel.Button2.ClickButton() 
  else:   
    Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane.ClickTab("Texture")
    Delay(200) 
    Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane.Panel2.Panel.PatchableRealTextField.Keys(numberofdownsampling)
    Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.Panel.Button2.ClickButton()
  

def Setup_PSTSClusterPerKeypoint(option, numberofcluster): 
  Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane.ClickTab("Contour")
  Delay(200) 
  Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane2.Panel.Panel.PatchableIntegerTextField2.Keys(numberofcluster)
  if option == "ok":
    Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.Panel.Button2.ClickButton()
  
  elif option == "cancel":
    Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.Panel.Button.ClickButton()

def Setup_PSTRetrainAll(panel, option):
  if panel == "train":
   Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel3.Panel.Button.ClickButton()
  else:
   Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.Panel.Panel2.Button.ClickButton()
  if option == "cancel":
    Aliases.javaw.Dialog2.RootPane.null_layeredPane.null_contentPane.Panel.Panel.Button.ClickButton()
  else:
    Log.Message("do nothing")

def Setup_PSTMode(mode):
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel2.Panel.PatchableComboBox.WindowsComboBoxUI_XPComboBoxButton.ClickButton()
  if mode == "Contour":
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel2.Panel.PatchableComboBox.ClickItem("Contour")

  elif mode == "Texture":
   Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel2.Panel.PatchableComboBox.ClickItem("Texture")
  else:
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel2.Panel.PatchableComboBox.ClickItem("Edge Match")
  #patchableComboBox = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel2.Panel.PatchableComboBox
#  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel2.Panel.PatchableComboBox.WindowsComboBoxUI_XPComboBoxButton.ClickButton()
#  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel2.Panel.PatchableComboBox.ClickItem("Contour")

def Setup_PSTModeDB(mode):
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.Panel.Panel.Panel.ComboBox.WindowsComboBoxUI_XPComboBoxButton.ClickButton()
  if mode == "Contour":
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.Panel.Panel.Panel.ComboBox.ClickItem("Contour")

  elif mode == "Texture":
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.Panel.Panel.Panel.ComboBox.ClickItem("Texture")
  else:
     Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.Panel.Panel.Panel.ComboBox.ClickItem("Edge Match")


#Setiting all option in advance
def Setup_PSTAdvanceSet(panel, tab, numberofdownsampling, numberscale, numberofcluster, numberofkeypoint, maxdip, peakthreshold, upsample, maxduplicatepoint, option):
  if panel == "db":
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.Panel.Panel.Panel.Panel.Button.ClickButton()
  elif panel == None:
    Log.Message("do nothing")
  else:
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel2.Panel.Panel.Button2.ClickButton()

  if tab == "Contour":

     Delay(200)
     Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane2.Panel.Panel.PatchableRealTextField.Keys(numberofdownsampling)
     Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane2.Panel.Panel.PatchableIntegerTextField.Keys(numberscale)         
     Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane2.Panel.Panel.PatchableIntegerTextField2.Keys(numberofcluster)
     Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane2.Panel.Panel.PatchableIntegerTextField3.Keys(numberofkeypoint)
     
  elif tab == "Edge Match":
  
     Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane3.Panel.Panel.PatchableRealTextField.Keys(numberofdownsampling)

  elif tab == "Texture":
      
    Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane.Panel2.Panel.PatchableRealTextField.Keys(numberofdownsampling)
    Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane.Panel2.Panel.PatchableRealTextField3.Keys(maxdip)
    Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane.Panel2.Panel.PatchableRealTextField2.Keys(peakthreshold)

    Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane.Panel2.Panel.PatchableIntegerTextField.Keys(maxduplicatepoint)
    if upsample == True:
      Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane.Panel2.Panel.PatchableCheckBox.ClickButton(True)
      #Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog3.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane.Panel.Panel.PatchableCheckBox.ClickButton(True)
    elif upsample == False:
      Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane.Panel2.Panel.PatchableCheckBox.ClickButton(False)
    else:
      Log.Message("do nothing")

  if option == "ok":
     Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.Panel.Button2.ClickButton()
     if Aliases.javaw.Dialog12.Exists:
      Aliases.javaw.Dialog12.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
      Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.Panel.Button2.ClickButton()
     else:
      Log.Message("do nothing")
  elif option == "cancel":
     Aliases.javaw.PatternSortingSetup1_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.Panel.Button.ClickButton()
     
  else:
     Log.Message("do nothing")
 
def Setup_PSTAutomode():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel3.Panel.PatchableCheckBox.ClickButton(True)

 
def Setup_PSTPassFailPanel(): 
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.BaseSetupPanel_ButtonBar_.ToolSetupCardPanel_HashcodeRadioButton3.Click(True)

def Setup_PSTAddPatternImage(ImageName):
   Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ToolBar.Panel.Button2.ClickButton()
   a = aqFileSystem.GetCurrentFolder()
   Aliases.javaw.Dialog20.RootPane.null_layeredPane.null_contentPane.FileChooser.Panel.Panel.Panel.WindowsFileChooserUI_7.Keys(a + "\\PST\\Image\\" +ImageName +"[Enter]")
  
def Setup_PSTImport(name, option):
  
  if name == None:
    Log.Message("do nothing")
  else:
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ToolBar.Panel.Button4.ClickButton()

    Aliases.javaw.Dialog21.RootPane.null_layeredPane.null_contentPane.PatternSortDatabaseViewer_28.Panel.Panel.Panel2.WindowsFileChooserUI_7.Keys(name1+name)
  if option == "cancel":
    Aliases.javaw.Dialog21.RootPane.null_layeredPane.null_contentPane.PatternSortDatabaseViewer_28.Panel.Panel.Panel.WindowsFileChooserUI_10.ClickButton()
  else: 
    Log.Message("do nothing")
  
def Setup_PSTRoot():  

    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.ClickCell(8, "E")
    
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.Panel.ExtendedTextField.Keys(name1 + "[Enter]")
    
  
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.ClickCell(10, "E")
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.Panel.ExtendedTextField.Keys(name1)

def Setup_VPMloadvp():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.Panel.Main_Toolbar.LoadProgramButton.ClickButton()
  Aliases.javaw.ToolBar_LoadProgramAction_LoadProgramDialog.RootPane.null_layeredPane.null_contentPane.Panel.Panel.VisionProgramsPanel.ScrollPane.Viewport.Table.ClickCell(0, "File Name")
  Aliases.javaw.ToolBar_LoadProgramAction_LoadProgramDialog.RootPane.null_layeredPane.null_contentPane.Panel.Panel2.Button.ClickButton()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.ClickItem("Root|Image In Task|Pattern Sort 1")
  Setup_VPMtriggerOne()
  
def Setup_PSTExport(name, option):
 
  if name == None:
    Log.Message("do nothing")
  else:
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ToolBar.Panel.Button5.ClickButton()

    Aliases.javaw.Dialog23.RootPane.null_layeredPane.null_contentPane.PatternSortDatabaseViewer_25.Panel.Panel.Panel.WindowsFileChooserUI_7.Keys(name)
  if option == "cancel":
    Aliases.javaw.Dialog23.RootPane.null_layeredPane.null_contentPane.PatternSortDatabaseViewer_25.Panel.Panel.Panel2.WindowsFileChooserUI_10.ClickButton()
  elif option == "export":
     Aliases.javaw.Dialog23.RootPane.null_layeredPane.null_contentPane.PatternSortDatabaseViewer_25.Panel.Panel.Panel2.WindowsFileChooserUI_9.ClickButton()
  else: 
    Log.Message("do nothing")

def Setup_PSTAddImage(name, option):
 
  if name == None:
    Log.Message("do nothing")
  else:
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ToolBar.Panel.Button2.ClickButton()

    Aliases.javaw.Dialog20.RootPane.null_layeredPane.null_contentPane.FileChooser.Panel.Panel.Panel.WindowsFileChooserUI_7.Keys(name1 + name)
  if option == "cancel":
    Aliases.javaw.Dialog20.RootPane.null_layeredPane.null_contentPane.FileChooser.Panel.Panel.Panel2.WindowsFileChooserUI_10.ClickButton()
  elif option == "add":
     Aliases.javaw.Dialog20.RootPane.null_layeredPane.null_contentPane.FileChooser.Panel.Panel.Panel2.WindowsFileChooserUI_9.ClickButton()
  else: 
    Log.Message("do nothing")
  #Aliases.javaw.Dialog24.RootPane.null_layeredPane.null_contentPane.FileChooser.Panel.Panel.Panel.WindowsFileChooserUI_7.Click(68, 10)

def Setup_PSTDeleteAllPatten():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ToolBar.Panel.Button7.ClickButton()
  Aliases.javaw.Dialog22.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button2.ClickButton()
  
def Setup_PSTRunpropertytab():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.VPMMethodBar.Button.ClickButton()
 
def Setup_PSTSort():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ToolBar.Panel.Button3.ClickButton()
  
  
def Setup_PSTDisplay(option):
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ToolBar.Panel.ToggleButton2.ClickButton(option)

def Setup_PSTDisplayTrainingModeROI(option):
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ToolBar.Panel.ToggleButton.ClickButton(option)

def Setup_PSTZoomin():
   Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ToolBar.Panel.Button8.ClickButton()

def Setup_PSTZoomOut():
   Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ToolBar.Panel.Button9.ClickButton()
 
def Setup_PSTZoom100():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ToolBar.Panel.Button10.ClickButton()

def Setup_PSTTrainROI(option):
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.PatternSortDatabaseViewer.Panel.ToolBar.Panel.ToggleButton3.ClickButton(option)

def Setup_PSTLinkDB():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.Panel.Panel2.LinkPanel.ToggleButton.ClickButton(True)  
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.DblClickItem("Root|Image In Task|Pattern Sort")
  ImageRepository.LinkButton.LinkDatabase.Click()

def Setup_PSTMatchScore(option, score):
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingPassFailPanel.Panel2.Panel.Panel.PatchableCheckBox.ClickButton(option)
    if score != None:
      Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingPassFailPanel.Panel2.Panel.Panel.PatchableRealTextField2.Keys(score)
    else:
      Log.Message("do nothing")

def Setup_PSTMatchFraction(option, score):
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingPassFailPanel.Panel2.Panel.Panel.PatchableCheckBox2.ClickButton(True)
    #Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingPassFailPanel.Panel2.Panel.Panel.PatchableCheckBox3.ClickButton(option)
    if score != None:
      Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingPassFailPanel.Panel2.Panel.Panel.PatchableRealTextField3.Keys(score)
    else:
      Log.Message("do nothing")
  

def Setup_PSTMatchConfidence(option, score):
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingPassFailPanel.Panel2.Panel.Panel.PatchableCheckBox3.ClickButton(option)

    #Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingPassFailPanel.Panel2.Panel.Panel.PatchableCheckBox2.ClickButton(option)
    if score != None:
       Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingPassFailPanel.Panel2.Panel.Panel.PatchableRealTextField4.Keys(score)
    else:
      Log.Message("do nothing")
def Setup_PSTEnableFailedMatch(option):
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingPassFailPanel.Panel2.Panel2.Panel2.Panel.PatchableCheckBox.ClickButton(option)
 
def Setup_PSTIndependentMatchScore(option, score):
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingPassFailPanel.Panel2.Panel.Panel.CheckBox.ClickButton(option) 
    if score != None:
         Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingPassFailPanel.Panel2.Panel.Panel.TextField.Keys(score)
    else:
      Log.Message("do nothing")
 
def Setup_PSTTrainProperties():
   Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.VPMMethodBar.Button2.ClickButton()

def Setup_PSTLinkPatternDB():
  Setup_PSTDBPanel()
  splitPane = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingDatabasePanel.Panel.Panel.Panel.Panel.Panel2.LinkPanel.ToggleButton.ClickButton(True)  
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.DblClickItem("Root|Image In Task|Pattern Sort 1")

  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.wItems.Item[0].Items.Item[1].Items.Item[0].Items.Item[7].Click()

  
def Setup_PSTRunButton():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.VPMMethodBar.Button.ClickButton()

def Setup_PSTResetButton():
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.VPMMethodBar.Button3.ClickButton()
    
def Setup_PSTCPMDragDropPatternDBToPanel():
  Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.CPMPatchPanel.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.TasksTabbedPane_TaskTree_.DblClickItem("Root|Image In Task|Pattern Sort 1")
  Delay(5000)
  Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.CPMPatchPanel.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.TasksTabbedPane_TaskTree_.ClickItemR("Root|Image In Task|Pattern Sort 1|Pattern Database")

  Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.CPMPatchPanel.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.TasksTabbedPane_TaskTree_.SwingPopupMenu.Click("Get link from here")

  Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.ScrollPane.Viewport.CpmFrame_25.Panel_1.ClickR(173, 259)
  Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.ScrollPane.Viewport.CpmFrame_25.Panel_1.SwingPopupMenu.Click("Create Pattern Database")
  Delay(5000)

def Setup_PSTCPMNewDb(name, option):
  
  if name != None:
    Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.NewButton.ClickButton()

    Aliases.javaw.Dialog4.RootPane.null_layeredPane.null_contentPane.PatternSortDatabase_15.Panel.Panel.Panel.WindowsFileChooserUI_7.Keys(name1 +name)

    if option == "cancel":
      Aliases.javaw.Dialog4.RootPane.null_layeredPane.null_contentPane.PatternSortDatabase_15.Panel.Panel.Panel2.WindowsFileChooserUI_10.ClickButton()
    elif option == "create":
      Aliases.javaw.Dialog4.RootPane.null_layeredPane.null_contentPane.PatternSortDatabase_15.Panel.Panel.Panel2.WindowsFileChooserUI_9.ClickButton()
    else:
      Log.Message("BD has been created")
  else:
    if option == "cancel":
      Aliases.javaw.Dialog4.RootPane.null_layeredPane.null_contentPane.PatternSortDatabase_15.Panel.Panel.Panel2.WindowsFileChooserUI_10.ClickButton()
    elif option == "create":
      Aliases.javaw.Dialog4.RootPane.null_layeredPane.null_contentPane.PatternSortDatabase_15.Panel.Panel.Panel2.WindowsFileChooserUI_9.ClickButton()
    else:
      Log.Message("BD has been created")
  Delay(5000)
def Setup_PSTCPMAddLabelInfo(button, label, info, mode, option):
  if button == False:
    Log.Message("do nothing")
  else:
      Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternFrame.AddButton.ClickButton()
      if label != None:
        
        Aliases.javaw.PatternSortDatabase_AddPatternDialog.RootPane.null_layeredPane.null_contentPane.Panel.Panel.Panel.PatternSortModelDropdown.BasicComboBoxEditor_BorderlessTextField.Keys(label)
      else:
        Log.Message("do nothing")
      if info != None:
        Aliases.javaw.PatternSortDatabase_AddPatternDialog.RootPane.null_layeredPane.null_contentPane.Panel.Panel.Panel.PatternSortModelDropdown2.BasicComboBoxEditor_BorderlessTextField.Keys(info)
  
      if mode == "Texture":
        Aliases.javaw.PatternSortDatabase_AddPatternDialog.RootPane.null_layeredPane.null_contentPane.Panel.Panel.Panel.ComboBox.ClickItem("Texture")
      elif mode == "Edge Match":
        Aliases.javaw.PatternSortDatabase_AddPatternDialog.RootPane.null_layeredPane.null_contentPane.Panel.Panel.Panel.ComboBox.ClickItem("Edge Match")
      elif mode == "Contour":
        Aliases.javaw.PatternSortDatabase_AddPatternDialog.RootPane.null_layeredPane.null_contentPane.Panel.Panel.Panel.ComboBox.ClickItem("Contour")      
      elif mode == "Auto-Selected":
        Aliases.javaw.PatternSortDatabase_AddPatternDialog.RootPane.null_layeredPane.null_contentPane.Panel.Panel.Panel.ComboBox.ClickItem("Auto-Selected")
      else:
        Log.Message("do nothing")      
      if option == "add":
        
        Aliases.javaw.PatternSortDatabase_AddPatternDialog.RootPane.null_layeredPane.null_contentPane.Panel.Panel2.Button.ClickButton()
      elif option == "cancel":
        Aliases.javaw.PatternSortDatabase_AddPatternDialog.RootPane.null_layeredPane.null_contentPane.Panel.Panel2.Button2.ClickButton()
      else:
        Log.Message("do nothing")

def Setup_PSTCPMAdvanceSet(panel, tab, numberofdownsampling, numberscale, numberofcluster, numberofkeypoint, maxdip, peakthreshold, upsample, maxduplicatepoint, option):
  if panel == "add":
    Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternFrame.AddButton.ClickButton()
    Aliases.javaw.PatternSortDatabase_AddPatternDialog.RootPane.null_layeredPane.null_contentPane.Panel.Panel.Panel.Button.ClickButton()
  elif panel == None:
    Log.Message("do nothing")
  else:
     Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternFrame.AdvancedButton.ClickButton()

  if tab == "Contour":

     Delay(200)
     Aliases.javaw.PatternSortDatabase_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane.Panel.Panel.NumericEntry_2.Keys(numberofdownsampling)
     Aliases.javaw.PatternSortDatabase_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane.Panel.Panel.NumericEntry_22.Keys(numberscale)   
     Aliases.javaw.PatternSortDatabase_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane.Panel.Panel.NumericEntry_23.Keys(numberofcluster)
     Aliases.javaw.PatternSortDatabase_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane.Panel.Panel.NumericEntry_24.Keys(numberofkeypoint)
     
  elif tab == "Edge Match":
  
       Aliases.javaw.PatternSortDatabase_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane2.Panel.Panel.NumericEntry_2.Keys(numberofdownsampling)

  elif tab == "Texture":
    Aliases.javaw.PatternSortDatabase_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane3.Panel.Panel.NumericEntry_2.Keys(numberofdownsampling)
    Aliases.javaw.PatternSortDatabase_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane3.Panel.Panel.NumericEntry_22.Keys(maxdip)
    Aliases.javaw.PatternSortDatabase_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane3.Panel.Panel.NumericEntry_23.Keys(peakthreshold)
    
    Aliases.javaw.PatternSortDatabase_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane3.Panel.Panel.NumericEntry_24.Keys(maxduplicatepoint)     

    if upsample == True:
      Aliases.javaw.PatternSortDatabase_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane3.Panel.Panel.CheckBox.ClickButton(True)
     
    elif upsample == False:
      Aliases.javaw.PatternSortDatabase_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane3.Panel.Panel.CheckBox.ClickButton(False)
    else:
      Log.Message("do nothing")

  if option == "ok":
     Aliases.javaw.PatternSortDatabase_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.Panel.Button.ClickButton()
     
  elif option == "cancel":
    Aliases.javaw.PatternSortDatabase_AdvancedTrainDialog2.RootPane.null_layeredPane.null_contentPane.Panel.Panel.Button2.ClickButton()
     
  else:
     Log.Message("do nothing")
  #Aliases.javaw.PatternSortDatabase_AdvancedTrainDialog.RootPane.null_layeredPane.null_contentPane.Panel.TabbedPane.Panel.Panel.NumericEntry_2.Click(60, 14)


def Setup_PSTCPMRetrainAll(option):
  Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.RetrainButton.ClickButton()
  if option == "cancel":   
    Aliases.javaw.Dialog2.RootPane.null_layeredPane.null_contentPane.Panel.Panel.Button.ClickButton()
  else:
    Log.Message("do nothing")

def Setup_PSTCPMUpdateMode(mode):
  Delay(700)
  Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternFrame.ModeValue.ClickItem(mode) 


def Setup_PSTCPMLoadDB(name, option):  

 if name != None:
    Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.LoadButton.ClickButton()

    Aliases.javaw.Dialog3.RootPane.null_layeredPane.null_contentPane.PatternSortDatabase_13.Panel.Panel.Panel.WindowsFileChooserUI_7.Keys("\\\\192.168.0.13\\c\\Users\\hale\\Documents\\PST\\" + name)

    if option == "cancel":
      Aliases.javaw.Dialog3.RootPane.null_layeredPane.null_contentPane.PatternSortDatabase_13.Panel.Panel.Panel2.WindowsFileChooserUI_10.ClickButton()
    elif option == "load":
      Aliases.javaw.Dialog3.RootPane.null_layeredPane.null_contentPane.PatternSortDatabase_13.Panel.Panel.Panel2.WindowsFileChooserUI_9.ClickButton()
    else:
      Log.Message("BD has been created")
 else:
    if option == "cancel":
      Aliases.javaw.Dialog3.RootPane.null_layeredPane.null_contentPane.PatternSortDatabase_13.Panel.Panel.Panel2.WindowsFileChooserUI_10.ClickButton()
    elif option == "load":
      Aliases.javaw.Dialog3.RootPane.null_layeredPane.null_contentPane.PatternSortDatabase_13.Panel.Panel.Panel2.WindowsFileChooserUI_9.ClickButton()
    else:
      Log.Message("BD has been created")

def Setup_PSTCPMDeletePattern():
  Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternSortDatabaseDisplay.PatternSortDatabaseViewer.Panel.ToolBar.Panel.Button.ClickButton()



def Setup_PSTCPMAddImage(name, option):
  if name == None:
    Log.Message("do nothing")
  else:
    Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternSortDatabaseDisplay.PatternSortDatabaseViewer.Panel.ToolBar.Panel.Button2.ClickButton() 
    Aliases.javaw.Dialog20.RootPane.null_layeredPane.null_contentPane.FileChooser.Panel.Panel.Panel.WindowsFileChooserUI_7.Keys(name)
  if option == "add":
    Aliases.javaw.Dialog20.RootPane.null_layeredPane.null_contentPane.FileChooser.Panel.Panel.Panel2.WindowsFileChooserUI_9.ClickButton()
  elif option == "cancel":
    Aliases.javaw.Dialog20.RootPane.null_layeredPane.null_contentPane.FileChooser.Panel.Panel.Panel2.WindowsFileChooserUI_10.ClickButton()
  else: 
    Log.Message("do nothing")

def Setup_PSTCPMDeleteall():
  Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternSortDatabaseDisplay.PatternSortDatabaseViewer.Panel.ToolBar.Panel.Button3.ClickButton()
  Aliases.javaw.Dialog22.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button2.ClickButton()

def Setup_PSTCPMExportDb(name, option):
  #global name1
  if name == None:
    Log.Message("do nothing")
  else:
    Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternSortDatabaseDisplay.PatternSortDatabaseViewer.Panel.ToolBar.Panel.Button5.ClickButton()
    Aliases.javaw.Dialog23.RootPane.null_layeredPane.null_contentPane.PatternSortDatabaseViewer_25.Panel.Panel.Panel.WindowsFileChooserUI_7.Keys(name)

  if option == "cancel":
    Aliases.javaw.Dialog23.RootPane.null_layeredPane.null_contentPane.PatternSortDatabaseViewer_25.Panel.Panel.Panel2.WindowsFileChooserUI_10.ClickButton()
  elif option == "export":
     Aliases.javaw.Dialog23.RootPane.null_layeredPane.null_contentPane.PatternSortDatabaseViewer_25.Panel.Panel.Panel2.WindowsFileChooserUI_9.ClickButton()
  else: 
    Log.Message("do nothing")
 
 
def Setup_PSTCPMImportDb(name, option):
  #global name1
  if name == None:
    Log.Message("do nothing")
  else:
    Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternSortDatabaseDisplay.PatternSortDatabaseViewer.Panel.ToolBar.Panel.Button4.ClickButton() 
    Aliases.javaw.Dialog21.RootPane.null_layeredPane.null_contentPane.PatternSortDatabaseViewer_28.Panel.Panel.Panel2.WindowsFileChooserUI_7.Keys(name)
 
  if option == "cancel":
    Aliases.javaw.Dialog20.RootPane.null_layeredPane.null_contentPane.FileChooser.Panel.Panel.WindowsFileChooserUI_10.ClickButton() 
  elif option == "import": 
    Aliases.javaw.Dialog20.RootPane.null_layeredPane.null_contentPane.FileChooser.Panel.Panel.WindowsFileChooserUI_9.ClickButton()
  else: 
    Log.Message("do nothing")
    
def Setup_PSTCPMSort(option):
  Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternSortDatabaseDisplay.PatternSortDatabaseViewer.Panel.ToolBar.Panel.Button6.ClickButton()
  Aliases.javaw.CpmFrame2.SwingPopupMenu.Click(option)
  
def Setup_PSTCPMZoom(option):
  if option == "in":
    Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternSortDatabaseDisplay.PatternSortDatabaseViewer.Panel.ToolBar.Panel.Button7.ClickButton()
  elif option == "out":
    Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternSortDatabaseDisplay.PatternSortDatabaseViewer.Panel.ToolBar.Panel.Button8.ClickButton()
  else:
    Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternSortDatabaseDisplay.PatternSortDatabaseViewer.Panel.ToolBar.Panel.Button9.ClickButton()
  
def Setup_PSTCPMPoint(option):    
  Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.ScrollPane.Viewport.CpmFrame_25.Panel_1.PatternSortDatabase.PatternSortDatabaseDisplay.PatternSortDatabaseViewer.Panel.ToolBar.Panel.ToggleButton.ClickButton(option)

def Setup_CPMRename(name):
  Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.ScrollPane.Viewport.ControlStatusPane.Panel.TextField.Keys(name)
  
def Setup_CPMCopyItem(item):
  Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.ClickItemR(item)
  Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.SwingPopupMenu.Click("Copy")
#  Aliases.explorer.wndShell_TrayWnd.ReBarWindow32.MSTaskSwWClass.MSTaskListWClass.Click(671, 14)
#  splitPane = Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane
#  tree = splitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree
#  tree.ClickItemR("|[0]|Panel 1|OCR test")
#  tree.SwingPopupMenu.Click("Copy")
#  scrollPane = splitPane.SplitPane.ScrollPane
#  scrollPane.VScroll.Pos = 0
#  scrollPane.HScroll.Pos = 0
#  controlPanel = scrollPane.Viewport.CpmFrame_25.Panel_1
#  controlPanel.ClickR(85, 143)
#  tree.ClickItem("|[0]|Panel 1")
#  tree.ClickItemR("|[0]|Panel 1")
#  tree.SwingPopupMenu.Click("Paste Control(s)")
#  controlPanel.Click(143, 135)

def Setup_CPMPasteItem(item, name):
  Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.ClickItemR(item)
  Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.SwingPopupMenu.Click(name)

  Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.ScrollPane.Viewport.CpmFrame_25.Panel_1.Click(True)
  Delay(1000)

def Setup_CPMDeleteItem(item):
  Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.ClickItemR(item)
  Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.SwingPopupMenu.Click("Delete")
  if Aliases.javaw.Dialog22.Exists:
    Aliases.javaw.Dialog22.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
  else:
    Log.Message("do nothing")

def Setup_CPMCollaspItem(item):
  Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.CollapseItem(item)
 
def Setup_CPMExpandItem(item):
  Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.ExpandItem(item)

def Setup_CPMRenameItem(item, name):
  Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.ClickItem(item)
  Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.ScrollPane.Viewport.ControlStatusPane.Panel.TextField.Keys(name)

def Setup_CPM_ModifyItem(item, row, colunm, value): 
  if item != None:
    Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.ApplicationPane.VisionProgramPanel.SplitPane.SplitPane.ApplicationPane_PanelTabbedPane.PanelContentsEditor.PanelContentsEditor_CPTreeView.ScrollPane.Viewport.ControlPanelTree.ClickItem(item)
  else:
    Log.Message("do nothing")
  Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.ClickCell(row, colunm)
  Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.Keys("[BS][BS][BS][BS][BS][BS]" + value)
  Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.ClickCell(row, colunm)
  Aliases.javaw.CpmFrame3.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.Keys("[Up]")
  

#=============================================================List Edit==========================================================
def Setup_ListEdit():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane_ToolPalettePanelSplitPane_.ScrollPane.Viewport.Panel.ToolTree.ClickItemR("|[0]|Logic|List Edit")
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane_ToolPalettePanelSplitPane_.ScrollPane.SwingPopupMenu.Click("Copy List Edit")
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.ClickR(True)
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.SwingPopupMenu.Click("Paste List Edit")
def Setup_LEPanel(name):
  if name == "Setup":
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.BaseSetupPanel_ButtonBar_.ToolSetupCardPanel_HashcodeRadioButton5.Click(True)
  elif name == "Display":
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.BaseSetupPanel_ButtonBar_.ToolSetupCardPanel_HashcodeRadioButton6.Click(True)
  else:
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.BaseSetupPanel_ButtonBar_.ToolSetupCardPanel_HashcodeRadioButton7.Click(True)

def Setup_LEInput1(type, action, index, length):
  if type !=str(None):
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel.Panel.ComboBox.WindowsComboBoxUI_XPComboBoxButton.ClickButton()
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel.Panel.ComboBox.ClickItem(type)
  else:
    Log.Message("Ingore setting type")
  if action != str(None):
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel.Panel2.Panel.PatchableAutoComboBox.WindowsComboBoxUI_XPComboBoxButton.ClickButton()
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel.Panel2.Panel.PatchableAutoComboBox.ClickItem(action)
  else:
    Log.Message("Ingore setting action")
  if index !=str(None):
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel.Panel2.Panel.PatchableIntegerTextField.Keys(index)
  else:
    Log.Message("Ingore setting index")
  if length !=str(None):
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel.Panel2.Panel.PatchableIntegerTextField2.Keys(length)
  else:
    Log.Message("Ingore setting length")
    
def Setup_LELinkImageList():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel.Panel.LinkPanel.ToggleButton.ClickButton(True)
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.wItems.Item[0].Items.Item[1].DblClick()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.wItems.Item[0].Items.Item[1].Items.Item[6].DblClick()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.wItems.Item[0].Items.Item[1].Items.Item[6].Items.Item[3].Click()

def Setup_LELinkImage():
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel.Panel.LinkPanel.ToggleButton.ClickButton(True)
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.wItems.Item[0].Items.Item[1].Click(True)
  Aliases.javaw.VpmFrame.SwingPopupMenu.Click("Image")

  
def Setup_LELinkInput1(item, name):
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel.Panel.LinkPanel.ToggleButton.ClickButton(True)
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_TaskComponent_.Panel.ScrollPane.Viewport.CustomSplitPane.TasksTabbedPane_FilledLayeredPane_.TaskTree.ClickItem(item)
  Aliases.javaw.VpmFrame.SwingPopupMenu.Click(name)

def Setup_LEInput2(type, action, index):
  if type != str(None):
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel2.Panel.ComboBox.WindowsComboBoxUI_XPComboBoxButton.ClickButton()
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel2.Panel.ComboBox.ClickItem(type)
  else:
    Log.Message("Ingore setting type")
  if action != str(None):
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel2.Panel2.Panel.PatchableAutoComboBox.WindowsComboBoxUI_XPComboBoxButton.ClickButton()
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel2.Panel2.Panel.PatchableAutoComboBox.ClickItem(action)
  else:
    Log.Message("Ingore setting action")
  if index !=str(None):
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel2.Panel2.Panel.PatchableIntegerTextField.Keys(index)
  else:
    Log.Message("Ingore setting index")

def Setup_LoadApplication(name):
   if name == "VPM":  
    Setup_loadVPM()
   elif name == "CPM":
    Setup_LoadCPM()
   else:
     Log.Message(name, "do nothing")
       
def Setup_LoadImage(ImageName):  
  if ImageName == "PST":
    Setup_LoadPSTImages()
  else:
    Log.Message("do nothing")
 
def Setup_LoadTool(name):
  if name == "List Edit":
    Setup_ListEdit()
  else:
    Log.Message(name,"do nothing")
def Setup_Action(name, n):
  if name == "New Button":
    Setup_VPMNewButton()
  elif name == "Link Image":
    Setup_LELinkImage()
  elif name == "Trigger One":
    for i in range(0, n):
      Setup_VPMtriggerOne()
  elif name == "Tear Down":
    Setup_closeVPM()
  else:
    Log.Message("do nothing")
 
def RestartDevice():
  #TestedApps.Xmx_Setup.Run(1, True)
  #Delay(7000)
  if Aliases.javaw.Dialog10.Exists:  
    Aliases.javaw.Dialog10.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()

    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.OverviewComponent.SplitPane.TasksTabbedPane.TasksTabbedPane_SystemComponent_.ScrollPane.Viewport.Panel.TaskTree.ClickItem("Root|[0]|General")
 

    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.BaseSetupPanel_ButtonBar_.SwingObject("ToolSetupCardPanel$HashcodeRadioButton", "Diagnostics", 2).ClickButton(True)
    Delay(500)
    Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.SwingObject("SystemSetup$DiagnosticsSetupPanel", "", 0).SwingObject("JPanel", "", 0).SwingObject("JPanel", "", 0).SwingObject("JPanel", "", 4).SwingObject("JPanel", "", 0).SwingObject("JButton", "Reboot Device", 0).Click(True)
    #Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.SystemSetup_DiagnosticsSetupPanel.Panel.Panel.Panel.Panel.Button.ClickButton()
    #Aliases.javaw.Dialog22.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button2.ClickButton()
    Aliases.javaw.Dialog30.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
    #Aliases.javaw.Dialog.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button3.ClickButton()
    Delay(1000)
   # Aliases.javaw.Dialog29.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
    Setup_closeVPM()
    Log.Message("Fish to restart device")
    Setup_loadVPM()
    a = Project.FileName
  
    if a == "E:\mv-testcomplete\Emulator1\PatternSortingTool\PatternSortingTool.mds":
      Setup_LoadPSTImages()
    elif a == "E:\mv-testcomplete\Emulator1\PatternSortingTool\AdvOCR.mds":
      Setup_OCRImages()
    else:
      Setup_PinpointPatternFindImages()
    Setup_VPMNewButton()
  else:
    Log.Message("do nothing")
  

#  javaw.Dialog4.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
#  Aliases.javaw.Dialog4.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button.ClickButton()
#


  