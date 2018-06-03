#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Copyright © 2018 Little Sparkle,
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

'''
  Generate the Mac address and the S/N code of the device.
  @author: Tian Ye
  @since: 2014-11-14
'''

import random
import os
import os.path


def g_mac(sn):
  '''
    Generate the Mac address.
    Keyword arguments: 
    sn - {string} S/N code.
  '''

  sn = sn[5:-3]
  n1 = random.randint(0,9)
  n2 = random.randint(0,9)
  return '%s%s:%s:%s:%s:%s:%s'%(n1, n2, sn[0:2], sn[2:4], sn[4:6], sn[6:8], sn[8:])


def g_device(num, model, v, y, w, fac):
  '''
      Generate the list of the S/N code.
      e.g. A380A7DE23026F5EMD. #[A380][A][7DF][01-35][00001-FFFFF][EMD]

    Keyword arguments: 
    num - {int} quantity of the devices.
    model - {sting}  model of the device.
    v - {sting} version of the Hardware.
    y - {int} year of manufacture.
    w - {int} week of manufacture.
    fac - {Sting} The Factory.
  '''

  model = model.upper()
  v = v.upper()
  fac = fac.upper()

  y = str(hex(y))[2:].upper()

  w = hex(w)[2:].upper()
  w = (2-len(w))*'0'+w
  
  folder = './devices'
  if not os.path.exists(folder): 
    os.makedirs(folder)

  f = open('%s/%s.list'%(folder, w),'a+')

  for i in range(0, num):
    n = i+1

    n = str(hex(n))[2:].upper()
    n = (5-len(n))*'0'+n
    sn = '%s%s%s%s%s%s'%(model, v, y, w, n, fac)
    mac = g_mac(sn)
    f.write('%s %s\n'%(sn, mac))

  f.close()


if __name__ == '__main__':

  # Test code 
  for i in range(1,5):
    g_device(10000, "A380", "A", 2014, i, "EMD")

  # [A380][A][7DF][01-35][00001-FFFFF][EMD]
  s = 'A380A7DE23026F5EMD'

  model = s[:4]
  hd_v = s[4:5]
  y = int(s[5:8], 16)
  w = int (s[8:10], 16)
  n = int(s[10:15], 16)
  fac = s[15:]

  print 'model: ', model
  print 'hd_v: ', hd_v
  print 'y: ', y
  print 'w: ', w
  print 'n: ', s[10:15], n
  print 'fac: ', fac

