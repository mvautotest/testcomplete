
import Setup
#import CheckPoint


Driver = DDT.ExcelDriver("../../PST_TestSteps.xlsx", "Sheet1")
Driver1 = DDT.ExcelDriver("../../PST_TestSteps.xlsx", "Sheet2")
Driver2 = DDT.ExcelDriver("../../PST_TestSteps.xlsx", "Sheet3")

def CheckPathPro():
  #The test perform check the input value in properties tab then compare with the value expected in excel sheet or .csv file
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[102, "E"], "stringValue_", cmpEqual, Driver2.Value[2])
          

    
def CheckTrainTime():
  #The test perform check the input value in Setup tab then compare with the value expected in excel sheet or .csv file
  aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[23, "E"].wtBase_.wt_, "yearDay", cmpNotEqual, Driver2.Value[3])
    
def CheckText():
  #The test perform check the detail of input1 value in setup tab then compare with the value expected in excel sheet or .csv file

 aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.PatternSortingSetup1_SortingTrainPanel.Panel.Panel.PatchableStringTextField, "wText", cmpEqual, Driver2.Value[4])

def CheckOutput1():
  #The test perform check the output1 value in setup tab then compare with the value expected in excel sheet or .csv file
  if not "None" in Driver1.Value[15]:
    aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel3.Panel.Panel.Panel2.Panel.Label, str(Driver2.Value[5]).strip('""'), cmpEqual, str(Driver2.Value[4]).strip('""'))
  else:
    Log.Message("Not in checkpoint check") 

def CheckOutput1Pro():
  #The test perform check the output 1 value in properties tab then compare with the value expected in excel sheet or .csv file
    if not "None" in Driver1.Value[35]:
        check = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[11, "C"].localizedName_
        if check ==Driver2.Value[41]=="Image" or check ==Driver2.Value[41]=="Integer" or check ==Driver2.Value[41]=="Line Segment" or check ==Driver2.Value[41]=="Origin" or check ==Driver2.Value[41]=="Point" or check ==Driver2.Value[41]=="Real" or check ==Driver2.Value[41]=="Rectangle" or check ==Driver2.Value[41]=="String" or check ==Driver2.Value[41]=="Blob" or check ==Driver2.Value[41]=="Boolean" or Driver2.Value[41]=="Calibration Info" or Driver2.Value[41]=="OCR Font Library" or Driver2.Value[41]=="OCR Field Definition" or Driver2.Value[41]=="OCR Space Model" or Driver2.Value[41]=="OCRVerificationParams" or Driver2.Value[41]=="Pattern Model":
          Log.Checkpoint("Check Output1 in properties for " + Driver2.Value[1] + " Pass")  
          a = 0      
        elif Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[11, "C"].localizedName_==Driver2.Value[41]=="Image List":
          a= Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[11, "E"].imageList_.elementCount
                    
        elif Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[11, "C"].localizedName_=="Integer List"==Driver2.Value[41]:
          a= Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[11, "E"].integerList_.elementCount
        elif Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[11, "C"].localizedName_=="Line Segment List"==Driver2.Value[41]:
           
          a= Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[11, "E"].lineSegmentList_.elementCount
        elif Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[11, "C"].localizedName_=="Origin List"==Driver2.Value[41]: 
          a= Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[11, "E"].originList_.elementCount
        elif Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[11, "C"].localizedName_=="Point List"==Driver2.Value[41]: 
 
          a= Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[11, "E"].pointList_.elementCount
        elif Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[11, "C"].localizedName_=="Real List"==Driver2.Value[41]:   

          a= Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[11, "E"].realList_.elementCount
        elif Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[11, "C"].localizedName_=="Rectangle List"==Driver2.Value[41]: 
 
          a= Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[11, "E"].rectangleList_.elementCount
        elif Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[11, "C"].localizedName_=="String List"==Driver2.Value[41]: 
          a= Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[11, "E"].stringList_.elementCount
          
        elif Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[11, "C"].localizedName_=="Blob List"==Driver2.Value[41]:   

          a= Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[11, "E"].blobList_.elementCount
        elif Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[11, "C"].localizedName_=="Boolean List"==Driver2.Value[41]:    
          a= Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[11, "E"].booleanList_.elementCount
        elif check=="Calibration Info List"==Driver2.Value[41]:   

          a= Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[11, "E"].calibrationInfoList_.elementCount
        elif check=="OCR Font Library List"==Driver2.Value[41]: 
 
          a= Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[11, "E"].ocrTrainingSetList_.elementCount
        elif check=="OCR Field Definition List"==Driver2.Value[41]: 
          a= Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[11, "E"].ocrFieldDefinitionList_.elementCount
          
        elif check=="OCR Space Model List"==Driver2.Value[41]:   

          a= Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[11, "E"].ocrspaceModelList_.elementCount
        elif check=="OCRVerificationParams List"==Driver2.Value[41]:    
          a= Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[11, "E"].ocrVerificationParamsList_.elementCount
        elif check=="Pattern Model List"==Driver2.Value[41]:    
          a= Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[11, "E"].ShapeFindModelList_.elementCount

        else:
          Log.Message("not found")
        if a == int(Driver2.Value[42]):
          Log.Checkpoint("Check Output1 in properties for " + Driver2.Value[1] + " Pass")
        else:
          Log.Error("Check Output1 in properties for " + Driver2.Value[1] + " Fail with actual value: " + str(a))

    
def CheckOutput2Pro():
  #The test perform check the output 2 value in properties tab then compare with the value expected in excel sheet or .csv file
  if not "None" in Driver1.Value[36]:


        check = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[12, "C"].localizedName_
        if check ==Driver2.Value[43]=="Image" or check ==Driver2.Value[43]=="Integer" or check ==Driver2.Value[43]=="Line Segment" or check ==Driver2.Value[43]=="Origin" or check ==Driver2.Value[43]=="Point" or check ==Driver2.Value[43]=="Real" or check ==Driver2.Value[43]=="Rectangle" or check ==Driver2.Value[43]=="String" or check ==Driver2.Value[43]=="Blob" or check ==Driver2.Value[43]=="Boolean" or Driver2.Value[43]=="Calibration Info" or Driver2.Value[43]=="OCR Font Library" or Driver2.Value[43]=="OCR Field Definition" or Driver2.Value[43]=="OCR Space Model" or Driver2.Value[43]=="OCRVerificationParams" or Driver2.Value[43]=="Pattern Model":
  
          Log.Checkpoint("Check Output2 in properties for " + Driver2.Value[1] + " Pass")
          a=0;         
        elif Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[12, "C"].localizedName_==Driver2.Value[43]=="Image List":
            a= Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[12, "E"].imageList_.elementCount
        elif Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[12, "C"].localizedName_=="Integer List"==Driver2.Value[43]:
   
            a= Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[12, "E"].integerList_.elementCount
        elif Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[12, "C"].localizedName_=="Line Segment List"==Driver2.Value[43]:
           
            a= Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[12, "E"].lineSegmentList_.elementCount
        elif Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[12, "C"].localizedName_=="Origin List"==Driver2.Value[43]: 
            a= Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[12, "E"].originList_.elementCount
        elif Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[12, "C"].localizedName_=="Point List"==Driver2.Value[43]: 
 
            a= Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[12, "E"].pointList_.elementCount
        elif Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[12, "C"].localizedName_=="Real List"==Driver2.Value[43]:   
            a= Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[12, "E"].realList_.elementCount
        elif Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[12, "C"].localizedName_=="Rectangle List"==Driver2.Value[43]: 
 
            a= Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[12, "E"].rectangleList_.elementCount
        elif Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[12, "C"].localizedName_=="String List"==Driver2.Value[43]: 
            a= Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[12, "E"].stringList_.elementCount
        elif Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[12, "C"].localizedName_=="Blob List"==Driver2.Value[43]:   

            a= Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[12, "E"].blobList_.elementCount
        elif Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[12, "C"].localizedName_=="Boolean List"==Driver2.Value[43]:   
 
            a= Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[12, "E"].booleanList_.elementCount
        elif check=="Calibration Info List"==Driver2.Value[43]:   

          a= Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[12, "E"].calibrationInfoList_.elementCount
        elif check=="OCR Font Library List"==Driver2.Value[43]: 
 
          a= Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[12, "E"].ocrTrainingSetList_.elementCount
        elif check=="OCR Field Definition List"==Driver2.Value[43]: 
          a= Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[12, "E"].ocrFieldDefinitionList_.elementCount
          
        elif check=="OCR Space Model List"==Driver2.Value[43]:   

          a= Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[12, "E"].ocrspaceModelList_.elementCount
        elif check=="OCRVerificationParams List"==Driver2.Value[43]:    
          a= Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[12, "E"].ocrVerificationParamsList_.elementCount
        elif check=="Pattern Model List"==Driver2.Value[43]:    
          a= Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane2.Panel.PropertiesScrollPane.Viewport.PropertyTable.wValue[12, "E"].ShapeFindModelList_.elementCount

        else:
          Log.Message("cannot find")
          
        if a == int(Driver2.Value[44]):
          Log.Checkpoint("Check Output2 in properties for " + Driver2.Value[1] + " Pass")
        else:
          Log.Error("Check Output2 in properties for " + Driver2.Value[1] + " Fail with actual value: " + str(a))                    
  
 
  else:
    Log.Message("Not in checkpoint check") 

    
def CheckOutput1Detail():
  #The test perform check the detail of output 1 value in setup tab then compare with the value expected in excel sheet or .csv file
  Log.Message(Driver1.Value[23])
  if not "None" in Driver1.Value[23]:
    count = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel3.Panel.Panel.Panel2.Panel.Label.text
    count1 = aqConvert.StrToInt(count)
    if Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel3.Panel.Panel.Panel2.Panel2.Panel.ScrollPane.Viewport.ListEditSetup_PortDataTable.Exists:
      for i in range(0, count1):  
        check = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel3.Panel.Panel.Panel2.Panel2.Panel.ScrollPane.Viewport.ListEditSetup_PortDataTable.wValue[i, 1]
   
        j = i+18
        a = Driver2.Value[j]
        Log.Message(Driver2.Value[j])
  
        if str(check.strip()) == a.strip('""'):
      
          Log.Checkpoint("Check Output 1 for " + Driver2.Value[1] + " Pass")
        else:
          Log.Error("Check Output 1 for " + Driver2.Value[1] + " Fail with actual value" + str(check))
    else:
       if str(count.strip()) == "1":
      
          Log.Checkpoint("Check Output 1 for " + Driver2.Value[1] + " Pass")
       else:
          Log.Error("Check Output 1 for " + Driver2.Value[1] + " Fail with actual value" + str(count))
  else:
    Log.Message("Not in checkpoint check")  
    
    
def CheckInput2():
  #The test perform check the input 2 value in setup tab then compare with the value expected in excel sheet or .csv file
  if not "None" in Driver1.Value[16]:
    for i in range(21, 30):
      check =  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel3.Panel.Panel.Panel2.Panel2.Panel.ScrollPane.Viewport.ListEditSetup_PortDataTable.wValue[0, 1]
      j = i+2

      if str(check) == str(Driver2.Value[j]):
      
        Log.Checkpoint("Check Input 2 for " + Driver2.Value[1] + " Pass")
      else:
        Log.Error("Check Input 2 for " + Driver2.Value[1] + " Fail with actual value" + str(check))
  else:
    Log.Message("Not in checkpoint check") 
        
def CheckOutput2():
  #The test perform check the detail of output2 value in setup tab then compare with the value expected in excel sheet or .csv file
  if not "None" in Driver1.Value[17]:
    count = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel3.Panel.Panel.Panel3.Panel.Label3.text
    count1 = aqConvert.StrToInt(count)
    if Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel3.Panel.Panel.Panel3.Panel2.Panel.ScrollPane.Viewport.ListEditSetup_PortDataTable.Exists:
      for i in range(0, count1):  
        check = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel3.Panel.Panel.Panel3.Panel2.Panel.ScrollPane.Viewport.ListEditSetup_PortDataTable.wValue[i, 1]
   
        j = i+6
        a = Driver2.Value[j]
        Log.Message(Driver2.Value[j])
  #      v1 = str(check.strip())
  #      v2 = a.strip('""')
  #      Log.Message(v1)
  #      Log.Message(v2)
        if str(check.strip()) == a.strip('""'):
      
          Log.Checkpoint("Check Output 2 for " + Driver2.Value[1] + " Pass")
        else:
          Log.Error("Check Output 2 for " + Driver2.Value[1] + " Fail with actual value" + str(check))
    else:
       if str(count.strip()) == "1":
      
          Log.Checkpoint("Check Output 2 for " + Driver2.Value[1] + " Pass")
       else:
          Log.Error("Check Output 2 for " + Driver2.Value[1] + " Fail with actual value" + str(count))
  else:
    Log.Message("Not in checkpoint check")  

def CheckTextField1():
  if Driver1.Value[18] == "CheckTextField1":
    aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel.Panel2.Panel.PatchableIntegerTextField, "Enabled", cmpEqual, False, False)
  else:
    Log.Message("Not in checkpoint check")
def CheckTextField2():
  if Driver1.Value[19] == "CheckTextField2":
    aqObject.CheckProperty(Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel.Panel2.Panel.PatchableIntegerTextField2, "Enabled", cmpEqual, False, False)
  else:
    Log.Message("Not in checkpoint check")
    
def CheckPassFail():
  #The test perform check pass/fail value in setup tab then compare with the value expected in excel sheet or .csv file
  if not "None" in Driver1.Value[20]:
    a = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel4.Panel.PassFailLabel.text
    if a == Driver2.Value[16]:
      Log.Checkpoint("Check pass/fail for " + Driver2.Value[1] + " Pass")
    else:
      Log.Error("Check pass/fail for " + Driver2.Value[1] + " Fail with actual value: " + str(a))
  else:
    Log.Message("Not in checkpoint check")

def CheckMessage():
  #The test perform check the message error return in setup tab then compare with the value expected in excel sheet or .csv file
  if not "None" in Driver1.Value[21]:
    a = Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.ScrollPane.Viewport.Panel.Panel.ToolSetupCardPanel.ListEditSetup_ListDataPanel.Panel.Panel4.Panel.EnumeratedLabel.text
    if a == Driver2.Value[17]:
      Log.Checkpoint("Check Message for " + Driver2.Value[1] + " Pass")
    else:
      Log.Error("Check Message for " + Driver2.Value[1] + " Fail with actual value: " + str(a))
  else:
    Log.Message("Not in checkpoint check")


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
        if Driver.Value[i] == "Setup_LoadPSTImages":
          Setup.Setup_LoadPSTImages()
        if Driver.Value[i] == "Setup_PSTCheck":
          Setup.Setup_PSTCheck()
        if Driver.Value[i] == "Setup_VPMNewButton":  
          Setup.Setup_VPMNewButton()
        if Driver.Value[i] == "Setup_PSTTrainPanel":   
          Setup.Setup_PSTTrainPanel()
        if Driver.Value[i] == "Setup_PSTLoadDB": 
          Setup.Setup_PSTLoadDB(Driver1.Value[2])
        if Driver.Value[i] == "Setup_PSTTrainProperties": 
          Setup.Setup_PSTTrainProperties()
        if Driver.Value[i] == "PST_ProClick":  
          Setup.PST_ProClick()
        if Driver.Value[i] == "Setup_PSTLinkPatternDB":    
          Setup.Setup_PSTLinkPatternDB()
        if Driver.Value[i] == "Setup_PSTRunButton":  
          Setup.Setup_PSTRunButton()
        if Driver.Value[i] == "PST_ProClick1":  
          Setup.PST_ProClick1()
        if Driver.Value[i] == "PST_ClickItem":  
          Setup.PST_ClickItem()
        if Driver.Value[i] == "Setup_PSTLoadDBSet":   
          Setup.Setup_PSTLoadDBSet(Driver1.Value[3], Driver1.Value[4])

        if Driver.Value[i] == "Setup_DragPatternSortToTaskTree":
          Setup.Setup_DragPatternSortToTaskTree()
        if Driver.Value[i] == "Setup_VPMPropertiesTab":  
          Setup.Setup_VPMPropertiesTab()
     
        if Driver.Value[i] == "Setup_PSTDeleteFoder":  
          Setup.Setup_PSTDeleteFoder(Driver1.Value[5])  
        if Driver.Value[i] == "Setup_VPMAdvSetupTab":
          Setup.Setup_VPMAdvSetupTab()
        if Driver.Value[i] == "Setup_LoadImages":
          Setup.Setup_LoadImages(Driver1.Value[2], Driver1.Value[6])
          
          
        if Driver.Value[i] == "Setup_VPMtriggerOne": 
          for i in range(0, aqConvert.StrToInt(Driver1.Value[24])):
            Setup.Setup_VPMtriggerOne()
            Log.Message(Driver1.Value[24])
        
        
        if Driver.Value[i] == "Setup_CheckPoint": 
         
            CheckPathPro()
           
            
        if Driver.Value[i] == "Setup_CheckPointPro":  
            CheckInput1Pro()
            CheckOutput1Pro()
            CheckOutput2Pro()


            
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
    if not "N" in Driver.Value[24]:
      
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

  

  
 
    
