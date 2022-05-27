#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 
# 
#  Doviz kurlari icin ornekler icerir
#
#

# import edilir.
import opydoviz

# class belirlenir
kur = opydoviz.kur()


# TCMB icin ornek içerir
tcmb = kur.tcmb('USD', 'ALIS', 'text', verbose=False)
print (tcmb)

# Truncgil icin ornek icerir
truncgil = kur.truncgil('USD', 'ALIS', 'text', verbose=False)
print (truncgil)

