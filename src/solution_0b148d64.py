import json

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
            print("TESTINP", output_grid)
            result_grid = self.solve(input_grid)
            print("TESTOUT",result_grid)

    # def list_to_json




######################## Test #########################
json0b148d64 = "../data/training/0b148d64.json"
# Create the object
solution = SolutionFor0b148d64(json0b148d64)
solution.testing_solve()

