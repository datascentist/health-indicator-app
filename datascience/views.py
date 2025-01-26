from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import RegistrationForm, UserDataForm, DiabeteDataForm, Support
from .models import Registration, UserData, DiabeteDataModel, Messages
from django.contrib import messages
from .utils import heart_health, personnal_recommendations, diabete_health

# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# Create your views here.


def home(request):
    return render(request, "pro.html")


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            if Registration.objects.filter(email=email).exists():
                messages.error(request, "Email Already Exists")
            else:
                if password1 == password2:
                    Registration.objects.create(
                        name=name, email=email, password=password1
                    )
                    messages.success(
                        request, f"You Have Successful Registered As {name}"
                    )
                    return redirect("home")
                else:
                    messages.error(request, "Password Don't Match!")
        else:
            messages.error(request, "Data Entered are Incorrect!")
    else:
        form = RegistrationForm()
    return render(request, "register.html", {"form": form})


def heart(request):
    return render(request, "heart.html")


def predict_user_input(request):
    if request.method == "POST":
        form = UserDataForm(request.POST)
        if form.is_valid():
            # personal info..
            age = form.cleaned_data["age"]
            gender = form.cleaned_data["gender"]
            # vital signs info..
            resting_bp = form.cleaned_data["resting_bp"]
            maximum_htr = form.cleaned_data["maximum_htr"]
            # medical histform.cleaned_data['']ory info..
            chest_pain = form.cleaned_data["chest_pain"]
            fasting_bs = form.cleaned_data["fasting_bs"]
            exersise_ia = form.cleaned_data["exersise_ia"]
            # laboratory results info..
            cholesterol = form.cleaned_data["cholesterol"]
            # diagnostic tests info...
            resting_elr = form.cleaned_data["resting_elr"]
            st_depression = form.cleaned_data["st_depression"]
            slop_peak_exercise = form.cleaned_data["slop_peak_exercise"]

            user_input = [
                age,
                gender,
                chest_pain,
                resting_bp,
                cholesterol,
                fasting_bs,
                resting_elr,
                maximum_htr,
                exersise_ia,
                st_depression,
                slop_peak_exercise,
            ]
            model = heart_health()

            result = model.predict([user_input])

            if result[0] == 0:
                result = "Negative"
            elif result[0] == 1:
                result = "Positive"
            else:
                result = ""

            UserData.objects.create(
                age=age,
                gender=gender,
                resting_bp=resting_bp,
                maximum_htr=maximum_htr,
                chest_pain=chest_pain,
                fasting_bs=fasting_bs,
                exersise_ia=exersise_ia,
                cholesterol=cholesterol,
                resting_elr=resting_elr,
                st_depression=st_depression,
                slop_peak_exercise=slop_peak_exercise,
            )
            disease = "Heart"
            recommendations = personnal_recommendations(user_input, "heart")
            return render(
                request,
                "heart_result.html",
                {
                    "result": result,
                    "recommendations": recommendations,
                    "disease": disease,
                },
            )

        else:
            messages.error(
                request, "Can't Check Heart Health, Check Your Inputs and Try Again!"
            )

    else:
        return render(request, "heart.html")

    return render(request, "heart.html")


def diabete_prediction(request):
    if request.method == "POST":
        form = DiabeteDataForm(request.POST)
        if form.is_valid():
            pregnancies = form.cleaned_data["pregnancies"]
            glucose = form.cleaned_data["glucose"]
            blood_pressure = form.cleaned_data["blood_pressure"]
            skin_thickness = form.cleaned_data["skin_thickness"]
            insulin = form.cleaned_data["insulin"]
            bmi = form.cleaned_data["bmi"]
            diabete_pf = form.cleaned_data["diabete_pf"]
            age = form.cleaned_data["age"]

            model = diabete_health()

            if diabete_pf <= 2.0:
                user_input = [
                    pregnancies,
                    glucose,
                    blood_pressure,
                    skin_thickness,
                    insulin,
                    bmi,
                    diabete_pf,
                    age,
                ]
                DiabeteDataModel.objects.create(
                    pregnancies=pregnancies,
                    glucose=glucose,
                    blood_pressure=blood_pressure,
                    skin_thickness=skin_thickness,
                    insulin=insulin,
                    bmi=bmi,
                    diabete_pf=diabete_pf,
                    age=age,
                )
                prediction = model.predict([user_input])
                if prediction[0] == 0:
                    prediction = "Negative"
                elif prediction[0] == 1:
                    prediction = "Positive"
                else:
                    prediction = ""
                disease = "Diabete"
                recommendations = personnal_recommendations(user_input, "diabete")
                return render(
                    request,
                    "heart_result.html",
                    {
                        "result": prediction,
                        "recommendations": recommendations,
                        "disease": disease,
                    },
                )

            else:
                messages.error(
                    request,
                    "Diabetes Pedigree Function, value must be in range 0 to 2!",
                )
        else:
            messages.error(request, "Invalid Data, Try Again!")
    else:
        return render(request, "diabete.html")
    return render(request, "diabete.html")


def embed_chart(request):
    return render(request, "charts.html")

def contact(request):
    return render(request, "contact.html")

def sendMessage(request):
    if request.method == "POST":
        form = Support(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data['name']
            useremail = form.cleaned_data['email']
            contact = form.cleaned_data['contact']
            subject = form.cleaned_data['subject']
            usermessage = form.cleaned_data['message']
            
            Messages.objects.create(name=name,
                                    email=useremail,
                                    contact=contact,
                                    subject=subject,
                                    message=usermessage)
            messages.success(request, "Message Sent Successful")
            return render(request, "pro.html")
        else:
            messages.error(request, "Invalid Input")
            return render(request, "contact.html")
    return render(request, "contact.html")