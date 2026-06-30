# 飞翔的小鸟 (Flappy Bird)

一个使用 Pygame 制作的经典 Flappy Bird 复刻版。控制小鸟躲避管道，挑战最高分！

[![Download Flappy Bird](https://img.shields.io/github/downloads/Hsh003/Flappy-Bird/total?style=for-the-badge&logo=windows)](https://github.com/Hsh003/Flappy-Bird/releases/latest)

---

## 🎮 游戏玩法

| 操作 | 说明 |
|------|------|
| **空格键** | 小鸟向上跳跃 |
| **游戏结束后再按空格** | 重新开始 |

**目标**：穿过绿色管道，避免碰撞，获得更高分数。

---

## 🛠️ 运行方式

### 方式一：直接游玩（推荐，无需 Python）
1. 前往 [Releases](https://github.com/Hsh003/Flappy-Bird/releases/latest)
2. 下载 `flappy_bird.exe`
3. 双击即可运行

### 方式二：源码运行（需要 Python）

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
Flappy-Bird/
├── flappy_bird.py   # 主程序
├── LICENSE          # MIT
├── README.md        # 说明
└── .gitattributes
```


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
