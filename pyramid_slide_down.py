def longest_path(pyramid):
    #gradually fill the best paths from bottom to top
    best_paths = [[0 for i in range(len(pyramid)-1)] for i in range(len(pyramid)-1)]
    def minipath(l,a): #solution for a two floor pyramid
        return a + max(l[0],l[1])
    for f in range(len(pyramid)-1,0,-1): #from the last floor to the top
        for b in range(len(pyramid[f])-1): #iterating through bricks
            l = [pyramid[f][b],pyramid[f][b+1]]
            a = pyramid[f-1][b]
            best_paths[f-1][b] = minipath(l,a) #populate floor of the new pyramid with sums
            pyramid[f-1][b] = best_paths[f-1][b] #update parameter
    return best_paths[0][0]





'''TESTS'''
pyramid_test = [[3],[7,4],[2,4,6],[8,5,9,3]]
print(longest_path(pyramid_test))
