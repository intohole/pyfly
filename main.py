#coding=utf-8
#!/usr/bin/env python




from cocos.layer import Layer 
from cocos.sprite import Sprite
from cocos.scene import Scene
from cocos.director import director
from cocos.actions import MoveTo
from cocos.actions import Repeat
from cocos.actions import Delay






class BossPlane(Layer):

    def __init__(self , image , position , duration , delay = 3.0):
        super(BossPlane , self ).__init__()
        self.plane = Sprite(image = image  , position = position)
        move = MoveTo((position[0], -self.plane.image.height ) , duration = duration )
        move_back = MoveTo( position , 0 )
        delay_action = Delay(delay)
        self.plane.do(Repeat(move + delay_action + move_back))
        self.add(self.plane)






class MouseDisplay(Layer):
    is_event_handler = True # 接收事件信息标志位

    def __init__ (self):
        super( MouseDisplay, self ).__init__()
        director.window
        self.posx = director.window.width / 2 
        self.posy = 50 
        self.plane = Sprite(image = 'pics/icon36x36.png',  position = (self.posx , self.posy))
        self.add( self.plane )

    def update_position (self, x, y):
        self.plane.position = x,y


    def on_mouse_motion (self, x, y, dx, dy):
        """Called when the mouse moves over the app window with no button pressed
        
        (x, y) are the physical coordinates of the mouse
        (dx, dy) is the distance vector covered by the mouse pointer since the
          last call.
        """
        self.update_position (x, y)




if __name__== "__main__":
	director.init()
	control_layer = MouseDisplay()
	p1 = BossPlane(image = 'pics/icon36x36.png' , position = ( director.window.width /2 , director.window.height) , duration = 3)
	main_scene=Scene(control_layer , p1)
    	director.run(main_scene)