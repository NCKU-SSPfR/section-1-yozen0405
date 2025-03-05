import random

CIRCLE_RADIUS = 1
TOTAL_RANDOM_POINTS = 1_000_000  
SQUARE_BOUNDARY = CIRCLE_RADIUS  
QUARTER_CIRCLE_AREA_FACTOR = 4   
EXPONENT_SQUARED = 2  

inside_circle_count = 0

for _ in range(TOTAL_RANDOM_POINTS):
    x = random.uniform(-SQUARE_BOUNDARY, SQUARE_BOUNDARY)
    y = random.uniform(-SQUARE_BOUNDARY, SQUARE_BOUNDARY)
    
    if x**EXPONENT_SQUARED + y**EXPONENT_SQUARED <= CIRCLE_RADIUS**EXPONENT_SQUARED:
        inside_circle_count += 1

estimated_pi = (inside_circle_count / TOTAL_RANDOM_POINTS) * QUARTER_CIRCLE_AREA_FACTOR

print(f"Estimated value of pi is: {estimated_pi}")