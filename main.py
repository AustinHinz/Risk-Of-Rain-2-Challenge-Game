# Imports needed resources
import ItemList
import random

# Variables that SHOULD NOT be changed (used in code)
MinItems = 1  # Minimum amount of items for challenge

# Variables user can change to determine generated outcome
MaxItems = 3  # Max number of items a player can be given
Player = 2    # Number of players that will be in challenge

# Function that returns number of items for that tier, for that player
def GenItems():
  GenItems = random.randint(MinItems, MaxItems)
  return GenItems

# For statement that generates challenge for each player
for player in range(Player):

  # Variables whoms value will be randomly selected from ItemList.py
  HeroPicks           = random.choice(ItemList.HeroSelection);
  CommonItemPicks     = str(random.choices(ItemList.CommonItems, k = GenItems()))[1:-1];
  UncommonItemPicks   = str(random.choices(ItemList.UncommonItems, k = GenItems()))[1:-1];
  LegendaryItemPicks  = str(random.choices(ItemList.LegendaryItems, k = GenItems()))[1:-1];
  Boss_PlanetPicks    = str(random.choices(ItemList.Boss_PlanetItems, k = GenItems()))[1:-1];
  EquipmentPicks      = str(random.choices(ItemList.EquipmentItems, k = GenItems()))[1:-1];

  # Displays the challenge results to the user
  print(f"""
-------------------------------------------

  Today's Challenge for player {player+1} is...

  Hero: {HeroPicks}

        Common Item(s): {CommonItemPicks}
      Uncommon Item(s): {UncommonItemPicks}
    Lengendary Item(s): {LegendaryItemPicks}
   Boss/Planet Item(s): {Boss_PlanetPicks}
          Equipment(s): {EquipmentPicks}

  -------------------------------------------
  """)
  player += 1
