class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start.replace("_", "") != target.replace("_", ""):
            return False
        start_L_positions = []
        start_R_positions = []
        target_L_positions = []
        target_R_positions = []
        for i in range(len(start)):
            if start[i] == "L":
                start_L_positions.append(i)
            if start[i] == "R":
                start_R_positions.append(i)
            if target[i] == "L":
                target_L_positions.append(i)
            if target[i] == "R":
                target_R_positions.append(i)
        for s_pos, t_pos in zip(start_L_positions, target_L_positions):
            if s_pos < t_pos:
                return False
        for s_pos, t_pos in zip(start_R_positions, target_R_positions):
            if s_pos > t_pos:
                return False
        return True