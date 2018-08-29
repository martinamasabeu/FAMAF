#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ej1.py
#  
#  Copyright 2018 Live System User <liveuser@localhost>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
from turtle import*

from graficos import poligonos
def casas():
	for a in range (5):
		poligonos(4,20)
		left(90)
		forward(20)
		right(90)
		poligonos(3,20)
		forward(20)
		right(90)
		forward(20)
		left(90)
	left(90)
	forward(40)
	left(90)
	forward(100)
	right(180)
for a in range(5):
	casas()	
exitonclick()
