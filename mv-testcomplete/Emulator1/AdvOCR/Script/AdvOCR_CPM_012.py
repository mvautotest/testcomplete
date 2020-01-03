#Author: Ha Le
#The test verify user cannot set data or delete padlock icon

import Setup
def AdvOCR_CPM_012(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  Setup.Setup_AdvOCR()
  Setup.Setup_LoadCPM()
  Setup.Setup_DragOCRFontLibraryToCpFile()


  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.wValue[20, 3]
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.ClickCell(20, 3)
  Regions.PropertiesViewport.Check(Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport)
  #Regions.ControlPropertiesPane_ControlPropertiesInnerPane4.Check(Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane)
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.wValue[20, 4]
  Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane.ClickCell(20, 4)
  Regions.PropertiesViewport.Check(Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport)
  #Regions.ControlPropertiesPane_ControlPropertiesInnerPane4.Check(Aliases.javaw.CpmFrame2.RootPane.null_layeredPane.null_contentPane.Panel.SplitPane.SplitPane.Panel.PropertyPane.PropertyPaneTabs.Properties.ScrollPane.PropertiesViewport.ControlPropertiesPane_ControlPropertiesInnerPane)
  Setup.Setup_closeCPM()
  Setup.Setup_closeVPM()