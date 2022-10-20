from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

    city = forms.TypedChoiceField(label='State',
                                  choices=[('is_CA', 'California'), ('is_NY', 'New York'), ('is_MA', 'Massachusetts'),
                                           ('is_TX', 'Texas'),
                                           ('is_otherstate', 'Other state')], required=False,
                                  widget=forms.Select(attrs={'class': 'input select'}))

    category = forms.TypedChoiceField(label='Category',
                                      choices=[('is_software', 'Software'), ('is_web', 'Web-development'),
                                               ('is_mobile', 'Mobile development'), ('is_enterprise', 'Enterprise'),
                                               ('is_advertising', 'Advertising'), ('is_gamesvideo', 'Video games'),
                                               ('is_ecommerce', 'Ecommerce'),
                                               ('is_biotech', 'Biotech'), ('is_consulting', 'Consulting'),
                                               ('is_othercategory', 'Other category')],
                                      required=False, widget=forms.Select(attrs={'class': 'input select'}))

    avg_members = forms.IntegerField(label='Number of participants', widget=forms.NumberInput(attrs={'class': 'input'}))
    relationships = forms.IntegerField(label='Relationship quality', widget=forms.NumberInput(attrs={'class': 'input'}))

    milestones = forms.IntegerField(label='Startup milestones', widget=forms.NumberInput(attrs={'class': 'input'}))

    funding_rounds = forms.IntegerField(label='Number of funding rounds', widget=forms.NumberInput(attrs={'class': 'input'}))

    round_a = forms.BooleanField(label='Round A funding', required=False,
                                 widget=forms.CheckboxInput(attrs={'class': 'checkbox new_checkbox'}))
    round_b = forms.BooleanField(label='Round B funding', required=False,
                                 widget=forms.CheckboxInput(attrs={'class': 'checkbox new_checkbox'}))
