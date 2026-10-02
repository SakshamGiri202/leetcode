// Last updated: 10/2/2026, 10:10:59 AM
/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const filteredArr = [];
    for(let i = 0; i < arr.length; i++){
       if(fn(arr[i], i)){
        filteredArr.push(arr[i]);
       }else{
        continue;
       }
    }
    return filteredArr;
};