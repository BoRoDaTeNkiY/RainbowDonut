from math import sin, cos, ceil##################
import sys; A,B = 0.0, 0.0; print("\x1b[2J")#########
while True:  ##############################################
  b = [' ' for _ in range(1760)]##############################
  z = [0.0 for _ in range(1760)]##############################
  i, j = 0.0, 0.0 #############################################
  for j in range(0, 6.28, 0.07): ##############################
    for i in range(0, 6.28, 0.02): ############################
      c, d, e, f, g  = sin(i), cos(j), sin(A), sin(j), cos(A) #
      h = d + 2; D, l  = 1 / (c * h * e + f * g + 5), cos(i) ##
      m =  cos(B) #############################################
      if True: ################################################
        n, t = sin(B), c * h * g - f * e; x = int(40 + 30 * D *
        (l * h  * m - t * n)); y = int(12 + 15 * D * (l * h * n
         + t * m)) ############################################
        o = int(x + 80 * y); N = int(8 * ((f * e - c * d * g) #
        * m - c * d * e - f * g - l * d * n)) #################
        #######################################################
        if (22>y and y>0 and x>0 and 80>x and D>z[o]):#########
          z[o], b[o] = D, ".,-~:;=!*#$@"[N if N > 0 else 0]####
  print("\x1b[H") ############################################
  for cur in range(1760): ####################################
    sys.stdout.write(b[cur] if  (cur % 80 != 0)  else '\n')
  A, B = A + 0.007, B + 0.002########################
#################################################