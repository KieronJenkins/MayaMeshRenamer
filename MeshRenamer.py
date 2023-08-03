# -------------------------- IMPORTS
from maya import cmds

# -------------------------- CLASS
class MayaMeshRenamer:
    # -------------------------- VARIABLES
    WINDOW_HEIGHT = 435
    WINDOW_WIDTH = 250
    WINDOW_TITLE = "Maya Mesh Rename"
    WINDOW_CHECK = "mayaMeshRenamer"
    WINDOW_ATTR = "meshRenameMayaWindow"

    # -------------------------- WINDOW START
    def __init__(self):

        self.CheckWindowExists()
        self.WINDOW_ATTR = cmds.window(self.WINDOW_CHECK, title=self.WINDOW_TITLE, widthHeight=(self.WINDOW_WIDTH, self.WINDOW_HEIGHT), sizeable=False, resizeToFitChildren=True)

        cmds.columnLayout(adjustableColumn=True)
        cmds.separator(height=10, style="none")

        cmds.rowColumnLayout(numberOfRows=1)

        cmds.separator(width=5)
        cmds.button(label="Select All", width=235, command=self.SelectAllMeshes)
        cmds.separator(width=10)

        cmds.setParent('..')

        cmds.separator(height=10, style="none")

        cmds.rowColumnLayout(numberOfRows=1)
        cmds.separator(width=5)
        cmds.button(label="Select via Name", width=110, command=self.SelectByName)
        cmds.separator(width=15)
        self.selection_name_field = cmds.textField(width=110)
        cmds.separator(width=5)

        cmds.setParent('..')

        cmds.separator(height=15, style="none")

        rename_section = cmds.frameLayout(label="Rename Mesh", labelAlign="top", collapsable=True)
        cmds.separator(height=5, style="none")
        cmds.rowColumnLayout(numberOfRows=1)
        cmds.separator(width=5)
        cmds.text(label="Rename:")
        cmds.separator(width=10)
        self.rename_text = cmds.textField(width=183)
        cmds.separator(width=5)

        cmds.setParent('..')

        cmds.separator(height=1, style="none")

        cmds.rowColumnLayout(numberOfRows=1)
        cmds.separator(width=5)
        cmds.button(label="Apply and Rename", width=235, command=self.RenameMeshObjects)
        cmds.separator(width=5)

        cmds.setParent('..')
        cmds.setParent('..')

        cmds.separator(height=15, style="none")

        cmds.frameLayout(label="Prefix/Suffix", labelAlign="top", collapsable=True)

        cmds.separator(height=5, style="none")

        cmds.rowColumnLayout(numberOfRows=1)

        cmds.separator(width=5)
        cmds.text(label="Prefix:")
        cmds.separator(width=5)
        self.prefix_textfield = cmds.textField(width=200, pht="Prefix_")

        cmds.setParent('..')

        cmds.separator(height=1, style="none")

        cmds.rowColumnLayout(numberOfRows=1)

        cmds.separator(width=5)
        cmds.button(label="Add Prefix", width=235, command=self.AddPrefixText)
        cmds.separator(width=5)

        cmds.setParent('..')

        cmds.rowColumnLayout(numberOfRows=1)
        cmds.separator(width=5)
        cmds.button(label="Ext_", width=55, command=lambda *args: self.PrefixPresetButton("Ext_"))
        cmds.separator(width=5)
        cmds.button(label="Chr_", width=55, command=lambda *args: self.PrefixPresetButton("Chr_"))
        cmds.separator(width=5)
        cmds.button(label="Sm_", width=55, command=lambda *args: self.PrefixPresetButton("Sm_"))
        cmds.separator(width=5)
        cmds.button(label="Sk_", width=55, command=lambda *args: self.PrefixPresetButton("Sk_"))
        cmds.separator(width=5)
        cmds.setParent('..')

        cmds.separator(height=5, style="none")

        cmds.rowColumnLayout(numberOfRows=1)
        cmds.separator(width=5)
        cmds.text(label="Suffix:")
        cmds.separator(width=5)
        self.suffix_textfield = cmds.textField(width=200, pht="_Suffix")

        cmds.setParent('..')

        cmds.separator(height=1, style="none")

        cmds.rowColumnLayout(numberOfRows=1)

        cmds.separator(width=5)
        cmds.button(label="Add Suffix", width=235, command=self.AddSuffixText)
        cmds.separator(width=5)

        cmds.setParent('..')

        cmds.rowColumnLayout(numberOfRows=1)
        cmds.separator(width=5)
        cmds.button(label="_Grp", width=55, command=lambda *args: self.SuffixPresetButton("_Grp"))
        cmds.separator(width=5)
        cmds.button(label="_Geo", width=55, command=lambda *args: self.SuffixPresetButton("_Geo"))
        cmds.separator(width=5)
        cmds.button(label="_Loc", width=55, command=lambda *args: self.SuffixPresetButton("_Loc"))
        cmds.separator(width=5)
        cmds.button(label="_Ctrl", width=55, command=lambda *args: self.SuffixPresetButton("_Ctrl"))
        cmds.separator(width=5)

        cmds.setParent('..')
        cmds.setParent('..')

        cmds.separator(height=5, style="none")

        cmds.showWindow(self.WINDOW_ATTR)

    # -------------------------- FUNCTIONS
    def CheckWindowExists(self):
        if (cmds.window(self.WINDOW_CHECK, exists=True)):
            cmds.deleteUI(self.WINDOW_CHECK)

    def SelectAllMeshes(*args):  # Used by Select All Button
        cmds.select(clear=True)
        cmds.select(cmds.listRelatives(cmds.ls(geometry=True), p=True, path=True), r=True)

    def SelectByName(self, *args):  # Used by Select Via Name Button
        selection_name = cmds.textField(self.selection_name_field, query=True, text=True)
        if cmds.objExists(selection_name):
            cmds.select(selection_name)
        else:
            print("No object found with that name")

    def RenameMeshObjects(self, *args):  # Used by Apply and Rename Button
        selected_object = cmds.ls(selection=True)
        text_to_rename = cmds.textField(self.rename_text, query=True, text=True)
        for mesh_objects in selected_object:
            cmds.rename(mesh_objects, text_to_rename + "_01")

    def AddPrefixText(self, *args): # Used by Add Prefix Button
        selected_object = cmds.ls(selection=True)
        prefix_text = cmds.textField(self.prefix_textfield, query=True, text=True)
        if prefix_text == "":
            print("No prefix text found in the prefix textfield")
        else:
            for mesh_objects in selected_object:
                cmds.rename(mesh_objects, prefix_text + "_" + mesh_objects)

    def AddSuffixText(self, *args): # Used by Add Suffix Button
        selected_object = cmds.ls(selection=True)
        suffix_text = cmds.textField(self.suffix_textfield, query=True, text=True)
        if suffix_text == "":
            print("No suffix text found in the prefix textfield")
        else:
            for mesh_objects in selected_object:
                cmds.rename(mesh_objects, mesh_objects + "_" + suffix_text)

    def PrefixPresetButton(self, prefix_btn_label, *args): # Used By Default Prefix Buttons
        selected_object = cmds.ls(selection=True)
        if prefix_btn_label == "Ext_":
            for mesh_objects in selected_object:
                cmds.rename(mesh_objects, "Ext_" + mesh_objects)
        elif prefix_btn_label == "Chr_":
            for mesh_objects in selected_object:
                cmds.rename(mesh_objects, "Chr_" + mesh_objects)
        elif prefix_btn_label == "Sm_":
            for mesh_objects in selected_object:
                cmds.rename(mesh_objects, "Sm_" + mesh_objects)
        elif prefix_btn_label == "Sk_":
            for mesh_objects in selected_object:
                cmds.rename(mesh_objects, "Sk_" + mesh_objects)

    def SuffixPresetButton(self, suffix_btn_label, *args): # Used By Default Suffix Buttons
        selected_object = cmds.ls(selection=True)
        if suffix_btn_label == "_Grp":
            for mesh_objects in selected_object:
                cmds.rename(mesh_objects, mesh_objects + "_Grp")
        elif suffix_btn_label == "_Geo":
            for mesh_objects in selected_object:
                cmds.rename(mesh_objects, mesh_objects + "_Geo")
        elif suffix_btn_label == "_Loc":
            for mesh_objects in selected_object:
                cmds.rename(mesh_objects, mesh_objects + "_Loc")
        elif suffix_btn_label == "_Ctrl":
            for mesh_objects in selected_object:
                cmds.rename(mesh_objects, mesh_objects + "_Ctrl")

MayaMeshRenamer()
