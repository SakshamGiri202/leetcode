class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        
        height_map = {}

        for i in range(len(names)):
            height_map[heights[i]] = names[i]

        sorted_names = []

        for height in sorted(height_map.keys(), reverse=True):
            sorted_names.append(height_map[height])

        return sorted_names

