#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('transformer_super_buff.txt',
        "Super buff for The Transformer.  Cheating!",
        [
            "Vastly buffs The Transformer, making you basically invulnerable",
            "when wearing it.",
            "",
            "Used by myself primarily just for mod testing purposes, for when I",
            "don't want to be bothered by actual combat.",
        ],
        'Transformer',
        )

attr_effects = []
for (attr, mod_type, mod_val) in [

        # Stock values
        ('/Game/Gear/Shields/_Design/Naming/Att_Shield_IgnoreManufacturerName', 'OverrideBaseValue', 1),
        ('/Game/Gear/Shields/_Design/Balance/Attributes/Att_ShieldBalance_ElementalResistance', 'OverrideBaseValue', 1.25),

        # Our buffs
        ('/Game/Gear/Shields/_Design/Balance/Attributes/Att_ShieldBalance_Capacity', 'ScaleSimple', 5000),
        ('/Game/Gear/Shields/_Design/Balance/Attributes/Att_ShieldBalance_RegenDelay', 'ScaleSimple', 0.0001),
        ('/Game/Gear/Shields/_Design/Balance/Attributes/Att_ShieldBalance_RegenRate', 'ScaleSimple', 50000),

        ]:

    last_part = attr.split('/')[-1]
    full_attr = '{}.{}'.format(attr, last_part)
    
    attr_effects.append(f"""(
        AttributeToModify=GbxAttributeData'"{full_attr}"',
        ModifierType={mod_type},
        ModifierValue=(BaseValueConstant={mod_val})
    )""")

# Apply all our custom effects
mod.reg_hotfix(Mod.PATCH, '',
        '/Game/Gear/Shields/_Design/_Uniques/Transformer/Parts/Shield_Part_Aug_HYP_LGD_Transformer',
        'InventoryAttributeEffects',
        '({})'.format(','.join(attr_effects)),
        )

mod.close()