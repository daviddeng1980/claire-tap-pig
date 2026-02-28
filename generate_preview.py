from PIL import Image, ImageDraw, ImageFont
import os

# 创建设计预览图
width, height = 800, 1000
img = Image.new('RGB', (width, height), color='#87CEEB')
draw = ImageDraw.Draw(img)

# 渐变背景
for y in range(height):
    r = int(135 + (152-135) * y / height)
    g = int(206 + (251-206) * y / height)
    b = int(235 + (152-235) * y / height)
    draw.line([(0, y), (width, y)], fill=(r, g, b))

# 标题
try:
    font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 36)
    font_text = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 20)
    font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 16)
except:
    font_title = ImageFont.load_default()
    font_text = ImageFont.load_default()
    font_small = ImageFont.load_default()

# 标题
draw.text((width//2, 30), "🐷 Claire 点猪游戏 - 设计预览", fill='#333333', font=font_title, anchor='mt')

# UI 区域示意
draw.rounded_rectangle([20, 80, 780, 140], radius=20, fill='white', outline='#ddd', width=2)
draw.text((40, 95), "🐷 分数: 250", fill='#333', font=font_text)
draw.text((250, 95), "🔥 连击: x5", fill='#333', font=font_text)
draw.text((420, 95), "❤️ 生命: 3", fill='#e74c3c', font=font_text)
draw.text((580, 95), "⏱️ 时间: 45秒", fill='#fff', font=font_text)
draw.rounded_rectangle([560, 85, 760, 135], radius=15, fill='#FF6B6B')
draw.text((660, 110), "⏱️ 45秒", fill='white', font=font_text, anchor='mm')

# 游戏区域
draw.rounded_rectangle([20, 160, 780, 600], radius=10, fill='#e8f8f5', outline='#98FB98', width=3)

# 绘制各种动物及其说明
y_pos = 180

# 普通猪
draw.text((100, y_pos), "🐷", fill='#333', font=font_title)
draw.text((160, y_pos-10), "普通小猪", fill='#333', font=font_text)
draw.text((160, y_pos+15), "+10分 | 安全", fill='#2ecc71', font=font_small)

y_pos += 70
draw.text((100, y_pos), "🐽", fill='#333', font=font_title)
draw.text((160, y_pos-10), "猪鼻子", fill='#333', font=font_text)
draw.text((160, y_pos+15), "+20分 | 移动快", fill='#2ecc71', font=font_small)

y_pos += 70
draw.text((100, y_pos), "🐖", fill='#333', font=font_title)
draw.text((160, y_pos-10), "大肥猪", fill='#333', font=font_text)
draw.text((160, y_pos+15), "+30分 | 体型大", fill='#2ecc71', font=font_small)

y_pos += 70
draw.text((100, y_pos), "🐗", fill='#333', font=font_title)
draw.text((160, y_pos-10), "野猪", fill='#333', font=font_text)
draw.text((160, y_pos+15), "+50分 | 速度快", fill='#2ecc71', font=font_small)

# 危险动物（右侧）
y_pos = 180
draw.text((450, y_pos), "🐺", fill='#333', font=font_title)
draw.text((510, y_pos-10), "狼 ⚠️", fill='#e74c3c', font=font_text)
draw.text((510, y_pos+15), "-30分 | 扣1生命", fill='#e74c3c', font=font_small)
# 红色警告光环示意
draw.ellipse([430, y_pos-20, 490, y_pos+40], outline='#e74c3c', width=3)

y_pos += 70
draw.text((450, y_pos), "🐯", fill='#333', font=font_title)
draw.text((510, y_pos-10), "老虎 ⚠️", fill='#e74c3c', font=font_text)
draw.text((510, y_pos+15), "-50分 | 扣1生命", fill='#e74c3c', font=font_small)
draw.ellipse([430, y_pos-20, 490, y_pos+40], outline='#e74c3c', width=3)

# 伪装猪（重点）
y_pos = 460
draw.rounded_rectangle([50, y_pos-20, 750, y_pos+80], radius=15, fill='#f0e6ff', outline='#9b59b6', width=3)
draw.text((100, y_pos), "🐺", fill='#333', font=font_title)
draw.text((160, y_pos-10), "披着狼皮的小猪 ⭐", fill='#9b59b6', font=font_text)
draw.text((160, y_pos+20), "外表是狼，点击+100分！", fill='#9b59b6', font=font_small)
draw.text((160, y_pos+40), "破绽：偶尔露出小猪轮廓/尾巴", fill='#9b59b6', font=font_small)

# 游戏机制说明
y_pos = 620
draw.text((width//2, y_pos), "游戏机制", fill='#333', font=font_title, anchor='mt')

mechanics = [
    "⏱️ 60秒倒计时",
    "❤️ 3条生命（点到狼/老虎扣生命）",
    "🔥 连击系统（连续点中分数加成）",
    "👀 伪装猪每1.5秒露出破绽（显示小猪轮廓）",
    "⚡ 动物会自动消失，手速要快！"
]

y_pos += 50
for mech in mechanics:
    draw.text((60, y_pos), mech, fill='#333', font=font_text)
    y_pos += 35

# 策略提示
y_pos += 20
draw.rounded_rectangle([40, y_pos, 760, y_pos+120], radius=15, fill='#fff9e6', outline='#FFD700', width=2)
draw.text((width//2, y_pos+20), "💡 策略要点", fill='#333', font=font_text, anchor='mt')
tips = [
    "1. 不要看到🐺就躲 — 可能是伪装猪，值100分！",
    "2. 观察红色光环 — 真正的狼和老虎有危险警告",
    "3. 等破绽出现 — 伪装猪会偶尔露出小猪特征"
]
y_tip = y_pos + 50
for tip in tips:
    draw.text((60, y_tip), tip, fill='#555', font=font_small)
    y_tip += 25

# 底部按钮示意
y_pos = height - 80
draw.rounded_rectangle([width//2-100, y_pos, width//2+100, y_pos+50], radius=25, fill='#FF6B6B')
draw.text((width//2, y_pos+25), "开始游戏", fill='white', font=font_text, anchor='mm')

# 保存
img.save('/root/.openclaw/workspace/claire-tap-pig/design_preview.png')
print("设计预览图已保存")
