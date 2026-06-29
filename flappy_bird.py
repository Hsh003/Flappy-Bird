import pygame
import random
import sys

# 初始化 Pygame
pygame.init()

# 游戏常量
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 60

# 颜色定义 (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SKY_BLUE = (135, 206, 235)
GROUND_BROWN = (139, 90, 43)
PIPE_GREEN = (50, 205, 50)
BIRD_YELLOW = (255, 255, 0)

# 创建屏幕
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird")

# 时钟控制帧率
clock = pygame.time.Clock()

class Bird:
    def __init__(self):
        self.x = 50
        self.y = SCREEN_HEIGHT // 2
        self.width = 30
        self.height = 30
        self.velocity = 0
        self.gravity = 0.6
        self.jump_strength = -8
        
    def update(self):
        # 应用重力
        self.velocity += self.gravity
        self.y += self.velocity
        
    def jump(self):
        self.velocity = self.jump_strength
        
    def draw(self, surface):
        pygame.draw.rect(surface, BIRD_YELLOW, (self.x, self.y, self.width, self.height))
        # 画眼睛
        pygame.draw.circle(surface, BLACK, (self.x + 20, self.y + 10), 5)

class Pipe:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.width = 60
        self.gap_height = 150
        # 随机生成管道位置
        min_pipe_top = 50
        max_pipe_top = SCREEN_HEIGHT - self.gap_height - min_pipe_top
        self.top_pipe_y = random.randint(min_pipe_top, max_pipe_top)
        
    def update(self):
        self.x -= 3
        
    def draw(self, surface):
        # 上管道
        pygame.draw.rect(surface, PIPE_GREEN, (self.x, 0, self.width, self.top_pipe_y))
        # 下管道
        bottom_pipe_y = self.top_pipe_y + self.gap_height
        pygame.draw.rect(surface, PIPE_GREEN, (self.x, bottom_pipe_y, self.width, SCREEN_HEIGHT - bottom_pipe_y))

def draw_ground(surface):
    """绘制地面"""
    ground_rect = pygame.Rect(0, SCREEN_HEIGHT - 50, SCREEN_WIDTH, 50)
    pygame.draw.rect(surface, GROUND_BROWN, ground_rect)
    # 画草地边缘
    pygame.draw.line(surface, (144, 238, 144), (0, SCREEN_HEIGHT - 50), 
                     (SCREEN_WIDTH, SCREEN_HEIGHT - 50), 3)

def check_ground_collision(bird):
    """检查地面碰撞"""
    ground_y = SCREEN_HEIGHT - 50
    return bird.y + bird.height >= ground_y

def draw_score(surface):
    """绘制分数"""
    font = pygame.font.Font(None, 36)
    score_text = font.render(str(score), True, BLACK)
    surface.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 10))

def draw_game_over(surface):
    """绘制游戏结束画面"""
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    overlay.fill(BLACK)
    overlay.set_alpha(0.7)
    surface.blit(overlay, (0, 0))
    
    font = pygame.font.Font(None, 48)
    text = font.render("GAME OVER", True, WHITE)
    surface.blit(text, 
                 ((SCREEN_WIDTH - text.get_width()) // 2, SCREEN_HEIGHT // 2 - 30))
                  
    restart_font = pygame.font.Font(None, 28)
    restart_text = restart_font.render("Press Space to Restart", True, WHITE)
    surface.blit(restart_text, 
                 ((SCREEN_WIDTH - restart_text.get_width()) // 2, SCREEN_HEIGHT // 2 + 30))


def draw_start_page(surface):
    """绘制开始页面"""
    # 半透明遮罩
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    overlay.fill(BLACK)
    overlay.set_alpha(150)
    surface.blit(overlay, (0, 0))
    
    # 标题
    title_font = pygame.font.Font(None, 72)
    title_text = title_font.render("Flappy Bird", True, BIRD_YELLOW)
    surface.blit(title_text, 
                 ((SCREEN_WIDTH - title_text.get_width()) // 2, SCREEN_HEIGHT // 3))
    
    # 说明文字
    instruction_font = pygame.font.Font(None, 36)
    instr1 = instruction_font.render("Press Space or Enter to Start", True, WHITE)
    surface.blit(instr1, 
                 ((SCREEN_WIDTH - instr1.get_width()) // 2, SCREEN_HEIGHT // 2))
    
    instr2 = instruction_font.render("Be careful not to hit the pipes!", True, WHITE)
    surface.blit(instr2, 
                 ((SCREEN_WIDTH - instr2.get_width()) // 2, SCREEN_HEIGHT // 2 + 40))



# 游戏主循环
score = 0
game_over = False
start_page = True
bird = Bird()
pipe = Pipe()
last_pass_time = pygame.time.get_ticks()
game_started = True

running = True
while running:
    # 事件处理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.KEYDOWN:
            if start_page and (event.key == pygame.K_SPACE or event.key == pygame.K_RETURN):
                # 开始游戏
                start_page = False
                
            elif game_over and event.key == pygame.K_SPACE:
                # 重置游戏
                bird = Bird()
                pipe = Pipe()
                score = 0
                game_over = False
                start_page = True
                
            elif not game_over and event.key == pygame.K_SPACE:
                bird.jump()

        
    # 如果不在开始页面且游戏未结束，才更新游戏逻辑
    if not start_page and not game_over:
        # 更新小鸟位置
        bird.update()
        
        # 更新管道位置
        pipe.update()
        
        # 检查碰撞（使用矩形碰撞检测）
        if pygame.Rect(bird.x, bird.y, bird.width, bird.height).colliderect(
               (pipe.x, 0, pipe.width, pipe.top_pipe_y)):
            game_over = True
        elif pygame.Rect(bird.x, bird.y, bird.width, bird.height).colliderect(
               (pipe.x, pipe.top_pipe_y + pipe.gap_height, pipe.width, SCREEN_HEIGHT - pipe.top_pipe_y - pipe.gap_height)):
            game_over = True
        
        # 检查地面碰撞
        if check_ground_collision(bird):
            game_over = True
            
        # 管道移出屏幕后生成新管道
        if pipe.x + pipe.width < 0:
            pipe = Pipe()
            
        # 每通过一个管道加分（小鸟右边缘超过管道右边缘）
        if bird.x + bird.width > pipe.x + pipe.width:
            pass_time = pygame.time.get_ticks() - last_pass_time
            if pass_time >= 1000:  # 缓冲时间 1000ms
                score += 1
                last_pass_time = pygame.time.get_ticks()

    # 绘制背景
    screen.fill(SKY_BLUE)
    
    # 绘制地面
    draw_ground(screen)
    
    # 绘制管道
    pipe.draw(screen)
    
    # 绘制小鸟
    bird.draw(screen)
    
    # 绘制分数
    draw_score(screen)
    
    # 如果游戏结束，显示游戏结束画面
    if game_over:
        draw_game_over(screen)
    elif start_page:
        draw_start_page(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
