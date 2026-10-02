// Last updated: 10/2/2026, 10:11:06 AM
/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const cache =  {};

    return function(...args) {
        const key = String(args);
        if(key in cache){
            return cache[key];
        }
        const result = fn(...args);
        cache[key] = result;
        return result;
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