// Last updated: 10/2/2026, 10:11:20 AM
/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
  const revserseX = String(x).split("").reverse().join("");
  if(x === Number(revserseX)){
    return true;
  }else{
    return false;
  }
};