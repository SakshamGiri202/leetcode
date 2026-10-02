// Last updated: 10/2/2026, 10:11:02 AM
/**
 * @param {number} millis
 * @return {Promise}
 */
async function sleep(millis) {
    return await  new Promise((resolve, reject)=>{
         setTimeout(() => {
            resolve(millis);
    }, millis);
    })
}

/** 
 * let t = Date.now()
 * sleep(100).then(() => console.log(Date.now() - t)) // 100
 */