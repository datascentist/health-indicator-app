from django.shortcuts import render
import os
from django.templatetags.static import static
import joblib

# External data file path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
csv_file_pah = os.path.join(BASE_DIR, "datascience", "data", "heart.csv")
model_file_pah = os.path.join(BASE_DIR, "datascience", "data", "diabetes.joblib")
heart_model = os.path.join(BASE_DIR, "datascience", "data", "heart1.joblib")


def heart_health():
    with open(heart_model, "rb") as file:
        loaded_model = joblib.load(file)
    return loaded_model


def personnal_recommendations(user_input, disease):
    recommendations = []
    if disease == "heart":
        if user_input[0] > 50:
            recommendations.append(
                (
                    "Regular check-ups with your healthcare provider are essential.",
                    static("images/docter2.jpeg"),
                )
            )
        if user_input[1]:
            if user_input[1] == "0":
                recommendations.append(
                    (
                        "Ensure adequate intake of calcium and vitamin D to maintain bone health.",
                        static("images/image2.jpg"),
                    )
                )
            else:
                recommendations.append(
                    (
                        """Ensure adequate intake of calcium and vitamin D to maintain bone health,
                "Increase Physical Exercise and eat balanced diet.""",
                        static("images/fe5.jpeg"),
                    )
                )
        if user_input[3] > 120:
            recommendations.append(
                (
                    "Monitor your blood pressure regularly and consider reducing salt intake.",
                    static("images/blood2.jpeg"),
                )
            )
        if user_input[4] > 200:
            recommendations.append(
                (
                    """Consider a low-cholesterol diet with more fruits, vegetables, and whole grains""",
                    static("images/image3.jpg"),
                )
            )
        if user_input[7] < 145:
            recommendations.append(
                (
                    "Increase Physical exercise like walking at least 30 minutes per day.",
                    static("images/exercise2.jpeg"),
                )
            )

    elif disease == "diabete":
        if user_input[5]:
            if user_input[5] < 18.5:
                recommendations.append(
                    (
                        """Increase caloric intake with nutritious, calorie dense foods, like nuts, 
                                       avocados, and whole grains.""",
                        static("images/image3.jpg"),
                    )
                )

                recommendations.append(
                    (
                        "Consider strength training exercises to build muscle mass",
                        static("images/exercise1.jpeg"),
                    )
                )

            elif user_input[5] >= 18.5 and user_input[5] <= 24.9:
                recommendations.append(
                    (
                        """Maintain current lifestyle with a balanced diet and regular exercise. 
                                       Monitor (Body Mass Index) BMI periodically to ensure it remains stable""",
                        static("images/image4.jpg"),
                    )
                )

            elif user_input[5] >= 25.0 and user_input[5] <= 29.9:
                recommendations.append(
                    (
                        """Introduce a balanced diet focusing on reducing calorie intake.
                                       or cycling. """,
                        static("images/image2.jpg"),
                    )
                )
                recommendations.append(
                    (
                        """Encourage regular physical activity, like brisk walking, swimming,
                                       Aim for at least 150 minutes of moderate exercise per week
                                       """,
                        static("images/exercise2.jpeg"),
                    )
                )
            elif user_input[5] > 30.0:
                recommendations.append(
                    (
                        """Consult with a healthcare provider or dietitian for a personalized weight loss plan. 
                                       """,
                        static("images/docter1.jpeg"),
                    )
                )

                recommendations.append(
                    (
                        """Focus on a balanced, low-calorie diet, and include both aerobic and 
                                       resistance exercises in the routine""",
                        static("images/fe5.jpeg"),
                    )
                )
            else:
                return
        if user_input[2]:
            if user_input[2] < 120:
                recommendations.append(
                    (
                        """Your Blood Pressure is Normal, but Maintain a healthy lifestyle with 
                                       regular exercise and a balanced diet low in sodium.""",
                        static("images/fe5.jpeg"),
                    )
                )

            elif user_input[2] >= 120 and user_input[2] <= 129:
                recommendations.append(
                    (
                        """Your Blood Pressure is Elevated, Please Implement lifestyle changes 
                                       such as reducing sodium intake, increasing physical activity, 
                                       and managing stress through techniques like yoga or meditation.""",
                        static("images/fe2.jpeg"),
                    )
                )

            elif user_input[2] >= 130 and user_input[2] <= 139:
                recommendations.append(
                    (
                        """Your Blood Pressure is on Hypertension stage 1, Consider consulting a 
                                       healthcare provider for possible medication and regular monitoring.""",
                        static("images/docter1.jpeg"),
                    )
                )

            elif user_input[2] >= 140 and user_input[2] <= 149:
                recommendations.append(
                    (
                        """Your Blood Pressure is on Hypertension stage 2, Seek medical advice 
                                       for a comprehensive treatment plan, which may include medication 
                                       and lifestyle adjustments.""",
                        static("images/docter3.jpeg"),
                    )
                )

        if user_input[1]:
            if user_input[1] < 100:
                recommendations.append(
                    (
                        """Normal glucose level, Continue with a balanced diet and regular physical activity,
                                        Monitor glucose levels periodically
                                    """,
                        static("images/fe5.jpeg"),
                    )
                )

            elif user_input[1] >= 100 and user_input[1] <= 125:
                recommendations.append(
                    (
                        """Prediabetes glucose level, Implement dietary changes to reduce sugar and refined carbs,
                                        Increase physical activity and aim for weight loss if overweight.
                                       """,
                        static("images/image2.jpg"),
                    )
                )

            elif user_input[1] >= 126:
                recommendations.append(
                    (
                        """Diabetes glucose level, Consult a healthcare provider for a comprehensive diabetes management plan, 
                                       which may include medication, dietary changes, and regular exercise""",
                        static("images/de2.jpeg"),
                    )
                )

        if user_input[7] and user_input[6]:
            if user_input[7] <= 30 and user_input[6] < 1.5:
                recommendations.append(
                    (
                        """Emphasize education on healthy lifestyle choices to prevent future diabetes risk,
                                       Encourage regular exercise and a balanced diet.
                                    """,
                        static("images/fe1.jpeg"),
                    )
                )

            elif user_input[7] <= 30 or (user_input[6] >= 1.5 and user_input[6] <= 2.0):
                recommendations.append(
                    (
                        """
                                       Regular screenings for diabetes and proactive lifestyle changes, 
                                       Include a diet low in refined sugars and fats, and regular physical activity.
                                       """,
                        static("images/sfe1.jpeg"),
                    )
                )
        if user_input[0] > 5:
            recommendations.append(
                (
                    """
                                   Monitor glucose levels more frequently, as there’s a higher risk for gestational diabetes, 
                                   Follow a balanced diet and engage in regular, moderate exercise
                                   """,
                    static("images/image6.jpg"),
                )
            )
    return recommendations


def diabete_health():
    with open(model_file_pah, "rb") as file:
        loaded_model = joblib.load(file)
    return loaded_model
