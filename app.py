from flask import Flask, render_template, request
import math

app = Flask(__name__)
G = 6.674e-11
speed_of_light=3e8

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
    error_1=None
    error_2=None
    if request.method == 'POST':
        if 'mass1' in request.form and 'distance' in request.form:
                try:
                    m1 = float(request.form['mass1'])
                    m2 = float(request.form['mass2'])
                    r = float(request.form['distance'])

                    if m1<=0 or m2<=0 or r<=0:
                        error_1="Mass and Distance must be positive numbers!"
                    else:
                        result_force = calculate_gravity(m1, m2, r)

                except ValueError:
                    error_1="Enter a valid number!"

        if 'gravity' in request.form:
            try:
                m1 = float(request.form['mass1'])
                m2 = float(request.form['mass2'])
                f = float(request.form['gravity'])
                if m1<=0 or m2<=0 or f<=0:
                    error_2="Mass and Gravity must be positive numbers!"
                else: 
                    result_radius = calculate_radius(m1, m2, f)
            except:
                error_2="Enter a valid number!"

    return render_template('gravity.html', result_force=result_force, result_radius=result_radius,error_1=error_1, error_2=error_2)

#Orbit calculation page
@app.route('/orbit', methods=['GET', 'POST'])
def orbit():
    result = None
    error_1=None
    if request.method == 'POST':
        r = float(request.form['Radius'])
        if r<=0:
            error_1="Radius must be a positive number!"
        else:
            result = calculate_orbit(r)
        
    return render_template('orbit.html', result=result,error_1=error_1)

#Escape Velocity calculate logic
def escape_velocity(m,r):
    G=6.674e-11
    velocity=math.sqrt(2*(G*m)/r)
    return velocity

#Escape Velocity Page
@app.route('/escape', methods=['GET','POST'])
def escape():
    result=None
    error_1=None
    if request.method=='POST':
        r=float(request.form['Radius'])
        m=float(request.form['Mass'])
        if r<=0 or m<=0:
            error_1="Radius and Mass must be positive numbers!" 
        else:
            result=escape_velocity(m,r)
    return render_template('escape.html',result=result,error_1=error_1)

#Centripetal Force calculation logic
def centripetal_force(m,v,r):
    force=(m*math.pow(v,2))/r
    return force

#Centripetal Force page
@app.route('/centripetal', methods=['GET','POST'])
def centripetal():
    result=None
    error_1=None
    if request.method=='POST':
        m=float(request.form['Mass'])
        v=float(request.form['Velocity'])
        r=float(request.form['Radius'])
        if r<=0 or m<=0 or v<=0:
            error_1="Radius, Mass and Velocity must be positive numbers!" 
        else:
            result=centripetal_force(m,v,r)
    return render_template('centripetal.html', result=result,error_1=error_1)


#Gravitatin time dilation logic
def g_time(t,m, r):
    time=t*(math.sqrt(1-(2*G*m/(r*math.pow(speed_of_light,2)))))
    return time

#Gravitatin time dilation page
@app.route('/time', methods=['GET','POST'])
def time():
    result=None
    error_1=None
    if request.method== 'POST':
        t=float(request.form['Z_time'])
        m=float(request.form['Mass'])
        r=float(request.form['Rdius'])
        if r<=0 or m<=0 or t<=0:
            error_1="Radius, Mass and Time must be positive numbers!" 
        else:
            result=g_time(t,m, r)
    return render_template('time.html', result=result,error_1=error_1)


#Mass-Energy Equivalence logic
def energy_calculate(m):
    energy=m*math.pow(speed_of_light, 2)
    return energy

#Mass-Energy Equivalence page
@app.route('/energy', methods=['GET','POST'])
def energy():
    result_energy=None
    error_1=None
    if request.method=='POST':
        m=float(request.form['Mass'])
        if m<=0:
            error_1="Mass must be a positive number!" 
        else:
            result_energy=energy_calculate(m)
    return render_template('energy_mass.html', result_energy=result_energy,error_1=error_1)

#Velocity time dilation logic
def v_time_calculate(t,v):
    observer_clock=t/(math.sqrt(1-(math.pow(v,2)/math.pow(speed_of_light,2))))
    return observer_clock

#Velocity time dilation page
@app.route('/v_time', methods=['GET','POST'])
def v_time():
    result_time=None
    error_1=None
    if request.method=='POST':
        t=float(request.form['time'])
        v=float(request.form['velocity'])
        if t<=0 or v<=0 :
            error_1="Velocity and Time must be positive numbers!" 
        else:
            result_time=v_time_calculate(t,v)

    return render_template('v_time.html', result_time=result_time,error_1=error_1)

#Gravitational redshift calculate by using physical data of the object that emitted the light
def g_redshift_calculate_phy(m,r):
    redshift=(1/(math.sqrt(1-(2*G*m/(r*math.pow(speed_of_light,2)))))) -1
    return redshift

#Gravitational redshift calculate by using wavelength
def g_redshift_calculate_wav(o_wev,emi_wev):
    redshift=(o_wev-emi_wev)/emi_wev
    return redshift

#Gravitational redshift page
@app.route('/redshift', methods=['GET', 'POST'])
def redshift():
    result_py_redshift = None
    result_wev_redahift=None
    error_1=None
    error_2=None
    if request.method == 'POST':
        if 'Mass' in request.form and 'Radius' in request.form:
            try:
                m = float(request.form['Mass'])
                r = float(request.form['Radius'])
                if m<=0 or r<=0 :
                    error_1="Mass and Radius must be positive numbers!" 
                else:
                    result_py_redshift = g_redshift_calculate_phy(m,r)
            except ValueError:
                error_1="Enter a valid number!"

        if 'Observed_w' in request.form and 'Emitted_w' in request.form:
            try:
                o_wev = float(request.form['Observed_w'])
                emi_wev = float(request.form['Emitted_w'])
                if  o_wev <=0 or emi_wev<=0 :
                    error_2="Observed Wavelength and Emitted Wavelength must be positive numbers!"
                else:

                    result_wev_redahift = g_redshift_calculate_wav(o_wev,emi_wev)
            except ValueError:
                error_2="Enter a valid number!"

    return render_template('redshift.html', result_py_redshift=result_py_redshift, result_wev_redahift=result_wev_redahift,error_1=error_1, error_2=error_2)

    
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=10000)