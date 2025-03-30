# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
# 
# Copyright (c) 2025 Guillermo Leira Temes

import math

def small_random(seed):
	p = 61343
	g = 48799
	m = 36277
	return (g*seed*m//(g+seed-m)) % p
#   28912384984
#--------------------------
# 2|Hola sdfhasf
# 4|
# 5|
# 7|
# 9|
#10|
#11|
#13|
#-------------------------

# sqrt(longitud_datos)*2

def normal_tms(data, passwords, mode):
	
	new_text = [[0]*len(passwords[0]) for _ in range(len(passwords[1]))]
	for x in range(len(data)):
		for y in range(len(data[0])):
			if mode=="encrypt":
				new_text[x][y] = data[x][y] + (passwords[0][x] + passwords[1][y])
			elif mode=="decrypt":
				new_text[x][y] = data[x][y] - (passwords[0][x] + passwords[1][y])
	return new_text

class Tms:
	def __init__(self):
		self.seeda = seeda
		self.seedb = seedb
		self.keya = []
		self.keyb = []
	def gen_key(self, len):
		a = self.seeda
		b = self.seedb
		for i in range(len):
			a = small_random(b)
			b = small_random(a)
			self.keya.append(a)
			self.keyb.append(b)
	def keygen(self, txt_len):
		len = round(math.sqrt(txt_len)*2)+1
		self.gen_key(len)
	def encrypt(self, txt):
		c_txt = ""
		lent = len(self.keya)
		if (lent)**2 >= len(txt):
			pass
		else:
			return -1
		l = 0
		c = 0
		while (l*lent+c) < len(txt):
			c = 0
			while c < lent:
				if c+l*lent >= len(txt):
					break
				c_txt += chr(ord(txt[c+l*lent]) + self.keya[c] + self.keyb[l])
				c += 1
			l += 1
		return c_txt
	def decrypt(self, txt):
		c_txt = ""
		lent = len(self.keya)
		if lent**2 >= len(txt):
			pass
		else:
			return -1
		l = 0
		c = 0
		while (l*lent+c) < len(txt):
			c = 0
			while c < lent:
				if c+l*lent >= len(txt):
					break
				c_txt += chr(ord(txt[c+l*lent]) - self.keya[c] - self.keyb[l])
				c += 1
			l += 1
		return c_txt
	def data_crypt(self, data):
		c_data = []
		lent = len(self.keya)
		if lent**2 >= len(data):
			pass
		else:
			return -1
		l = 0
		c = 0
		while (l*lent+c) < len(data):
			c = 0
			while c < lent:
				if c+l*lent >= len(txt):
					break
				c_data.append(data[c+l*lent]+self.keya[c] + self.keyb[l])
				c += 1
			l += 1
		return c_data
	def data_decrypt(self, data):
		c_data = []
		lent = len(self.keya)
		if lent**2 >= len(data):
			pass
		else:
			return -1
		l = 0
		c = 0
		while (l*lent+c) < len(data):
			c = 0
			while c < lent:
				if c+l*lent >= len(txt):
					break
				c_data.append(data[c+l*lent]-self.keya[c] - self.keyb[l])
				c += 1
			l += 1
		return c_data
