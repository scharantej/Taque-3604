
# Import the necessary modules.
from flask import Flask, render_template

# Create a Flask app.
app = Flask(__name__)

# Define the route for the landing page.
@app.route('/')
def index():
  # Render the landing page.
  return render_template('index.html')

# Run the app.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)
