from flask import Flask, render_template

# from controllers.fittnes_class_controller import fittnes_classes_blueprint
from controllers.gym_controller import gyms_blueprint
# from controllers.member_controller import members_blueprint

app = Flask(__name__)

# app.register_blueprint(fittnes_classes_blueprint)
app.register_blueprint(gyms_blueprint)
# app.register_blueprint(members_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)