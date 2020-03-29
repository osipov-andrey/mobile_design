from django import forms

from .models import SubElement, SuperElement


class SubElementForm(forms.ModelForm):
    super_element = forms.ModelChoiceField(queryset=SuperElement.objects.all(), empty_label=None,
                                           label='Группа элементов', required=True)

    class Meta:
        model = SubElement
        fields = '__all__'
