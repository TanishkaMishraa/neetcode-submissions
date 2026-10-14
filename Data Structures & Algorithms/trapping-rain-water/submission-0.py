class Solution:
    def trap(self, height: List[int]) -> int:
        m_left = 0
        m_right = 0
        left = [0] * len(height)
        right = [0] * len(height)

        for i in range(len(height)):
            j = -i - 1
            left[i] = m_left
            right[j] = m_right

            m_left = max(m_left, height[i])
            m_right = max(m_right, height[j])

        water = 0 

        for i in range(len(height)):
            pot = min (left[i], right[i])

            water += max(0, pot - height[i]) 

        return water       