import pygame
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((500,250))

image_sprite = [pygame.image.load("/etc/project/speedometer/ezgif-frame-001.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-002.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-003.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-004.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-005.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-006.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-007.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-008.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-009.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-010.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-011.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-012.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-013.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-014.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-015.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-016.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-017.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-018.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-019.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-020.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-021.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-022.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-023.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-024.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-025.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-026.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-027.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-028.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-029.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-030.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-031.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-032.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-033.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-034.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-035.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-036.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-037.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-038.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-039.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-040.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-041.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-042.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-043.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-044.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-045.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-046.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-047.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-048.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-049.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-050.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-051.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-052.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-053.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-054.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-055.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-056.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-057.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-058.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-059.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-060.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-061.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-062.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-063.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-064.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-065.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-066.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-067.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-068.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-069.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-070.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-071.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-072.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-073.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-074.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-075.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-076.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-077.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-078.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-079.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-080.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-081.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-082.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-083.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-084.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-085.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-086.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-087.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-088.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-089.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-090.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-091.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-092.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-093.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-094.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-095.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-096.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-097.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-098.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-099.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-100.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-101.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-102.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-103.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-104.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-105.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-106.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-107.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-108.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-109.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-110.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-111.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-112.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-113.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-114.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-115.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-116.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-117.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-118.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-119.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-120.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-121.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-122.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-123.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-124.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-125.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-126.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-127.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-128.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-129.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-130.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-131.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-132.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-133.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-134.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-135.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-136.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-137.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-138.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-139.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-140.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-141.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-142.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-143.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-144.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-145.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-146.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-147.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-148.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-149.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-150.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-151.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-152.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-153.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-154.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-155.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-156.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-157.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-158.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-159.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-160.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-161.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-162.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-163.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-164.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-165.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-166.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-167.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-168.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-169.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-170.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-171.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-172.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-173.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-174.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-175.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-176.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-177.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-178.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-179.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-180.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-181.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-182.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-183.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-184.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-185.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-186.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-187.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-188.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-189.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-190.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-191.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-192.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-193.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-194.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-195.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-196.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-197.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-198.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-199.jpg"),
                pygame.image.load("/etc/project/speedometer/ezgif-frame-200.jpg"),]
                
image_sprite2 =[pygame.image.load("/etc/project/fuel_guage/ezgif-frame-001.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-002.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-003.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-004.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-005.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-006.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-007.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-008.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-009.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-010.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-011.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-012.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-013.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-014.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-015.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-016.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-017.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-018.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-019.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-020.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-021.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-022.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-023.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-024.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-025.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-026.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-027.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-028.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-029.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-030.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-031.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-032.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-033.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-034.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-035.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-036.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-037.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-038.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-039.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-040.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-041.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-042.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-043.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-044.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-045.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-046.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-047.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-048.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-049.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-050.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-051.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-052.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-053.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-054.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-055.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-056.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-057.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-058.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-059.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-060.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-061.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-062.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-063.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-064.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-065.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-066.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-067.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-068.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-069.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-070.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-071.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-072.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-073.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-074.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-075.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-076.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-077.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-078.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-079.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-080.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-081.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-082.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-083.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-084.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-085.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-086.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-087.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-088.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-089.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-090.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-091.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-092.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-093.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-094.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-095.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-096.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-097.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-098.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-099.jpg"),
                pygame.image.load("/etc/project/fuel_guage/ezgif-frame-100.jpg")]
                
image_sprite3 = [pygame.image.load("/etc/project/map/map.jpg")]
                
clock = pygame.time.Clock()

value = 0
value2 = 99

run = True

moving = True

x = 0
y = 0
i = 1

x2 = 250
y2 = 0

x3 = 0
y3 = 200

while run:
  
      clock.tick(20)
      
      if moving:
        value = value + i
        if(value == 199):
          i = -1
        elif(value == 0):
          i = 1
          
      
      if moving:
        if (value%10) == 0:
          value2 = value2 - 1
          if(value2 == 0):
            value2 = 99
        
            
      image = image_sprite[value]
      
      image2 = image_sprite2[value2]
      
      image3 = image_sprite3[0]
      
      image = pygame.transform.scale(image, (250, 250))
      
      image2 = pygame.transform.scale(image2, (250, 250))
      
      #image3 = pygame.transform.scale(image3, (400, 200))
      
      window.blit(image, (x,y))
      
      window.blit(image2, (x2,y2))
      
      #window.blit(image3, (x3, y3))
      
      pygame.display.update()
      
      window.fill((0,0,0)) 
        