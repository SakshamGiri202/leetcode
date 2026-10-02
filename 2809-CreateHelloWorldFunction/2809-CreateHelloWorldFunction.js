// Last updated: 10/2/2026, 10:10:51 AM
/**
 * @return {Function}
 */
function createHelloWorld(){
    return function(...agrs){
        return "Hello World"
    }
};


createHelloWorld();


/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */