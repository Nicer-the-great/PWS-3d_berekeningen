## dit moet nu een python bestand zijn.

import math

class cartagisch:
  @staticmethod
  def optel(a, b):
    c = [a[0] + b[0], a[1] + b[1], a[2] + b[2]]
    return c 
  
  @staticmethod
  def aftrek(a, b):
    ## b is het nulpunt
    c = [a[0] - b[0], a[1] - b[1], a[2] - b[2]]
    return c 
  
  @staticmethod
  def projectie(a, b ,ThetaX, ThetaY):
    ## b zijn de coordinaten van de observeerder
    c = cartagisch.aftrek(a, b)
    ThetaXb = math.atan2(c[2],c[0])
    ThetaYb = math.atan2(c[1], math.sqrt( ((c[0])**2) + ((c[2])**2) ))
    ## nu rekenen we de relatieve hoeken uit.
    ThetaXr = ThetaXb - ThetaX
    ThetaYr = ThetaYb - ThetaY
    ## hoeken binnen pi tot -pi zetten:
    ThetaXr = ( (ThetaXr + math.pi) % ( math.tau) ) - math.pi
    ThetaYr = ( (ThetaYr + math.pi) % ( math.tau) ) - math.pi
    ## afstandsverschil uitrekenen.
    afstand = math.sqrt(((c[0])**2)+((c[1])**2)+((c[2])**2))
    ## waarde terugsturen in bolcoordinaten:
    return [ThetaXr, ThetaYr, afstand]
  
  @staticmethod
  def rotatie(a, b, vector, Theta):
    ## b is het punt waar a omheen draait.
    a = cartagisch.aftrek(a, b)
    ## variabelen vooraf uitrekenen zodat de eindberekening niet zo groot wordt:
    afstand = math.sqrt(a[0], a[1], a[2])

    ## wortels berekenen
    sqrt_zy = math.sqrt(((a[1])**2) + ((a[2])**2))
    sqrt_xy = math.sqrt(((a[0])**2) + ((a[1])**2))
    sqrt_xz = math.sqrt(((a[0])**2) + ((a[2])**2))

    ## cosinusen
    
    Xnieuw =  afstand *  * 
  
