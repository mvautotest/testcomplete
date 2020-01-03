<<<<<<< HEAD
﻿
import Setup
#import CheckPoint


Driver = DDT.ExcelDriver("../../ROIFind_TestSteps.xlsx", "TestSteps")
Driver1 = DDT.ExcelDriver("../../ROIFind_TestSteps.xlsx", "TestData")
Driver2 = DDT.ExcelDriver("../../ROIFind_TestSteps.xlsx", "ExpectedOutput")

def CheckPassFail():
  if Driver1.Value[14] !="None":
    aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ROIFindSetup_PassFailPanel.Panel3.Panel.PassFailLabel, "text", cmpEqual, Driver2.Value[2])
  else: 
    Log.Message("pass fail not check")
def CheckRectangle():
  if Driver1.Value[15] !="None":
    Setup.Setup_VPMPropertiesTab()
    Delay(1000)
    aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel2.PropertiesScrollPane.Viewport.PropertyTable.wValue[22, "E"].rectangleList_, "elementCount", cmpEqual, Driver2.Value[3])
    aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel2.PropertiesScrollPane.Viewport.PropertyTable.wValue[23, "E"].rectangleList_, "elementCount", cmpEqual, Driver2.Value[4])
  else: 
    Log.Message("Rectangle not check")

def CheckEdgePoint():
  if Driver1.Value[16] !="None":
    #aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel2.PropertiesScrollPane.Viewport.PropertyTable.wValue[20, "E"].rectangleList_, "elementCount", cmpEqual, )
    aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel2.PropertiesScrollPane.Viewport.PropertyTable.wValue[20, "E"].pointList_, "elementCount", cmpEqual, Driver2.Value[5])
  else: 
    Log.Message("Rectangle not check")
def CheckPassFailPro():
  if Driver1.Value[17] !="None":
    aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[19, "E"], "value_", cmpEqual, Driver2.Value[6])
  else: 
    Log.Message("pass fail not check")
    
def TestCase():
  #map testcase and test data from the excel sheet/csv file and excute
    global Driver
    global Driver1
    global Driver2
    aqTestCase.Begin("Start test ID: " + Driver.Value[1]);
    
    for i in range(2, Driver.ColumnCount):
        
        if Driver.Value[i] == "Setup_InnitializeVPM":
          Setup.Setup_InnitializeVPM()
        if Driver.Value[i] == "Setup_loadVPM":
          Setup.Setup_loadVPM()
      
        if Driver.Value[i] == "Setup_LoadImage1":
          Setup.Setup_LoadImage1(Driver1.Value[2])
        
        if Driver.Value[i] == "Setup_VPMNewButton":
          Setup.Setup_VPMNewButton()
       
          
        if Driver.Value[i] == "Setup_ROIFind":
          Setup.Setup_ROIFind()
          
        if Driver.Value[i] == "Setup_RFEdgeDetectPanel":
          Setup.Setup_RFEdgeDetectPanel()  
          
        if Driver.Value[i] == "Setup_RFDeleteROIEdgeDetectPanel":
          Setup.Setup_RFDeleteROIEdgeDetectPanel()
          


          
        if Driver.Value[i] == "Setup_RFEdgeDetectionSet":
          Log.Message(Driver1.Value[6])
          Setup.Setup_RFEdgeDetectionSet(Driver1.Value[3], Driver1.Value[4], Driver1.Value[5], Driver1.Value[6])

        if Driver.Value[i] == "Setup_PassFailPanel":
          Setup.Setup_PassFailPanel()
          
        if Driver.Value[i] == "Setup_PassFailSet":
          Setup.Setup_PassFailSet(Driver1.Value[7], Driver1.Value[8], Driver1.Value[9], Driver1.Value[10], Driver1.Value[11])
        
        if Driver.Value[i] == "Setup_SamplingStepPro":
          Setup.Setup_SamplingStepPro(Driver1.Value[12])
          
        if Driver.Value[i] == "Setup_RunPro":
          Setup.Setup_RunPro()
         
        if Driver.Value[i] == "Setup_VPMUnloadProgram":
          Setup.Setup_VPMUnloadProgram()
                  
     
          
        if Driver.Value[i] == "Setup_VPMPropertiesTab":
          Setup.Setup_VPMPropertiesTab()
          
      
      
        if Driver.Value[i] == "Setup_VPMAdvSetupTab":
          Setup.Setup_VPMAdvSetupTab()

          
        if Driver.Value[i] == "Setup_VPMtriggerOne": 
          for i in range(0, aqConvert.StrToInt(Driver1.Value[24])):
            Setup.Setup_VPMtriggerOne()
            Log.Message(Driver1.Value[24])
        
        
        if Driver.Value[i] == "Setup_CheckPoint": 
         CheckPassFail()
         CheckRectangle()
         CheckEdgePoint()
         CheckPassFailPro()
            
            
        #if Driver.Value[i] == "Setup_CheckPointPro":  
           


            
        if Driver.Value[i] == "Setup_LEReset":
          Setup.Setup_LEReset() 
        if Driver.Value[i] == "Setup_LERun":
          Setup.Setup_LERun()       
        if Driver.Value[i] == "Setup_LEResetPro":
          Setup.Setup_LEResetPro() 
        if Driver.Value[i] == "Setup_LERunPro":
          Setup.Setup_LERunPro()    
        if Driver.Value[i] == "Setup_LEDeleteLinkPro":
          Setup.Setup_LEDeleteLinkPro() 
          
        if Driver.Value[i] == "Setup_LEErrorConfirmPro":
          Setup.Setup_LEErrorConfirmPro()   
        
        if Driver.Value[i] == "Setup_closeVPM":
          Setup.Setup_closeVPM()
          
   
    aqTestCase.End();
  
RecNo = 0
current = 0
current1 = 0
current2 = 0
testcase = 0
def processData():
  #function to push data in excel/csv to log file
  global RecNo
  fo = Log.CreateFolder("Record: " + aqConvert.VarToStr(RecNo))
  Log.PushLogFolder(fo)
  for i in range(Driver.ColumnCount):
    Log.Message(Driver.ColumnName[i] + ": " + aqConvert.VarToStr(Driver.Value[i]))
  for j in range(Driver1.ColumnCount):
      Log.Message(Driver1.ColumnName[j] + ": " + aqConvert.VarToStr(Driver1.Value[j]))
  for k in range(Driver2.ColumnCount):
    Log.Message(Driver2.ColumnName[k] + ": " + aqConvert.VarToStr(Driver2.Value[k]))

  Log.PopLogFolder()
  RecNo = RecNo + 1
  
  

def test():
  #main function to run test case though the excel/csv file
  global current
  global current1
  global current2

  while not Driver.EOF()& Driver1.EOF():
  #the test only run from line start by "Y" and inogre the line config for "N"
    if not "N" in Driver.Value[23]:
      
      processData()
      TestCase()
      Driver.Next()
      Driver1.Next()
      Driver2.Next()
    else:
      current = Driver.Next()
      current1 = Driver1.Next()
      current2 = Driver2.Next()

  current = aqConvert.VarToInt(current) + 1
  current1 = aqConvert.VarToInt(current1) + 1
  current2 = aqConvert.VarToInt(current2) + 1

  
  DDT.CloseDriver(Driver.Name) 
  DDT.CloseDriver(Driver1.Name) 
  DDT.CloseDriver(Driver2.Name) 

  

  
 
    
=======
﻿
import Setup
#import CheckPoint


Driver = DDT.ExcelDriver("../../ROIFind_TestSteps.xlsx", "TestSteps")
Driver1 = DDT.ExcelDriver("../../ROIFind_TestSteps.xlsx", "TestData")
Driver2 = DDT.ExcelDriver("../../ROIFind_TestSteps.xlsx", "ExpectedOutput")

def CheckPassFail():
  if Driver1.Value[14] !="None":
    aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ROIFindSetup_PassFailPanel.Panel3.Panel.PassFailLabel, "text", cmpEqual, Driver2.Value[2])
  else: 
    Log.Message("pass fail not check")
def CheckRectangle():
  if Driver1.Value[15] !="None":
    Setup.Setup_VPMPropertiesTab()
    Delay(1000)
    aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel2.PropertiesScrollPane.Viewport.PropertyTable.wValue[22, "E"].rectangleList_, "elementCount", cmpEqual, Driver2.Value[3])
    aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel2.PropertiesScrollPane.Viewport.PropertyTable.wValue[23, "E"].rectangleList_, "elementCount", cmpEqual, Driver2.Value[4])
  else: 
    Log.Message("Rectangle not check")

def CheckEdgePoint():
  if Driver1.Value[16] !="None":
    #aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel2.PropertiesScrollPane.Viewport.PropertyTable.wValue[20, "E"].rectangleList_, "elementCount", cmpEqual, )
    aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel2.PropertiesScrollPane.Viewport.PropertyTable.wValue[20, "E"].pointList_, "elementCount", cmpEqual, Driver2.Value[5])
  else: 
    Log.Message("Rectangle not check")
def CheckPassFailPro():
  if Driver1.Value[17] !="None":
    aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[19, "E"], "value_", cmpEqual, Driver2.Value[6])
  else: 
    Log.Message("pass fail not check")
    
def TestCase():
  #map testcase and test data from the excel sheet/csv file and excute
    global Driver
    global Driver1
    global Driver2
    aqTestCase.Begin("Start test ID: " + Driver.Value[1]);
    
    for i in range(2, Driver.ColumnCount):
        
        if Driver.Value[i] == "Setup_InnitializeVPM":
          Setup.Setup_InnitializeVPM()
        if Driver.Value[i] == "Setup_loadVPM":
          Setup.Setup_loadVPM()
      
        if Driver.Value[i] == "Setup_LoadImage1":
          Setup.Setup_LoadImage1(Driver1.Value[2])
        
        if Driver.Value[i] == "Setup_VPMNewButton":
          Setup.Setup_VPMNewButton()
       
          
        if Driver.Value[i] == "Setup_ROIFind":
          Setup.Setup_ROIFind()
          
        if Driver.Value[i] == "Setup_RFEdgeDetectPanel":
          Setup.Setup_RFEdgeDetectPanel()  
          
        if Driver.Value[i] == "Setup_RFDeleteROIEdgeDetectPanel":
          Setup.Setup_RFDeleteROIEdgeDetectPanel()
          


          
        if Driver.Value[i] == "Setup_RFEdgeDetectionSet":
          Log.Message(Driver1.Value[6])
          Setup.Setup_RFEdgeDetectionSet(Driver1.Value[3], Driver1.Value[4], Driver1.Value[5], Driver1.Value[6])

        if Driver.Value[i] == "Setup_PassFailPanel":
          Setup.Setup_PassFailPanel()
          
        if Driver.Value[i] == "Setup_PassFailSet":
          Setup.Setup_PassFailSet(Driver1.Value[7], Driver1.Value[8], Driver1.Value[9], Driver1.Value[10], Driver1.Value[11])
        
        if Driver.Value[i] == "Setup_SamplingStepPro":
          Setup.Setup_SamplingStepPro(Driver1.Value[12])
          
        if Driver.Value[i] == "Setup_RunPro":
          Setup.Setup_RunPro()
         
        if Driver.Value[i] == "Setup_VPMUnloadProgram":
          Setup.Setup_VPMUnloadProgram()
                  
     
          
        if Driver.Value[i] == "Setup_VPMPropertiesTab":
          Setup.Setup_VPMPropertiesTab()
          
      
      
        if Driver.Value[i] == "Setup_VPMAdvSetupTab":
          Setup.Setup_VPMAdvSetupTab()

          
        if Driver.Value[i] == "Setup_VPMtriggerOne": 
          for i in range(0, aqConvert.StrToInt(Driver1.Value[24])):
            Setup.Setup_VPMtriggerOne()
            Log.Message(Driver1.Value[24])
        
        
        if Driver.Value[i] == "Setup_CheckPoint": 
         CheckPassFail()
         CheckRectangle()
         CheckEdgePoint()
         CheckPassFailPro()
            
            
        #if Driver.Value[i] == "Setup_CheckPointPro":  
           


            
        if Driver.Value[i] == "Setup_LEReset":
          Setup.Setup_LEReset() 
        if Driver.Value[i] == "Setup_LERun":
          Setup.Setup_LERun()       
        if Driver.Value[i] == "Setup_LEResetPro":
          Setup.Setup_LEResetPro() 
        if Driver.Value[i] == "Setup_LERunPro":
          Setup.Setup_LERunPro()    
        if Driver.Value[i] == "Setup_LEDeleteLinkPro":
          Setup.Setup_LEDeleteLinkPro() 
          
        if Driver.Value[i] == "Setup_LEErrorConfirmPro":
          Setup.Setup_LEErrorConfirmPro()   
        
        if Driver.Value[i] == "Setup_closeVPM":
          Setup.Setup_closeVPM()
          
   
    aqTestCase.End();
  
RecNo = 0
current = 0
current1 = 0
current2 = 0
testcase = 0
def processData():
  #function to push data in excel/csv to log file
  global RecNo
  fo = Log.CreateFolder("Record: " + aqConvert.VarToStr(RecNo))
  Log.PushLogFolder(fo)
  for i in range(Driver.ColumnCount):
    Log.Message(Driver.ColumnName[i] + ": " + aqConvert.VarToStr(Driver.Value[i]))
  for j in range(Driver1.ColumnCount):
      Log.Message(Driver1.ColumnName[j] + ": " + aqConvert.VarToStr(Driver1.Value[j]))
  for k in range(Driver2.ColumnCount):
    Log.Message(Driver2.ColumnName[k] + ": " + aqConvert.VarToStr(Driver2.Value[k]))

  Log.PopLogFolder()
  RecNo = RecNo + 1
  
  

def test():
  #main function to run test case though the excel/csv file
  global current
  global current1
  global current2

  while not Driver.EOF()& Driver1.EOF():
  #the test only run from line start by "Y" and inogre the line config for "N"
    if not "N" in Driver.Value[23]:
      
      processData()
      TestCase()
      Driver.Next()
      Driver1.Next()
      Driver2.Next()
    else:
      current = Driver.Next()
      current1 = Driver1.Next()
      current2 = Driver2.Next()

  current = aqConvert.VarToInt(current) + 1
  current1 = aqConvert.VarToInt(current1) + 1
  current2 = aqConvert.VarToInt(current2) + 1

  
  DDT.CloseDriver(Driver.Name) 
  DDT.CloseDriver(Driver1.Name) 
  DDT.CloseDriver(Driver2.Name) 

  

  
 
    
>>>>>>> 4550603c95fc33a9cabececc04615fbdac4a4867
