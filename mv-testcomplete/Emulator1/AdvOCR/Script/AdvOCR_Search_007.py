#Author: Ha Le
#The test verify a prompting dialog appear if try to navigate to train panel during ROI off image watermark displays
import Setup
def AdvOCR_Search_007(): 
  Setup.Setup_InnitializeCPM()
  Setup.Setup_InnitializeVPM() 
  Setup.Setup_loadVPM()
  Setup.Setup_OCRImages()
  Setup.Setup_VPMNewButton()
  #Setup.Setup_AdvOCRManual()
  
  Setup.Setup_DragAvdToTaskTree()
  Setup.Setup_VPMSearchPanel()
  Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_1.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.Drag(150, 116, 479, 141)
  Setup.Setup_VPMTrainPanel()
  aqObject.CheckProperty(Aliases.javaw.Dialog8, "WndCaption", cmpEqual, "")
  Aliases.javaw.Dialog8.RootPane.null_layeredPane.null_contentPane.OptionPane.OptionPane_buttonArea.OptionPane_button2.ClickButton()

  Setup.Setup_closeVPM()
  #Aliases.javaw.VpmFrame.RootPane.null_layeredPane.null_contentPane.VPM.HideableTabbedPane.SplitPane.DetailComponent.DetailComponent_1.DetailComponent_BottomComponent_.PropertiesTabbedPane.Panel.Setup.BaseSetupPanel_1.Panel.Panel.HOG_OCRSetup_HOG_OCRSetupPanel_1.ROIEditor.Panel.Panel.ScrollPane.Viewport.DisplayCanvas.Drag(150, 116, 479, 141)
