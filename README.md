# 👁️ Eye Clinic Finder App

A web application to help users find nearby eye clinics based on their location and search radius.

## Features

✨ **Easy to Use**
- Auto-detect your current location
- Manually enter coordinates
- Adjustable search radius (1-50 km)

📍 **Smart Search**
- Find nearby eye clinics
- View distance from your location
- Sort results by proximity

📊 **Clinic Information**
- Clinic name and rating
- Address and phone number
- Operating hours
- Specialties offered

🎨 **Beautiful UI**
- Modern, responsive design
- Smooth animations
- Mobile-friendly layout

## Prerequisites

- Python 3.7+
- pip (Python package manager)

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/Kavitha-here/eyec.git
cd eyec
```

2. **Create a virtual environment:**
```bash
python -m venv venv
```

3. **Activate the virtual environment:**

   **On Windows:**
   ```bash
   venv\Scripts\activate
   ```

   **On macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## Running the App

1. **Start the Flask server:**
```bash
python app.py
```

2. **Open your browser and navigate to:**
```
http://localhost:5000
```

3. **Find clinics:**
   - Click "📍 Auto-Detect" to use your current location (requires browser permission)
   - Or manually enter latitude and longitude
   - Adjust the search radius using the slider
   - Click "🔍 Find Clinics" to search

## Project Structure

```
eyec/
├── app.py              # Flask backend with API routes
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html      # Frontend UI
└── README.md           # This file
```

## API Endpoints

### Get All Clinics
```
GET /api/clinics
```
Returns a list of all eye clinics in the database.

### Find Nearby Clinics
```
POST /api/nearby-clinics
Content-Type: application/json

{
    "lat": 40.7128,
    "lon": -74.0060,
    "radius": 10
}
```
Returns clinics within the specified radius from the given coordinates, sorted by distance.

## Sample Data

The app includes 3 sample eye clinics:

1. **Vision Care Center** - 123 Main St, New York, NY (Rating: 4.8/5)
2. **Bright Eyes Optometry** - 456 Park Ave, New York, NY (Rating: 4.6/5)
3. **Crystal Vision Clinic** - 789 5th Ave, New York, NY (Rating: 4.9/5)

## Future Enhancements

- 🗄️ Integration with a real database
- 🔐 User authentication and accounts
- ❤️ Save favorite clinics
- 💬 User reviews and ratings
- 📅 Appointment booking system
- 🗺️ Interactive map view
- 📞 Direct calling functionality
- 🌙 Dark mode theme

## Technologies Used

- **Backend:** Flask (Python web framework)
- **Frontend:** HTML5, CSS3, JavaScript
- **Geolocation:** Geopy library for distance calculations
- **API:** RESTful API with JSON

## License

This project is open source and available under the MIT License.

## Author

Created by [Kavitha-here](https://github.com/Kavitha-here)

---

**Ready to find your nearest eye clinic? Start the app and begin searching!** 👁️✨