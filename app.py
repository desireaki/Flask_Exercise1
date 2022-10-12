from datetime import date, datetime
from unittest import result
from urllib import request
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)
global studentOrganisationDetails
# Assign default 5 values to studentOrganisationDetails for Application  3.
studentOrganisationDetails = [  {"name" : "Chris", "organisation" : "Sick Speed"},
                                {"name" : "Eric", "organisation" : "CS Power"},
                                {"name" : "John", "organisation" : "FitBit"}] 
    

@app.get('/')
def index():
    # Complete this function to get current date and time assign this value to currentDate, display this data on index.html
    currentDate = datetime.now()
    # dd-mm-YY H-M
    currentDate = currentDate.strftime("%d-%m-%Y  %H:%M")
    return render_template('index.html', currentDate=currentDate)

@app.get('/calculate')
def displayNumberPage():
    # Complete this function to display form.html page
    return render_template('form.html')

@app.route('/calculate', methods=['POST'])
def checkNumber():
    # Get Number from form and display message according to number
    # Display "Number {Number} is even" if given number is even on result.html page
    # Display "Number {Number} is odd" if given number is odd on result.html page
    # Display "No number provided" if value is null or blank on result.html page
    # Display "Provided input is not an integer!" if value is not a number on result.html page
    global number
    number = request.form['number']
    # Write your to code here to check whether number is even or odd and render result.html page
    message_list=["No number provided", "Provided input is not an integer!", "even", "odd"]
    if(number == ""):
        return render_template('form.html', number = number, message = message_list[0])
    elif(type(number) != str):
        return render_template('form.html', number = number, message = message_list[1])
    elif(int(number) % 2 == 0):
        return render_template('form.html', number = number, message = message_list[2])
    else:
        return render_template('form.html', number = number, message = message_list[3])  

@app.get('/addStudentOrganisation')
def displayStudentForm():
    # Complete this function to display studentFrom.html page
    return render_template("studentForm.html")


@app.route('/addStudentOrganisation', methods=['POST'])
def displayRegistrationPage():
    # Get student name and organisation from form.
    studentName = request.form['name']
    organisation = request.form['organisation']
    # Append this value to studentOrganisationDetails
    studentOrganisationDetails.append({"name": studentName, "organisation": organisation})
    # Display studentDetails.html with all students and organisations
    return render_template("studentDetails.html")