import aocd
input = aocd.get_data(day=24, year=2024)

# input = """x00: 1
# x01: 1
# x02: 1
# y00: 0
# y01: 1
# y02: 0

# x00 AND y00 -> z00
# x01 XOR y01 -> z01
# x02 OR y02 -> z02"""

# input = """x00: 1
# x01: 0
# x02: 1
# x03: 1
# x04: 0
# y00: 1
# y01: 1
# y02: 1
# y03: 1
# y04: 1

# ntg XOR fgs -> mjb
# y02 OR x01 -> tnw
# kwq OR kpj -> z05
# x00 OR x03 -> fst
# tgd XOR rvg -> z01
# vdt OR tnw -> bfw
# bfw AND frj -> z10
# ffh OR nrd -> bqk
# y00 AND y03 -> djm
# y03 OR y00 -> psh
# bqk OR frj -> z08
# tnw OR fst -> frj
# gnj AND tgd -> z11
# bfw XOR mjb -> z00
# x03 OR x00 -> vdt
# gnj AND wpb -> z02
# x04 AND y00 -> kjc
# djm OR pbm -> qhw
# nrd AND vdt -> hwm
# kjc AND fst -> rvg
# y04 OR y02 -> fgs
# y01 AND x02 -> pbm
# ntg OR kjc -> kwq
# psh XOR fgs -> tgd
# qhw XOR tgd -> z09
# pbm OR djm -> kpj
# x03 XOR y03 -> ffh
# x00 XOR y04 -> ntg
# bfw OR bqk -> z06
# nrd XOR fgs -> wpb
# frj XOR qhw -> z04
# bqk OR frj -> z07
# y03 OR x01 -> nrd
# hwm AND bqk -> z03
# tgd XOR rvg -> z12
# tnw OR pbm -> gnj"""

### Part 1 - Straightforward simulation 
start_vals, gates = input.split("\n\n")
wires = set()

import re
def parse(input):
    initial_values = {}
    gates = []

    for line in input.splitlines():
        if ":" in line:  # initial wire value
            wire, value = line.split(": ")
            initial_values[wire] = int(value)
        elif "->" in line:  # gate connection
            gates.append(line)

    return initial_values, gates

def run_gate(gate, wire_values):
    match = re.match(r"(.+) -> (\w+)", gate)
    if not match:
        raise ValueError(f"Invalid gate syntax: {gate}")

    expression, output_wire = match.groups()
    tokens = expression.split()

    if len(tokens) == 3:
        left, op, right = tokens
        if left.isdigit():
            left_val = int(left)
        elif left in wire_values:
            left_val = wire_values[left]
        else:
            return None

        if right.isdigit():
            right_val = int(right)
        elif right in wire_values:
            right_val = wire_values[right]
        else:
            return None

        if op == "AND":
            return output_wire, left_val & right_val
        elif op == "OR":
            return output_wire, left_val | right_val
        elif op == "XOR":
            return output_wire, left_val ^ right_val

    return None

def simulate(initial_values, gates):
    wire_values = initial_values.copy()
    remaining_gates = gates[:]

    while remaining_gates:
        for gate in remaining_gates[:]:
            result = run_gate(gate, wire_values)
            if result:
                output_wire, value = result
                wire_values[output_wire] = value
                remaining_gates.remove(gate)
    return wire_values

def calculate_output(wire_values):
    z_wires = {k: v for k, v in wire_values.items() if k.startswith('z')}
    # print(z_wires)
    binary_number = "".join(str(z_wires[f"z{str(i).zfill(2)}"]) for i in range(len(z_wires)))[::-1]
    return int(binary_number, 2), binary_number

initial_values, gates = parse(input)
wire_values = simulate(initial_values, gates)
decimal_z, binary_z = calculate_output(wire_values)

print(decimal_z)
print("===")
### Part 2 - I did this mostly manually.
# First I generated a visualisation of the circuit graph to see the structure of the circuit.
# Then, I extracted the position of bit differences between the expected and actual
# Finally, I proceeded to inspect only those regions of the circuit to find the swapped wires.
# This is not full proof for the general case where the swaps could be overlapping - I needed to test the circuit on multiple inputs to be sure.
# However, an improvement that could be done to check for functional equivalence is to use a SAT solver like z3 to check if the two circuits are equivalent.
import networkx as nx
def get_circuit_graph(gates):
    G = nx.DiGraph()

    for gate in gates:
        match = re.match(r"(.+) -> (\w+)", gate)
        if not match:
            raise ValueError(f"Invalid gate syntax: {gate}")

        expression, output_wire = match.groups()
        tokens = expression.split()

        if len(tokens) == 1:
            input_wire = tokens[0]
            G.add_edge(input_wire, output_wire)
        elif len(tokens) == 3:
            left, op, right = tokens
            G.add_edge(left, output_wire, label = op)
            G.add_edge(right, output_wire, label = op)

    return G

def get_decimal_initial_values(wire_values):
    x_wires = {k: v for k, v in wire_values.items() if k.startswith('x')}
    y_wires = {k: v for k, v in wire_values.items() if k.startswith('y')}

    x_binary = "".join(str(x_wires[f"x{str(i).zfill(2)}"]) for i in range(len(x_wires)))[::-1]
    y_binary = "".join(str(y_wires[f"y{str(i).zfill(2)}"]) for i in range(len(y_wires)))[::-1]
    
    return x_binary, y_binary

def binary_addition(x, y):
    max_len = max(len(x), len(y))
    if len(x) == len(y):
        max_len += 1
    x = x.zfill(max_len)
    y = y.zfill(max_len)
    carry = 0
    result = ""
    for i in range(max_len-1, -1, -1):
        bit_sum = int(x[i]) + int(y[i]) + carry
        result = str(bit_sum % 2) + result
        carry = bit_sum // 2
    # prune leading zeros
    result = result.lstrip("0")
    return result

def bit_diff(x, y):
    max_len = max(len(x), len(y))
    x = x.zfill(max_len)
    y = y.zfill(max_len)

    diff = []
    x = x[::-1] # lsb first
    y = y[::-1]
    for i in range(max_len):
        if x[i] != y[i]:
            print(f"{i}: {x[i], y[i]}")
            diff.append((i, x[i], y[i]))
    return diff

graph = get_circuit_graph(gates)
# visualization
nx.nx_agraph.write_dot(graph, "./coziyu/day24/circuit.dot")

expected_z = binary_addition(get_decimal_initial_values(wire_values)[0], get_decimal_initial_values(wire_values)[1])
print(expected_z)
print(binary_z)
bit_diff(expected_z, binary_z)
    
# By inspection, the following gate outputs are swapped:
# x15 xor y15 -> jgt
# x15 and y15 -> mht
# --
# dpr and nvv -> z30
# dpr xor nvv -> nbf
# --
# tsw xor wwm -> hdt 
# rnk or  mkq -> z05 
# --
# x09 and y09 -> z09 
# vkd xor wqr -> gbf 
swapped_wires = ["jgt", "mht", "z30", "nbf", "hdt", "z05", "z09", "gbf"]

print(",".join(sorted(swapped_wires)))