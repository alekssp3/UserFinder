# -*- coding: utf-8 -*-
import os, time, random

class DB:
  def __init__(self, *params):
    self.coding = 'utf-8'
    if len(params) > 0:
      self.ll = self.parse(self.load(params[0]))
    else:
      self.ll = self.parse(self.load('pr1.txt'))
      #for i in range(len(self.ll)):
        #self.ll[i] = unicode(self.ll[i], 'cp1251')

  def setCoding(self, string=''):
    if string == '':
      self.coding = 'utf-8'
    else:
      self.coding = string

  def swapKeys(self, string):
    en = '`1234567890-=qwertyuiop[]\\asdfghjkl;\'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>?'
    ru = 'ё1234567890-=йцукенгшщзхъ\\фывапролджэячсмитьбю.Ё!"№;%:?*()_+ЙЦУКЕНГШЩЗХЪ/ФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,'
    #print('EN: %d, RU: %d' % (len(en), len(ru)))
    tmp = ''
    index = -1
    for i in string:
      if i in en:
        index = en.find(i)
        tmp += ru[index]
      elif i in ru:
        index = ru.find(i)
        tmp += en[index]
      else:
        tmp += i
    return tmp

  def stupidFind(self, string, full=False):
    count = 0
    result = []
    if string == '':
      print ('!')
      return
    if not full:
      for i in self.ll:
        if i.lower().find(string.lower()) > -1:
          count += 1
          result.append(i)
    else:
      for i in self.ll:
        if i.find(string) > -1:
          count += 1
          result.append(i)
    return (count, result)

  def question(self, string, ansvers):
    ans = input(string)
    if ans == '':
      return False
    if ans in ansvers:
      return True
    return False

  def find(self, string):
    showLimit = 10
    if string == '':
      print ("!")
      return
    swapString = self.swapKeys(string)
    f1 = self.stupidFind(string)
    if f1[0] > 0:
      print ("Find %d results in \"%s\":" % (f1[0], string))
      for i in range(min(f1[0],showLimit)):
        self.show(f1[1][i])
      if f1[0] > showLimit:
        if self.question("Show all results? ", ('y', 'yes')):
          for i in range(showLimit+1, f1[0]):
            self.show(f1[1][i])
    f2 = self.stupidFind(swapString)
    if f2[0] > 0:
      if f1[0] > 0:
        print ("Find also %d results in \"%s\":" % (f2[0], swapString))
      else:
        print ("Maybe you mean \"%s\" (%d results):" % (swapString, f2[0]))
      for i in range(min(f2[0], showLimit)):
        if f2[0] == 1:
          self.printBB(f2[1][i])
        else:
          self.show(f2[1][i])
      if f2[0] > showLimit:
        if self.question("Show all results? ", ('y', 'yes')):
          for i in range(showLimit+1, f2[0]):
            self.show(f2[1][i])

  def showFilesInDir(self, path='.'):
    ld = os.listdir(path)
    for i in ld:
      if os.path.isfile(i):
        print (i)

  def load(self, path=''):
    if path == '':
      self.showFilesInDir()
      path = input('File: ')
    f = open(path)
    return f

  def check(self, string):
    t = string.split('\t')
    for i in t:
      if len(i) == 0:
        return False
    return True

  def parse(self, f):
    l = f.readlines()
    if not f.closed:
      f.close()
    ll = []
    for i in l:
      if self.check(i):
        ll.append(i)
    return ll

  def show(self, string, coding=''):
    if coding =='':
      print (string.encode(self.coding).decode())
    else:
      print (string.encode(coding).decode())

  def showAll(self, l):
    for i in l:
      self.show(i)
      time.sleep(1)

  def console(self):
    command = ''
    while True:
      command = input('> ')
      cmds = command.split(' ')
      cmd = cmds[0]
      par = ''
      tmp = []
      for i in cmds[1:]:
        tmp.append(i)
        tmp.append(' ')
      par = par.join(tmp).strip()
      if cmds[0] in ('exit', 'quit', 'q'):
        return
      if cmds[0] == 'find':
        self.find(par)
      else:
        print ('?')

  def printBB(self, string, sleep = 0.001):
    for i in string:
      sleep=(random.random() * 0.09 + 0.001)
      print('%s' % (i)),
      time.sleep(sleep)
      
if __name__ == '__main__':
  db = DB()
  db.console()

