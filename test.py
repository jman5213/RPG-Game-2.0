import player

Player = player.Character()

print(Player.getHP())
print(Player.showInventory())

Player.addToInventory("Rock", "carry",3.0,0,0)
Player.addToInventory("Sword", "carry",2.0,3,10)
Player.addToInventory("Water", "carry",5.3,0,0)

Player.dropItem("Apple", "carry")
Player.dropItem("Water", "backpack")
Player.dropItem("Water", "carry")

print(Player.showInventory())

Player.moveToPack("Banana", "bag", "carry")
Player.moveToPack("Rock", "backpack", "carry")
Player.moveToPack("Rock", "bag", "pocket")
Player.moveToPack("Rock", "bag", "bag")
Player.moveToPack("Rock", "bag", "carry")

print(Player.showInventory())

Player.addPack("box")
print(Player.showInventory())

Player.hit(3)
Player.heal(1)
print(Player.getHP())
Player.changeMaxHP(15)
Player.changeMaxHP(-3)
Player.heal(4)
print(Player.getHP())

Player.rest()
print(Player.getHP())
print(Player.getLvl())
Player.queLvlUp()
print(Player.getHP())
print(Player.getMaxHP())
Player.rest()
print(Player.getLvl())
print(Player.getHP())
print(Player.getMaxHP())

print(Player.getModifier("str"))
print(Player.scoreCheck("dex", 3))

print("GP:",Player.getGp())

Player.sellItem("Sword","carry")
print("GP:",Player.getGp())
print(Player.showInventory())

print(Player.isEncumbered())
print(Player.getWt())