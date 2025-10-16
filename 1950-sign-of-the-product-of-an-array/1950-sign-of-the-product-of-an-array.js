/**
 * @param {number[]} nums
 * @return {number}
 */
var arraySign = function(nums) {
    let product = 1;
    for(const num of nums) {
        console.log(nums)
        if (num === 0) {
            return 0
        }
        let sign = num > 0 ? 1 : -1;
        product *= sign
    };
    return product;
};