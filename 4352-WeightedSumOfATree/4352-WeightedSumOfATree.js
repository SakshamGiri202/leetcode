// Last updated: 10/2/2026, 10:10:43 AM
/**
 * @param {number[]} parent
 * @param {number[]} nums
 * @return {number}
 */
var weightedSum = function(parent, nums) {
    const n = parent.length;

    const adj = Array.from({ length:n}, ()=> []);
    for (let i = 1; i <n; i++){
        adj[parent[i]].push(i);
    }

    const depth = new Array(n).fill(0);
    let maxHeight = 0;

    const stack = [[0, 1]];
    while(stack.length > 0){
        const [currentNode, currentDepth] = stack.pop();
        depth[currentNode] = currentDepth;
        maxHeight = Math.max(maxHeight, currentDepth);

        for(const child of adj[currentNode]){
            stack.push([child, currentDepth+1]);
        }
    }

    let totalWeightSum = 0;
    for(let i = 0; i < n; i++){
        const weightMultiplier = maxHeight - depth[i] + 1;
        totalWeightSum += nums[i] * weightMultiplier;
    }

    return totalWeightSum;
};