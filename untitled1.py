# class Circle:
#     def __init__(self, x:int, y:int, r:int, color:str):
#         self.x = x
#         self.y = y
#         self.r = r
#         self.color = color
        
#     def __str__(self):  
#         return f"круг расположен x:{self.x}, y:{self.y}, его радиус = {self.r} и цвет {self.color}"
        
        
 
# circle = Circle(1,45,2, 'red')
         
# print(circle)
         
 
class Camera:
    main_camera =None
    
    def __init__(self, number):
        self.number = number
        
        if Camera.main_camera == None:
            Camera.main_camera = self
            
    def __str__(self):
        return f'Номер камеры {self.number}'
    
    def set_active(self):
        Camera.main_camera = self
        
    def clear_main_camera():
        Camera.main_camera = None
        
camera1 = Camera('1')
camera2 = Camera('2')
camera3 = Camera('3')

print(Camera.main_camera)

camera3.set_active()

print(Camera.main_camera)

Camera.clear_main_camera()
print(Camera.main_camera)




