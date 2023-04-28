##

filep = "pack.mcmeta"
fileread = "README.txt"
filereadimp = "READMEIMPORTANT.txt"
filejsonload = "load.json"
filejsontick = "tick.json"
fileload = "load.mcfunction"
fileloop = "loop.mcfunction"
filehow = "FunctionGuide.txt"
filerec = "InsertCustomRecipeTemplate.py"
fileloot = "InsertCustomLootTableEntitiesTemplate.py"
dataname = "datapackname" # Change datapackname to whatever you wish your datapack to be called. Do not remove the quotes. Do not capitalize.

import os

def backthree(): # Saving myself 4 lines of code.
	os.chdir("..")
	os.chdir("..")
	os.chdir("..")

os.mkdir(dataname)

os.chdir(dataname)

with open(filep, "w") as fp:
	fp.write("{\n \"pack\": {\n  \"pack_format\": 10,\n  \"description\": \"Put your description here.\"\n }\n}")

os.mkdir("data")

os.chdir("data")

with open(filereadimp, "w") as frii:
	frii.write("If you change the name of " + dataname + " file you see here (the file inside of the file called \"data\"), you will need to go into minecraft/tags/functions and change the " + dataname + ":loop and " + dataname + ":load in each of the json files there to [WHATYOUCHANGEDITTO]:loop and [WHATYOUCHANGEDITTO]:load.")

os.mkdir("minecraft")

os.mkdir(dataname)

os.chdir("minecraft")

os.mkdir("tags")

with open(fileread, "w") as frr:
	frr.write("The \"tags\" contains your tick and load functions. The tick function triggers every tick, and the load function only runs when the dapatack first starts up, and when the datapack is reloaded with \"/reload\".")

os.chdir("tags")

os.mkdir("functions")

os.chdir("functions")

with open(filejsontick, "w") as fjt:
	fjt.write("{\n \"values\": [\n  \"" + dataname + ":loop\"\n ]\n}")
with open(filejsonload, "w") as fjl:
	fjl.write("{\n \"values\": [\n  \"" + dataname + ":load\"\n ]\n}")

backthree()

os.chdir(dataname)

os.mkdir("functions")

os.chdir("functions")

with open(fileload, "w") as flo:
	flo.write("## This function loads when you first start the world, and whenever you use \"/reload\"\n\nexecute at @a run tellraw @a [{\"text\":\"[\",\"color\":\"dark_green\"},{\"text\":\"SERVER\",\"color\":\"red\"},{\"text\":\"]\",\"color\":\"dark_green\"},{\"text\":\" Datapack v.1.19.3 has been loaded!\",\"color\":\"white\"}]\n\n## This command tells you that the datapack has successfully loaded.")
with open(fileloop, "w") as fl:
	fl.write("## This function is being ran every tick.")
with open(filehow, "w") as fh:
	fh.write("##\n\n#.mcfunction file type#  .mcfunction file types are used to create functions that are used by minecraft.\n\n#.mcfunction file type use#  Inside of a .mcfunction file type there can only be in game commands. For ex. \"teleport @a 69 420 10\". Each command must be written on a new line, and each command must NOT have / as the first character. That is only for in game, the .mcfunction adds that automatically.\n\n#loop.mcfunction#  The loop.mcfunction file is connected to minecraft/tags/tick in your datapack and will run every tick. The default tick speed is 20 ticks per second, meaning that loop.mcfunction runs 20 times every second.\n\n#load.mcfunction#  The load.mcfunction file runs whenever the world is opened(for single player), whenever the server starts(for mc servers), or whenever you run \"/restart\".\n\n#order#  When you enter commands into the .mcfunction files, the commands run from the top to bottom.\n\n#linking#  You can link other mcfunctions into a mcfunction (using \"function "+ dataname +":[mcfunction name without .mcfunction extension.]\") and those functions will run with the other commands in the mcfunction file.\n\n#checking if it works#  While in minecraft, you can test to see if a function works by running \"/function "+ dataname +":[Mcfunction name without extension.]\" if it gives an error, that means a command was invalid.")

backthree()

os.mkdir("PythonFiles")

os.chdir("PythonFiles")

with open(filerec, "w") as fr:
	fr.write("##\n\nimport os\n\ndataname = (\"" + dataname + "\")\n\nrec = (\"templaterecipe.json\")\nread = (\"README.txt\")\n\nos.chdir(\"..\")\nos.chdir(\"data\")\nos.chdir(dataname)\n\nos.mkdir(\"recipes\")\n\nos.chdir(\"recipes\")\n\nwith open(rec, \"w\") as filewrite:\n\tfilewrite.write(\"{\\n  \\\"type\\\": \\\"minecraft:crafting_shaped\\\",\\n  \\\"pattern\\\": [\\n    \\\"   \\\",\\n    \\\" X \\\",\\n    \\\"   \\\"\\n   ],\\n  \\\"key\\\": {\\n    \\\"X\\\": {\\n      \\\"item\\\": \\\"minecraft:dirt\\\"\\n    }\\n  },\\n  \\\"result\\\": {\\n    \\\"item\\\": \\\"minecraft:diamond\\\",\\n    \\\"count\\\": 1\\n  }\\n}\")\nwith open(read, \"w\") as filewrite:\n\tfilewrite.write(\"## TEMPLATE USE INSTRUCTIONS ##\\n\\nYou can change \\\"minecraft:dirt\\\" to any item you want to use to craft items with. You can change X to any letter you choose, but you have to change X everywhere if you change Key:{ X. You can put that letter anywhere inside of the \\\"\\\" and that represents your crafting table. You can change \\\"minecraft:diamond\\\" to any item you want to be your output item(the item that gets crafted). You can change the name of the templaterecipe.json to anything you choose, but you cannot have capitals, numbers, or symbols.\")")
with open(fileloot, "w") as flt:
	flt.write("##\n\nimport os\n\ndataname = (\"" + dataname + "\")\n\nloot = (\"loottabletemplate.json\")\nread = (\"README.txt\")\n\nos.chdir(\"..\")\nos.chdir(\"data\")\nos.chdir(dataname)\n\nos.mkdir(\"loot_tables\")\n\nos.chdir(\"loot_tables\")\n\nos.mkdir(\"entities\")\n\nos.chdir(\"entities\")\n\nwith open (loot, \"w\") as filewrite:\n\tfilewrite.write(\"##\\n\\nRead README file.\")\n\nwith open (read, \"w\") as filewrite:\n\tfilewrite.write(\"##\\n\\nGo to https://misode.github.io/loot-table/ and check that out. If you do not get the gist of it after a little bit, try taking a tutorial.\")")
with open(filereadimp, "w") as fri:
	fri.write("## THESE PYTHON SCRIPTS ONLY WORK IF YOU HAVE NOT CHANGED \"" + dataname + "\" IN THE DATA FILE. ##\n\nThese python scripts are used to create additional content for your datapack, for the new(or truly lazy) datapack creators.")
