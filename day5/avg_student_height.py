heights = input("Enter Student Heights: ").split(" ")
height_sum = 0
for idx, height in enumerate(heights):
    heights[idx] = int(height)

height_sum = sum(heights)

avg = height_sum/len(heights)
print(round(avg))
