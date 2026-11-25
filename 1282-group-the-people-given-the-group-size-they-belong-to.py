class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        grp = defaultdict(list)
        result = []

        for i, size in enumerate(groupSizes):
            grp[size].append(i)

            if len(grp[size]) == size:
                result.append(grp[size])
                grp[size] = []

        return result


        