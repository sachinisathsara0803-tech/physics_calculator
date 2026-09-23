from flask import Flask, render_template, request
import math

app = Flask(__name__)
G = 6.674e-11

# 1. Home Page
@app.route('/')
def home():
    return render_template('home.html')

# Newton's Gravity Calculation Logic
def calculate_gravity(m1, m2, r):
    force = (G * m1 * m2) / (r ** 2)
    return force

#redius according to gravity function
def calculate_radius(m1,m2,f):
    radius=math.sqrt((G * m1 * m2) / f)
    return radius

#Orbital Velocity calculation logic
def calculate_orbit(r):
    G=6.674e-11
    M=6e24
    Velocity=math.sqrt(G*M/r)
    return Velocity

# 2.radius/Gravity Calculator Page(according to gravity)
@app.route('/gravity', methods=['GET', 'POST'])
def gravity():
    result_force = None
    result_radius=None
    if request.method == 'POST':
        if 'mass1' in request.form and 'distance' in request.form:
            try:
                m1 = float(request.form['mass1'])
                m2 = float(request.form['mass2'])
                r = float(request.form['distance'])
                result_force = calculate_gravity(m1, m2, r)

            except:
                pass

        if 'gravity' in request.form:
            try:
                m1 = float(request.form['mass1'])
                m2 = float(request.form['mass2'])
                f = float(request.form['gravity'])
                result_radius = calculate_radius(m1, m2, f)
            except:
                pass

    return render_template('gravity.html', result_force=result_force, result_radius=result_radius)

#Orbit calculation page
@app.route('/orbit', methods=['GET', 'POST'])
def orbit():
    result = None
    if request.method == 'POST':
        r = float(request.form['Radius'])
        
        result = calculate_orbit(r)
        
    return render_template('orbit.html', result=result)

#Escape Velocity calculate logic
def escape_velocity(m,r):
    G=6.674e-11
    velocity=math.sqrt(2*(G*m)/r)
    return velocity

#Escape Velocity Page
@app.route('/escape', methods=['GET','POST'])
def escape():
    result=None
    if request.method=='POST':
        r=float(request.form['Radius'])
        m=float(request.form['Mass'])
        result=escape_velocity(m,r)
    return render_template('escape.html',result=result)

#Centripetal Force calculation logic
def centripetal_force(m,v,r):
    force=(m*math.pow(v,2))/r
    return force

#Centripetal Force page
@app.route('/centripetal', methods=['GET','POST'])
def centripetal():
    result=None
    if request.method=='POST':
        m=float(request.form['Mass'])
        v=float(request.form['Velocity'])
        r=float(request.form['Radius'])
        result=centripetal_force(m,v,r)
    return render_template('centripetal.html', result=result)


#Gravitatin time dilation logic
def g_time(t,m, r):
    speed_of_light=3e8
    G=6.674e-11
    time=t*(math.sqrt(1-(2*G*m/(r*math.pow(speed_of_light,2)))))
    return time

#Gravitatin time dilation page
@app.route('/time', methods=['GET','POST'])
def time():
    result=None
    if request.method== 'POST':
        t=float(request.form['Z_time'])
        m=float(request.form['Mass'])
        r=float(request.form['Rdius'])
        result=g_time(t,m, r)
    return render_template('time.html', result=result)

    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=10000)