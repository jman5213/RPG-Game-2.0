import save

armor = {}
wpns = {}
magicalyAtuned = {}

#for more info, phb. 45
classes = ["barbarian","fighter","ranger","rouge","wizard","bard"]

classfeaturesStart = {#add abilitys for 1 subclass per, also add starting equipment
  "barbarian":{
    "hitDice":12,
    "savingThrowProficiencies":["str","con"],
    "armorProf":["light","medium","sheilds"],
    "wpnProf":{"type":["simple","martial"],"specific":[]}
  },
  "fighter":{
    "hitDice":10,
    "savingThrowProficiencies":["str","con"],
    "armorProf":["light","medium","heavy","sheilds"],
    "wpnProf":{"type":["simple","martial"],"specific":[]}
  },
  "ranger":{
    "hitDice":10,
    "savingThrowProficiencies":["str","dex"],
    "armorProf":["light","medium","sheilds"],
    "wpnProf":{"type":["simple","martial"],"specific":[]}
  },
  "rouge":{
    "hitDice":8,
    "savingThrowProficiencies":["dex","int"],
    "armorProf":["light"],
    "wpnProf":{"type":["simple"],"specific":["hand crossbow","longsword","rapier","shortsword"]}
  },
  "wizard":{
    "hitDice":6,
    "savingThrowProficiencies":["int","wiz"],
    "armorProf":[],
    "wpnProf":{"type":[],"specific":["dagger","dart","sling","quarterstaffs","light crossbow"]}
  },
  "bard":{
    "hitDice":8,
    "savingThrowProficiencies":["dex","cha"],
    "armorProf":["light"],
    "wpnProf":{"type":["simple"],"specific":["handcrossbow","longsword","rapier","shortsword"]}
  }
}

races = ["mtn. dwarf phb. 18", "hill dwarf phb. 18","high elf phb. 23","wood elf phb. 24","dark elf phb. 24","human phb. 29","light foot halfling phb. 28","stout halfling phb.28"]

racefeaturesStart = {
  "mountain dwarf":{
    "abilityPlus":{"str":2,"con":2},
    "MaxHpMod":0,
    "MaxHpLvlUpMod":0,
    "ageMinMax":[50,250],
    "baseHeight":4.0,
    "heightMultiplyerDice":[2,4],#e.a. [2,d4]
    "baseWt":130,
    "wtMultiplyerDice":[2,6],
    "size":"medium",
    "speed":25,
    "slowedByHeavyArmor":False,
    "darkvision":{"dim":"bright","dark":"dim","range":60},
    "advantageOnTrowsAgainst":["poison"],
    "resistantToAtks":["poison"],
    "profArmor":["light","medium"],
    "profWeapons":["batleaxe","handaxe","light hammer","warhammer"]
  },
  "hill dwarf":{
  "abilityPlus":{"con":2,"wis":1},
  "MaxHpMod":1,
  "MaxHpLvlUpMod":1,
  "ageMinMax":[50,250],
  "baseHeight":3.8,
  "heightMultiplyerDice":[2,4],#e.a. [2,d4]
  "baseWt":115,
  "wtMultiplyerDice":[2,6],
  "size":"medium",
  "speed":25,
  "slowedByHeavyArmor":False,
  "darkvision":{"dim":"bright","dark":"dim","range":60},
  "advantageOnTrowsAgainst":["poison"],
  "resistantToAtks":["poison"],
  "profArmor":["light","medium"],
  "profWeapons":["batleaxe","handaxe","light hammer","warhammer"]
  },
  "high elf":{
  "abilityPlus":{"dex":2,"int":1},
  "MaxHpMod":0,
  "MaxHpLvlUpMod":0,
  "ageMinMax":[100,675],
  "baseHeight":4.6,
  "heightMultiplyerDice":[2,10],#e.a. [2,d4]
  "baseWt":90,
  "wtMultiplyerDice":[1,4],
  "size":"medium",
  "speed":30,
  "slowedByHeavyArmor":True,
  "darkvision":{"dim":"bright","dark":"dim","range":60},
  "advantageOnTrowsAgainst":["charmed"],
  "resistantToAtks":[],
  "profArmor":[],
  "profWeapons":["longsword","shortsword","longbow","shortbow"]
  }#add wood elf, dark elf, human, lightfoot halfling, and stout halfling
}


onlvlup = {}#what happens when players lvl up

spells = {}

#save all