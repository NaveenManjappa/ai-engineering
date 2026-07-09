# coin-cli — Session Log

## Session 1 — 2026-06-24

### Starting state
Single-file project: `index.js` contained all logic inline — the CoinGecko API URL and fetch call, two formatting helpers, and the table printer, ending with an IIFE entry point.

### Task: Refactor into focused ES modules
Split `index.js` into four files with no new dependencies. Project was already `"type": "module"` in `package.json`, so native ES module syntax (`import`/`export`) was used throughout.

#### Files created
- **`api.js`** — `fetchTopCoins()`: holds the API URL constant and the fetch + error-check logic.
- **`format.js`** — `formatPrice(usd)` and `formatChange(pct)`: pure helpers for USD string formatting and ANSI-coloured percentage display.
- **`table.js`** — `printTable(coins)`: layout constants (`COL` widths, `TOTAL_WIDTH`) hoisted to module scope so they are computed once; imports from `format.js`; renders the divider, header row, and coin rows to stdout.
- **`index.js`** (rewritten) — entry point only: imports `fetchTopCoins` and `printTable`, runs the async IIFE, handles errors and `process.exit(1)`.

#### Output verified
`node index.js` produced the correct table:

```
  Top 5 Cryptocurrencies  (USD)  —  Wed, 24 Jun 2026 16:52:43 GMT

  ─────────────────────────────────────────────────────────────────
  #    Name              Symbol             Price  24h Change
  ─────────────────────────────────────────────────────────────────
  1    Bitcoin           BTC           $59,980.00  -3.96%
  2    Ethereum          ETH            $1,610.15  -2.87%
  3    Tether            USDT               $1.00  -0.03%
  4    BNB               BNB              $558.03  -2.78%
  5    USDC              USDC               $1.00  -0.01%
  ─────────────────────────────────────────────────────────────────
```

(24h change values render in green/red in a real terminal via ANSI codes.)
