from django import forms
import os






class bearingcapacity(forms.Form):
    nc = forms.DecimalField(label='Nc', max_digits = 5)
    nq = forms.DecimalField(label='Nq', max_digits = 5)
    nr = forms.DecimalField(label='Nr', max_digits = 5)
    foundation = forms.ChoiceField(label='Foundation Type',choices=(('----', '----'), ('Strip', 'Strip'),('Square', 'Square'), ('Circular', 'Circular')))
    cohesion = forms.DecimalField(label='Soil Cohesion (C)', max_digits = 5)
    r1 = forms.DecimalField(label='Unit Weight (Above)', max_digits = 5)
    r2 = forms.DecimalField(label='Unit Weight (Below)', max_digits = 5)
    b = forms.DecimalField(label='Width Of Pile (b)', max_digits = 5)
    d = forms.DecimalField(label='Depth Of Pilen (d)', max_digits = 5)
    off1 = forms.DecimalField(label='Interval', max_digits = 5)
    off2 = forms.DecimalField(label='Interval', max_digits = 5)



   
    def __init__(self, *args):
        super(bearingcapacity, self).__init__(*args)
        self.fields['nc'].widget.attrs['class'] = 'loginTxtbox'
        self.fields['nq'].widget.attrs['class'] = 'loginTxtbox'





class endbearingcapacity(forms.Form):
    nc = forms.DecimalField(label='Nc', max_digits=15)
    nq = forms.DecimalField(label='Nq', max_digits=15)
    nr = forms.DecimalField(label='Nr', max_digits=15)
    cohesion = forms.DecimalField(label='Soil Cohesion (C)', max_digits=15)
    r1 = forms.DecimalField(label='Unit WeightOf Soil', max_digits=15)
    b = forms.DecimalField(label='Width Of Pile (b)', max_digits=15)
    d = forms.DecimalField(label='Depth Of Pile (d)', max_digits=15)
    off1 = forms.DecimalField(label='Interval', max_digits=15)
    off2 = forms.DecimalField(label='Interval', max_digits=15)



   
    def __init__(self, *args):
        super(endbearingcapacity, self).__init__(*args)
        self.fields['nc'].widget.attrs['class'] = 'loginTxtbox'
        self.fields['nq'].widget.attrs['class'] = 'loginTxtbox'


class skincapacity(forms.Form):
    unit = forms.DecimalField(label='Unit weight, r', max_digits=15)
    friction = forms.DecimalField(label='Friction btw pile and soil', max_digits=15)
    adhession = forms.DecimalField(label='Adhession Factor, Ca')
    frictionangle = forms.DecimalField(label='Friction Angle of Soil', max_digits=15)
    off2 = forms.DecimalField(label='Interval', max_digits=15)
    d = forms.DecimalField(label='Depth ,d', max_digits=15)
   
    def __init__(self, *args):
        super(skincapacity, self).__init__(*args)
        self.fields['unit'].widget.attrs['class'] = 'loginTxtbox'
        self.fields['friction'].widget.attrs['class'] = 'loginTxtbox'


class settlement(forms.Form):
    compression = forms.DecimalField(label='Compression Index', max_digits=15)
    void = forms.DecimalField(label='Initial Void Ratio', max_digits=15)
    unit = forms.DecimalField(label='Unit weight Of Soil')
    thick= forms.DecimalField(label='Clay thickness', max_digits=15)
    off2 = forms.DecimalField(label='Interval', max_digits=15)
    off1 = forms.DecimalField(label='Interval', max_digits=15)
    d = forms.DecimalField(label='Soil Depth ,d', max_digits=15)
    pressure = forms.DecimalField(label='Change in Pressure', max_digits=15)
   
    def __init__(self, *args):
        super(settlement, self).__init__(*args)
        self.fields['unit'].widget.attrs['class'] = 'loginTxtbox'
        self.fields['off1'].widget.attrs['class'] = 'loginTxtbox'