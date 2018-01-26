from flask import Flask, render_template
from GPIO.led import LED

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control/<action>')
def led_control(action):
    if action == 'on':
        LED.open()
    elif action == 'off':
        LED.close()

    return 'Success'

if __name__ == '__main__':
    try:
        app.run(debug=True, host='0.0.0.0')
    except KeyboardInterrupt:
        print('Exit')

    finally:
        print('clear')
        LED.clear()