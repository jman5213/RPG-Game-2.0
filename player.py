from random import randint

class Character():

  def __init__(self, Lvl=1, LvlPlusHp=5):
    self.LvlHpGain = LvlPlusHp
    self.LvlUpSoon = 0
    self.Lvl = Lvl
    self.MaxHP = 10
    self.HitPoints = self.MaxHP
    self.HPisFull = True
    self.GP = 10
    self.carried = 0.0#pounds
    self.Inventory = {"carry":{},"bag":{}}
    self.abilityScores = {"str":1,"dex":1,"con":1,"int":1,"wis":1,"char":1}
    self.abilityMods = {
      1:-5,
      2:-4,
      3:-4,
      4:-3,
      5:-3,
      6:-2,
      7:-2,
      8:-1,
      9:-1,
      10:0,
      11:0,
      12:1,
      13:1,
      14:2,
      15:2,
      16:3,
      17:3,
      18:4,
      19:4,
      20:5,
      21:5,
      22:6,
      23:6,
      24:7,
      25:7,
      26:8,
      27:8,
      28:9,
      29:9,
      30:10
    }
    self.maxWt = self.abilityScores["str"] * 15
    self.encumbered = False

  def rollDice(self, sides):
    return randint(0,sides)

  def getAbilityScore(self, type):
    return self.abilityScores[type]

  def getModifier(self, type):
    return self.abilityMods[self.abilityScores[type]]

  def scoreCheck(self, type, dc):
    roll = self.rollDice(20)
    if roll != 0 and roll != 20:
      return self.abilityMods[self.abilityScores[type]]+roll == dc
    else:
      return roll
    #add initialization, and lvl up
  def getMaxHP(self):
    return self.MaxHP
#move to player class
  def queLvlUp(self):
    self.LvlUpSoon = 1
#move to player class
  def rest(self):
    if self.LvlUpSoon == 1:
      self.Lvl += 1
      self.MaxHP += self.LvlHpGain
    self.HitPoints = self.MaxHP
    self.HPisFull = True
#move to player class
  def getLvl(self):
    return self.Lvl
    
  def addPack(self, pack):
    self.Inventory[pack] = {}
  
  def changeMaxHP(self, newMHP):
    if newMHP > 0:
      self.MaxHP = newMHP
    else:
      print(newMHP,"is negative!")
    
  def getHP(self):
    return self.HitPoints

  def showInventory(self):
    return self.Inventory
    
  def addToInventory(self, add, pack, wt, cost, value):
    if self.GP > cost:
      self.Inventory[pack][add]={"wt":wt,"value":value}
      self.GP -= cost
      self.carried += wt
      if self.carried > self.maxWt:
        self.encumbered = True
    else:
      print("Too Expensive!")
    
  def hit(self, damage):
    self.HitPoints -= damage
    if self.HitPoints < 0:
      self.HitPoints = 0
    self.HPisFull = False

  def heal(self, heal):
    self.HitPoints += heal
    if self.HitPoints > self.MaxHP:
      self.HitPoints = self.MaxHP
      self.HPisFull = True

  def getGp(self):
    return self.GP

  def sellItem(self, item, pack, customPrice=0):
    if pack in self.Inventory:
      if item in self.Inventory[pack]:
        if customPrice!=0:
          self.GP += customPrice
        else:
          self.GP += self.Inventory[pack][item]["value"]
        self.carried -= self.Inventory[pack][item]["wt"]
        del self.Inventory[pack][item]
      else:
        print("Item not in pack!")
    else:
      print("Pack not found!")
      
  def dropItem(self, item, pack):
    if pack in self.Inventory:
      if item in self.Inventory[pack]:
        del self.Inventory[pack][item]
      else:
        print(item,"not found in inventory!")
    else:
      print(pack,"not found in inventory!")

  def moveToPack(self, item, toPack, fromPack):
    if fromPack in self.Inventory:
      if toPack in self.Inventory:
        if item in self.Inventory[fromPack]:
          self.Inventory[toPack][item]:self.Inventory[toPack][item]
          del self.Inventory[fromPack][item]
        else:
          print(item,"does not exist in",fromPack+"!")
      else:
        print(toPack,"not found in inventory!")
    else:
      print(fromPack,"not found in inventory!")

  def getWt(self):
    if self.carried > self.maxWt:
      self.encumbered = True
    return self.carried

  def isEncumbered(self):
    return self.encumbered