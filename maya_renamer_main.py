import maya.cmds as cmds

class main_window(object):
        
    #constructor
    def __init__(self):
            
        self.window = "main_window"
            
        #create new window
        self.window = cmds.window(title="Maya Renamer", iconName='Renamer', widthHeight=(402, 80), s=False)
        
        cmds.rowColumnLayout()
        cmds.separator( style='none', h=5 )
        cmds.rowColumnLayout(numberOfRows=1)
        self.prefix_text = cmds.textField(h=30, w=100, pht="Prefix")
        cmds.separator( style='none', w=5 )
        self.main_text = cmds.textField(h=30, w=150, pht="Main")
        cmds.separator( style='none', w=5 )
        self.suffix_text = cmds.textField(h=30, w=100, pht="Suffix")
        cmds.separator( style='none', w=5 )
        self.rename_btn = cmds.button(l="R", h=30, w=30,bgc=(1,0.5,0.0), ann="Rename", command=self.rename_btn_command)
        cmds.setParent('..')
        
        cmds.rowColumnLayout(numberOfRows=1)
        self.underscore_check = cmds.checkBox( label='Add Underscores' )
        cmds.setParent('..')
        
        cmds.separator( style='none', h=5 )
        cmds.text(l="Made by Kieron", fn="smallBoldLabelFont")
        #display new window
        cmds.showWindow()


    def rename_btn_command(self, *args):
        main_prefix = cmds.textField(self.prefix_text, q=True, text=True)
        main_text = cmds.textField(self.main_text, q=True, text=True)
        main_suffix = cmds.textField(self.suffix_text, q=True, text=True)
        underscore_value = cmds.checkBox(self.underscore_check, q=True, value=True)
        
        if underscore_value == True:
            obj_to_rename = cmds.ls( selection=True )
            full_name = main_prefix + "_" + main_text + "_"+ main_suffix
            cmds.rename( obj_to_rename, full_name )
        elif underscore_value == False:
            obj_to_rename = cmds.ls( selection=True )
            full_name = main_prefix + main_text + main_suffix
            cmds.rename( obj_to_rename, full_name )

        
            
    

myWindow = main_window()
