from flask import Flask, render_template, request

app = Flask(__name__)

def find_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2*a)
        return root, None
    else:
        return None, None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        coefficient_a = float(request.form['coefficient_a'])
        coefficient_b = float(request.form['coefficient_b'])
        coefficient_c = float(request.form['coefficient_c'])
        root1, root2 = find_roots(coefficient_a, coefficient_b, coefficient_c)
        return render_template('result.html', root1=root1, root2=root2)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
