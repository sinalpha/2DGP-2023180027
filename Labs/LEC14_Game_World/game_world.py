# 게임월드 리스트 초기화
world = [[],[]] # 객체들의 리스트, 빈 리스트

# 객체를 게임월드에 추가하는 함수
def add_object(o, depth=0):
    world[depth].append(o)


def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return 
        
    if o in world:
        world.remove(o)


def update():
    for layer in world:
        for o in layer:
            o.update()

def render():
    for layer in world:
        for o in layer:
            o.draw()
        