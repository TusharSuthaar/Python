#!/usr/bin/env python3
"""
Tuple vs List Comparison - Demonstrate differences between tuples and lists
"""

import sys
import time

def demonstrate_tuple_vs_list():
    """Demonstrate the differences between tuples and lists"""
    print("=== Tuple vs List Comparison ===")
    
    # 1. Basic differences table
    print("\n1. Basic Differences:")
    print("-" * 60)
    print(f"{'Feature':<15} {'Tuple':<20} {'List':<20}")
    print("-" * 60)
    print(f"{'Mutability':<15} {'Immutable':<20} {'Mutable':<20}")
    print(f"{'Syntax':<15} {'()':<20} {'[]':<20}")
    print(f"{'Performance':<15} {'Faster':<20} {'Slower':<20}")
    print(f"{'Use Case':<15} {'Fixed Data':<20} {'Dynamic Data':<20}")
    print(f"{'Memory Usage':<15} {'Less':<20} {'More':<20}")
    print("-" * 60)
    
    # 2. Practical examples
    print("\n2. Practical Examples:")
    
    # Create examples
    my_tuple = (1, 2, 3, 4, 5)
    my_list = [1, 2, 3, 4, 5]
    
    print(f"Tuple: {my_tuple}")
    print(f"List:  {my_list}")
    
    # 3. Memory usage comparison
    print("\n3. Memory Usage:")
    tuple_size = sys.getsizeof(my_tuple)
    list_size = sys.getsizeof(my_list)
    print(f"Tuple memory: {tuple_size} bytes")
    print(f"List memory:  {list_size} bytes")
    print(f"Difference:   {list_size - tuple_size} bytes ({((list_size/tuple_size - 1) * 100):.1f}% more for list)")
    
    # 4. Performance comparison
    print("\n4. Performance Comparison:")
    
    # Tuple creation time
    start_time = time.time()
    for _ in range(100000):
        temp_tuple = (1, 2, 3, 4, 5)
    tuple_time = time.time() - start_time
    
    # List creation time
    start_time = time.time()
    for _ in range(100000):
        temp_list = [1, 2, 3, 4, 5]
    list_time = time.time() - start_time
    
    print(f"Tuple creation time: {tuple_time:.6f} seconds")
    print(f"List creation time:  {list_time:.6f} seconds")
    print(f"Tuple is {(list_time/tuple_time):.2f}x faster for creation")
    
    # 5. Mutability demonstration
    print("\n5. Mutability Demonstration:")
    
    print("Trying to modify tuple...")
    try:
        my_tuple[0] = 10
    except TypeError as e:
        print(f"❌ Error: {e}")
    
    print("Trying to modify list...")
    try:
        my_list[0] = 10
        print(f"✅ Success: List modified to {my_list}")
    except Exception as e:
        print(f"❌ Error: {e}")
    
    # 6. Use cases
    print("\n6. When to Use Each:")
    print("Use Tuples for:")
    print("  - Fixed data that won't change (coordinates, RGB values)")
    print("  - Dictionary keys (tuples are hashable)")
    print("  - Function returns with multiple values")
    print("  - Configuration settings")
    
    print("\nUse Lists for:")
    print("  - Data that needs to be modified")
    print("  - Adding/removing elements")
    print("  - Sorting operations")
    print("  - Dynamic collections")

if __name__ == "__main__":
    demonstrate_tuple_vs_list() 