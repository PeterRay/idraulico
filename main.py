import hydraulics
#------------------------------------------------------------------------
# impianto idraulico

#roomType=0 #cucina base
#roomType=1 #cucina lusso
#roomType=2 #bath base
#roomType=3 #bath lusso

roomType=3

squareMeters=10
standardPriceForTenSquareMeters=800
h2oPointsNum=3
sanitaryNum=3

R1 = hydraulics.room(99,"CUCINA")
if(roomType==0 or roomType==1):
    R1.chitchen(roomType)
    R1.report()

if(roomType==2 or roomType==3):
    R1.bath(roomType, squareMeters, standardPriceForTenSquareMeters,h2oPointsNum,sanitaryNum)
    R1.report()

del R1
