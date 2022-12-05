#                         mimi project[  "clock angle"  ]  (24 hours clock)
def clock_angle(h,m):
  #To get 24 hours notation(remander)
  h = h % 12
  #To find the position of the hour's              [formula]
  hours = (h*360)//12 + (m*360)//(12*60)
  #To find the poaition of the minute's            [formula]
  minutes=(m*360)//(60)
  #To find the angle beteweem hours and minutes    [formula]
  angle=abs(hours-minutes)
  if angle > 180:
    angle = 360 - angle
  return angle
h=int(input("Hours: "))
m=int(input("Minutes: "))
print("Angle: ",clock_angle(h,m))

