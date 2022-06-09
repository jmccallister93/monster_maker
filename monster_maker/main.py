from sqlite3 import Row
import numpy as np 
import pandas as pd
import os
import tkinter
import customtkinter
from tkinter import *

#TODO 
#Create completely random option
#Create complete manual option
#Create mix of both
#Import Data
#Fix health options low, medium high extreme

#Create Starting Window
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
root = customtkinter.CTk()
root.title("Monster Maker")
root.geometry("1450x900")

#Set row headings list
monster_stat_list = [
    "Name",
    "Size",
    "Type",
    "AC",
    "HP",
    "Speed",
    "STR",
    "DEX",
    "CON",
    "INT",
    "WIS",
    "CHA",
    "Saves",
    "Skills",
    "Senses",
    "Languages",
    "Abilites",
    "Attacks",
    "Spells"
]

#Set the row heading from list
for index, row in enumerate(monster_stat_list): 
    monster_stats_label = customtkinter.CTkLabel(root, text=row + ":")
    #may want to add index + 1 to start it on row 2 
    monster_stats_label.grid(row=index + 7, column=0)

#Create a generate function for button 
def generate_monster():
    pass

#Create Generate Button
generate_monster_button = customtkinter.CTkButton(root, text="Generate Monster", command=generate_monster)
generate_monster_button.grid(row=0, column=0)

### Create Monster Options ###

#Size Combobox
size_label = customtkinter.CTkLabel(root, text="Size Option")
size_label.grid(row=1,column=0)
size_options = ["Random", "Tiny", "Small", "Medium", "Large", "Huge", "Gargantuan"]
size_combobox = customtkinter.CTkComboBox(root, values=size_options)
size_combobox.grid(row=2, column=0)
size_combobox.set("Choose Size")
current_size = size_combobox.current_value

#Monster type Combobox
type_label = customtkinter.CTkLabel(root, text="Monster Type Option")
type_label.grid(row=1,column=1)
type_options = ["Random",
                "Aberration", 
                "Beast", 
                "Celestial", 
                "Construct", 
                "Dragon", 
                "Elemental", 
                "Fey", 
                "Fiend", 
                "Giant", 
                "Humanoid", 
                "Monstrosity", 
                "Ooze", 
                "Plant", 
                "Undead"
                ]
type_combobox = customtkinter.CTkComboBox(root, values=type_options)
type_combobox.grid(row=2, column=1)
type_combobox.set("Choose Type")
current_type = type_combobox.current_value

#AC type Combobox
ac_type_label = customtkinter.CTkLabel(root, text="AC Type Option")
ac_type_label.grid(row=1,column=2)
ac_type_options = ["Random", "Ancestral", "Magic", "Natural", "Worn"]
ac_type_combobox = customtkinter.CTkComboBox(root, values= ac_type_options)
ac_type_combobox.grid(row=2, column=2)
ac_type_combobox.set("Choose AC Type")
current_ac_type = ac_type_combobox.current_value


#AC Combobox
ac_label = customtkinter.CTkLabel(root, text="AC Option")
ac_label.grid(row=1,column=3)
ac_options = ["Random",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20",
            "21",
            "22",
            "23",
            "24",
            "25",
]
# ac = 6
# for a in range(19):
#     ac += 1
#     ac_options.append(ac)
ac_combobox = customtkinter.CTkComboBox(root, values= ac_options)
ac_combobox.grid(row=2, column=3)
ac_combobox.set("Choose AC")
current_ac = ac_combobox.current_value

#HP low Combobox
hp_low_label = customtkinter.CTkLabel(root, text="Low HP Option")
hp_low_label.grid(row=1,column=4)
hp_low_options = [
    "Random",
    "5",
    "10",
    "15",
    "20",
    "25",
    "30",
    "35",
    "40",
    "45",
    "50",
    "55",
    "60",
    "65",
    "70",
    "75",
    "80",
    "85",
    "90",
    "95",
    "100",
]
# hp = 0
# for h in range(30):
#     hp += 5
#     hp_options.append(hp)
hp_low_combobox = customtkinter.CTkComboBox(root, values=hp_low_options)
hp_low_combobox.grid(row=2, column=4)
hp_low_combobox.set("Choose HP")
current_hp = hp_low_combobox.current_value

#Medium HP combobox
hp_medium_label = customtkinter.CTkLabel(root, text="Medium HP Option")
hp_medium_label.grid(row=1,column=5)
hp_medium_options = [
    "Random",
    "105",
    "110",
    "115",
    "120",
    "125",
    "130",
    "135",
    "140",
    "145",
    "150",
    "155",
    "160",
    "165",
    "170",
    "175",
    "180",
    "185",
    "190",
    "195",
    "200",
]
hp_medium_combobox = customtkinter.CTkComboBox(root, values=hp_medium_options)
hp_medium_combobox.grid(row=2, column=5)
hp_medium_combobox.set("Choose HP")
current_hp = hp_medium_combobox.current_value

#High HP combobox
hp_high_label = customtkinter.CTkLabel(root, text="High HP Option")
hp_high_label.grid(row=1,column=6)
hp_high_options = [
    "Random",
    "205",
    "210",
    "215",
    "220",
    "225",
    "230",
    "235",
    "240",
    "245",
    "250",
    "255",
    "260",
    "265",
    "270",
    "275",
    "280",
    "285",
    "290",
    "295",
    "300",
]
hp_high_combobox = customtkinter.CTkComboBox(root, values=hp_high_options)
hp_high_combobox.grid(row=2, column=6)
hp_high_combobox.set("Choose HP")
current_hp = hp_high_combobox.current_value

#Movement Options
# Base Movement Speed Combobox
move_speed_label = customtkinter.CTkLabel(root, text="Base Move Speed Option")
move_speed_label.grid(row=1,column=7)
move_speed_options = ["Random", 
                    "10", 
                    "20", 
                    "30", 
                    "40", 
                    "50", 
                    "60", 
                    "70", 
                    "80",
                    "90",
                    "100",
                    "110",
                    "120",
]
move_speed_combobox = customtkinter.CTkComboBox(root, values=move_speed_options)
move_speed_combobox.grid(row=2, column=7)
move_speed_combobox.set("Choose Move Speed")
current_move_speed = move_speed_combobox.current_value

#Movement Type Combobox
move_type_label = customtkinter.CTkLabel(root, text="Extra Move Type Option")
move_type_label.grid(row=1,column=8)
move_type_options = ["Random", "Burrow", "Climb", "Fly", "Swim"]
move_type_combobox = customtkinter.CTkComboBox(root, values=move_type_options)
move_type_combobox.grid(row=2, column=8)
move_type_combobox.set("Choose Move Type")
current_move_type = move_type_combobox.current_value

#Extra Speed
extra_speed_label = customtkinter.CTkLabel(root, text="Extra Move Speed Option")
extra_speed_label.grid(row=1,column=9)
extra_speed_options = ["Random", 
                    "10", 
                    "20", 
                    "30", 
                    "40", 
                    "50", 
                    "60", 
                    "70", 
                    "80",
                    "90",
                    "100",
                    "110",
                    "120",
]
extra_speed_combobox = customtkinter.CTkComboBox(root, values=extra_speed_options)
extra_speed_combobox.grid(row=2, column=9)
extra_speed_combobox.set("Choose Extra Move Speed")
current_extra_speed = extra_speed_combobox.current_value

#Stats
stats_options = [
    "Random",
    "1",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
]
#STR Combobox
str_label = customtkinter.CTkLabel(root, text="STR Option")
str_label.grid(row=3,column=0)
str_combobox = customtkinter.CTkComboBox(root, values=stats_options)
str_combobox.grid(row=4, column=0)
str_combobox.set("Choose STR")
current_str = str_combobox.current_value

#DEX Combobox
dex_label = customtkinter.CTkLabel(root, text="DEX Option")
dex_label.grid(row=3,column=1)
dex_combobox = customtkinter.CTkComboBox(root, values=stats_options)
dex_combobox.grid(row=4, column=1)
dex_combobox.set("Choose STR")
current_dex = dex_combobox.current_value

#CON Combobox
con_label = customtkinter.CTkLabel(root, text="CON Option")
con_label.grid(row=3,column=2)
con_combobox = customtkinter.CTkComboBox(root, values=stats_options)
con_combobox.grid(row=4, column=2)
con_combobox.set("Choose CON")
current_con = con_combobox.current_value

#INT Combobox
int_label = customtkinter.CTkLabel(root, text="INT Option")
int_label.grid(row=3,column=3)
int_combobox = customtkinter.CTkComboBox(root, values=stats_options)
int_combobox.grid(row=4, column=3)
int_combobox.set("Choose INT")
current_int = int_combobox.current_value

#WIS Combobox
wis_label = customtkinter.CTkLabel(root, text="WIS Option")
wis_label.grid(row=3,column=4)
wis_combobox = customtkinter.CTkComboBox(root, values=stats_options)
wis_combobox.grid(row=4, column=4)
wis_combobox.set("Choose WIS")
current_wis = wis_combobox.current_value

#CHA Combobox
cha_label = customtkinter.CTkLabel(root, text="CHA Option")
cha_label.grid(row=3,column=5)
cha_combobox = customtkinter.CTkComboBox(root, values=stats_options)
cha_combobox.grid(row=4, column=5)
cha_combobox.set("Choose CHA")
current_cha = cha_combobox.current_value

#Saving Throws
saves_label = customtkinter.CTkLabel(root, text="Saves Option")
saves_label.grid(row=3,column=6)
saves_options = ["Random","STR","DEX","CON","INT","WIS","CHA"]
saves_combobox = customtkinter.CTkComboBox(root, values=saves_options)
saves_combobox.grid(row=4, column=6)
saves_combobox.set("Choose Saves")
current_saves = saves_combobox.current_value

###TODO
#Saving throw value combobox
saves_value_label = customtkinter.CTkLabel(root, text="Saves Value Option")
saves_value_label.grid(row=3,column=7)
saves_value_options = ["Random"]
saves_value_combobox = customtkinter.CTkComboBox(root, values=saves_value_options)
saves_value_combobox.grid(row=4, column=7)
saves_value_combobox.set("Choose Saves Value")
current_saves_value = saves_value_combobox.current_value

#Skills combobox
skills_label = customtkinter.CTkLabel(root, text="Skills Option")
skills_label.grid(row=3,column=8)
skills_options = ["Random",
                "Acrobatics",
                "Animal Handling",
                "Arcana",
                "Athletics",
                "Deception",
                "History",
                "Insight",
                "Intimidation",
                "Investigation",
                "Medicine",
                "Nature",
                "Perception",
                "Performance",
                "Persuasion",
                "Religion",
                "Sleight of Hand",
                "Stealth",
                "Survival",
]
skills_combobox = customtkinter.CTkComboBox(root, values=skills_options)
skills_combobox.grid(row=4, column=8)
skills_combobox.set("Choose Skills")
current_skills = skills_combobox.current_value

###TODO
#Skills value combobox
skills_value_label = customtkinter.CTkLabel(root, text="Skills Value Option")
skills_value_label.grid(row=3,column=9)
skills_value_options = ["Random"]
skills_value_combobox = customtkinter.CTkComboBox(root, values=skills_value_options)
skills_value_combobox.grid(row=4, column=9)
skills_value_combobox.set("Choose Skills Value")
current_skills_value = skills_value_combobox.current_value

#Vulnerabilites combobox
vuln_label = customtkinter.CTkLabel(root, text="Vulnerability Option")
vuln_label.grid(row=5,column=0)
vuln_options = ["Random",
                "Acid",
                "Cold",	
                "Fire",
                "Force",
                "Lightning",
                "Necrotic",
                "Poison",
                "Psychic",
                "Radiant",
                "Thunder",
                "Bludgeoning",
                "Slashing",
                "Piercing",
                "Magical",
                "Magical Bludgeoning",
                "Magical Slashing",
                "Magical Piercing",
]
vuln_combobox = customtkinter.CTkComboBox(root, values=vuln_options)
vuln_combobox.grid(row=6, column=0)
vuln_combobox.set("Choose Vulnerability")
current_vuln = vuln_combobox.current_value

#Immunities combobox
immune_label = customtkinter.CTkLabel(root, text="Immunity Option")
immune_label.grid(row=5,column=1)
immune_options = ["Random",
                "Acid",
                "Cold",	
                "Fire",
                "Force",
                "Lightning",
                "Necrotic",
                "Poison",
                "Psychic",
                "Radiant",
                "Thunder",
                "Bludgeoning",
                "Slashing",
                "Piercing",
                "Magical",
                "Magical Bludgeoning",
                "Magical Slashing",
                "Magical Piercing",
]
immune_combobox = customtkinter.CTkComboBox(root, values=immune_options)
immune_combobox.grid(row=6, column=1)
immune_combobox.set("Choose Immunity")
current_immune = immune_combobox.current_value

#Sense combobox
senses_label = customtkinter.CTkLabel(root, text="Senses Option")
senses_label.grid(row=5,column=2)
senses_options = ["Random","Normal","Darkvision","Blindsight","Truesight","Tremorsense"]
senses_combobox = customtkinter.CTkComboBox(root, values=senses_options)
senses_combobox.grid(row=6, column=2)
senses_combobox.set("Choose Senses")
current_sense = senses_combobox.current_value

#Sense value combobox
senses_value_label = customtkinter.CTkLabel(root, text="Senses Value Option")
senses_value_label.grid(row=5,column=3)
senses_value_options = ["Random",
                        "10","20","30",
                        "40","50","60",
                        "70","80","90",
                        "100","110","120"
                        ]
senses_value_combobox = customtkinter.CTkComboBox(root, values=senses_value_options)
senses_value_combobox.grid(row=6, column=3)
senses_value_combobox.set("Choose Senses Value")
current_sense_value = senses_value_combobox.current_value

#Languages combobox
lang_label = customtkinter.CTkLabel(root, text="Languages Option")
lang_label.grid(row=5,column=4)
lang_options = ["Random",
                    "Common",
                    "Dwarvish",
                    "Elvish",
                    "Giant",
                    "Gnomish",
                    "Goblin",
                    "Halfling",
                    "Orc",
                    "Abyssal",
                    "Celestial",
                    "Deep Speech",
                    "Draconic",
                    "Infernal",
                    "Primordial",
                    "Sylvan",
                    "Undercommon"
                    ]
lang_combobox = customtkinter.CTkComboBox(root, values=lang_options)
lang_combobox.grid(row=6, column=4)
lang_combobox.set("Choose Languages")
current_lang = lang_combobox.current_value

###TODO
#Abilites value combobox
abilities_label = customtkinter.CTkLabel(root, text="Abilities Option")
abilities_label.grid(row=5,column=5)
abilities_options = ["Random"]
abilities_combobox = customtkinter.CTkComboBox(root, values=abilities_options)
abilities_combobox.grid(row=6, column=5)
abilities_combobox.set("Choose Abilities")
current_abilities = abilities_combobox.current_value

###TODO
#Attacks value combobox
attacks_label = customtkinter.CTkLabel(root, text="Attacks Option")
attacks_label.grid(row=5,column=6)
attacks_options = ["Random"]
attacks_combobox = customtkinter.CTkComboBox(root, values=attacks_options)
attacks_combobox.grid(row=6, column=6)
attacks_combobox.set("Choose Attacks Value")
current_attacks = attacks_combobox.current_value

###TODO
#Spells value combobox
spells_label = customtkinter.CTkLabel(root, text="Spells Option")
spells_label.grid(row=5,column=7)
spells_options = ["Random"]
spells_combobox = customtkinter.CTkComboBox(root, values=spells_options)
spells_combobox.grid(row=6, column=7)
spells_combobox.set("Choose Spells")
current_spells = spells_combobox.current_value

#Main loop to run window
root.mainloop()