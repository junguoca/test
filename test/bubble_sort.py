def bubble_sort(arr):
    """
    冒泡排序算法
    
    参数:
        arr: 待排序的列表
    
    返回:
        排序后的列表
    """
    # 复制列表，避免修改原列表
    arr = arr.copy()
    n = len(arr)
    
    # 外层循环控制排序轮数
    for i in range(n):
        # 标记是否发生交换，用于优化
        swapped = False
        
        # 内层循环进行相邻元素比较和交换
        # 每轮排序后，最大的元素会"冒泡"到末尾
        # 所以每轮可以减少一次比较
        for j in range(0, n - i - 1):
            # 如果前一个元素大于后一个元素，则交换
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # 如果本轮没有发生交换，说明数组已经有序，可以提前结束
        if not swapped:
            break
    
    return arr


def bubble_sort_descending(arr):
    """
    降序冒泡排序
    
    参数:
        arr: 待排序的列表
    
    返回:
        降序排序后的列表
    """
    arr = arr.copy()
    n = len(arr)
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            # 降序：如果前一个元素小于后一个元素，则交换
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break
    
    return arr


if __name__ == "__main__":
    # 测试数组
    test_cases = [[6, 3, 34, 21, 98, 54, 12, 64, 11, 22,12]]
    
    print("冒泡排序测试（升序）：")
    print("=" * 50)
    for i, test_arr in enumerate(test_cases, 1):
        if test_arr:  # 跳过空列表
            sorted_arr = bubble_sort(test_arr)
            print(f"测试 {i}: {test_arr} -> {sorted_arr}")
        else:
            sorted_arr = bubble_sort(test_arr)
            print(f"测试 {i}: [] -> {sorted_arr}")
    
    print("\n冒泡排序测试（降序）：")
    print("=" * 50)
    for i, test_arr in enumerate(test_cases, 1):
        if test_arr:  # 跳过空列表
            sorted_arr = bubble_sort_descending(test_arr)
            print(f"测试 {i}: {test_arr} -> {sorted_arr}")
        else:
            sorted_arr = bubble_sort_descending(test_arr)
            print(f"测试 {i}: [] -> {sorted_arr}")

