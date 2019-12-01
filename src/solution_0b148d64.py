'''[CT5148] Assignment 3
Student Name: Narae Kim
Student ID: 19240062
'''

import sys
import json
import codecs

# test with other data. I will need "if color not exist"


class SolutionFor0b148d64:
    def __init__(self, filename):
        self.filename = filename

    def split_json_into_train_test(self):
        with open(self.filename) as file:
            input = json.load(file)
        train = input["train"]
        test = input["test"]
        return (train, test)

    def solve(self, input_grid):
        firstline_numbers = set(input_grid[0])
        lastline_numbers = set(input_grid[-1])
        if len(firstline_numbers) > len(lastline_numbers):
            color = firstline_numbers.difference(lastline_numbers)
            not_this_color = firstline_numbers.difference(color, {0}).pop()
            color = color.pop()
        else:
            color = lastline_numbers.difference(firstline_numbers)
            not_this_color = lastline_numbers.difference(color, {0}).pop()
            color = color.pop()
        output_grid = []
        max_index = 0
        min_index = len(input_grid[0])
        for input in input_grid:
            input_numbers = set(input)
            if len(input_numbers) == 3:
                color_index = input.index(color)
                not_this_color_index = input.index(not_this_color)
                if color_index < not_this_color_index:
                    max_color_index = max([i for i, x in enumerate(input) if x == color])
                    max_index = max(max_index, max_color_index)
                else:
                    min_index = min(min_index, color_index)
        for input_iter in input_grid:
            input_numbers = set(input_iter)
            if len(input_numbers) == 3:
                if color_index < not_this_color_index:
                    output_grid.append(input_iter[:max_index+1])
                else:
                    output_grid.append(input_iter[min_index:])
        return output_grid

    def printing_grid(self, result_grid):
        for r in result_grid:
            print(*r)
        print("\n\n")

    def testing_solve(self, json_file=""):
        if json_file == "":
            json_file = "output_0b148d64.json"
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
    json0b148d64 = sys.argv[1]
else:
    json0b148d64 = "../data/training/0b148d64.json"

# Create the object
solution = SolutionFor0b148d64(json0b148d64)
solution.testing_solve()

