// Last updated: 10/2/2026, 10:10:41 AM
/**
 * @param {number[]} prices
 * @param {number[]} discounts
 * @return {number}
 */
var minPrice = function(prices, discounts) {
    const sortedPrices = [...prices].sort((a,b) => b-a);
    const sortedDiscounts = [...discounts].sort((a,b) => b-a);

    var totalSum = 0;
    const m = sortedPrices.length;
    const n = sortedDiscounts.length;


    const discountableItemCount = Math.min(m,n);
    
    for(let i = 0; i < discountableItemCount; i++ ){
        totalSum += (sortedPrices[i] * (100 - sortedDiscounts[i]))/100;
    }
    
    for(let i = discountableItemCount; i < m; i++){
        totalSum += sortedPrices[i];
    }

    return totalSum;
    
};