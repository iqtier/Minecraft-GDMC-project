# once the structure is build , we start building the path using A star heuristic
                for pr in range(plot.shape[0]):
                    for pc in range(plot.shape[1]):
                        plot[pr, pc] = 1 if plot[pr, pc] != 15 else 2
                build_area_map[houseX - area[0]:houseX - area[0] + plot.shape[0],
                houseZ - area[1]: houseZ - area[1] + plot.shape[1]] = plot

                # creating intersection of a road
                intersections = np.where(build_area_map == 20)
                try:
                    nx = doors[0][0] + houseX
                    nz = doors[1][0] + houseZ

                except:
                    print("Door not found")
                    continue
                bestChoice = -1
                dist = 10000000
                for i in range(len(intersections[0])):
                    dist_test = pathfinder.aStarHeuristic(nx - area[0], nz - area[1], intersections[0][i],
                                                          intersections[1][i])
                    if dist_test < dist:
                        dist = dist_test
                        bestChoice = i
                try:

                    print(
                        f"A-Star: {nx - area[0]}, {nz - area[1]}, {intersections[0][bestChoice]}, {intersections[1][bestChoice]} ")
                    path = pathfinder.aStarSearch(build_area_map, nx - area[0], nz - area[1],
                                                  intersections[0][bestChoice],
                                                  intersections[1][bestChoice], heightmapGround)
                    build_area_map = pathfinder.drawPath(build_area_map, nx, nz, path, heightmapGround, worldSlice,
                                                         area[0], area[1])
                    iterationCount = iterationCount + 1

                except Exception:
                    print(traceback.format_exc())