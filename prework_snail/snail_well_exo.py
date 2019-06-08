WellHeight = 125
DistancePerDay = 30
LostDistancePerNight = 20
TotalDistanceDone = (DistancePerDay) - (LostDistancePerNight)
NumberDay = 0

print("The snail keep climbing")
NumberDay += TotalDistanceDone

if TotalDistanceDone < WellHeight:
    print("The snail is still in the well")
    while TotalDistanceDone >= WellHeight:
        NumberDay += TotalDistanceDone
print("It's done. The snail is out of the well in", NumberDay, "days!")
