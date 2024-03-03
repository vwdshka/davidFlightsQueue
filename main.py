import random
import heapq

takeoffQueue = []

landingQueue = []


class AirportQueue:
    def __init__(self, flight_number, req):
        self.flightNumber = flight_number
        self.req = req


def add_req():
    flight_num = random.randint(100, 999)
    req = random.choice(["landing", "takeoff", "emergency landing"])
    print(F"Flight {flight_num} requests {req}")
    return AirportQueue(flight_num, req)


def add_takeoff():
    if not landingQueue and takeoffQueue:
        flight = takeoffQueue.pop(0)
        print(f"CONTROL: {flight.flightNumber} takeoff")


def add_landing():
    if landingQueue:
        flight = heapq.heappop(landingQueue)
        print(f"CONTROL: {flight.flightNumber} landing")


def add_emergency_landing():
    if landingQueue:
        flight = heapq.heappop(landingQueue)
        print(f"CONTROL: {flight.flightNumber} emergency landing")


def airport_system(request_count):
    for i in range(request_count):
        req = add_req()

        if req.req == "takeoff":
            takeoffQueue.append(req)
            add_takeoff()
        elif req.req == "landing":
            if req.req == "emergency landing":
                heapq.heappush(landingQueue, req)
                add_emergency_landing()
            else:
                heapq.heappush(landingQueue, req)
                add_landing()


answer = int(input("Welcome to the implementation of the application.\n"
                   "Please enter how many flights you want to commit to the system: "))

airport_system(answer)