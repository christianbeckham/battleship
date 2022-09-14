class Board:
    def __init__(self):
        self.dimensions = 10
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.grid = None
        self.rows = None
        self.columns = None
        self.create_board()

    def create_board(self):
        self.create_grid()
        self.create_list_of_row_names()
        self.create_list_of_column_names()

    def display(self):
        layout = ''
        layout += self.create_header()
        for row_index, row in enumerate(self.grid):
            layout += '\n'
            formatted_row_letter = f'[{self.alphabet[row_index].upper()}]'
            layout += formatted_row_letter
            for col in row:
                layout += f" {col['label']}"
        layout += '\n'
        print(layout)

    def create_header(self):
        placeholder = '\n[-]'
        for number in range(1, self.dimensions + 1):
            placeholder += f'[{number}]'
        return placeholder

    def update(self, cell, value):
        for row in self.grid:
            for item in row:
                if item['name'] == cell:
                    item['label'] = value

    def create_grid(self):
        '''Set the grid instance variable of the class to a multi-dimensional list of dictionaries for each cell.

        Each dictionary contains the name of the cell, the index position, and a label used to display in the console.

        Args:
            None

        Returns:
            None
        '''
        map = []
        for row in range(0, self.dimensions):
            row_of_cells = []
            row_letter = self.alphabet[row]
            for col in range(0, self.dimensions):
                column_number = col + 1
                cell = {
                    'name': f'{row_letter}{column_number}',
                    'index': [row, col],
                    'label': '🟦'
                }
                row_of_cells.append(cell)
            map.append(row_of_cells)
        self.grid = map

    def create_list_of_row_names(self):
        '''Creates a multi-dimensional list where inner-lists contain the cell names by row.

        This list is used to check if the ship is placed in a row.
        Example: [['a1', 'a2', 'a3'...], ['b1', 'b2', 'b3'...], ['c1', 'c2', 'c3']]

        Args:
            None

        Returns:
            None
        '''
        rows_list = []
        for row in self.grid:
            sub_list = []
            for item in row:
                sub_list.append(item['name'])
            rows_list.append(sub_list)
        self.rows = rows_list

    def create_list_of_column_names(self):
        '''Creates a multi-dimensional list where inner-lists contain the cell names by column.

        This list is used to check if the ship is placed in a column.
        Example: [['a1', 'b1', 'c1'...], ['a2', 'b2', 'c2'...], ['a3', 'b3', 'c3']]

        Args:
            None

        Returns:
            None
        '''
        columns_list = []
        for row in zip(*self.grid):
            sub_list = []
            for item in row:
                sub_list.append(item['name'])
            columns_list.append(sub_list)
        self.columns = columns_list
