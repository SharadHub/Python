from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    single_year_result = None
    leap_year_range_result = []
    explanation = ""

    if request.method == "POST":
        # Single  leap year check
        if "single_year" in request.form:  
            year = int(request.form.get("single_year"))
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                single_year_result = f"{year} is a leap year!"
                explanation = f"{year} is divisible by 4 but not by 100, or it is divisible by 400."
            else:
                single_year_result = f"{year} is not a leap year."
                explanation = f"{year} is not divisible by 4 or it is divisible by 100 but not by 400."
        #checking leap years in the given range
        elif "start_year" in request.form and "end_year" in request.form:
            start_year = int(request.form.get("start_year"))
            end_year = int(request.form.get("end_year"))
            leap_year_range_result = [
                year
                for year in range(start_year, end_year + 1)
                if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
            ]
            explanation = "Leap years are divisible by 4 but not by 100, unless also divisible by 400." #explain why it is leap year
    #connecting to the frontend
    return render_template(
        "index.html",
        single_year_result=single_year_result,
        leap_year_range_result=leap_year_range_result,
        explanation=explanation,
    )

if __name__ == "__main__":
    app.run(debug=True)
