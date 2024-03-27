class BinarySearch:
    def binary_search(self, A, k):
        left = 0
        right = len(A) - 1
        while (left <= right):
            mid = (left + right) // 2
            if (A[mid] >= k):
                right = mid - 1
            else:
                left = mid + 1
        if (left > len(A)-1):
            return -1
        return A[left]

 
class TestBinarySearch:
    def test_1(self):
        actual_output = BinarySearch().binary_search([5], 4)
        expected_output = 5
        assert actual_output == expected_output

    def test_2(self):
        actual_output = BinarySearch().binary_search([], 100)
        expected_output = -1
        assert actual_output == expected_output
    
    def test_3(self):
        actual_output = BinarySearch().binary_search([3], 4)
        expected_output = -1
        assert actual_output == expected_output