playing_field = [[' - ' for j in range(3)] for i in range(3)]

step = 0
char = 'x'

def field():
    """Displays the playing field"""
    print('   0  1  2')
    for i, row in enumerate(playing_field):
        print(i, end=' ')
        print(''.join(row))
    return row

def win_check():
    """Checks the playing field for a win"""
    row_temp = []
    count = [0, 0, 0]
    
    if (((playing_field[0][0] == playing_field[1][1] == playing_field[2][2]) or \
       (playing_field[2][0] == playing_field[1][1] == playing_field[0][2])) and playing_field[1][1] != ' - '):
            return True
    
    for row in playing_field:
        if len(set(row)) == 1 and ' - ' not in row:
            return True
            
        if not row_temp:
                row_temp = row
        else: 
            column_index = 0       
            while column_index < len(row):
                if row_temp[column_index] == row[column_index] and row_temp[column_index] != ' - ':
                    count[column_index] += 1
                column_index += 1                
                    
    for col_sum in count:        
        if col_sum == 2:
            return True
            
    return False
    
while ' - ' in field():
    """Main game loop"""
    row_input = input(f'Enter the row number for player {char} (from 0 to 2): ')
    column_input = input(f'Enter the column number for player {char} (from 0 to 2): ')
    
    if row_input in ['0', '1', '2'] and column_input in ['0', '1', '2']:
        if playing_field[int(row_input)][int(column_input)] != ' - ':
            print('Occupied!')
        else:
            playing_field[int(row_input)][int(column_input)] = f' {char} ' 
            
            if win_check():
                field()
                print(f'Player {char} wins!')
                break 
            else:
                if step == 8:
                    field()
                    print('Draw!')
                    break
            
            step += 1
            char = 'o'
                       
    else:
        print('Input error. Please try again.')
    
    if step > 1:
        step = 0
        char = 'x'
        
        
    

