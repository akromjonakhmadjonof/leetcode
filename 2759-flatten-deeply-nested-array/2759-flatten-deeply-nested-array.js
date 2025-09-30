/**
 * @param {Array} arr
 * @param {number} n
 * @return {Array}
 */
var flat = function (arr, n) {
    let result = [];

    function flatten(target, depth) {
        if (Array.isArray(target) && depth > 0) {
            for (let item of target) {
                flatten(item, depth - 1);
            }
        } else {
            result.push(target);
        }
    }

    for (let item of arr) {
        flatten(item, n);
    }

    return result;
};
