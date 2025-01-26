from django import forms


class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=100, label="Name")
    email = forms.EmailField(label="Email")
    password1 = forms.CharField()
    password2 = forms.CharField()


class UserDataForm(forms.Form):
    CHEST_PAIN_CHOICES = [
        ("3", "Typical Angina"),
        ("1", "Atypical Angina"),
        ("2", "Non-Anginal Pain"),
        ("0", "Asymptomatic"),
    ]
    FASTING_BS_CHOICES = [
        (0, "No"),
        (1, "Yes"),
    ]
    RESTING_ECG_CHOICES = [
        ("1", "Normal"),
        ("2", "Having ST-T wave abnormality"),
        ("0", "Showing probable or definite left ventricular hypertrophy"),
    ]
    EXERCISE_ANGINA_CHOICES = [
        ("0", "No"),
        ("1", "Yes"),
    ]
    ST_SLOPE_CHOICES = [("2", "Upsloping"), ("1", "Flat"), ("0", "Downsloping")]

    age = forms.IntegerField()
    gender = forms.CharField(max_length=20)
    resting_bp = forms.IntegerField()
    maximum_htr = forms.IntegerField()
    chest_pain = forms.ChoiceField(choices=CHEST_PAIN_CHOICES)
    fasting_bs = forms.ChoiceField(choices=FASTING_BS_CHOICES)
    exersise_ia = forms.ChoiceField(choices=EXERCISE_ANGINA_CHOICES)
    # laboratory results info..
    cholesterol = forms.IntegerField()
    # diagnostic tests info...
    resting_elr = forms.ChoiceField(choices=RESTING_ECG_CHOICES)
    st_depression = forms.FloatField()
    slop_peak_exercise = forms.ChoiceField(choices=ST_SLOPE_CHOICES)


class DiabeteDataForm(forms.Form):
    pregnancies = forms.IntegerField()
    glucose = forms.IntegerField()
    blood_pressure = forms.IntegerField()
    skin_thickness = forms.IntegerField()
    insulin = forms.IntegerField()
    bmi = forms.FloatField()
    diabete_pf = forms.FloatField()
    age = forms.IntegerField()

class Support(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.EmailField()
    contact = forms.IntegerField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField()