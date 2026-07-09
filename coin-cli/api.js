const BASE_URL =
  "https://api.coingecko.com/api/v3/coins/markets" +
  "?vs_currency=usd&order=market_cap_desc&page=1&price_change_percentage=24h";

export async function fetchTopCoins(limit = 5) {
  const res = await fetch(`${BASE_URL}&per_page=${limit}`);
  if (!res.ok) throw new Error(`CoinGecko API error: ${res.status} ${res.statusText}`);
  return res.json();
}
