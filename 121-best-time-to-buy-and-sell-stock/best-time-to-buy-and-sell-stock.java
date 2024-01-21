class Solution {

public int maxProfit(int[] prices) {

int maxProfit = 0;

int sellingPrice = prices[prices.length-1];

for (int i = prices.length - 1; i > -1; --i) {



int currProfit = sellingPrice - prices[i];


maxProfit = Math.max(currProfit, maxProfit);

sellingPrice = Math.max(sellingPrice, prices[i]);

}

return maxProfit;

}

}