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

class Tms:
	def __init__(self, seed_1, seed_2):
		self.seeda = seed_1
		self.seedb = seed_2
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
