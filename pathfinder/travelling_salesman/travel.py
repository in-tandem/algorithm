
'''

Lets use the dynamic programming model for solving travelling salesman problem

formula for the same is 

g(i, s) = min(  C(i,k) + g(k, s-{k})  ) for all k belonging to s.
where i is a starting point
C(i,k) is the cost of travelling from i to k

there are four nodes 1,2,3,4. we need to start from 1 and end in 1 . travelling every city once

the following are the costs of each:

1->2 = 10, 1->3 = 15, 1->4=20
2->3 = 35, 2->4 = 25, 2->1=10
3->2 = 35, 3->4 = 30, 3->1=15
4->3 = 30, 4->2 = 25, 4->1=20

we will use a matrix to denote the above notation. and similarly use indexing to get costs
to travel from point 1 to point 3 ,etc

'''

adjacency_matrix = [[]]
adjacency_matrix[0]= [0,10,15,20]
adjacency_matrix.append([10,0,35,25])
adjacency_matrix.append([15,35,0,30])
adjacency_matrix.append([20,25,30,0])

points = list(range(1,4+1))
print(points)

starting_point = 3

def cost_function(starting_point, points, end_point, sum_distance = 0):
    """

    :param points : sequence of other locations to be scanned, if length is one. means we can calc the distaince
    :param end_point : current end point. ie dist(starting_point, end_point). end_point is returned so we can show the path
    :param sum_distance: sum of cost of distance travelled so far
    """
 
    end_point = [] if end_point is None else end_point

    if len(points) == 1:
        sum_distance = sum_distance + adjacency_matrix[starting_point-1][points[0]-1]
        end_point.append(points[0])
        return sum_distance  ,end_point

    else:

        return min(map(lambda x :cost_function(starting_point,[x], end_point + [x],sum_distance) + \
                cost_function(x, [i for i in points if i !=x and i!= starting_point],end_point + [x],sum_distance),\
                 points))


cost_and_path = cost_function(1,[1,2,3,4],None)
print('shortest cost : ', sum(cost_and_path[::2])+ \
    adjacency_matrix[starting_point-1][cost_and_path[-1][-1]-1], \
        ' \n path: ', cost_and_path[-1])
final_node = cost_and_path[:-1][:-1]






