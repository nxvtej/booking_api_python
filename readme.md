<!-- @format -->

### Booking API

This is a simple FastAPI backend service with 3 endpoint and data.json as in-memory db.

### Start with

```
docker run -it --rm -p 8000:8000 nxvtej/booking-api:latest
```

This will automatically start the API and seed data into json file.

Test the running API
Once running, open your browser or use curl:

```
curl http://localhost:8000/classes
```

You should see a list of available classes.

### Manual installation

```
git clone https://github.com/nxvtej/booking_api_python.git
cd booking_api_python
python -m venv venv
source venv/bin/activate  #Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.server:app --reload

# for classes
curl "http://localhost:8000/classes?timezone=Asia/Kolkata"

# for book
curl -X POST http://localhost:8000/book -H "Content-Type: application/json" -d "{\"id\":1 ,\"class_id\": 1, \"client_name\": \"John Doe\", \"client_email\": \"john@example.com\"}"

# for bookings
curl http://localhost:8000/bookings
```
