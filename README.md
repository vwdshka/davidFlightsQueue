<h2>Air Traffic Management System</h2>

This project aims to simulate an air traffic management system for a small airport using Python. The system efficiently manages landing and takeoff requests while prioritizing emergency situations.

- `AirportQueue` class: Represents a flight queue object with attributes for flight number and request type.
- `add_req()` function: Generates random flight requests (landing, takeoff, or emergency landing) with random flight numbers.
- `add_takeoff()` function: Handles takeoff requests by allowing planes to take off if no planes are landing.
- `add_landing()` function: Manages landing requests by prioritizing planes in the landing queue.
- `add_emergency_landing()` function: Handles emergency landing requests by prioritizing them over regular landing requests.
- `airport_system()` function: Simulates the airport system by generating a specified number of flight requests and processing them accordingly.

To use the air traffic management system, simply run the Python script and enter the desired number of flights when prompted. The system will simulate the airport operations and display the actions taken for each flight request.
