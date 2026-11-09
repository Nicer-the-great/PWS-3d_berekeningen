## dit moet nu een python bestand zijn.

import math

class cartagisch:
  @staticmethod
  def optel(a, b):
    list c = [a[0] + b[0], a[1] + b[1], a[2] + b[2]]
    return c 
  
  def aftrek(a, b):
    ## b is het nulpunt
    list c = [a[0] - b[0], a[1] - b[1], a[2] - b[2]]
    return c 
  
  def projectie(a, b ,ThetaX, ThetaY):
    ## b zijn de coordinaten van de observeerder
    c = cartagisch.aftrek(a, b)
    ThetaXb = math.tan(z,x)
    ThetaYb = math.tan(y, math.sqrt( ((c[0])**2) + ((c[2])**2) ))
    ## nu rekenen we de relatieve hoeken uit.
    ThetaXr = ThetaXb - ThetaX
    ThetaYr = ThetaYb - ThetaY
    ## hoeken binnen pi tot -pi zetten:
    ThetaXr = ( (ThetaXr + math.pi) % ( math.tau) ) + math.pi
    ThetaYr = ( (ThetaYr + math.pi) % ( math.tau) ) + math.pi
    ## afstand tot punt
