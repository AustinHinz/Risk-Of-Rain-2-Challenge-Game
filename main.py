# Imports needed resources
import ItemList
import random

# Variables user can change to determine generated outcome
NumItems = 1

# Variables whoms value will be randomly selected from ItemList.py
HeroPicks           = random.choice(ItemList.HeroSelection);
CommonItemPicks     = random.choices(ItemList.CommonItems, k = NumItems);
UncommonItemPicks   = random.choices(ItemList.UncommonItems, k = NumItems);
LegendaryItemPicks  = random.choices(ItemList.LegendaryItems, k = NumItems);
Boss_PlanetPicks    = random.choices(ItemList.Boss_PlanetItems, k = NumItems);
EquipmentPicks      = random.choices(ItemList.EquipmentItems, k = NumItems);

# Displays the challenge to the user
print(f"""

Today's Challenge is.....

-------------------------------------------

Hero: {HeroPicks}

      Common Items: {CommonItemPicks}
    Uncommon Items: {UncommonItemPicks}
  Lengendary Items: {LegendaryItemPicks}
Boss/Planent Items: {Boss_PlanetPicks}
         Equipment: {EquipmentPicks}

-------------------------------------------
""")
