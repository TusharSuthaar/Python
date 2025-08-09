#!/usr/bin/env python3
"""
RAM Monitor - Check system memory usage
"""

import psutil

def get_ram_info():
    """Get and display RAM information"""
    mem = psutil.virtual_memory()
    
    print("=== RAM Information ===")
    print(f"Total: {mem.total / (1024**3):.2f} GB")
    print(f"Available: {mem.available / (1024**3):.2f} GB")
    print(f"Used: {mem.used / (1024**3):.2f} GB")
    print(f"Percentage Used: {mem.percent}%")
    print(f"Free: {mem.free / (1024**3):.2f} GB")

if __name__ == "__main__":
    get_ram_info() 