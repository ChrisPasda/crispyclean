from flask import Flask, render_template, request
import webbrowser
from send_email import send_email
import attach



app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/error", methods=['POST'])
def error():
    return render_template("error.html")

@app.route("/success", methods=['POST'])
def success():
#if available = success
#else: error

    if request.method == 'POST':
        bam = request.form["bam_name"]
        numbers = request.form["anzahl_name"]
        company = request.form["company_name"]
        #print(bam,numbers,company)
        #sendShit(bam,numbers)
    if (sendShit(bam,numbers)) == True:
       return render_template("success.html")
    else:
       return render_template("error.html")

def sendShit(bam, number):
    import frontend
    hardware_list = []
    numbers = int(number)
    mylist = frontend.check_status()

    for item in mylist:
        if len(mylist) < numbers:
            return False
        if numbers > 0:
           frontend.book_server(item[0], bam)
           hardware_list.append(item[0])
           numbers = numbers -1
           print(numbers)
        else:
           break
    #write Word by numbers input
    frontend.hardware_list_from_booking(hardware_list, bam)
    attach.sendMail(bam, number)
    print("Mail sent")
    return True


if __name__ == '__main__':
    webbrowser.open('http://localhost:5000/')
    app.debug = True
    app.run()
