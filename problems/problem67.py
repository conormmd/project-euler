from problems.problem18 import MaxPathSum

if __name__ == '__main__':
    path = 'C:/Users/Conor/PycharmProjects/project-euler/problems/files/'
    filename = '0067_triangle.txt'

    with open(f'{path}{filename}', 'r') as file:
        triangle = file.read()

    MaxPathSum(triangle)
