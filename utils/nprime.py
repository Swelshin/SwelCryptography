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

def prime(num):
    for i in range(2, num):
        if num % i == 0:
            return num, False
    print("[*] " + str(num) + " [*]")
    return str(num), True
def check():
    l = []
    for i in range(2, int(input("HASTA QUE NUMERO SE COMPROBARA? →  "))):
        n, b = prime(i)
        if b == True:
            l.append("[*]" + n + "[*]")
    f = open("primes.txt", "w")
    for a in l:
        f.write(a + "\n")
    f.close()
check()
