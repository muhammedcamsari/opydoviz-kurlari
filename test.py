#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 
# 
#  Doviz kurlari icin ornekler icerir
#
#

import opydoviz

kur = opydoviz.kur()

# Doviz kurlari birim kodlari
opydoviz.birimler('truncgil')

# TCMB icin ornek içerir
tcmb = kur.tcmb('USD', 'SATIS', 'json', verbose=False)
print (tcmb)

# # Truncgil icin ornek icerir
truncgil = kur.truncgil('USD', 'ALIS', 'clear', verbose=False)
print (truncgil)
