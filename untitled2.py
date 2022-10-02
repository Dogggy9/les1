class Shape:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
    
    def __str__(self):
        return f'{self.x},{self.y},{self.color}'
    
    def draw(self):
        print(self)
        
    @property
    def x(self):
        return self.__x
        
        
    @x.setter
    def x(self, x):
        is_int = type(x) is type(int())
        assert is_int, "Назначай целые  значения"
        self.__x = x
        
    @property
    def y(self):
        return self.__y
        
        
    @y.setter
    def y(self, y):
        # assert title is str, "Назначай заголовок строкой"
        self.__y = y
        
    @property
    def color(self):
        return self.__color
        
        
    @color.setter
    def color(self, color):
        # assert title is str, "Назначай заголовок строкой"
        self.__color = color
        
class Triangle(Shape):
    def __init__(self,x,y,color,a,b,angle):
        super().__init__(x,y,color)
        self.a = a
        self.b = b
        self.angle = angle
        
    def __str__(self):
        return f'{self.x},{self.y},{self.a}, {self.b},{self.angle}'
    
    def draw(self):
        print("Я   треугольник")
        print(self)
        
    @property
    def angle(self):
        return self.__angle
    
    @angle.setter
    def angle(self,  angle):
        assert angle > 0 and  angle  <  90,  "Угол некорректен" 
        self.__angle = angle
        
        
class Controller:
    def __init__(self):
        self.__shape_list = []
        
    def add_shape(self, shape):
        self.__shape_list.append(shape)
        
    def draw_all(self):
        for shape in self.__shape_list:
            shape.draw()
            
            
controller = Controller()
controller.add_shape(Triangle(1,2,"red",3,4,30))
controller.add_shape(Triangle(21,21,"black",1,1,1))    
controller.add_shape(Shape(21,21,"black"))  

controller.draw_all()       
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    