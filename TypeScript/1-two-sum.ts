function twoSum(nums: number[], target: number): number[] {
    const seen = new Map()
    let result: number[] = []
    
    nums.forEach((num, index) => {
        const diff = target - num
        if (seen.has(diff)) {
            result = [seen.get(diff), index]
        }
        
        seen.set(num, index)
    })
    
    return result
};
