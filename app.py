from flask import Flask, render_template
import psycopg2

# Create the Flask application
app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = psycopg2.connect(
        host="db",
        database="bitcoin_db",
        user="bitcoin_user",
        password="bitcoin_password"
    )
    return conn

# Define the home route
@app.route('/')
def home():
    conn = get_db_connection()
    # Example query (ensure the table exists in your database)
    cur = conn.cursor()
    cur.execute('SELECT version();')
    db_version = cur.fetchone()
    cur.close()
    conn.close()
    return render_template('index.html', db_version=db_version)
# Define the about route
@app.route('/about')
def about():
    return render_template('about.html')
# Define the contact route
@app.route('/contact')
def contact():
    return render_template('contact.html')
# Define the portfolio route
@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')
# Define the news route
@app.route('/news')
def news():
    return render_template('news.html')
# Define the chart route
@app.route('/chart')
def chart():
    return render_template('chart.html')
# Define the login route
@app.route('/login')
def login():
    return render_template('login.html')
# Define the register route
@app.route('/register')
def register():
    return render_template('register.html')
# Define the dashboard route
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
# Define the settings route
@app.route('/settings')
def settings():
    return render_template('settings.html')
# Define the logout route
@app.route('/logout')
def logout():
    return render_template('logout.html')
# Define the error route
@app.route('/error')
def error():
    return render_template('error.html')
# Define the 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
# Define the 500 error handler
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
# Define the maintenance route
@app.route('/maintenance')
def maintenance():
    return render_template('maintenance.html')
# Define the terms and conditions route
@app.route('/terms')
def terms():
    return render_template('terms.html')
# Define the privacy policy route
@app.route('/privacy')
def privacy():
    return render_template('privacy.html')
# Define the FAQ route
@app.route('/faq')
def faq():
    return render_template('faq.html')
# Define the contact us route
@app.route('/contact-us')
def contact_us():
    return render_template('contact-us.html')
# Define the feedback route
@app.route('/feedback')
def feedback():
    return render_template('feedback.html')
# Define the support route
@app.route('/support')
def support():
    return render_template('support.html')
# Define the API route
# Run the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)