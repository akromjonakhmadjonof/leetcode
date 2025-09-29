/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    return {
        toBe: function(target) {
            if (target === val) {
                return true;
            }
            throw new Error("Not Equal");
        },
        notToBe: function(target) {
            if (target !== val) {
                return true;
            }
            throw new Error("Equal");
        }
    }
};

/**
 * Usage:
 * expect(5).toBe(5);       // true
 * expect(5).notToBe(5);    // throws "Equal"
 */
