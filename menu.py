import nuke

toolbar = nuke.menu("Nodes")
deepMenu = toolbar.findItem("Deep")
if deepMenu is None:
    deepMenu = toolbar.addMenu("Deep", icon="DeepToolset.png")

deepMenu.addCommand("DeepThinner", "nuke.createNode('DeepThinner')", icon="DeepThinner.png")
