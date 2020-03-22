from recordclass import recordclass

Curve = recordclass("Curve", ["id", "points", "color", "width", "isVisible", "pointsVisible", "hullVisible"])
curves = []



class Point2(x, y):
    def __init__(self):
        assert(isInstance(x, 'number') && isInstance(y, 'number'))
        self.x = x
        self.y = y


class Point2(x, y, z):
    def __init__(self):
        assert(isInstance(x, 'number') && isInstance(y, 'number') && isInstance(z, 'number'))
        self.x = x
        self.y = y
        self.z = z


class Curve(curveType, points, is3D=False, color=(0, 0, 0), width=2, isVisible=True, pointsVisible=True, hullVisible=False):
    def __init__(self):
        assert(curveType in ['broken-line'])
        assert(len(points) > 0)
        for p in points:
            if is3D:
                assert(isInstance(p, Point2))
            else
                assert(isInstance(p, Point3))

        self.index = len(curves)
        self.curveType = curveType
        self.is3D = is3D
        self.color = color
        self.width = width
        self.isVisible = isVisible
        self.pointsVisible = pointsVisible
        self.hullVisible = hullVisible
        self.points = points


def printHelp(command):
print(
'''
    
    
''')


def main():
    actions = {
        "quit" : quit,
        "help" : printHelp,

        "save_json" : saveAsJson,
        "read_json" : readFromJson,
        "save_image" : saveAsImage,
        "curves_info" : printCurvesInfo,

        "info" : printInfoCurve,
        "new_curve" : newCurve,
        "remove_curve" : removeCurve,

        "add_point" : addPoint,
        "move_point" : movePoint,
        "remove_point" : removePoint,
        "swap_points" : swapPoints,
        
        "move_curve" : moveCurve,
        "reverse" : reversePointOrder,
        "scale" : scaleCurve,
        "rotate" : rotateCurve,
        "append" : appendCurve,

        "set_color" : setColor,
        "set_width" : setWidth,

        "show_curve" : showCurve,
        "hide_curve" : hideCurve,
        "show_points" : showPoints,
        "hide_points" : hidePoints,
        "show_hull" : showHull,
        "hide_hull" : hideHull
    } 


    while True:
        inp = input()
        inp = inp.split()

        if len(inp) < 1:
            print("See 'help' for more information about available commands.")
            continue

        command = inp[0]

        if command in actions:
            actions[command](inp)
            updateView()
        else:
            print("Command unknown. Please try again or see 'help' for more information.")


main()