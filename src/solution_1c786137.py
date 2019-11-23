import json
import numpy as np


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
        #print(input_grid_copy)
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
        #print(output_grid,"\n\n")
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
json1c786137 = "../data/training/1c786137.json"
# Create the object
solution = SolutionFor1c786137(json1c786137)
solution.testing_solve()