class Solution:
    def maxArea(self, heights: List[int]) -> int:
        slow, fast = 0,1
        left,right = 0,len(heights) -1
        max_area = 0
        # while fast < len(heights)-1 :
        while right > left:
            x = right-left
            y = min(heights[right],heights[left])
            area = x*y
            if area > max_area:
                    max_area = area
    #     if heights[left] < heights[right]:
    #     move left
    # else:
    #     move right
            if heights[left] < heights[right]:
                left +=1
            else:
                right -=1
        return max_area

        # while fast >
        # for slow in range(len(heights)):
        #     for fast in range(slow, len(heights)):
        #         x = fast-slow
        #         y = min(heights[fast],heights[slow])
        #         area = x*y
        #         if area > max_area:
        #             max_area = area
        #             slow +=1
        #             if slow == fast:
        #                 fast +=1
        #         slow +=1
        #         fast +=1
        # return max_area
            
        