class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles = set((o[0], o[1]) for o in obstacles)
        place = [0,0]
        state = 0 #up = 0, left = 1, down = 2, right = 3
        currmax = 0
        for command in commands:
            if command == -2:
                state = (state + 5) % 4
            elif command == -1:
                state = (state + 7) % 4
            else:
                for i in range(command):
                    temp_place = [place[0], place[1]]
                    if state == 0:
                        place[1] += 1
                    if state == 1:
                        place[0] -= 1
                    if state == 2:
                        place[1] -= 1
                    if state == 3:
                        place[0] += 1
                    if (place[0], place[1]) in obstacles:
                        place = temp_place
                        break
                currmax = max(currmax, place[0] ** 2 + place[1] ** 2)
        return currmax
                





