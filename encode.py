def convert_hex_to_binary(hex_string):
    # Validate if the input is a hexadecimal string
    try:
        int(hex_string, 16)
    except ValueError:
        raise ValueError(f"Invalid input: {hex_string} is not a hexadecimal string.")
    
    # Convert hex string to binary string
    binary_string = bin(int(hex_string, 16))[2:].zfill(len(hex_string) * 4)
    return binary_string

def break_binary_string(binary_string):
    # Validate if the input is a binary string
    if not all(char in '01' for char in binary_string):
        raise ValueError(f"Invalid input: {binary_string} is not a binary string.")
    
    output = []
    current_char = binary_string[0]
    current_segment = current_char
    
    for i in range(1, len(binary_string)):
        if binary_string[i] == current_char:
            current_segment += binary_string[i]
        else:
            output.append(current_segment)
            current_char = binary_string[i]
            current_segment = current_char
    
    # Append the last segment
    output.append(current_segment)
    
    return output

def calculate_rf_raw(binary_signal_array, sample_rate, repeat):
    rf_raw_signal = []
    
    for line in binary_signal_array:
        length = len(line)
        if line[0] == '1':
            rf_raw_signal.append(str(length * sample_rate))
        else:
            rf_raw_signal.append(str(length * -sample_rate))
    
    # Repeat the signal if necessary
    if repeat:
        rf_raw_signal *= repeat
    
    rf_raw_string = "[" + ', '.join(rf_raw_signal) + "]"
    return rf_raw_string

def convert_hex_to_esphome_raw(hex_string, sample_rate, repeat):
    # Step 1: Convert Hex String to Binary String
    binary_string = convert_hex_to_binary(hex_string)
    #print(f"BinaryString: {binary_string}")
    
    # Step 2: Break the Binary String
    binary_array = break_binary_string(binary_string)
    
    # Step 3: Calculate RF Raw
    rf_raw_string = calculate_rf_raw(binary_array, sample_rate, repeat)
    return rf_raw_string

# Example usage:
hex_string = "e8eeee88ee888ee88e8e8e8ee8e8e80000"
sample_rate = 60
repeat = 0

result = convert_hex_to_esphome_raw(hex_string, sample_rate, repeat)
print(result)
