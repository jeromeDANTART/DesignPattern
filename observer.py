class Publisher():
  def initSubcribers(self):
    self._subcribers = []
      
  def addSubcribers(self,Subcribers):
    self._subcribers.append(Subcribers)
    Subcribers.update(self) 
    
  def removeSubcribers(self,Subcribers):
    try:
      self._subcribers.remove(Subcribers)
      Subcribers.update(None) 
    except:
      pass
      
  def notifySubcribers(self):
    for i in self._subcribers:
      i.update(self)

class Observable(Publisher):
  def __init__(self):
    self.initSubcribers()
    self.setVS(5)

  def setVS(self,value):
    self._valeurSurveille=value
    self.notifySubcribers()

  def getVS(self):
    return self._valeurSurveille
       
class Subcribers():
  def update(self,publisher):
    if publisher==None:
      del self._valeurSurveille
    else:
      self._valeurSurveille = publisher.getVS()

class Observer(Subcribers):
  def getVS(self):
    try:
      return self._valeurSurveille
    except:
      return "aucun abonnement"


# init objet 
#
Oable1 = Observable()
Oable2 = Observable()
Oer1 = Observer()
Oer2 = Observer()
Oer3 = Observer()
# il y a une mise a jour de la valeur observée, pour les observeurs, lors de la souscription
Oable1.addSubcribers(Oer1)
Oable2.addSubcribers(Oer2)
Oable1.addSubcribers(Oer3)
Oable2.addSubcribers(Oer3)
print("Observer1 est abonné a Observable1")
print("Observer2 est abonné a Observable2")
print("Observer3 est abonné a Observable1 & Observable2")
print("--------------")
print(" Valeur par defaut = 5")
print("--------------")
print("Observable1 = " , Oable1.getVS())
print("Observer1 = " , Oer1.getVS())
print("Observable2 = " , Oable2.getVS())
print("Observer2 = " ,Oer2.getVS())
print("Observer3 = " ,Oer3.getVS())
print("--------------")
print(" set Observable1 = 2")
print("--------------")
Oable1.setVS(2)
print("Observable1 = " , Oable1.getVS())
print("Observer1 = " , Oer1.getVS())
print("Observable2 = " , Oable2.getVS())
print("Observer2 = " ,Oer2.getVS())
print("Observer3 = " ,Oer3.getVS())
print("--------------")
print(" set Observable2 = 3")
print(" desabonnement de Observer2 ")
print("--------------")
Oable2.setVS(3)
Oable2.removeSubcribers(Oer2)
print("Observable1 = " , Oable1.getVS())
print("Observer1 = " , Oer1.getVS())
print("Observable2 = " , Oable2.getVS())
print("Observer2 = " ,Oer2.getVS())
print("Observer3 = " ,Oer3.getVS())
print("--------------")
print(" Observer3 etant abonné a deux Observables, sa valeur sera la valeur la plus recente des Observables auquels il est abonné")
