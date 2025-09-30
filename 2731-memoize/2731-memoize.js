/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    let memo = {};
    return function(...args) {
        const [num1, num2] = args
        const key = `${num1},${num2}`
        if (key in memo) {
            return memo[key]
        }
        memo[key] = fn(...args)  
        return memo[key]      
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */