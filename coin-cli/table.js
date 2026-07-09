import { formatPrice, formatChange } from "./format.js";

const COL = { rank: 5, name: 18, symbol: 8, price: 16, change: 14 };
const TOTAL_WIDTH = Object.values(COL).reduce((a, b) => a + b, 0) + 4;

const pad  = (str, len) => String(str).padEnd(len);
const padL = (str, len) => String(str).padStart(len);

export function printTable(coins) {
  const divider = "─".repeat(TOTAL_WIDTH);

  console.log(`\n  Top 5 Cryptocurrencies  (USD)  —  ${new Date().toUTCString()}\n`);
  console.log(`  ${divider}`);
  console.log(
    `  ${pad("#", COL.rank)}${pad("Name", COL.name)}${pad("Symbol", COL.symbol)}` +
    `${padL("Price", COL.price)}  ${pad("24h Change", COL.change)}`
  );
  console.log(`  ${divider}`);

  coins.forEach((coin, i) => {
    const rank   = pad(i + 1, COL.rank);
    const name   = pad(coin.name, COL.name);
    const symbol = pad(coin.symbol.toUpperCase(), COL.symbol);
    const price  = padL(formatPrice(coin.current_price), COL.price);
    const change = formatChange(coin.price_change_percentage_24h);
    console.log(`  ${rank}${name}${symbol}${price}  ${change}`);
  });

  console.log(`  ${divider}\n`);
}
