
class ngonTriang:

    def __init__(self, n, triangles):

        # make sure triangles are sorted themselves
        # this aswell as the following lexicographical sort will be more
        # important for the flips
        for i in range(len(triangles)):
            triangles[i].sort()

        # make sure list is sorted lexicographically
        triangles.sort(key=lambda x: [x[0], x[1], x[2]])

        potwalls = []
        self.walls = []
        self.triangles = triangles
        self.n = n

        # find potential candidates for walls
        for i in range(len(self.triangles)):
            potwalls.append([self.triangles[i][0], self.triangles[i][1]])
            potwalls.append([self.triangles[i][0], self.triangles[i][2]])
            potwalls.append([self.triangles[i][1], self.triangles[i][2]])

        # if potential wall adjacent to two triangles -> wall
        for i in range(len(potwalls)):
            if potwalls.count(potwalls[i]) == 2 and \
                    potwalls[i] not in self.walls:
                self.walls.append(potwalls[i])

        self.walls.sort(key=lambda x: [x[0], x[1]])

        if not self._is_triangulation():
            raise ValueError("no triangulation")

    def n_walls(self):

        return len(self.walls)

    def flip(self, wall):

        square = []

        newtriangle = self.triangles

        for i in range(len(self.triangles)):

            if wall[0] in self.triangles[i] and wall[1] in self.triangles[i]:
                square.append(self.triangles[i])

        for i in range(len(square)):
            newtriangle.remove(square[i])

        for i in range(len(square)):
            square[i].remove(wall[0])
            square[i].remove(wall[1])

        newwall = [square[0][0], square[1][0]]

        flipped_1 = newwall + [wall[0]]
        flipped_2 = newwall + [wall[1]]

        newtriangle.append(flipped_1)
        newtriangle.append(flipped_2)

        A = ngonTriang(self.n, newtriangle)

        return A

    def _is_triangulation(self):

        # triangulation needs to have exactly n-3 walls
        if self.n_walls() != self.n - 3:
            return False

        # triangulation needs to have exactly n-2 triangles
        if len(self.triangles) != self.n - 2:
            return False

        # check for crossing edges
        for i in range(len(self.walls)):
            for j in range(i+1, len(self.walls)):
                if self.walls[i][0] < self.walls[j][0] \
                        and self.walls[i][1] < self.walls[j][1] \
                        and self.walls[i][1] > self.walls[j][0]:
                    return False

        return True
