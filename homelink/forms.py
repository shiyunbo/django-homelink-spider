from django import forms


DISTRICT_CHOICES = (('pudong', '浦东'), ('minhang', '闵行'), ('xuhui', '徐汇'))
PRICE_CHOICES = (('p3', '300-400万'), ('p4', '400-500万'), ('p5', '500-800万'))
BEDROOM_CHOICES = (('l2', '二室'), ('l3', '三室'))


class HouseChoiceForm(forms.Form):
    district = forms.CharField(label="区域", widget=forms.RadioSelect(choices=DISTRICT_CHOICES))
    price = forms.CharField(label="价格", widget=forms.RadioSelect(choices=PRICE_CHOICES))
    bedroom = forms.CharField(label="庭室", widget=forms.RadioSelect(choices=BEDROOM_CHOICES))

