from django import forms


from drivers.models import Driver



class DriverForm(forms.ModelForm):


    class Meta:

        model = Driver

        fields = "__all__"

        widgets = {

            "birthday": forms.DateInput(format="%Y-%m-%d",

                                        attrs={"type": "date"}),

        }