from django import forms


class get_single_coin_form(forms.Form):
    symbol_or_name = forms.CharField(widget=forms.TextInput(attrs={'id':'input-id','class':'input-class'}))
    def __init__(self, *args, **kwargs):
        super(get_single_coin_form, self).__init__(*args, **kwargs)
        self.fields['symbol_or_name'].label = ""
        # for visible in self.visible_fields():
        #     visible.field.widget.attrs['class'] = 'input-class'