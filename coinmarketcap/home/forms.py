from django import forms


class get_single_coin_form(forms.Form):
    symbol_or_name = forms.CharField(max_length=30)
    def __init__(self, *args, **kwargs):
        super(get_single_coin_form, self).__init__(*args, **kwargs)
        self.fields['symbol_or_name'].label = ""