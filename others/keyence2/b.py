class Robot:
    def __init__(self, index, x, l):
        self.index = index
        self.l = l
        self.x = x
        self.left = x - l
        self.right = x + l

    def __repr__(self):
        return "<reprtest '%s' : '%s'>" % (self.x, self.l)


if __name__ == "__main__":
    N = int(input())

    robot_list = []
    for i in range(N):
        x, l = map(int, input().split())
        robot_list.append(Robot(i, x, l))

    x_robot_list = sorted(robot_list, key=lambda x: x.x)
    left_robot_list = sorted(robot_list, key=lambda x: x.x)
    right_robot_list = sorted(robot_list, key=lambda x: x.x)

    delete_count = 0
    for robot in x_robot_list
