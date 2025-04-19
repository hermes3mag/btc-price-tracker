from flask import Flask, render_template
from db_utils import get_db_connection, close_db_connection
import psycopg2

# Create the Flask application
app = Flask(__name__)

@app.route('/routes')
def list_routes():
    return {rule.rule: rule.endpoint for rule in app.url_map.iter_rules()}
    
@app.route('/test_db')
def test_db():
    try:
        conn = get_db_connection()
        if conn:
            return {"status": "Database connection successful"}
        else:
            return {"error": "Database connection failed"}
    except Exception as e:
        return {"error": str(e)}

def insert_price_to_db(price_usd):
    print(f"Attempting to insert price: {price_usd}")  # Debugging
    conn = get_db_connection()
    if not conn:
        return {"error": "Database connection failed"}, 500
    try:
        cur = conn.cursor()
        insert_query = """
        INSERT INTO btc_prices (timestamp, price_usd)
        VALUES (CURRENT_TIMESTAMP, %s);
        """
        print(f"Executing query: {insert_query} with price: {price_usd}")
        cur.execute(insert_query, (price_usd,))
        conn.commit()
        return {"status": "success"}, 200
    except Exception as e:
        print(f"Error inserting price: {e}")
        return {"error": str(e)}, 500
    finally:
        cur.close()
        close_db_connection(conn)

@app.route('/insert_price/<float:price>')
def insert_price(price_usd):
    return insert_price_to_db(price_usd)

@app.route('/test_insert/<float:price>')
def test_insert(price):
    return insert_price_to_db(price)

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
# Note: Ensure that the database and table exist before running the application.
# You can create the table using the init_db.py script provided earlier.
# Make sure to set the DATABASE_URL environment variable in your Dockerfile or docker-compose.yml