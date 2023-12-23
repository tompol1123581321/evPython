
def handle_possible_collision(current_position,step_velocity,MIN,MAX):
    new_position = current_position
    for (i,value) in  enumerate(current_position):
        possible_new_value =  value + step_velocity[i]
 
        is_possible_value_ok = possible_new_value <= MAX and possible_new_value >= MIN
        is_possible_value_low = possible_new_value < MIN
        is_possible_value_heigh = possible_new_value > MAX
        
        if is_possible_value_ok:
            new_position[i] = possible_new_value
        elif is_possible_value_heigh:
            overflow =  possible_new_value - MAX
            new_position[i] = MAX - overflow
        elif is_possible_value_low:
            overflow = MIN - possible_new_value
            new_position[i] = MIN + overflow

    return new_position