# Imports needed resources
import ItemList
import random

# Variables user can change to determine generated outcome
NumItems = 1

# Variables whoms value will be randomly selected from ItemList.py
HeroPicks           = random.choice(ItemList.HeroSelection);
CommonItemPicks     = str(random.choices(ItemList.CommonItems, k = NumItems))[1:-1];
UncommonItemPicks   = str(random.choices(ItemList.UncommonItems, k = NumItems))[1:-1];
LegendaryItemPicks  = str(random.choices(ItemList.LegendaryItems, k = NumItems))[1:-1];
Boss_PlanetPicks    = str(random.choices(ItemList.Boss_PlanetItems, k = NumItems))[1:-1];
EquipmentPicks      = str(random.choices(ItemList.EquipmentItems, k = NumItems))[1:-1];

# Displays the challenge to the user
print(f"""

Today's Challenge is.....

-------------------------------------------

Hero: {HeroPicks}

      Common Item(s): {CommonItemPicks}
    Uncommon Item(s): {UncommonItemPicks}
  Lengendary Item(s): {LegendaryItemPicks}
Boss/Planent Item(s): {Boss_PlanetPicks}
        Equipment(s): {EquipmentPicks}

-------------------------------------------
""")
