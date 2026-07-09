export function formatPrice(usd) {
  return `$${usd.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
}

export function formatChange(pct) {
  const sign  = pct >= 0 ? "+" : "";
  const color = pct >= 0 ? "\x1b[32m" : "\x1b[31m";
  return `${color}${sign}${pct.toFixed(2)}%\x1b[0m`;
}
