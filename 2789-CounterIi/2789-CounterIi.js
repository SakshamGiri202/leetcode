// Last updated: 10/2/2026, 10:10:54 AM
/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
     let currentCount = init;
    let object = {
        increment: function(){
            return ++currentCount;
        },
        decrement: function(){

            return --currentCount;
        },
        reset: function(){
           
            return currentCount= init;
        }
    }
    return object;
    
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */