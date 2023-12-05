class Scene:
    def __init__(self, objects = []):
        self.sceneList = objects

    def push(self, object):
        self.sceneList.append(object)

    def hits(self, ray, t_min, t_max, record):
        hitsomething = False
        tempRecord = record
        closestsofar = t_max

        for object in self.sceneList:
           if object.hit(ray, t_min, closestsofar, tempRecord):
               hitsomething = True
               closestsofar = tempRecord.t

               record.p = tempRecord.p
               record.t = tempRecord.t
               record.normal = tempRecord.normal
               record.frontface = tempRecord.frontface
               record.material = tempRecord.material

        return hitsomething