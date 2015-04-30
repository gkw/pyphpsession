import memcache
from phpserialize import loads, serialize

class phpsession:
  __server = ""
  def __init__(self, server):
    self.__server = server

  def __getSessionFromMemcache(self, key):
    mc = memcache.Client( [self.__server if self.__server != "" else "127.0.0.1:11211"])
    return mc.get(str(key))

  def getSession(self, key):

    try:  
      __dict = {}
      __ses = self.__getSessionFromMemcache(key)
    except Exception as error01:
       print error01
       pass
       return {}

    if __ses != None: 
 
      for item in loads(serialize(__ses)).split(";"):
        if len(item.split(":")) == 3:
          __dict[item.split(":")[0].replace("|s","")] = str(item.split(":")[2]).replace('"','')

    try:
      del __dict[''] 
    except:
      pass

    return __dict


