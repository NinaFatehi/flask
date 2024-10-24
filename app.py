from flask import Flask
from flask import render_template
from random import choices

app = Flask(__name__)


def random_fruit():
    """Returns random fruit"""

    fruits = ["apple", "cherry", "orange", "banana"]
    return choices(fruits)


## A homepage of a web application and returns back the random fruit from the radom_fruit() function!
@app.route("/")
def fruit():
    """Return random fruit"""

    my_fruit = random_fruit()
    return render_template(
        "index.html", title="Random Fruit", fruit=my_fruit
    )  ## a template to do a little bit of html


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
