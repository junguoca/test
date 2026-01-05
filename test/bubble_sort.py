"""
冒泡排序算法实现
Bubble Sort Algorithm Implementation
"""


def bubble_sort(arr):
    """
    冒泡排序函数
    
    参数:
        arr: 待排序的列表
    
    返回:
        排序后的列表（原地排序，也会修改原列表）
    
    时间复杂度: O(n²)
    空间复杂度: O(1)
    """
    # 创建列表的副本，避免修改原列表
    arr = arr.copy()
    n = len(arr)
    
    # 外层循环控制排序轮数
    for i in range(n):
        # 标记是否发生交换，用于优化
        swapped = False
        
        # 内层循环进行相邻元素比较和交换
        # 每轮排序后，最大的元素会"冒泡"到末尾
        for j in range(0, n - i - 1):
            # 如果前一个元素大于后一个元素，则交换
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # 如果本轮没有发生交换，说明数组已经有序，可以提前结束
        if not swapped:
            break
    
    return arr


def bubble_sort_inplace(arr):
    """
    原地冒泡排序（直接修改原列表）
    
    参数:
        arr: 待排序的列表（会被直接修改）
    
    返回:
        None（原地排序）
    """
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break


if __name__ == "__main__":
    # 主要测试用例：用户指定的数组
    user_array = [19, 21, 12, 12, 45, 24, 223]
    
    print("冒泡排序测试结果:")
    print("=" * 50)
    
    # 测试用户指定的数组
    original = user_array.copy()
    sorted_arr = bubble_sort(user_array)
    
    print("主要测试用例:")
    print(f"  原数组: {original}")
    print(f"  排序后: {sorted_arr}")
    print()
    
    # 验证排序结果
    expected = sorted(original)
    if sorted_arr == expected:
        print("✓ 排序结果正确！")
    else:
        print("✗ 排序结果有误！")
        print(f"  期望结果: {expected}")
    print()
    
    # 其他测试用例
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 8, 1, 9],
        [1],
        [],
        [3, 3, 3, 3],
        [9, 8, 7, 6, 5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5]
    ]
    
    print("其他测试用例:")
    print("-" * 50)
    
    for i, test_arr in enumerate(test_cases, 1):
        original = test_arr.copy()
        sorted_arr = bubble_sort(test_arr)
        
        print(f"测试 {i}:")
        print(f"  原数组: {original}")
        print(f"  排序后: {sorted_arr}")
        print()

