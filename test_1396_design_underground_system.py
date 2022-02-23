from code_1396_design_underground_system import UndergroundSystem

def test_example_1():
    undergroundSystem = UndergroundSystem()
    assert undergroundSystem.checkIn(45, "Leyton", 3) == None
    assert undergroundSystem.checkIn(32, "Paradise", 8) == None
    assert undergroundSystem.checkIn(27, "Leyton", 10) == None
    assert undergroundSystem.checkOut(45, "Waterloo", 15) == None #  // Customer 45 "Leyton" -> "Waterloo" in 15-3 = 12
    assert undergroundSystem.checkOut(27, "Waterloo", 20) == None #  // Customer 27 "Leyton" -> "Waterloo" in 20-10 = 10
    assert undergroundSystem.checkOut(32, "Cambridge", 22) == None # // Customer 32 "Paradise" -> "Cambridge" in 22-8 = 14
    assert undergroundSystem.getAverageTime("Paradise", "Cambridge") == 14.00000 # // return 14.00000. One trip "Paradise" -> "Cambridge", (14) / 1 = 14
    assert undergroundSystem.getAverageTime("Leyton", "Waterloo") == 11.00000 #    // return 11.00000. Two trips "Leyton" -> "Waterloo", (10 + 12) / 2 = 11
    assert undergroundSystem.checkIn(10, "Leyton", 24) == None
    assert undergroundSystem.getAverageTime("Leyton", "Waterloo") == 11.00000 #    // return 11.00000
    assert undergroundSystem.checkOut(10, "Waterloo", 38) == None #  // Customer 10 "Leyton" -> "Waterloo" in 38-24 = 14
    assert undergroundSystem.getAverageTime("Leyton", "Waterloo") == 12.00000 #    // return 12.00000. Three trips "Leyton" -> "Waterloo", (10 + 12 + 14) / 3 = 12


def test_example_2():
    undergroundSystem = UndergroundSystem()
    assert undergroundSystem.checkIn(10, "Leyton", 3) == None #
    assert undergroundSystem.checkOut(10, "Paradise", 8) == None # // Customer 10 "Leyton" -> "Paradise" in 8-3 = 5
    assert undergroundSystem.getAverageTime("Leyton", "Paradise") == 5.00000 # // return 5.00000, (5) / 1 = 5
    assert undergroundSystem.checkIn(5, "Leyton", 10) == None #
    assert undergroundSystem.checkOut(5, "Paradise", 16) == None # // Customer 5 "Leyton" -> "Paradise" in 16-10 = 6
    assert undergroundSystem.getAverageTime("Leyton", "Paradise") == 5.50000 # // return 5.50000, (5 + 6) / 2 = 5.5
    assert undergroundSystem.checkIn(2, "Leyton", 21) == None #
    assert undergroundSystem.checkOut(2, "Paradise", 30) == None # // Customer 2 "Leyton" -> "Paradise" in 30-21 = 9
    assert undergroundSystem.getAverageTime("Leyton", "Paradise") == 20/3 # // return 6.66667, (5 + 6 + 9) / 3 = 6.66667