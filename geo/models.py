from django.db import models


from student.models import Student



class tblgeo(models.Model):
    cohession= models.DecimalField('cohession',decimal_places=2, max_digits = 15)
    nc= models.DecimalField('cohession',decimal_places=2, max_digits = 15)
    d= models.DecimalField('cohession',decimal_places=2, max_digits = 15)
    r1= models.DecimalField('cohession',decimal_places=2, max_digits = 15)
    nq= models.DecimalField('cohession',decimal_places=2, max_digits = 15)
    b= models.DecimalField('cohession',decimal_places=2, max_digits = 15)
    r2= models.DecimalField('cohession',decimal_places=2, max_digits = 15)
    nr= models.DecimalField('cohession',decimal_places=2, max_digits = 15)
    qu= models.DecimalField('cohession',decimal_places=2, max_digits = 15)
    # App= models.CharField('cohession',max_length = 50)


    def __unicode__(self):
        return '%s %s %s'%(self.qu,self.r1,self.nr)




class tblendbearing(models.Model):
    cohession= models.DecimalField('cohession',decimal_places=2, max_digits = 15)
    nc= models.DecimalField('cohession',decimal_places=2, max_digits = 15)
    d= models.DecimalField('cohession',decimal_places=2, max_digits = 15)
    r1= models.DecimalField('cohession',decimal_places=2, max_digits = 15)
    nq= models.DecimalField('cohession',decimal_places=2, max_digits = 15)
    b= models.DecimalField('cohession',decimal_places=2, max_digits = 15)
    nr= models.DecimalField('cohession',decimal_places=2, max_digits = 15)
    qu= models.DecimalField('cohession',decimal_places=2, max_digits = 15)


    def __unicode__(self):
        return '%s %s %s'%(self.qu,self.r1,self.nr)


class tblskincapacity(models.Model):
    frictionangle= models.DecimalField('cohession',decimal_places=2, max_digits = 15)
    unit= models.DecimalField('cohession',decimal_places=2, max_digits = 15)
    friction= models.DecimalField('cohession',decimal_places=2, max_digits = 15)
    adhession= models.DecimalField('cohession',decimal_places=2, max_digits = 15)
    d= models.DecimalField('cohession',decimal_places=2, max_digits = 15)
    # off2= models.DecimalField('cohession',decimal_places=2, max_digits = 15)
    qs= models.DecimalField('cohession',decimal_places=2, max_digits = 15)


    def __unicode__(self):
        return '%s %s %s'%(self.qs,self.friction,self.d)



class tblsettlement(models.Model):
    compression = models.DecimalField('Compression Index', decimal_places = 2, max_digits=15)
    void = models.DecimalField('Void Ratio', decimal_places = 2, max_digits=15)
    unit = models.DecimalField('Unit weight', decimal_places = 2, max_digits=15)
    thick= models.DecimalField('Clay thickness', decimal_places = 2,max_digits=15)
    off2 = models.DecimalField('Interval', decimal_places = 2, max_digits=15)
    off1 = models.DecimalField('Interval', decimal_places = 2, max_digits=15)
    d = models.DecimalField('Soil Depth ,d', decimal_places = 2, max_digits=15)
    pressure = models.DecimalField('Change in Pressure', decimal_places = 2, max_digits=15)
    qs = models.DecimalField('Change in Pressure', decimal_places = 2, max_digits=15)
   
    def __unicode__(self):
       return '%s %s %s'%(self.qs,self.unit,self.d)
