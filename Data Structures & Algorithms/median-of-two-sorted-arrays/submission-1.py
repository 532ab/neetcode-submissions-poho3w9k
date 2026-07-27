class Solution:

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Get the lengths of both input arrays
        len1, len2 = len(nums1), len(nums2)

        # Initialize pointers 'i' for nums1 and 'j' for nums2
        i = j = 0

        # Stores the current value (median1) and the previous value (median2)
        # as we iterate through the merged elements
        median1 = median2 = 0

        # We only need to iterate up to the middle point of the combined array
        for count in range((len1 + len2) // 2 + 1):
            # Keep track of the previous element seen before updating median1
            median2 = median1

            # Case 1: Both arrays still have unvisited elements
            if i < len1 and j < len2:
                if nums1[i] > nums2[j]:
                    median1 = nums2[j]
                    j += 1  # Move pointer in nums2
                else:
                    median1 = nums1[i]
                    i += 1  # Move pointer in nums1

            # Case 2: Only nums1 has remaining elements
            elif i < len1:
                median1 = nums1[i]
                i += 1  # Move pointer in nums1

            # Case 3: Only nums2 has remaining elements
            else:
                median1 = nums2[j]
                j += 1  # Move pointer in nums2

        # If the total number of elements is odd, the median is the current middle element
        if (len1 + len2) % 2 == 1:
            return float(median1)
        # If the total number of elements is even, average the two middle values
        else:
            return (median1 + median2) / 2.0