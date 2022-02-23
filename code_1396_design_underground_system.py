class UndergroundSystem:
    def __init__(self):
        self.trips = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        current_trip = Trip(id, stationName, t)
        if id in self.trips:
            customer_trips = self.trips[id]
            for trip in customer_trips:
                if trip.is_currently_traveling():
                    return
            self.trips[id].append(current_trip)
        else:
            # if we made it here customer has no active trips
            self.trips[id] = [current_trip]
        return None

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        if id in self.trips:
            customer_trips = self.trips[id]
            for trip in customer_trips:
                if trip.is_currently_traveling():
                    trip.end_station_name = stationName
                    trip.end_time = t
                    break # we are going to assume they can only have one active trip
        return None

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        all_filtered_durations = list()
        for customer_id, customer_trips in self.trips.items():
            for trip in customer_trips:
                if trip.start_station_name == startStation and trip.end_station_name == endStation:
                    all_filtered_durations.append(trip.end_time - trip.start_time)
        return sum(all_filtered_durations)/len(all_filtered_durations)


class Trip:
    def __init__(self, customer_id:int, start_station_name:str, start_time:int, end_station_name:str=None, end_time:int=None):
        self.customer_id = customer_id
        self.start_station_name = start_station_name
        self.start_time = start_time
        self.end_station_name = end_station_name
        self.end_time = end_time
    
    def get_trip_duration(self):
        if not self.end_time or not self.end_station_name:
            return None
        return self.end_time - self.start_time

    def is_currently_traveling(self):
        return self.start_station_name and self.start_time and not self.end_time
