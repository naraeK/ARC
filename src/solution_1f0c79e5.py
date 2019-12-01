'''[CT5148] Assignment 3
Student Name: Narae Kim
Student ID: 19240062
'''

import sys
import json
import numpy as np
import codecs


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
        return output_grid.tolist()

    def printing_grid(self, result_grid):
        for r in result_grid:
            print(*r)
        print("\n\n")

    def testing_solve(self, json_file=""):
        if json_file == "":
            json_file = "output_1f0c79e5.json"
        train, test = self.split_json_into_train_test()
        train_dict_list = []
        for i in range(len(train)):
            train_dict = {}
            input_grid = train[i]["input"]
            train_dict['input'] = input_grid # json train input
            output_grid = train[i]["output"]
            result_grid = self.solve(input_grid)
            self.printing_grid(result_grid)
            train_dict['output'] = result_grid # json train output by solve function
            train_dict_list.append(train_dict)
        test_dict_list = []
        for j in range(len(test)):
            test_dict = {}
            test_input_grid = test[j]["input"]
            test_dict['input'] = test_input_grid
            test_output_grid = test[j]["output"]
            test_result_grid = self.solve(test_input_grid)
            self.printing_grid(test_result_grid)
            test_dict['output'] = test_result_grid
            test_dict_list.append(test_dict)
        json_dict = {'train': train_dict_list, 'test': test_dict_list}
        json.dump(json_dict, codecs.open(json_file, 'w', encoding='utf-8'), indent=None)





######################## Test #########################
if len(sys.argv) > 1:
    json1f0c79e5 = sys.argv[1]
else:
    json1f0c79e5 = "../data/training/1f0c79e5.json"

#output_json_file = "output.json"
# Create the object
solution = SolutionFor1f0c79e5(json1f0c79e5)
solution.testing_solve()#output_json_file)