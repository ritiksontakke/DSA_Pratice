# Top K Frequent Elements
nums = [1,2,2,3,3,3]
k = 2
# Output: [2,3]

class Solustion:

    def freqEkement(self, nums:list[int], k: int):

        count = {}

        for num in nums:
            count[num] = 1 + count.get(num,0)

        arr = []

        for num,cnt in count.items():
            arr.append([cnt,num])
        
        arr.sort()

        res = []

        while len(res) < k:
            res.append(arr.pop()[1])
        res.sort()
        return res
obj = Solustion()

print(obj.freqEkement(nums,k))