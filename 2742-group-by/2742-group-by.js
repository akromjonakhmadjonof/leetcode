/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    let groupped = {};

    for (item of this) {
        let key = fn(item).toString();
        if (key in groupped) {
            groupped[key].push(item)
        } else {
            groupped[key] = [item]
        }
    }
    return groupped;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */