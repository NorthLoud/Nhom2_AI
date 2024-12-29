from enum import Enum
from collections import namedtuple

# Định nghĩa các vị trí
Location = Enum('Location', ['A', 'B'])

# Định nghĩa trạng thái
State = namedtuple('State', ['man', 'cabbage', 'goat', 'wolf'])

# Kiểm tra trạng thái hợp lệ
def is_valid(state):
    goat_eats_cabbage = (state.goat == state.cabbage and state.man != state.goat)
    wolf_eats_goat = (state.wolf == state.goat and state.man != state.wolf)
    return not (goat_eats_cabbage or wolf_eats_goat)

# Tìm kiếm theo chiều sâu
def depth_first_search(start, is_goal, get_neighbors):
    parent = dict()                # tạo một từ điển để lưu trữ đỉnh cha của mỗi đình
    to_visit = [start]              # khởi tạo ngăn xếp stack
    discovered = set([start])        # tạo một tập thể để lưu trữ các đỉnh đã được khám phá
    while to_visit:
        vertex = to_visit.pop()         # lấy ra đình của ngăn xếp
        if is_goal(vertex):              # Nếu là đỉnh đích
            path = []                     # khởi tạo một danh sách để lưu trữ đường đi
            while vertex is not None:      # cho qua các đình
                path.insert(0, vertex)      # thêm đỉnh hiện tại vào danh sách đường đi
                vertex = parent.get(vertex)  # cập nhập đỉnh hiện tại thành đỉnh cha của nó
            return path                       # trả về đường đi của đỉnh đỉnh bắt đầu đến đích
        for neighbor in get_neighbors(vertex):  # lập qua các đỉnh con đỉnh hiện tại
            if neighbor not in discovered and is_valid(neighbor): # nêu đỉnh chưa xét thì hợp lệ
                discovered.add(neighbor)          # thêm đỉnh vào tập hợp đỉnh đã xét
                parent[neighbor] = vertex          # đặt hiện tại làm đỉnh cha
                to_visit.append(neighbor)           # thêm đình con vào ngăn xếp
    return None  # Nếu không tìm được đường đi

# Định nghĩa trạng thái ban đầu và trạng thái mục tiêu
start_state = State(man=Location.A, cabbage=Location.A, goat=Location.A, wolf=Location.A)
goal_state = State(man=Location.B, cabbage=Location.B, goat=Location.B, wolf=Location.B)

# Định nghĩa hàm lấy các trạng thái kế tiếp
def get_neighbors (state):
    neighbors = []
    for obj in ['man', 'cabbage', 'goat', 'wolf']:
      if getattr(state, obj) == state.man: # Nếu đối tượng đang ở cùng vị trí với người đàn ông
        new_location = Location. A if state.man == Location. B else Location.B # xác định vị trí người đàn ông và đối tượng
        new_state = State(**{k: new_location if k == obj or k == 'man' else v for k, v in state._asdict().items()})

#Tạo một trạng thái mới với người đàn ông và đối tượng ở vị trí mới, còn lại giữ nguyên.
        neighbors.append(new_state)
    return neighbors

# Tìm đường đi
path = depth_first_search(start=start_state, is_goal=goal_state.__eq__, get_neighbors=get_neighbors)

# In đường đi
for state in path:
         print(state)