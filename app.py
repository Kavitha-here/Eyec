from flask import Flask, render_template, request, jsonify
from geopy.distance import geodesic
import json

app = Flask(__name__)

# Sample eye clinic data (in production, this would be a database)
CLINICS = [
    {
        "id": 1,
        "name": "Vision Care Center",
        "lat": 40.7128,
        "lon": -74.0060,
        "rating": 4.8,
        "address": "123 Main St, New York, NY 10001",
        "phone": "(212) 555-0101",
        "hours": "9:00 AM - 6:00 PM",
        "specialties": ["General Eye Care", "Contact Lenses", "LASIK"]
    },
    {
        "id": 2,
        "name": "Bright Eyes Optometry",
        "lat": 40.7580,
        "lon": -73.9855,
        "rating": 4.6,
        "address": "456 Park Ave, New York, NY 10022",
        "phone": "(212) 555-0202",
        "hours": "10:00 AM - 7:00 PM",
        "specialties": ["Pediatric Eye Care", "Glasses", "Eye Exams"]
    },
    {
        "id": 3,
        "name": "Crystal Vision Clinic",
        "lat": 40.7505,
        "lon": -73.9972,
        "rating": 4.9,
        "address": "789 5th Ave, New York, NY 10003",
        "phone": "(212) 555-0303",
        "hours": "8:00 AM - 8:00 PM",
        "specialties": ["Cataract Surgery", "Cornea Care", "Advanced Treatment"]
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/clinics', methods=['GET'])
def get_all_clinics():
    return jsonify(CLINICS)

@app.route('/api/nearby-clinics', methods=['POST'])
def get_nearby_clinics():
    data = request.get_json()
    user_lat = data.get('lat')
    user_lon = data.get('lon')
    radius_km = data.get('radius', 10)
    
    if not user_lat or not user_lon:
        return jsonify({'error': 'Invalid coordinates'}), 400
    
    user_location = (user_lat, user_lon)
    nearby = []
    
    for clinic in CLINICS:
        clinic_location = (clinic['lat'], clinic['lon'])
        distance = geodesic(user_location, clinic_location).kilometers
        
        if distance <= radius_km:
            clinic_copy = clinic.copy()
            clinic_copy['distance'] = round(distance, 2)
            nearby.append(clinic_copy)
    
    # Sort by distance
    nearby.sort(key=lambda x: x['distance'])
    return jsonify(nearby)

if __name__ == '__main__':
    app.run(debug=True)