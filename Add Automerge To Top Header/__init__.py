# ------------------------------------------------------------------------------
# Add Automerge Button To Top Header
# Licensed under GNU General Public License v3 or later
# ------------------------------------------------------------------------------
import bpy

def draw_automerge_header(self, context):
    layout = self.layout
    tool_settings = context.tool_settings
    
    if context.mode == 'EDIT_MESH':
        row = layout.row(align=True)
        row.separator(factor=0.5)
        row.prop(tool_settings, "use_mesh_automerge", text="", icon='AUTOMERGE_ON')
        
        if tool_settings.use_mesh_automerge:
            row.prop(tool_settings, "double_threshold", text="")

def register():
    bpy.types.VIEW3D_HT_header.append(draw_automerge_header)

def unregister():
    bpy.types.VIEW3D_HT_header.remove(draw_automerge_header)

