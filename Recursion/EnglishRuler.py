"""Tick label argument starts empty unless we want to label each ticket with a value"""
def draw_line(tick_length, tick_label=''):  #draws a single tick with specified number of dashes and a label is used
    line= '-'* tick_length # this line will contain "-" amount of ticks that we want tick_length=3 -> ---
    if tick_label:
        line+= ' ' + tick_label # if there is a tick label attach to dash 
    print(line)

"""This function draws the sequence of minor ticks within some interval
based upon the length of the interval's central tick"""
def draw_interval(center_length):
    if center_length > 0: #stop when length drops to 0
        draw_interval(center_length -1 ) #recursively draw top ticks
        draw_line(center_length) #draw center tick
        draw_interval(center_length -1 ) #recursively draw bottom ticks



"""This function manages the construction of the ruler and the major tick length """
def draw_ruler(num_inches, major_length):
    """Draw english ruler based upon a central tick length"""
    draw_line(major_length, '0') #first line to be drawn -> inch 0 line 
    for j in range(1, 1+num_inches):
        draw_interval(major_length-1)
        draw_line(major_length, str(j))

draw_ruler(10, 3)