# 飞翔的小鸟 (Flappy Bird)

一个使用 Pygame 制作的经典游戏。控制小鸟躲避管道，尽可能获得高分！

## 🎮 游戏玩法

- **按空格键**：让小鸟向上飞
- **目标**：穿过绿色管道并避免碰撞
- **得分**：每成功通过一组管道得 1 分
- **重新开始**：游戏结束后按空格键重启

## 🛠️ 技术说明

想直接玩的 → Releases 下 exe

想看代码的 → clone 仓库:

### 依赖项

```bash
pip install pygame
```

### 系统要求

- Python 3.x
- Pygame 库

### 运行方法


```bash
python flappy_bird.py
```

或在 Windows 上：

```cmd
flappy_bird.py
```

## 📁 项目结构

```
Flappy Bird/
├── flappy_bird.py    # 主程序文件
└── README.md         # 本说明文档
```

## 💡 游戏机制

- **重力系统**：小鸟持续下落，按空格可向上跳跃
- **随机管道生成**：每次新管道的高度随机变化
- **碰撞检测**：使用矩形碰撞判断与地面/管道的接触
- **分数系统**：安全通过一组管道后加分（含防作弊延时）

## 🎨 配色方案

| 元素 | 颜色 | RGB |
|------|------|-----|
| 天空背景 | Sky Blue | (135, 206, 235) |
| 小鸟 | Yellow | (255, 255, 0) |
| 管道 | Green | (50, 205, 50) |
| 地面 | Brown | (139, 90, 43) |

## 🐛 类与函数概览

- `Bird`：小鸟类，管理位置和跳跃
- `Pipe`：管道类，生成随机高度的障碍物
- `draw_ground()`：绘制地面
- `check_ground_collision()`：检测地面碰撞
- `draw_score()`：显示当前分数
- `draw_game_over()`：游戏结束画面


**Happy Flapping! ✈️**
