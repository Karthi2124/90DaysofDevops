import logging
import os
from flask import Flask, jsonify, request # type: ignore
from dotenv import load_dotenv # type: ignore
from models import db, User
from prometheus_client import make_wsgi_app, Counter, generate_latest
from werkzeug.middleware.dispatcher import DispatcherMiddleware # type: ignore

# Load environment variables from .env file
load_dotenv()

# Create Flask application
app = Flask(__name__)

# Configure application
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'fallback-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Prometheus metrics setup
REQUEST_COUNT = Counter(
    'app_request_count',
    'Application Request Count',
    ['method', 'endpoint', 'http_status']
)

# Replacement for before_first_request
with app.app_context():
    logger.info("Initializing database tables")
    try:
        db.create_all()
        logger.info("Database tables created successfully")
    except Exception as e:
        logger.error(f"Error creating database tables: {str(e)}")
        raise

@app.after_request
def after_request(response):
    """Track request metrics after each request"""
    REQUEST_COUNT.labels(
        request.method,
        request.path,
        response.status_code
    ).inc()
    return response

@app.route('/')
def home():
    """Main endpoint that returns a welcome message"""
    logger.info("Home route accessed")
    return jsonify({
        "message": "Hello, DevOps Engineers! Your Dockerized Flask App is Running!",
        "status": "success",
        "database_configured": bool(app.config['SQLALCHEMY_DATABASE_URI']),
        "metrics_available": "/metrics"
    })

@app.route('/health')
def health_check():
    """Health check endpoint for monitoring"""
    logger.info("Health check route accessed")
    
    health_status = {
        "status": "healthy",
        "environment": os.getenv('FLASK_ENV', 'production'),
        "database_connection": "active" if app.config['SQLALCHEMY_DATABASE_URI'] else "inactive",
        "metrics_endpoint": "/metrics"
    }
    
    return jsonify(health_status), 200

@app.route('/metrics')
def metrics():
    """Prometheus metrics endpoint"""
    return generate_latest()

# Add prometheus wsgi middleware to route /metrics requests
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

if __name__ == '__main__':
    # Get port from environment variable or default to 5000
    port = int(os.getenv("PORT", 5000))
    
    # Run the application
    logger.info(f"Starting application on port {port}")
    app.run(host='0.0.0.0', port=port)