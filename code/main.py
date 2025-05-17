from setting import*
from player import player
from sprites import*
from pytmx.util_pygame import load_pygame
from random import randint,choice
from groups import*
import sqlite3
from gui.result_screen import show_ending_screen

class Game:
    def __init__(self):
        pygame.init()
        self.display_surface=pygame.display.set_mode((W_WIDTH,W_HEIGHT))# create window displaying game.
        pygame.display.set_caption("Hunter")#setup tittle
        self.Clock=pygame.time.Clock()#so luong man hinh duy chuyn trong 1 giay.
        self.running=True# ban đầu nó luôn chạy.
        
        # Load icon ảnh (nên là ảnh nhỏ, ví dụ 32x32)
        icon_surface = pygame.image.load('images\hunter (1).png')

        # Đặt icon cho cửa sổ
        pygame.display.set_icon(icon_surface)
        # tao Group sprite de chua cac doi tuong duoc tao tu sprite
        self.all_sprites=AllSprites()
        self.collision_spirits=pygame.sprite.Group()
        self.bullet_sprites=pygame.sprite.Group()
        self.enemy_sprites=pygame.sprite.Group()

        #Audio 
        self.shoot_Sound=pygame.mixer.Sound(join('audio','shoot.wav'))
        self.shoot_Sound.set_volume(0.4)
        self.impact_sound=pygame.mixer.Sound(join('audio','impact.ogg'))
        self.music=pygame.mixer.Sound(join('audio','music.wav'))
        self.music.set_volume(0.3)
        self.music.play(loops=-1)
        
        # gun setup
        self.can_shoot=True
        self.shoot_time=0
        self.gun_cooldown=100
        #Enemy timer
        self.enemy_events=pygame.event.custom_type()
        pygame.time.set_timer(self.enemy_events,300)
        self.spawn_position=[]

        #setup
        self.load_images()
        self.setup()
        self.game_over = False
        self.current_score = 0

    def load_images(self):
        self.bullet_surf = pygame.image.load(join('images', 'gun', 'bullet.png')).convert_alpha()
        
        folders = list(walk(join('images', 'enemies')))[0][1] # Lấy tên thư mục con
        
        self.enemy_frames = {}
        for folder in folders:
            for folder_path, _, file_names in walk(join('images', 'enemies', folder)):
                self.enemy_frames[folder]=[]
                for file_name in sorted(file_names, key=lambda name: int(name.split('.')[0])):
                    full_path = join(folder_path, file_name)
                    surf = pygame.image.load(full_path).convert_alpha()
                    self.enemy_frames[folder].append(surf)

        print("Enemy frames loaded:", self.enemy_frames.keys())
    def input(self):
          if pygame.mouse.get_pressed()[0]and self.can_shoot:
              self.shoot_Sound.play()
              pos=self.gun.rect.center+self.gun.play_direction*50

              Bullet(self.bullet_surf,pos,self.gun.play_direction,(self.all_sprites,self.bullet_sprites))
              self.can_shoot=False
              self.shoot_time=pygame.time.get_ticks()

    def gun_timer(self):
        if not self.can_shoot:
            current_time=pygame.time.get_ticks()
            if current_time-self.shoot_time>=self.gun_cooldown:
                self.can_shoot=True

    def bullet_collision(self):
        if self.bullet_sprites:
            for bullet in self.bullet_sprites:
                CollisionSprites=pygame.sprite.spritecollide(bullet,self.enemy_sprites,False,pygame.sprite.collide_mask)
                if CollisionSprites:
                    self.impact_sound.play()
                    for sprite in CollisionSprites:
                        sprite.destroy()
                        self.current_score+=1
                        print(f"Score increased: {self.current_score}")
    def player_collision(self):
        if pygame.sprite.spritecollide(self.player, self.enemy_sprites, False,pygame.sprite.collide_mask):
            self.running=False
            self.game_over = True
            self.save_score()
            



    def run(self):# cần duy trì màn hình nên phải có vòng lặp
        while self.running:
            #dt
            dt=self.Clock.tick()/1000


            #event loop
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    self.running=False
                if event.type==self.enemy_events:
                    enemy(
                        choice(self.spawn_position),
                        choice(list(self.enemy_frames.values())),
                        self.collision_spirits,
                        self.player,
                        self.all_sprites,
                        self.enemy_sprites
        
)

            #update
            self.gun_timer()
            self.input()
            self.all_sprites.update(dt)
            self.bullet_collision()
            self.player_collision()
            #draw other stuff/
            self.display_surface.fill("black")#che dấu dư ảnh khi chuyển động
            self.all_sprites.draw(self.player.rect.center)
            pygame.display.flip()#or update()
                    
        pygame.quit()
        if self.game_over:
            from gui.result_screen import show_ending_screen
            show_ending_screen(self.current_score)
        
        
    def setup(self):
        map=load_pygame(join('data','maps','world.tmx'))
        for x,y,image in map.get_layer_by_name('Ground').tiles():
            Sprite((x*TILE_SIZE,y*TILE_SIZE),image,self.all_sprites)
        for obj in map.get_layer_by_name('Objects'):
            CollisionSprites((obj.x,obj.y),obj.image,(self.all_sprites,self.collision_spirits))
        for obj in map.get_layer_by_name('Collisions'):
            CollisionSprites((obj.x,obj.y),pygame.Surface((obj.width,obj.height)),self.collision_spirits)        

        for obj in map.get_layer_by_name("Entities"):
            if obj.name=='Player':
                self.player=player((obj.x,obj.y),self.all_sprites,collision_sprites=self.collision_spirits)
                self.gun=Gun(self.player,self.all_sprites)
            else:
                self.spawn_position.append((obj.x,obj.y))
    def save_score(self):
        print("Saving score:", self.current_score)
        try:
            conn = sqlite3.connect("score.db")
            cursor = conn.cursor()
            cursor.execute("INSERT INTO game_sessions (total_score) VALUES (?)", (self.current_score,))
            conn.commit()
            conn.close()
            print("Score saved successfully!")
        except Exception as e:
            print("Error saving score:", e)
def run_all_game():
    game=Game()
    game.run()

if __name__=="__main__":# tái sử dụng code.
    game=Game()
    game.run()