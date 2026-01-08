import numpy as np

class DataAnalytics:
    def __init__(self):
        self.arr = None

    # 1. Create Array
    def create_array(self):
        print("\nSelect the type of array to create:")
        print("1. 1D Array\n2. 2D Array")
        ch = int(input("Enter choice: "))

        if ch == 1:
            size = int(input("Enter size: "))
            elements = list(map(int, input("Enter elements: ").split()))
            self.arr = np.array(elements[:size])

        elif ch == 2:
            r = int(input("Rows: "))
            c = int(input("Cols: "))
            elements = list(map(int, input(f"Enter {r*c} elements: ").split()))
            self.arr = np.array(elements).reshape(r, c)

        print("\nArray Created:\n", self.arr)

    # 2. Mathematical Operations
    def math_ops(self):
        if self.arr is None:
            print("Create array first!")
            return

        print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide")
        op = int(input("Enter choice: "))

        arr2 = np.array(list(map(int, input("Enter equal size elements: ").split())))
        arr2 = arr2.reshape(self.arr.shape)

        if op == 1:
            print("\nResult:\n", self.arr + arr2)
        elif op == 2:
            print("\nResult:\n", self.arr - arr2)
        elif op == 3:
            print("\nResult:\n", self.arr * arr2)
        elif op == 4:
            print("\nResult:\n", self.arr / arr2)

    # 3. Combine / Split
    def combine_split(self):
        print("\n1. Combine Arrays\n2. Split Array")
        op = int(input("Enter choice: "))

        if op == 1:
            elements = list(map(int, input("Enter elements of 2nd array: ").split()))
            arr2 = np.array(elements).reshape(self.arr.shape)
            print("\nCombined:\n", np.vstack((self.arr, arr2)))

        elif op == 2:
            print("\nSplit result:\n", np.vsplit(self.arr, len(self.arr)))

    # 4. Search, Sort, Filter
    def search_sort_filter(self):
        print("\n1. Search\n2. Sort\n3. Filter")
        ch = int(input("Enter choice: "))

        if ch == 1:
            val = int(input("Enter value: "))
            print("Found at:", np.where(self.arr == val))

        elif ch == 2:
            print("\nSorted:\n", np.sort(self.arr))

        elif ch == 3:
            val = int(input("Filter > value: "))
            print("\nFiltered:\n", self.arr[self.arr > val])

    # 5. Aggregates + Statistics
    def aggregate_stats(self):
        print("\n1. Sum\n2. Mean\n3. Median\n4. Std Dev\n5. Variance")
        ch = int(input("Enter choice: "))

        if ch == 1:
            print("Sum:", np.sum(self.arr))
        elif ch == 2:
            print("Mean:", np.mean(self.arr))
        elif ch == 3:
            print("Median:", np.median(self.arr))
        elif ch == 4:
            print("Std Dev:", np.std(self.arr))
        elif ch == 5:
            print("Variance:", np.var(self.arr))


# ---------------- MAIN MENU ----------------
obj = DataAnalytics()

while True:
    print("\n==============================")
    print(" NumPy Analyzer Menu")
    print("==============================")
    print("1. Create Array")
    print("2. Math Operations")
    print("3. Combine / Split")
    print("4. Search / Sort / Filter")
    print("5. Aggregates & Statistics")
    print("6. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        obj.create_array()
    elif choice == 2:
        obj.math_ops()
    elif choice == 3:
        obj.combine_split()
    elif choice == 4:
        obj.search_sort_filter()
    elif choice == 5:
        obj.aggregate_stats()
    elif choice == 6:
        print("Thank you! Exiting…")
        break
    else:
        print("Invalid choice")
