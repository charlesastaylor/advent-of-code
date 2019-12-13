INSTRUCTION_LENGTH = {1: 4, 2: 4, 3: 2, 4: 2, 5: 3, 6: 3, 7: 4, 8: 4, 9: 2}

def intcode(data, debug=False, prompt_for_input=False):
    """Second iteration of intcode program as a generator that uses yield for input/output"""
    # Variables
    i = 0
    relative_base = 0
    data = {i: data[i] for i in range(len(data))} # to allow expandable memory

    if debug:
        prev = data.copy()
        prev_rel_base = relative_base
    while i < len(data):
        # flags
        pointer_set = False
        # parse first position of instrcution for opcode and param modes
        first = str(data[i])
        op = int(first[-2:])
        if op == 99:
            break
        # Paramaters. 0 - position, 1 - immediate, 2- relative
        param_modes = first[:-2]
        param_modes = "0" * (INSTRUCTION_LENGTH[op] - 1 - len(param_modes)) + param_modes
        param_modes = param_modes[::-1]
        # collect paramaters based on mode
        param_addrs = [] # store addresses not actual values
        for j, p in enumerate(param_modes):
            if p == "0":
                param_addrs.append(data.get(i + j + 1, 0))
            elif p == "1":
                param_addrs.append(i + j + 1)
            elif p == "2":
                param_addrs.append(data.get(i + j + 1, 0) + relative_base)
        params = [data.get(addr, 0) for addr in param_addrs] # for backwards compatible
        # execute commands
        if op == 1:
            data[param_addrs[2]] = params[0] + params[1]
        elif op == 2:
            data[param_addrs[2]] = params[0] * params[1]
        elif op == 3:
            if prompt_for_input:
                # print("Expecting input")
                yield None
            data[param_addrs[0]] = yield
        elif op == 4:
            yield params[0]
        elif op == 5:
            if params[0] != 0:
                i = params[1]
                pointer_set = True
        elif op == 6:
            if params[0] == 0:
                i = params[1]
                pointer_set = True
        elif op == 7:
            data[param_addrs[2]] = 1 if params[0] < params[1]  else 0
        elif op == 8:
            data[param_addrs[2]] = 1 if params[0] == params[1]  else 0
        elif op == 9:
            relative_base += params[0]
        else:
            print(f"Unrecognized opcode: {op}")
        
        if debug:
            # print(data)
            print(f'Op: {op}, Instruction: {[data[j] for j in range(i, i+INSTRUCTION_LENGTH[op])]}, modes: {param_modes}, params: {params}')
            for idx in data:
                if data[idx] != prev.get(idx, 0):
                    print(f'Entry at index {idx} changed from {prev.get(idx, 0)} to {data[idx]}')
            if relative_base != prev_rel_base:
                print(f'Relative base changed from {prev_rel_base} to {relative_base}')
            prev = data.copy()
            prev_rel_base = relative_base
        if not pointer_set:
            i += INSTRUCTION_LENGTH[op]
    return None

def memory_dump(data):
    s = ""
    for i, val in enumerate(data):
        s += f'{i}: {val}  -  '
        if i % 10 == 0 and i != 0:
            s += '\n'
    return s

def tadd(a, b):
    return tuple(sum(x) for x in zip(a,b))

def _intcode(data, debug=False):
    """First iteration of intcode program that used stdin/out for input/output"""
    i = 0
    if debug:
        prev = data[:]
    while i < len(data):
        # flags
        pointer_set = False
        # parse first position of instrcution for opcode and param modes
        first = str(data[i])
        op = int(first[-2:])
        if op == 99:
            break
        param_modes = first[:-2]
        param_modes = "0" * (INSTRUCTION_LENGTH[op] - 1 - len(param_modes)) + param_modes
        param_modes = param_modes[::-1]
        # collect paramaters based on mode
        params = []
        for j, p in enumerate(param_modes):
            params.append(data[data[i + j + 1]] if p == "0" else data[i + j + 1])
        # execute commands
        if op == 1:
            data[data[i + 3]] = params[0] + params[1]
        elif op == 2:
            data[data[i + 3]] = params[0] * params[1]
        elif op == 3:
            data[data[i + 1]] = int(input("Opcode 3 input required > "))
        elif op == 4:
            print(f'Opcode 4 output: {params[0]}')
        elif op == 5:
            if params[0] != 0:
                i = params[1]
                pointer_set = True
        elif op == 6:
            if params[0] == 0:
                i = params[1]
                pointer_set = True
        elif op == 7:
            data[data[i + 3]] = 1 if params[0] < params[1]  else 0
        elif op == 8:
            data[data[i + 3]] = 1 if params[0] == params[1]  else 0
        else:
            print(f"Unrecognized opcode: {op}")
        if debug:
            print(f'Op: {op}, Instruction: {data[i:i+INSTRUCTION_LENGTH[op]]}, modes: {param_modes}, params: {params}')
            for j, x in enumerate(data):
                if x != prev[j]:
                    print(f'Entry at index {j} changed from {prev[j]} to {x}')
            prev = data[:]
        if not pointer_set:
            i += INSTRUCTION_LENGTH[op]
    return None
