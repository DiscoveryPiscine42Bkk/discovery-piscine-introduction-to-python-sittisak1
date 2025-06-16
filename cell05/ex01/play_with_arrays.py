#!/usr/bin/env python3

def main():
    original = [2, 8, 9, 48, 8, 22, -12, 2]
    new = [x + 2 for x in original]
    
    print("Original array:", original)
    print("New array:", new)

if __name__ == "__main__":
    main()
