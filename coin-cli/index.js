import { fetchTopCoins } from "./api.js";
import { printTable } from "./table.js";

(async () => {
  try {
    const limit = parseInt(process.argv[2], 10) || 5;
  const coins = await fetchTopCoins(limit);
    printTable(coins);
  } catch (err) {
    console.error("Error:", err.message);
    process.exit(1);
  }
})();
