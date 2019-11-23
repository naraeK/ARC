import sys
import json
import numpy as np


class SolutionFor1f0c79e5:
    def __init__(self, filename):
        self.filename = filename

    def split_json_into_train_test(self):
        with open(self.filename) as file:
            input = json.load(file)
        train = input["train"]
        test = input["test"]
        return (train, test)

    def defining_indices(self, row_index, col_index, isleft=True, istop=True):
        if isleft:
            col_stop = -1
            col_step = -1
        else:
            col_stop = self.c_end
            col_step = 1
        if istop:
            row_stop = -1
            row_step = -1
        else:
            row_stop = self.r_end
            row_step = 1

        row_indices = []
        for r_index in range(row_index, row_stop, row_step):
            row_indices.append(r_index + row_step)
            row_indices.append(r_index + row_step)
            row_indices.append(r_index)
            row_indices.append(r_index)
        col_indices = []
        for c_index in range(col_index, col_stop, col_step):
            col_indices.append(c_index + col_step)  # .append(c_index+1).append(c_index).append(c_index+1)
            col_indices.append(c_index)
            col_indices.append(c_index + col_step)
            col_indices.append(c_index)
        return row_indices, col_indices

    def solve(self, input_grid):
        input_grid_copy = np.array(input_grid.copy())
        #print(input_grid_copy)
        [color] = [c for c in np.unique(input_grid_copy) if c != 0 and c != 2]
        self.r_end, self.c_end = input_grid_copy.shape
        nonzero_indices = np.where(input_grid_copy != 0)
        box_indices = list(zip(nonzero_indices[0], nonzero_indices[1]))
        islefttop = (input_grid_copy[box_indices[0]] == 2)
        isrighttop = (input_grid_copy[box_indices[1]] == 2)
        isleftbottom = (input_grid_copy[box_indices[2]] == 2)
        isrightbottom = (input_grid_copy[box_indices[3]] == 2)
        output_grid = input_grid_copy.copy()

        if islefttop:
            rightbottom_row, rightbottom_col = box_indices[3]
            row_indices, col_indices = self.defining_indices(rightbottom_row, rightbottom_col, True, True)
            for r, c in zip(row_indices, col_indices):
                if r >= 0 and c >= 0:
                    output_grid[r,c] = color
        if isrighttop:
            leftbottom_row, leftbottom_col = box_indices[2]
            row_indices, col_indices = self.defining_indices(leftbottom_row, leftbottom_col, False, True)
            for r, c in zip(row_indices, col_indices):
                if r >= 0 and c < self.c_end:
                    output_grid[r,c] = color
        if isleftbottom:
            righttop_row, righttop_col = box_indices[1]
            row_indices, col_indices = self.defining_indices(righttop_row, righttop_col, True, False)
            for r, c in zip(row_indices, col_indices):
                if r >= 0 and c >= 0:
                    output_grid[r, c] = color
        if isrightbottom:
            lefttop_row, lefttop_col = box_indices[0]
            row_indices, col_indices = self.defining_indices(lefttop_row, lefttop_col, False, False)
            for r, c in zip(row_indices, col_indices):
                if r >= 0 and c < self.c_end:
                    output_grid[r, c] = color
        #print(output_grid)
        return output_grid.tolist()

    def testing_solve(self):
        train, test = self.split_json_into_train_test()
        for i in range(len(train)):
            input_grid = train[i]["input"]
            output_grid = train[i]["output"]
            print("REALOU", output_grid)
            result_grid = self.solve(input_grid)
            print("RESULT",result_grid)
        for j in range(len(test)):
            test_input_grid = test[j]["input"]
            test_output_grid = test[j]["output"]
            print("TESTOUT", test_output_grid)
            test_result_grid = self.solve(test_input_grid)
            print("TESTRES",test_result_grid)

    # def list_to_json




######################## Test #########################
if len(sys.argv) > 1:
    json1f0c79e5 = sys.argv[1]
else:
    json1f0c79e5 = "../data/training/1f0c79e5.json"

# Create the object
solution = SolutionFor1f0c79e5(json1f0c79e5)
solution.testing_solve()