"""
Manual trace of selection sort to understand where it gets stuck.
"""

import random


def trace_selection_sort(initial_values, max_timesteps=5):
    """Trace through selection sort step by step"""
    n = len(initial_values)
    values = initial_values.copy()
    ideal_pos = [0 for _ in range(n)]

    print(f"Initial: values={values}, ideal_pos={ideal_pos}\n")

    for timestep in range(max_timesteps):
        print(f"{'='*70}")
        print(f"TIMESTEP {timestep}")
        print(f"{'='*70}")
        print(f"Start: values={values}, ideal_pos={ideal_pos}\n")

        idx_order = list(range(n))
        random.seed(42 + timestep)
        random.shuffle(idx_order)
        print(f"Processing order: {idx_order}\n")

        swapped_any = False

        for idx in idx_order:
            cell_value = values[idx]
            target = max(0, min(n - 1, ideal_pos[idx]))

            print(f"  Process idx={idx} (value={cell_value}, wants position {ideal_pos[idx]})")

            if target == idx:
                print(f"    -> target==idx, increment ideal_pos[{idx}] to {ideal_pos[idx] + 1}")
                ideal_pos[idx] = min(n - 1, ideal_pos[idx] + 1)
                continue

            neighbor_value = values[target]
            print(f"    -> Compare with position {target} (value={neighbor_value})")
            print(f"    -> Is {cell_value} < {neighbor_value}?", end=" ")

            if cell_value < neighbor_value:
                print("YES! Swap")
                values[idx], values[target] = values[target], values[idx]
                ideal_pos[idx], ideal_pos[target] = ideal_pos[target], ideal_pos[idx]
                swapped_any = True
                print(f"    -> After swap: values={values}")
                print(f"    -> After swap: ideal_pos={ideal_pos}")
            else:
                print("NO, increment ideal_pos")
                ideal_pos[idx] = min(n - 1, ideal_pos[idx] + 1)
                print(f"    -> ideal_pos[{idx}] = {ideal_pos[idx]}")

        print(f"\nEnd of timestep: values={values}")
        print(f"End of timestep: ideal_pos={ideal_pos}")
        print(f"swapped_any={swapped_any}\n")

        if not swapped_any:
            print("No swaps this timestep - algorithm terminates")
            break

    return values


# Test
test_array = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Test array: {test_array}")
print(f"Expected:   {sorted(test_array)}")
print(f"\n{'='*70}\n")

result = trace_selection_sort(test_array, max_timesteps=10)

print(f"\n{'='*70}")
print(f"FINAL RESULT:")
print(f"Result:   {result}")
print(f"Expected: {sorted(test_array)}")
print(f"Correct:  {result == sorted(test_array)}")
