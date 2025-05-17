from setting import*
class player(pygame.sprite.Sprite):
    def __init__(self,pos,*groups,collision_sprites):
        super().__init__(*groups)
        self.load_images()
        self.state,self.frame_index='up',0
        self.image=pygame.image.load(join("images","player","down","0.png")).convert_alpha()#thiet lap hinh anh
        self.rect=self.image.get_frect(center=pos)#tao frame hcn voi vi tri pos.
        self.hitbox_rect=self.rect.inflate(-70,-60)#trả về 1 hcn va chạm nhỏ hơn ban đầu(chủ yếu dùng để thu gọn hình)
        #Movement.
        self.direction=pygame.Vector2()
        self.speed=500
        self.collision_sprites=collision_sprites
    
    def load_images(self):
        self.frames={'left':[],'right':[],'up':[],'down':[]}
        for state in self.frames.keys():
            for folder_path,sub_folders,file_names in walk(join('images','player',state)):
                if file_names:
                    for file_name in sorted(file_names, key=lambda name: int(name.split('.')[0])):
                        full_path=join(folder_path,file_name)
                        surf=pygame.image.load(full_path).convert_alpha()
                        self.frames[state].append(surf)
        print(self.frames)
    def input(self):# khien nhan vat di chuyen duoc
        keys = pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT]or keys[pygame.K_d]) - int(keys[pygame.K_LEFT]or keys[pygame.K_a])
        self.direction.y=int(keys[pygame.K_DOWN] or keys[pygame.K_s])-int(keys[pygame.K_UP]or keys[pygame.K_w])
        self.direction=self.direction.normalize() if self.direction else self.direction
    def move(self,dt):
       self.hitbox_rect.x+=self.direction.x*self.speed*dt
       self.collision("horizontal")
       self.hitbox_rect.y+=self.direction.y*self.speed*dt
       self.collision("Vertical")
       self.rect.center=self.hitbox_rect.center
    def animation(self,dt):
        #get state
        if self.direction.x != 0:
            self.state = 'right' if self.direction.x > 0 else 'left'
        elif self.direction.y != 0:
            self.state = 'down' if self.direction.y > 0 else 'up'
        elif self.direction==pygame.Vector2(0,0):
            self.frame_index=0
        else:
            self.frame_index+=5*dt
            
        #animate
        self.frame_index += 5 * dt
        self.image = self.frames[self.state][int(self.frame_index) % len(self.frames[self.state])]
    def collision(self,direction):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.hitbox_rect):#check va cham
                if direction=='horizontal':
                    if self.direction.x>0:self.hitbox_rect.right=sprite.rect.left
                    if self.direction.x<0:self.hitbox_rect.left=sprite.rect.right
                else:
                    if self.direction.y<0:self.hitbox_rect.top=sprite.rect.bottom
                    if self.direction.y>0:self.hitbox_rect.bottom=sprite.rect.top
    def update(self,dt):
        self.input()
        self.move(dt)
        self.animation(dt)