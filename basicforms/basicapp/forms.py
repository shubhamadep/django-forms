from django import forms
from django.core import validators

#value parameter is mandatory
def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Name needs to start with a z.")

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    #catch bots on the form_page
    botcatcher = forms.CharField(required=False,
                                widget=forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        v_email = all_clean_data['verify_email']
        if email != v_email:
            raise forms.ValidationError("Make sure emails match!")

    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("Bot spotted!")
    #     return botcatcher
