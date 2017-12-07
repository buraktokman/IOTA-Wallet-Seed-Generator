#!/usr/bin/env python
#-------------------------------------------------------------------------------
# Name      : IOTA Wallet Seed Generator
# Purpose   : Python script which generates 81 character lenght IOTA Wallet Seed
#			: string containing uppercase letters and number 9
# Author	: SirDavalos
# Created   : 7 Dec 2017
# Copyright : (c) https://github.com/sirdavalos
# Licence   : MIT
#-------------------------------------------------------------------------------
from random import SystemRandom

alphabet = u'9ABCDEFGHIJKLMNOPQRSTUVWXYZ'
generator = SystemRandom()
print(u''.join(generator.choice(alphabet) for _ in range(81)))