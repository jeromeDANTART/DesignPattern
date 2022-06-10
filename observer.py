class Publisher():
  def _initSubcribers(self):
    self._subcribers = []
    
  def _notifySubcribers(self):
    for s in self._subcribers:
      s._update(self)
      
  def addSubcriber(self,subcriber):
    self._subcribers.append(subcriber)
    subcriber._addPublisher(self)
    
  def removeSubcriber(self,subcriber):
    try:
      self._subcribers.remove(subcriber)
      subcriber._removePublisher(self)
    except:
      pass

  def nbOfSubcribers(self):
    return len(self._subcribers)

class Observable(Publisher):
  def __init__(self):
    self._initSubcribers()
    self.setValue(False)

  def setValue(self,value):
    if isinstance(value,bool):
      self._valeurSurveille=value
      self._notifySubcribers()

  def getValue(self):
    return self._valeurSurveille
       
class Subcribers():
  def _initPublisher(self):
    self._publishers=[]
    self._values=[]

  def _update(self,publisher):
    try:
      i=self._publishers.index(publisher)
      self._values[i] = publisher.getValue()
    except:
      pass

  def _addPublisher(self,publisher):
    self._publishers.append(publisher)
    self._values.append(None)
    self._update(publisher)

  def _removePublisher(self,publisher):
    try:
      i=self._publishers.index(publisher)
      self._publishers.remove(publisher)
      self._values.pop(i)
    except:
      pass

  def nbOfPublisher(self):
    return len(self._publishers)

  def subcripbeTo(self,publisher):
    publisher.addSubcriber(self)

  def unsubcripbeTo(self,publisher):
    publisher.removeSubcriber(self)


class Observer(Subcribers):
  def __init__(self):
    self._initPublisher()
    
  def getValueOf(self,publisher):
    try:
      i=self._publishers.index(publisher)
      return self._values[i]
    except:
      return "aucun abonnement"

  def getValue(self):
    return self._values
