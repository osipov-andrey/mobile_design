from django import forms

from .models import SubElement, SuperElement, SubPattern, SuperPattern


class SubElementForm(forms.ModelForm):
    super_element = forms.ModelChoiceField(queryset=SuperElement.objects.all(), empty_label=None,
                                           label='Группа элементов', required=True)

    class Meta:
        model = SubElement
        fields = '__all__'


class SubPatternForm(forms.ModelForm):
    super_pattern = forms.ModelChoiceField(queryset=SuperPattern.objects.all(), empty_label=None,
                                           label='Группа паттернов', required=True)

    class Meta:
        model = SubPattern
        fields = '__all__'
