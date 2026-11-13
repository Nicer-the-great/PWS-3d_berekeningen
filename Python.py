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
    afstand = math.sqrt(((a[0])**2) + ((a[1])**2) + ((a[2])**2))

    ## wortels berekenen
    sqrt_zy = math.sqrt(((a[1])**2) + ((a[2])**2))
    sqrt_xy = math.sqrt(((a[0])**2) + ((a[1])**2))
    sqrt_xz = math.sqrt(((a[0])**2) + ((a[2])**2))

    sqrt_vec_xy = math.sqrt(((vector[0])**2) + ((vector[1])**2))
    sqrt_vec_zy = math.sqrt(((vector[1])**2) + ((vector[2])**2))
    sqrt_vec_zx = math.sqrt(((vector[0])**2) + ((vector[2])**2))
    
        
    ## cosinus
    x_cos = math.cos(math.atan2(sqrt_zy, a[0]) + Theta)
    y_cos = math.cos(math.atan2(sqrt_xz, a[1]) + Theta)
    z_cos = math.cos(math.atan2(sqrt_xy, a[2]) + Theta)
    
    ## sinussen
    x_sin = math.sin(math.atan2(vector[0], sqrt_vec_zy))
    y_sin = math.sin(math.atan2(vector[1], sqrt_vec_zx))
    z_sin = math.sin(math.atan2(vector[2], sqrt_vec_xy))

    ## alles keer elkaar:
    Xnieuw = afstand * x_cos * x_sin
    Ynieuw = afstand * y_cos * y_sin
    Znieuw = afstand * z_cos * z_sin

    ## teruggeven juiste waarde
    return [Xnieuw + b[0] , Ynieuw + b[1] , Znieuw + b[2]]

class bolcoördinaten:

  @staticmethod 
  def projectie(a, b, ThetaX, ThetaY) :
    ## b is het nulpunt en notatie binnen deze fucntie is [r, ThetaX, ThetaY]
    
    ## berekenen van deltaX en deltaY
    rxa = math.cos(a[2]) * a[0] 
    rya = math.sin(a[2]) * a[0]

    rxb =  math.cos(b[2]) * b[0]
    ryb =  math.sin(b[2]) * b[0]

    ## we nemen de verschillen tussen de hoeken
    dThetaX = a[1] - b[1]
    dThetaY = a[2] - b[2]

    ## we rekenen hier nu de cosinusregels uit voor de afstandstandverschil in een X en Y

   dX = math.sqrt( ((rxa)**2) + ((rxb)**2) - (2* rxa * rxb * math.cos(dThetaX))  )
   dY = math.sqrt( ((rya)**2) + ((ryb)**2) - (2* rya * ryb * math.cos(dThetaY))  )

   ## nu rekenen we het afstandsverschil tussen de twee punten uit met de stelling van pytagoras:

   R = math.sqrt()