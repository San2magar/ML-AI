# solid with hemisphere on top of cylinder
""" A solid is made by placing a hemisphere on top of cylinder>
    - the radius is made by placing a hemisphere and th cylinder is 7 cm.
    - the height of the cylindrical part is 20 cm>
"""
import math
def combined_solid_solver(part):
    r=7
    h=20
    pi = math.pi

    match part:
        case 'volume':
            volume = lambda r,h: pi * r**2 *h +(2/3) * pi * r**3
            return round(volume(r,h),2)
        
        case 'surface_area':
            surface_area = lambda r, h: 2 * pi * r *h + pi * r**2
            return round(surface_area(r,h),2)
        
        case _ : return "invalid choice"

print("volume of solid:", combined_solid_solver('volume'),"cm3")        
print("surface area of solid:", combined_solid_solver('surface_area'),"cm2") 

