// Function to generate candidate itemsets of size k from frequent itemsets of size k-1
function generateCandidateItemsets(prevItemsets, k) {
  const candidateItemsets = new Set();
  for (let i of prevItemsets) {
    for (let j of prevItemsets) {
      // Create candidate itemset by combining i and j
      const candidate = new Set([...i, ...j]);
      // Check if candidate has length k and is not already in the candidate set
      if (candidate.size === k && !candidateItemsets.has(candidate)) {
        // Check if all subsets of the candidate are frequent
        if ([...candidate].every(subset => prevItemsets.has(subset))) {
          candidateItemsets.add(candidate);
        }
      }
    }
  }
  return candidateItemsets;
}

// Function to count the frequency of candidate itemsets in the dataset
function countFrequencies(candidateItemsets, dataset) {
  const itemsetCounts = {};
  for (let itemset of candidateItemsets) {
    // Count the number of transactions that contain the itemset
    const count = dataset.filter(transaction => itemset.every(item => transaction.has(item))).length;
    // Add the count to the itemsetCounts object
    itemsetCounts[JSON.stringify([...itemset])] = count;
  }
  return itemsetCounts;
}

// Function to generate frequent itemsets using the Apriori algorithm
function apriori(dataset, minSupport) {
  // Create a set of unique items in the dataset
  const items = new Set(dataset.flatMap(transaction => transaction));
  // Create an object to store frequent itemsets and their counts
  const frequentItemsets = {};
  // Generate frequent itemsets of size 1
  frequentItemsets[1] = Object.fromEntries([...items].map(item => [[item], dataset.filter(transaction => transaction.has(item)).length]));
  // Generate frequent itemsets of size > 1
  let k = 2;
  while (Object.keys(frequentItemsets[k-1]).length > 0) {
    // Generate candidate itemsets of size k from frequent itemsets of size k-1
    const candidateItemsets = generateCandidateItemsets(new Set(Object.keys(frequentItemsets[k-1]).map(itemset => new Set(JSON.parse(itemset)))), k);
    // Count the frequency of candidate itemsets in the dataset
    const itemsetCounts = countFrequencies(candidateItemsets, dataset);
    // Prune candidate itemsets that do not meet the minimum support threshold
    frequentItemsets[k] = Object.fromEntries(Object.entries(itemsetCounts).filter(([itemset, count]) => count >= minSupport));
    k++;
  }
  // Flatten the frequent itemsets object into an array of arrays
  const flattenedItemsets = Object.entries(frequentItemsets).flatMap(([k, itemsets]) => Object.entries(itemsets).map(([itemset, count]) => [JSON.parse(itemset), count]));
  // Return frequent itemsets sorted by descending frequency
  return flattenedItemsets.sort((a, b) => b[1] - a[1]);
}