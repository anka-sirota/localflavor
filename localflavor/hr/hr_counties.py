# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from localflavor.stub import _

#: Croatian Counties: http://en.wikipedia.org/wiki/ISO_3166-2:HR
#: Croatia doesn't have official abbreviations for counties. The ones provided are in common use.
COUNTY_CHOICES = (
    ('GZG', _('Grad Zagreb')),
    ('BBŽ', _('Bjelovarsko-bilogorska županija')),
    ('BPŽ', _('Brodsko-posavska županija')),
    ('DNŽ', _('Dubrovačko-neretvanska županija')),
    ('IŽ', _('Istarska županija')),
    ('KŽ', _('Karlovačka županija')),
    ('KKŽ', _('Koprivničko-križevačka županija')),
    ('KZŽ', _('Krapinsko-zagorska županija')),
    ('LSŽ', _('Ličko-senjska županija')),
    ('MŽ', _('Međimurska županija')),
    ('OBŽ', _('Osječko-baranjska županija')),
    ('PSŽ', _('Požeško-slavonska županija')),
    ('PGŽ', _('Primorsko-goranska županija')),
    ('SMŽ', _('Sisačko-moslavačka županija')),
    ('SDŽ', _('Splitsko-dalmatinska županija')),
    ('ŠKŽ', _('Šibensko-kninska županija')),
    ('VŽ', _('Varaždinska županija')),
    ('VPŽ', _('Virovitičko-podravska županija')),
    ('VSŽ', _('Vukovarsko-srijemska županija')),
    ('ZDŽ', _('Zadarska županija')),
    ('ZGŽ', _('Zagrebačka županija')),
)

#: Only common license plate prefixes are provided. Special cases and obsolete prefixes are omitted.
#: http://hr.wikipedia.org/wiki/Dodatak:Popis_registracijskih_oznaka_za_cestovna_vozila_u_Hrvatskoj
HR_LICENSE_PLATE_PREFIX_CHOICES = (
    ('BJ', 'BJ'),
    ('BM', 'BM'),
    ('ČK', 'ČK'),
    ('DA', 'DA'),
    ('DE', 'DE'),
    ('DJ', 'DJ'),
    ('DU', 'DU'),
    ('GS', 'GS'),
    ('IM', 'IM'),
    ('KA', 'KA'),
    ('KC', 'KC'),
    ('KR', 'KR'),
    ('KT', 'KT'),
    ('KŽ', 'KŽ'),
    ('MA', 'MA'),
    ('NA', 'NA'),
    ('NG', 'NG'),
    ('OG', 'OG'),
    ('OS', 'OS'),
    ('PU', 'PU'),
    ('PŽ', 'PŽ'),
    ('RI', 'RI'),
    ('SB', 'SB'),
    ('SK', 'SK'),
    ('SL', 'SL'),
    ('ST', 'ST'),
    ('ŠI', 'ŠI'),
    ('VK', 'VK'),
    ('VT', 'VT'),
    ('VU', 'VU'),
    ('VŽ', 'VŽ'),
    ('ZD', 'ZD'),
    ('ZG', 'ZG'),
    ('ŽU', 'ŽU'),
)