from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def main():
    # number1 = ""
    number1 = request.args.get("number1", "")
    number2 = request.args.get("number2", "")
    if number1:
        result = sum1(number1, number2)
    else:
        result = ""
    return (
            """<form action="" method="get">
            <center>
                    <b><h2> Welcome to my summation Application </b></h2>
                    <b><h4>Insert a number: </b><input type="text" name="number1" value=""" + number1 + """></h4>
                    <b><h4>Insert a number: </b><input type="text" name="number2" value=""" + number2 + """></h4>
                <input type="submit" value="Check">
            </center>
            </form>"""
            + result
    )


def sum1(number1, number2):
    hots = int(number1) + int(number2)
    return '''<center>
    <b> The sum of these two numbers is: {} </b> 
    '''.format(hots)
