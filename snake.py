import time
import os
import sys
import random
from PyQt5.QtWidgets import QMainWindow, QApplication
from frame import Ui_windows
import threading


class Snake:
    def __init__(self):  # 定义蛇的属性
        self.difficult = 0
        self.score = 0  # 分数
        self.head = {'x': 2, 'y': 3}  # 记录蛇头部坐标
        self.body = [{'x': 2, 'y': 1}, {'x': 2, 'y': 2}, {'x': 2, 'y': 3}]  # 身体坐标
        self.food = {'x': 0, 'y': 0}
        self.movement = 'down'
        self.ready_movement = 'down'
        while True:
            try:
                self.difficult = 1 / int(input('请输入难度(1~ 10):'))
                break
            except Exception as e:
                print("输入错误!", e)
        # 开启控制蛇移动的线程
        self.rebirth_food()
        self.refresh_screen()
        th = threading.Thread(target=self.main, args=())
        th.start()

    def set_movement(self, direction):
        """
        功能: 检测蛇的移动方位是否冲突
        :return: None
        """
        if direction == 'left' and self.movement == 'right':
            return False
        elif direction == 'right' and self.movement == 'left':
            return False
        elif direction == 'up' and self.movement == 'down':
            return False
        elif direction == 'down' and self.movement == 'up':
            return False
        self.ready_movement = direction

    def refresh_screen(self):
        """
        功能: 刷新蛇的位置[40 * 20]
        :return: None
        """
        os.system('cls')
        print("贪吃蛇    分数:", self.score)
        print_data = ""
        for y in range(22):
            for x in range(42):
                if x == 0 or y == 0 or x == 41 or y == 21:  # 绘制边界
                    print_data += "□"
                else:
                    point_data = 0  # 0: 无数据, 1: 身子, 2: 头部, 3: 食物
                    for body in self.body:  # 遍历蛇数据,判断是否是蛇身子
                        if body['x'] == x and body['y'] == y:
                            point_data = 1
                    if self.head['x'] == x and self.head['y'] == y:  # 判断是否为头部
                        point_data = 2
                    if self.food['x'] == x and self.food['y'] == y:  # 判断是否为食物
                        point_data = 3
                    # 打印数据
                    if point_data == 0:
                        print_data += "  "  # 空白
                    elif point_data == 1:
                        print_data += "■"  # 身体
                    elif point_data == 2:
                        print_data += "◆"  # 头部
                    elif point_data == 3:
                        print_data += "☆"  # 食物
            print_data += "\n"
        print(print_data)

    def move(self):
        """
        功能:对蛇进行移动
        :return: bol: Fail
        """
        self.movement = self.ready_movement
        new_head = self.head  # 移动后蛇的位置
        if self.movement == 'left':  # 向左移动
            new_head = {'x': self.head['x'] - 1, 'y': self.head['y']}
        elif self.movement == 'right':  # 向右移动
            new_head = {'x': self.head['x'] + 1, 'y': self.head['y']}
        elif self.movement == 'up':  # 向上移动
            new_head = {'x': self.head['x'], 'y': self.head['y'] - 1}
        elif self.movement == 'down':  # 向下移动
            new_head = {'x': self.head['x'], 'y': self.head['y'] + 1}
        # 吃到食物判断
        if new_head['x'] == self.food['x'] and new_head['y'] == self.food['y']:
            self.score += 1
            self.body.append(new_head)
            self.head = new_head
            self.rebirth_food()
            return True
        # 吃到自己判断
        for body in self.body:
            if new_head['x'] == body['x'] and new_head['y'] == body['y']:
                return False
        # 碰到墙判断
        if new_head['x'] == 41 or new_head['y'] == 21 or new_head['x'] == 0 or new_head['y'] == 0:
            return False
        # 什么都没有发生,更新头部位置
        self.body.append(new_head)
        self.head = new_head
        del self.body[0]
        return True

    def rebirth_food(self):
        """
        功能: 随机生成食物
        遍历列表,查找没有被蛇占的位置,随机选取一个
        """
        food_point = []
        for y in range(1, 21):
            for x in range(1, 41):
                for body in self.body:
                    if body['x'] != x and body['y'] != y:
                        food_point.append({'x': x, "y": y})
        self.food = random.choice(food_point)

    def main(self):
        """
        功能:负责主循环
        """
        while True:
            if self.move() is False:
                break
            self.refresh_screen()
            time.sleep(self.difficult)
        print("你死了,分数:", self.score)


class Windows(QMainWindow, Ui_windows):
    def __init__(self):
        """
        功能: 创建控制窗口
        """
        super(Windows, self).__init__()
        self.setupUi(self)
        self.bt_up.clicked.connect(lambda: snake.set_movement('up'))
        self.bt_down.clicked.connect(lambda: snake.set_movement('down'))
        self.bt_left.clicked.connect(lambda: snake.set_movement('left'))
        self.bt_right.clicked.connect(lambda: snake.set_movement('right'))
        self.show()


# 实例化对象,开启ui线程
snake = Snake()
app = QApplication(sys.argv)
windows = Windows()
sys.exit(app.exec_())
