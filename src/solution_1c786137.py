'''[CT5148] Assignment 3
Student Name: Narae Kim
Student ID: 19240062
'''

import sys
import json
import numpy as np
import codecs


class SolutionFor1c786137:
    def __init__(self, filename):
        self.filename = filename

    def split_json_into_train_test(self):
        with open(self.filename) as file:
            input = json.load(file)
        train = input["train"]
        test = input["test"]
        return (train, test)

    def solve(self, input_grid):
        input_grid_copy = np.array(input_grid.copy())
        r_len, c_len = input_grid_copy.shape
        index_edge_check = np.zeros((r_len,c_len), dtype = int)
        output_grid = []
        for r_index in range(r_len): # check from 0 to r_len-1
            for c_index in range(c_len-1):
                # Checking left top edge
                if r_index != r_len-1 and input_grid_copy[r_index][c_index] == input_grid_copy[r_index][c_index + 1] == input_grid_copy[r_index + 1][c_index] != 0:
                    index_edge_check[r_index][c_index] = 11 * input_grid_copy[r_index][c_index]
                # Checking left bottom edge
                if r_index != r_len-1 and input_grid_copy[r_index+1][c_index] == input_grid_copy[r_index+1][c_index + 1] == input_grid_copy[r_index][c_index] != 0:
                    index_edge_check[r_index+1][c_index] = 111 * input_grid_copy[r_index][c_index]
                    continue
                # Checking if that continue from right to left
                if input_grid_copy[r_index][c_index+1] == (index_edge_check[r_index][c_index] % 10) != 0:
                    index_edge_check[r_index][c_index+1] = input_grid_copy[r_index][c_index+1]
                    # Checking right top edge
                    if r_index != r_len-1 and input_grid_copy[r_index][c_index+1] == input_grid_copy[r_index+1][c_index+1] != 0:
                        index_edge_check[r_index][c_index + 1] = -11 * input_grid_copy[r_index][c_index + 1]
                    # Checking right bottom edge
                    if r_index != 0 and input_grid_copy[r_index][c_index+1] == input_grid_copy[r_index-1][c_index+1] != 0:
                        index_edge_check[r_index][c_index + 1] = -111 * input_grid_copy[r_index][c_index + 1]
                        righttop = np.argwhere(index_edge_check == -11 * input_grid_copy[r_index][c_index + 1])
                        rightbottom_row = r_index
                        rightbottom_col = c_index + 1
                        if len(righttop) != 0:
                            [[lefttop_row, lefttop_col]] = np.argwhere(index_edge_check == 11 * input_grid_copy[r_index][c_index + 1])
                            # add if righttopcol == rightbottomcol
                            output_grid = input_grid_copy[lefttop_row+1:rightbottom_row,lefttop_col+1:rightbottom_col] # remove the frame
                    continue
        return output_grid.tolist()

    def printing_grid(self, result_grid):
        for r in result_grid:
            print(*r)
        print("\n\n")

    def testing_solve(self, json_file=""):
        if json_file == "":
            json_file = "output_1c786137.json"
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
    json1c786137 = sys.argv[1]
else:
    json1c786137 = "../data/training/1c786137.json"

# Create the object
solution = SolutionFor1c786137(json1c786137)
solution.testing_solve()