def trap(self, height):
    L = 0
    R = len(height)-1
    print(R)
    Leftmax, Rightmax =0,0
    result =0
    while L< R:
        Leftmax = max(Leftmax, height[L])
        Rightmax = max (Rightmax, height[R])
        if Leftmax<=Rightmax:
            result+= Leftmax - height[L]
            L+=1
        elif Rightmax< Leftmax:
            result+= Rightmax - height[R]
            R-=1
    return result
        
