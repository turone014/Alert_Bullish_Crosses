#15minutes bullish cross

# Install necessary libraries if running in Google Colab
try:
    import ccxt
    import pandas as pd
    import pytz
    import requests
    import os
    from datetime import datetime
    from ta.momentum import RSIIndicator
    from ta.trend import MACD
except ImportError:
    import ccxt
    import pandas as pd
    import pytz
    import requests
    import os
    from datetime import datetime
    from ta.momentum import RSIIndicator
    from ta.trend import MACD
    
# ========== CONFIGURATION ==========
DISCORD_WEBHOOK_URL = os.getenv("FIFTEEN_MINS_WEBHOOK")
symbols = ['1INCH-USDT-SWAP','AAVE-USDT-SWAP','ACE-USDT-SWAP','ACH-USDT-SWAP','ACT-USDT-SWAP','ADA-USDT-SWAP','AEVO-USDT-SWAP','AGLD-USDT-SWAP','AI16Z-USDT-SWAP','AIDOGE-USDT-SWAP','AIXBT-USDT-SWAP','ALCH-USDT-SWAP','ALGO-USDT-SWAP','ALPHA-USDT-SWAP','ANIME-USDT-SWAP','APE-USDT-SWAP','API3-USDT-SWAP','APT-USDT-SWAP','ARB-USDT-SWAP','ARC-USDT-SWAP','ARKM-USDT-SWAP','AR-USDT-SWAP','ATH-USDT-SWAP','ATOM-USDT-SWAP','AUCTION-USDT-SWAP','A-USDT-SWAP','AVAAI-USDT-SWAP','AVAX-USDT-SWAP','AXS-USDT-SWAP','BABY-USDT-SWAP','BADGER-USDT-SWAP','BAL-USDT-SWAP','BAND-USDT-SWAP','BAT-USDT-SWAP','BCH-USDT-SWAP','BERA-USDT-SWAP','BICO-USDT-SWAP','BIGTIME-USDT-SWAP','BIO-USDT-SWAP','BLUR-USDT-SWAP','BNB-USDT-SWAP','BNT-USDT-SWAP','BOME-USDT-SWAP','BONK-USDT-SWAP','BRETT-USDT-SWAP','BTC-USDT-SWAP','BTC-USDT-SWAP','CATI-USDT-SWAP','CAT-USDT-SWAP','CELO-USDT-SWAP','CETUS-USDT-SWAP','CFX-USDT-SWAP','CHZ-USDT-SWAP','COMP-USDT-SWAP','COOKIE-USDT-SWAP','CORE-USDT-SWAP','CRO-USDT-SWAP','CRV-USDT-SWAP','CSPR-USDT-SWAP','CTC-USDT-SWAP','CVC-USDT-SWAP','CVX-USDT-SWAP','DEGEN-USDT-SWAP','DGB-USDT-SWAP','DOGE-USDT-SWAP','DOGS-USDT-SWAP','DOG-USDT-SWAP','DOOD-USDT-SWAP','DOT-USDT-SWAP','DUCK-USDT-SWAP','DYDX-USDT-SWAP','EGLD-USDT-SWAP','EIGEN-USDT-SWAP','ENJ-USDT-SWAP','ENS-USDT-SWAP','ETC-USDT-SWAP','ETHFI-USDT-SWAP','ETH-USDT-SWAP','ETHW-USDT-SWAP','FARTCOIN-USDT-SWAP','FIL-USDT-SWAP','FLM-USDT-SWAP','FLOKI-USDT-SWAP','FLOW-USDT-SWAP','FXS-USDT-SWAP','GALA-USDT-SWAP','GAS-USDT-SWAP','GLM-USDT-SWAP','GMT-USDT-SWAP','GMX-USDT-SWAP','GOAT-USDT-SWAP','GODS-USDT-SWAP','GPS-USDT-SWAP','GRASS-USDT-SWAP','GRIFFAIN-USDT-SWAP','GRT-USDT-SWAP','HBAR-USDT-SWAP','HMSTR-USDT-SWAP','HOME-USDT-SWAP','HUMA-USDT-SWAP','HYPE-USDT-SWAP','ICP-USDT-SWAP','ICX-USDT-SWAP','ID-USDT-SWAP','IMX-USDT-SWAP','INIT-USDT-SWAP','INJ-USDT-SWAP','IOST-USDT-SWAP','IOTA-USDT-SWAP','IP-USDT-SWAP','JELLYJELLY-USDT-SWAP','JOE-USDT-SWAP','JST-USDT-SWAP','JTO-USDT-SWAP','JUP-USDT-SWAP','KAITO-USDT-SWAP','KMNO-USDT-SWAP','KNC-USDT-SWAP','KSM-USDT-SWAP','LAUNCHCOIN-USDT-SWAP','LA-USDT-SWAP','LAYER-USDT-SWAP','LDO-USDT-SWAP','LINK-USDT-SWAP','LOOKS-USDT-SWAP','LPT-USDT-SWAP','LQTY-USDT-SWAP','LRC-USDT-SWAP','LSK-USDT-SWAP','LTC-USDT-SWAP','LUNA-USDT-SWAP','LUNC-USDT-SWAP','MAGIC-USDT-SWAP','MAJOR-USDT-SWAP','MANA-USDT-SWAP','MASK-USDT-SWAP','MEME-USDT-SWAP','MERL-USDT-SWAP','METIS-USDT-SWAP','ME-USDT-SWAP','MEW-USDT-SWAP','MINA-USDT-SWAP','MKR-USDT-SWAP','MOODENG-USDT-SWAP','MORPHO-USDT-SWAP','MOVE-USDT-SWAP','MUBARAK-USDT-SWAP','NC-USDT-SWAP','NEAR-USDT-SWAP','NEIROETH-USDT-SWAP','NEIRO-USDT-SWAP','NEO-USDT-SWAP','NIL-USDT-SWAP','NMR-USDT-SWAP','NOT-USDT-SWAP','NXPC-USDT-SWAP','OL-USDT-SWAP','OM-USDT-SWAP','ONDO-USDT-SWAP','ONE-USDT-SWAP','ONT-USDT-SWAP','OP-USDT-SWAP','ORBS-USDT-SWAP','ORDI-USDT-SWAP','PARTI-USDT-SWAP','PENGU-USDT-SWAP','PEOPLE-USDT-SWAP','PEPE-USDT-SWAP','PERP-USDT-SWAP','PIPPIN-USDT-SWAP','PI-USDT-SWAP','PLUME-USDT-SWAP','PNUT-USDT-SWAP','POL-USDT-SWAP','POPCAT-USDT-SWAP','PRCL-USDT-SWAP','PROMPT-USDT-SWAP','PYTH-USDT-SWAP','QTUM-USDT-SWAP','RAY-USDT-SWAP','RDNT-USDT-SWAP','RENDER-USDT-SWAP','RESOLV-USDT-SWAP','RSR-USDT-SWAP','RVN-USDT-SWAP','SAND-USDT-SWAP','SATS-USDT-SWAP','SCR-USDT-SWAP','SHELL-USDT-SWAP','SHIB-USDT-SWAP','SIGN-USDT-SWAP','SLERF-USDT-SWAP','SLP-USDT-SWAP','SNX-USDT-SWAP','SOL-USDT-SWAP','SOLV-USDT-SWAP','SONIC-USDT-SWAP','SOON-USDT-SWAP','SOPH-USDT-SWAP','SSV-USDT-SWAP','STORJ-USDT-SWAP','STRK-USDT-SWAP','STX-USDT-SWAP','SUI-USDT-SWAP','S-USDT-SWAP','SUSHI-USDT-SWAP','SWARMS-USDT-SWAP','TAO-USDT-SWAP','THETA-USDT-SWAP','TIA-USDT-SWAP','TNSR-USDT-SWAP','TON-USDT-SWAP','TRB-USDT-SWAP','TRUMP-USDT-SWAP','TRX-USDT-SWAP','TURBO-USDT-SWAP','T-USDT-SWAP','UMA-USDT-SWAP','UNI-USDT-SWAP','USDC-USDT-SWAP','USTC-USDT-SWAP','UXLINK-USDT-SWAP','VANA-USDT-SWAP','VINE-USDT-SWAP','VIRTUAL-USDT-SWAP','WAL-USDT-SWAP','WAXP-USDT-SWAP','WCT-USDT-SWAP','WIF-USDT-SWAP','WLD-USDT-SWAP','WOO-USDT-SWAP','W-USDT-SWAP','XAUT-USDT-SWAP','XCH-USDT-SWAP','XLM-USDT-SWAP','XRP-USDT-SWAP','XTZ-USDT-SWAP','YFI-USDT-SWAP','YGG-USDT-SWAP','ZENT-USDT-SWAP','ZEREBRO-USDT-SWAP','ZETA-USDT-SWAP','ZIL-USDT-SWAP','ZK-USDT-SWAP','ZRO-USDT-SWAP','ZRX-USDT-SWAP']  # Customize your list

rsi_period = 30
macd_fast = 12
macd_slow = 26
macd_signal = 9

timezone = pytz.timezone('Asia/Manila')
okx = ccxt.okx({'enableRateLimit': True})

# ========== FUNCTIONS ==========

def get_ohlcv(symbol, timeframe, limit=100):
    try:
        data = okx.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
        df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['datetime'] = pd.to_datetime(df['timestamp'], unit='ms')
        return df
    except Exception as e:
        print(f"[ERROR] Fetching {timeframe} data for {symbol}: {e}")
        return None

def add_indicators(df):
    rsi = RSIIndicator(df['close'], window=rsi_period)
    macd = MACD(df['close'], window_slow=macd_slow, window_fast=macd_fast, window_sign=macd_signal)
    df['rsi'] = rsi.rsi()
    df['macd'] = macd.macd()
    df['signal'] = macd.macd_signal()
    return df

def get_latest_macd_cross(df):
    for i in range(len(df) - 2, 0, -1):
        prev_macd = df['macd'].iloc[i]
        prev_signal = df['signal'].iloc[i]
        curr_macd = df['macd'].iloc[i + 1]
        curr_signal = df['signal'].iloc[i + 1]
        if pd.notna(prev_macd) and pd.notna(prev_signal) and pd.notna(curr_macd) and pd.notna(curr_signal):
            if prev_macd < prev_signal and curr_macd > curr_signal:
                return 'bullish'
            elif prev_macd > prev_signal and curr_macd < curr_signal:
                return 'bearish'
    return None

def is_rsi_above_50_or_crossing(df):
    if len(df) < 2 or pd.isna(df['rsi'].iloc[-1]) or pd.isna(df['rsi'].iloc[-2]):
        return False
    return df['rsi'].iloc[-1] > 50 or (df['rsi'].iloc[-2] < 50 and df['rsi'].iloc[-1] > 50)

def send_discord_alert(symbol, message):
    now_manila = datetime.now(timezone).strftime('%Y-%m-%d %H:%M:%S')
    content = f"🔔🟢 **Bullish Alert**\nSymbol: {symbol}\nDate: {now_manila}\n========================="
    try:
        requests.post(DISCORD_WEBHOOK_URL, json={"content": content})
        print(f"[ALERT SENT] {symbol}")
    except Exception as e:
        print(f"[ERROR] Sending Discord alert for {symbol}: {e}")

# ========== MAIN EXECUTION ==========
print("🚀 Starting trend check...")

for symbol in symbols:
    print(f"\n🔍 Checking {symbol}...")

    # Step 1: Check 15m MACD Bullish Cross
    df_15m = get_ohlcv(symbol, '15m')
    if df_15m is None:
        continue
    df_15m = add_indicators(df_15m)
    if get_latest_macd_cross(df_15m) != 'bullish':
        print(f"[INFO] No recent MACD bullish cross in 15m for {symbol}")
        continue
    print(f"[✓] 15m MACD bullish cross detected for {symbol}")

    # Step 2: Check 5m RSI above/cross 50
    df_5m = get_ohlcv(symbol, '5m')
    if df_5m is None:
        continue
    df_5m = add_indicators(df_5m)
    if not is_rsi_above_50_or_crossing(df_5m):
        print(f"[INFO] RSI(30) not above/crossing 50 on 5m for {symbol}")
        continue
    print(f"[✓] 5m RSI(30) is above or crossed above 50 for {symbol}")

    # Step 3: Check 5m MACD Bearish Cross
    if get_latest_macd_cross(df_5m) != 'bearish':
        print(f"[INFO] No recent MACD bearish cross in 5m for {symbol}")
        continue
    print(f"[✓] 5m MACD bearish cross confirmed for {symbol}")

    # Step 4: All conditions met — Alert!
    message = ""
    send_discord_alert(symbol, message)

print("\n✅ Script completed. No repeated scanning.")


#==================================================================
#1HR Bullish


import ccxt
import pandas as pd
import pytz
import os
from datetime import datetime
import requests
from ta.momentum import RSIIndicator
from ta.trend import MACD

# ========== CONFIGURATION ==========
DISCORD_WEBHOOK_URL = os.getenv("ONE_HOUR_WEBHOOK")

# Custom OKX USDT-margined Futures symbols
symbols = ['1INCH-USDT-SWAP','AAVE-USDT-SWAP','ACE-USDT-SWAP','ACH-USDT-SWAP','ACT-USDT-SWAP','ADA-USDT-SWAP','AEVO-USDT-SWAP','AGLD-USDT-SWAP','AI16Z-USDT-SWAP','AIDOGE-USDT-SWAP','AIXBT-USDT-SWAP','ALCH-USDT-SWAP','ALGO-USDT-SWAP','ALPHA-USDT-SWAP','ANIME-USDT-SWAP','APE-USDT-SWAP','API3-USDT-SWAP','APT-USDT-SWAP','ARB-USDT-SWAP','ARC-USDT-SWAP','ARKM-USDT-SWAP','AR-USDT-SWAP','ATH-USDT-SWAP','ATOM-USDT-SWAP','AUCTION-USDT-SWAP','A-USDT-SWAP','AVAAI-USDT-SWAP','AVAX-USDT-SWAP','AXS-USDT-SWAP','BABY-USDT-SWAP','BADGER-USDT-SWAP','BAL-USDT-SWAP','BAND-USDT-SWAP','BAT-USDT-SWAP','BCH-USDT-SWAP','BERA-USDT-SWAP','BICO-USDT-SWAP','BIGTIME-USDT-SWAP','BIO-USDT-SWAP','BLUR-USDT-SWAP','BNB-USDT-SWAP','BNT-USDT-SWAP','BOME-USDT-SWAP','BONK-USDT-SWAP','BRETT-USDT-SWAP','BTC-USDT-SWAP','BTC-USDT-SWAP','CATI-USDT-SWAP','CAT-USDT-SWAP','CELO-USDT-SWAP','CETUS-USDT-SWAP','CFX-USDT-SWAP','CHZ-USDT-SWAP','COMP-USDT-SWAP','COOKIE-USDT-SWAP','CORE-USDT-SWAP','CRO-USDT-SWAP','CRV-USDT-SWAP','CSPR-USDT-SWAP','CTC-USDT-SWAP','CVC-USDT-SWAP','CVX-USDT-SWAP','DEGEN-USDT-SWAP','DGB-USDT-SWAP','DOGE-USDT-SWAP','DOGS-USDT-SWAP','DOG-USDT-SWAP','DOOD-USDT-SWAP','DOT-USDT-SWAP','DUCK-USDT-SWAP','DYDX-USDT-SWAP','EGLD-USDT-SWAP','EIGEN-USDT-SWAP','ENJ-USDT-SWAP','ENS-USDT-SWAP','ETC-USDT-SWAP','ETHFI-USDT-SWAP','ETH-USDT-SWAP','ETHW-USDT-SWAP','FARTCOIN-USDT-SWAP','FIL-USDT-SWAP','FLM-USDT-SWAP','FLOKI-USDT-SWAP','FLOW-USDT-SWAP','FXS-USDT-SWAP','GALA-USDT-SWAP','GAS-USDT-SWAP','GLM-USDT-SWAP','GMT-USDT-SWAP','GMX-USDT-SWAP','GOAT-USDT-SWAP','GODS-USDT-SWAP','GPS-USDT-SWAP','GRASS-USDT-SWAP','GRIFFAIN-USDT-SWAP','GRT-USDT-SWAP','HBAR-USDT-SWAP','HMSTR-USDT-SWAP','HOME-USDT-SWAP','HUMA-USDT-SWAP','HYPE-USDT-SWAP','ICP-USDT-SWAP','ICX-USDT-SWAP','ID-USDT-SWAP','IMX-USDT-SWAP','INIT-USDT-SWAP','INJ-USDT-SWAP','IOST-USDT-SWAP','IOTA-USDT-SWAP','IP-USDT-SWAP','JELLYJELLY-USDT-SWAP','JOE-USDT-SWAP','JST-USDT-SWAP','JTO-USDT-SWAP','JUP-USDT-SWAP','KAITO-USDT-SWAP','KMNO-USDT-SWAP','KNC-USDT-SWAP','KSM-USDT-SWAP','LAUNCHCOIN-USDT-SWAP','LA-USDT-SWAP','LAYER-USDT-SWAP','LDO-USDT-SWAP','LINK-USDT-SWAP','LOOKS-USDT-SWAP','LPT-USDT-SWAP','LQTY-USDT-SWAP','LRC-USDT-SWAP','LSK-USDT-SWAP','LTC-USDT-SWAP','LUNA-USDT-SWAP','LUNC-USDT-SWAP','MAGIC-USDT-SWAP','MAJOR-USDT-SWAP','MANA-USDT-SWAP','MASK-USDT-SWAP','MEME-USDT-SWAP','MERL-USDT-SWAP','METIS-USDT-SWAP','ME-USDT-SWAP','MEW-USDT-SWAP','MINA-USDT-SWAP','MKR-USDT-SWAP','MOODENG-USDT-SWAP','MORPHO-USDT-SWAP','MOVE-USDT-SWAP','MUBARAK-USDT-SWAP','NC-USDT-SWAP','NEAR-USDT-SWAP','NEIROETH-USDT-SWAP','NEIRO-USDT-SWAP','NEO-USDT-SWAP','NIL-USDT-SWAP','NMR-USDT-SWAP','NOT-USDT-SWAP','NXPC-USDT-SWAP','OL-USDT-SWAP','OM-USDT-SWAP','ONDO-USDT-SWAP','ONE-USDT-SWAP','ONT-USDT-SWAP','OP-USDT-SWAP','ORBS-USDT-SWAP','ORDI-USDT-SWAP','PARTI-USDT-SWAP','PENGU-USDT-SWAP','PEOPLE-USDT-SWAP','PEPE-USDT-SWAP','PERP-USDT-SWAP','PIPPIN-USDT-SWAP','PI-USDT-SWAP','PLUME-USDT-SWAP','PNUT-USDT-SWAP','POL-USDT-SWAP','POPCAT-USDT-SWAP','PRCL-USDT-SWAP','PROMPT-USDT-SWAP','PYTH-USDT-SWAP','QTUM-USDT-SWAP','RAY-USDT-SWAP','RDNT-USDT-SWAP','RENDER-USDT-SWAP','RESOLV-USDT-SWAP','RSR-USDT-SWAP','RVN-USDT-SWAP','SAND-USDT-SWAP','SATS-USDT-SWAP','SCR-USDT-SWAP','SHELL-USDT-SWAP','SHIB-USDT-SWAP','SIGN-USDT-SWAP','SLERF-USDT-SWAP','SLP-USDT-SWAP','SNX-USDT-SWAP','SOL-USDT-SWAP','SOLV-USDT-SWAP','SONIC-USDT-SWAP','SOON-USDT-SWAP','SOPH-USDT-SWAP','SSV-USDT-SWAP','STORJ-USDT-SWAP','STRK-USDT-SWAP','STX-USDT-SWAP','SUI-USDT-SWAP','S-USDT-SWAP','SUSHI-USDT-SWAP','SWARMS-USDT-SWAP','TAO-USDT-SWAP','THETA-USDT-SWAP','TIA-USDT-SWAP','TNSR-USDT-SWAP','TON-USDT-SWAP','TRB-USDT-SWAP','TRUMP-USDT-SWAP','TRX-USDT-SWAP','TURBO-USDT-SWAP','T-USDT-SWAP','UMA-USDT-SWAP','UNI-USDT-SWAP','USDC-USDT-SWAP','USTC-USDT-SWAP','UXLINK-USDT-SWAP','VANA-USDT-SWAP','VINE-USDT-SWAP','VIRTUAL-USDT-SWAP','WAL-USDT-SWAP','WAXP-USDT-SWAP','WCT-USDT-SWAP','WIF-USDT-SWAP','WLD-USDT-SWAP','WOO-USDT-SWAP','W-USDT-SWAP','XAUT-USDT-SWAP','XCH-USDT-SWAP','XLM-USDT-SWAP','XRP-USDT-SWAP','XTZ-USDT-SWAP','YFI-USDT-SWAP','YGG-USDT-SWAP','ZENT-USDT-SWAP','ZEREBRO-USDT-SWAP','ZETA-USDT-SWAP','ZIL-USDT-SWAP','ZK-USDT-SWAP','ZRO-USDT-SWAP','ZRX-USDT-SWAP']  # Add your desired trading pairs


rsi_period = 30
macd_fast = 12
macd_slow = 26
macd_signal = 9

timezone = pytz.timezone('Asia/Manila')

# ========== INIT EXCHANGE ==========
okx = ccxt.okx({'enableRateLimit': True})

def get_ohlcv(symbol, timeframe, limit=100):
    try:
        data = okx.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
        df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['datetime'] = pd.to_datetime(df['timestamp'], unit='ms')
        return df
    except Exception as e:
        print(f"[ERROR] Fetching {timeframe} data for {symbol}: {e}")
        return None

def add_indicators(df):
    rsi = RSIIndicator(df['close'], window=rsi_period)
    macd = MACD(df['close'], window_slow=macd_slow, window_fast=macd_fast, window_sign=macd_signal)
    df['rsi'] = rsi.rsi()
    df['macd'] = macd.macd()
    df['signal'] = macd.macd_signal()
    return df

def get_latest_macd_cross(df):
    for i in range(len(df) - 2, 0, -1):
        prev_macd = df['macd'].iloc[i]
        prev_signal = df['signal'].iloc[i]
        curr_macd = df['macd'].iloc[i + 1]
        curr_signal = df['signal'].iloc[i + 1]
        
        if pd.notna(prev_macd) and pd.notna(prev_signal):
            if prev_macd < prev_signal and curr_macd > curr_signal:
                return 'bullish'
            elif prev_macd > prev_signal and curr_macd < curr_signal:
                return 'bearish'
    return None

def is_rsi_above_50_or_crossing(df):
    if pd.isna(df['rsi'].iloc[-1]) or pd.isna(df['rsi'].iloc[-2]):
        return False
    return df['rsi'].iloc[-1] > 50 or (df['rsi'].iloc[-2] < 50 and df['rsi'].iloc[-1] > 50)

def send_discord_alert(symbol, message):
    now_manila = datetime.now(timezone).strftime('%Y-%m-%d %H:%M:%S')
    content = f"🔔🟢 Bullish Alert \n Symbol: {symbol}\nDate: {now_manila}\n================================="
    try:
        requests.post(DISCORD_WEBHOOK_URL, json={"content": content})
        print(f"[ALERT SENT] {symbol}")
    except Exception as e:
        print(f"[ERROR] Sending Discord alert for {symbol}: {e}")

# ========== MAIN RUN ==========
for symbol in symbols:
    print(f"\n🔍 Checking {symbol}...")

    # Fetch 1H data & check MACD bullish cross
    df_1h = get_ohlcv(symbol, '1h')
    if df_1h is None:
        continue
    df_1h = add_indicators(df_1h)
    if get_latest_macd_cross(df_1h) != 'bullish':
        print(f"[INFO] No recent bullish MACD cross on 1H for {symbol}")
        continue
    print(f"[✓] 1H Bullish MACD cross confirmed for {symbol}")

    # Fetch 15m data & check RSI and MACD
    df_15m = get_ohlcv(symbol, '15m')
    if df_15m is None:
        continue
    df_15m = add_indicators(df_15m)

    if not is_rsi_above_50_or_crossing(df_15m):
        print(f"[INFO] RSI(30) not above or crossing 50 on 15m for {symbol}")
        continue
    print(f"[✓] 15m RSI(30) condition met for {symbol}")

    if get_latest_macd_cross(df_15m) != 'bearish':
        print(f"[INFO] No recent bearish MACD cross on 15m for {symbol}")
        continue
    print(f"[✓] 15m Bearish MACD cross confirmed for {symbol}")

    # Send Discord alert
    alert_message = (""
       
    )
    send_discord_alert(symbol, alert_message)

#====================================================================================================================
#4HRS Bullish - working

import ccxt
import pandas as pd
import pytz
import os
from datetime import datetime
import requests
from ta.momentum import RSIIndicator
from ta.trend import MACD

# ========== CONFIGURATION ==========
DISCORD_WEBHOOK_URL = os.getenv("FOUR_HOUR_WEBHOOK")

# Custom OKX USDT-margined Futures symbols
symbols = ['1INCH-USDT-SWAP','AAVE-USDT-SWAP','ACE-USDT-SWAP','ACH-USDT-SWAP','ACT-USDT-SWAP','ADA-USDT-SWAP','AEVO-USDT-SWAP','AGLD-USDT-SWAP','AI16Z-USDT-SWAP','AIDOGE-USDT-SWAP','AIXBT-USDT-SWAP','ALCH-USDT-SWAP','ALGO-USDT-SWAP','ALPHA-USDT-SWAP','ANIME-USDT-SWAP','APE-USDT-SWAP','API3-USDT-SWAP','APT-USDT-SWAP','ARB-USDT-SWAP','ARC-USDT-SWAP','ARKM-USDT-SWAP','AR-USDT-SWAP','ATH-USDT-SWAP','ATOM-USDT-SWAP','AUCTION-USDT-SWAP','A-USDT-SWAP','AVAAI-USDT-SWAP','AVAX-USDT-SWAP','AXS-USDT-SWAP','BABY-USDT-SWAP','BADGER-USDT-SWAP','BAL-USDT-SWAP','BAND-USDT-SWAP','BAT-USDT-SWAP','BCH-USDT-SWAP','BERA-USDT-SWAP','BICO-USDT-SWAP','BIGTIME-USDT-SWAP','BIO-USDT-SWAP','BLUR-USDT-SWAP','BNB-USDT-SWAP','BNT-USDT-SWAP','BOME-USDT-SWAP','BONK-USDT-SWAP','BRETT-USDT-SWAP','BTC-USDT-SWAP','BTC-USDT-SWAP','CATI-USDT-SWAP','CAT-USDT-SWAP','CELO-USDT-SWAP','CETUS-USDT-SWAP','CFX-USDT-SWAP','CHZ-USDT-SWAP','COMP-USDT-SWAP','COOKIE-USDT-SWAP','CORE-USDT-SWAP','CRO-USDT-SWAP','CRV-USDT-SWAP','CSPR-USDT-SWAP','CTC-USDT-SWAP','CVC-USDT-SWAP','CVX-USDT-SWAP','DEGEN-USDT-SWAP','DGB-USDT-SWAP','DOGE-USDT-SWAP','DOGS-USDT-SWAP','DOG-USDT-SWAP','DOOD-USDT-SWAP','DOT-USDT-SWAP','DUCK-USDT-SWAP','DYDX-USDT-SWAP','EGLD-USDT-SWAP','EIGEN-USDT-SWAP','ENJ-USDT-SWAP','ENS-USDT-SWAP','ETC-USDT-SWAP','ETHFI-USDT-SWAP','ETH-USDT-SWAP','ETHW-USDT-SWAP','FARTCOIN-USDT-SWAP','FIL-USDT-SWAP','FLM-USDT-SWAP','FLOKI-USDT-SWAP','FLOW-USDT-SWAP','FXS-USDT-SWAP','GALA-USDT-SWAP','GAS-USDT-SWAP','GLM-USDT-SWAP','GMT-USDT-SWAP','GMX-USDT-SWAP','GOAT-USDT-SWAP','GODS-USDT-SWAP','GPS-USDT-SWAP','GRASS-USDT-SWAP','GRIFFAIN-USDT-SWAP','GRT-USDT-SWAP','HBAR-USDT-SWAP','HMSTR-USDT-SWAP','HOME-USDT-SWAP','HUMA-USDT-SWAP','HYPE-USDT-SWAP','ICP-USDT-SWAP','ICX-USDT-SWAP','ID-USDT-SWAP','IMX-USDT-SWAP','INIT-USDT-SWAP','INJ-USDT-SWAP','IOST-USDT-SWAP','IOTA-USDT-SWAP','IP-USDT-SWAP','JELLYJELLY-USDT-SWAP','JOE-USDT-SWAP','JST-USDT-SWAP','JTO-USDT-SWAP','JUP-USDT-SWAP','KAITO-USDT-SWAP','KMNO-USDT-SWAP','KNC-USDT-SWAP','KSM-USDT-SWAP','LAUNCHCOIN-USDT-SWAP','LA-USDT-SWAP','LAYER-USDT-SWAP','LDO-USDT-SWAP','LINK-USDT-SWAP','LOOKS-USDT-SWAP','LPT-USDT-SWAP','LQTY-USDT-SWAP','LRC-USDT-SWAP','LSK-USDT-SWAP','LTC-USDT-SWAP','LUNA-USDT-SWAP','LUNC-USDT-SWAP','MAGIC-USDT-SWAP','MAJOR-USDT-SWAP','MANA-USDT-SWAP','MASK-USDT-SWAP','MEME-USDT-SWAP','MERL-USDT-SWAP','METIS-USDT-SWAP','ME-USDT-SWAP','MEW-USDT-SWAP','MINA-USDT-SWAP','MKR-USDT-SWAP','MOODENG-USDT-SWAP','MORPHO-USDT-SWAP','MOVE-USDT-SWAP','MUBARAK-USDT-SWAP','NC-USDT-SWAP','NEAR-USDT-SWAP','NEIROETH-USDT-SWAP','NEIRO-USDT-SWAP','NEO-USDT-SWAP','NIL-USDT-SWAP','NMR-USDT-SWAP','NOT-USDT-SWAP','NXPC-USDT-SWAP','OL-USDT-SWAP','OM-USDT-SWAP','ONDO-USDT-SWAP','ONE-USDT-SWAP','ONT-USDT-SWAP','OP-USDT-SWAP','ORBS-USDT-SWAP','ORDI-USDT-SWAP','PARTI-USDT-SWAP','PENGU-USDT-SWAP','PEOPLE-USDT-SWAP','PEPE-USDT-SWAP','PERP-USDT-SWAP','PIPPIN-USDT-SWAP','PI-USDT-SWAP','PLUME-USDT-SWAP','PNUT-USDT-SWAP','POL-USDT-SWAP','POPCAT-USDT-SWAP','PRCL-USDT-SWAP','PROMPT-USDT-SWAP','PYTH-USDT-SWAP','QTUM-USDT-SWAP','RAY-USDT-SWAP','RDNT-USDT-SWAP','RENDER-USDT-SWAP','RESOLV-USDT-SWAP','RSR-USDT-SWAP','RVN-USDT-SWAP','SAND-USDT-SWAP','SATS-USDT-SWAP','SCR-USDT-SWAP','SHELL-USDT-SWAP','SHIB-USDT-SWAP','SIGN-USDT-SWAP','SLERF-USDT-SWAP','SLP-USDT-SWAP','SNX-USDT-SWAP','SOL-USDT-SWAP','SOLV-USDT-SWAP','SONIC-USDT-SWAP','SOON-USDT-SWAP','SOPH-USDT-SWAP','SSV-USDT-SWAP','STORJ-USDT-SWAP','STRK-USDT-SWAP','STX-USDT-SWAP','SUI-USDT-SWAP','S-USDT-SWAP','SUSHI-USDT-SWAP','SWARMS-USDT-SWAP','TAO-USDT-SWAP','THETA-USDT-SWAP','TIA-USDT-SWAP','TNSR-USDT-SWAP','TON-USDT-SWAP','TRB-USDT-SWAP','TRUMP-USDT-SWAP','TRX-USDT-SWAP','TURBO-USDT-SWAP','T-USDT-SWAP','UMA-USDT-SWAP','UNI-USDT-SWAP','USDC-USDT-SWAP','USTC-USDT-SWAP','UXLINK-USDT-SWAP','VANA-USDT-SWAP','VINE-USDT-SWAP','VIRTUAL-USDT-SWAP','WAL-USDT-SWAP','WAXP-USDT-SWAP','WCT-USDT-SWAP','WIF-USDT-SWAP','WLD-USDT-SWAP','WOO-USDT-SWAP','W-USDT-SWAP','XAUT-USDT-SWAP','XCH-USDT-SWAP','XLM-USDT-SWAP','XRP-USDT-SWAP','XTZ-USDT-SWAP','YFI-USDT-SWAP','YGG-USDT-SWAP','ZENT-USDT-SWAP','ZEREBRO-USDT-SWAP','ZETA-USDT-SWAP','ZIL-USDT-SWAP','ZK-USDT-SWAP','ZRO-USDT-SWAP','ZRX-USDT-SWAP']  # Add your desired trading pairs


rsi_period = 30
macd_fast = 12
macd_slow = 26
macd_signal = 9

timezone = pytz.timezone('Asia/Manila')

# ========== INIT EXCHANGE ==========
okx = ccxt.okx({'enableRateLimit': True})

def get_ohlcv(symbol, timeframe, limit=100):
    try:
        data = okx.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
        df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['datetime'] = pd.to_datetime(df['timestamp'], unit='ms')
        return df
    except Exception as e:
        print(f"[ERROR] Fetching {timeframe} data for {symbol}: {e}")
        return None

def add_indicators(df):
    rsi = RSIIndicator(df['close'], window=rsi_period)
    macd = MACD(df['close'], window_slow=macd_slow, window_fast=macd_fast, window_sign=macd_signal)
    df['rsi'] = rsi.rsi()
    df['macd'] = macd.macd()
    df['signal'] = macd.macd_signal()
    return df

def get_latest_macd_cross(df):
    for i in range(len(df) - 2, 0, -1):
        prev_macd = df['macd'].iloc[i]
        prev_signal = df['signal'].iloc[i]
        curr_macd = df['macd'].iloc[i + 1]
        curr_signal = df['signal'].iloc[i + 1]
        if pd.notna(prev_macd) and pd.notna(prev_signal):
            if prev_macd < prev_signal and curr_macd > curr_signal:
                return 'bullish'
            elif prev_macd > prev_signal and curr_macd < curr_signal:
                return 'bearish'
    return None

def is_rsi_above_50_or_crossing(df):
    if pd.isna(df['rsi'].iloc[-1]) or pd.isna(df['rsi'].iloc[-2]):
        return False
    return df['rsi'].iloc[-1] > 50 or (df['rsi'].iloc[-2] < 50 and df['rsi'].iloc[-1] > 50)

def send_discord_alert(symbol, message):
    now_manila = datetime.now(timezone).strftime('%Y-%m-%d %H:%M:%S')
    content = f"🔔🟢 Bullish Alert \n Symbol: {symbol}\nDate: {now_manila}\n================================"
    try:
        requests.post(DISCORD_WEBHOOK_URL, json={"content": content})
        print(f"[ALERT SENT] {symbol}")
    except Exception as e:
        print(f"[ERROR] Sending Discord alert for {symbol}: {e}")

# ========== MAIN RUN ==========
for symbol in symbols:
    print(f"\n🔍 Checking {symbol}...")

    # Fetch 4H data & check MACD bullish cross
    df_4h = get_ohlcv(symbol, '4h')
    if df_4h is None:
        continue
    df_4h = add_indicators(df_4h)
    if get_latest_macd_cross(df_4h) != 'bullish':
        print(f"[INFO] No recent bullish MACD cross on 4H for {symbol}")
        continue
    print(f"[✓] 4H Bullish MACD cross confirmed for {symbol}")

    # Fetch 1H data
    df_1h = get_ohlcv(symbol, '1h')
    if df_1h is None:
        continue
    df_1h = add_indicators(df_1h)

    if not is_rsi_above_50_or_crossing(df_1h):
        print(f"[INFO] RSI(30) not above or crossing 50 on 1H for {symbol}")
        continue
    print(f"[✓] 1H RSI(30) condition met for {symbol}")

    if get_latest_macd_cross(df_1h) != 'bearish':
        print(f"[INFO] No recent bearish MACD cross on 1H for {symbol}")
        continue
    print(f"[✓] 1H Bearish MACD cross confirmed for {symbol}")

    # Send Discord alert
    alert_message = (
        ""
      
    )
    send_discord_alert(symbol, alert_message)


#=============================================================================================

#1Day Bullish

import ccxt
import pandas as pd
import pytz
import os
import requests
from datetime import datetime
from ta.momentum import RSIIndicator
from ta.trend import MACD

# ========== CONFIG ==========
DISCORD_WEBHOOK_URL = os.getenv("ONE_DAY_WEBHOOK")  # Replace this

symbols = ['1INCH-USDT-SWAP','AAVE-USDT-SWAP','ACE-USDT-SWAP','ACH-USDT-SWAP','ACT-USDT-SWAP','ADA-USDT-SWAP','AEVO-USDT-SWAP','AGLD-USDT-SWAP','AI16Z-USDT-SWAP','AIDOGE-USDT-SWAP','AIXBT-USDT-SWAP','ALCH-USDT-SWAP','ALGO-USDT-SWAP','ALPHA-USDT-SWAP','ANIME-USDT-SWAP','APE-USDT-SWAP','API3-USDT-SWAP','APT-USDT-SWAP','ARB-USDT-SWAP','ARC-USDT-SWAP','ARKM-USDT-SWAP','AR-USDT-SWAP','ATH-USDT-SWAP','ATOM-USDT-SWAP','AUCTION-USDT-SWAP','A-USDT-SWAP','AVAAI-USDT-SWAP','AVAX-USDT-SWAP','AXS-USDT-SWAP','BABY-USDT-SWAP','BADGER-USDT-SWAP','BAL-USDT-SWAP','BAND-USDT-SWAP','BAT-USDT-SWAP','BCH-USDT-SWAP','BERA-USDT-SWAP','BICO-USDT-SWAP','BIGTIME-USDT-SWAP','BIO-USDT-SWAP','BLUR-USDT-SWAP','BNB-USDT-SWAP','BNT-USDT-SWAP','BOME-USDT-SWAP','BONK-USDT-SWAP','BRETT-USDT-SWAP','BTC-USDT-SWAP','BTC-USDT-SWAP','CATI-USDT-SWAP','CAT-USDT-SWAP','CELO-USDT-SWAP','CETUS-USDT-SWAP','CFX-USDT-SWAP','CHZ-USDT-SWAP','COMP-USDT-SWAP','COOKIE-USDT-SWAP','CORE-USDT-SWAP','CRO-USDT-SWAP','CRV-USDT-SWAP','CSPR-USDT-SWAP','CTC-USDT-SWAP','CVC-USDT-SWAP','CVX-USDT-SWAP','DEGEN-USDT-SWAP','DGB-USDT-SWAP','DOGE-USDT-SWAP','DOGS-USDT-SWAP','DOG-USDT-SWAP','DOOD-USDT-SWAP','DOT-USDT-SWAP','DUCK-USDT-SWAP','DYDX-USDT-SWAP','EGLD-USDT-SWAP','EIGEN-USDT-SWAP','ENJ-USDT-SWAP','ENS-USDT-SWAP','ETC-USDT-SWAP','ETHFI-USDT-SWAP','ETH-USDT-SWAP','ETHW-USDT-SWAP','FARTCOIN-USDT-SWAP','FIL-USDT-SWAP','FLM-USDT-SWAP','FLOKI-USDT-SWAP','FLOW-USDT-SWAP','FXS-USDT-SWAP','GALA-USDT-SWAP','GAS-USDT-SWAP','GLM-USDT-SWAP','GMT-USDT-SWAP','GMX-USDT-SWAP','GOAT-USDT-SWAP','GODS-USDT-SWAP','GPS-USDT-SWAP','GRASS-USDT-SWAP','GRIFFAIN-USDT-SWAP','GRT-USDT-SWAP','HBAR-USDT-SWAP','HMSTR-USDT-SWAP','HOME-USDT-SWAP','HUMA-USDT-SWAP','HYPE-USDT-SWAP','ICP-USDT-SWAP','ICX-USDT-SWAP','ID-USDT-SWAP','IMX-USDT-SWAP','INIT-USDT-SWAP','INJ-USDT-SWAP','IOST-USDT-SWAP','IOTA-USDT-SWAP','IP-USDT-SWAP','JELLYJELLY-USDT-SWAP','JOE-USDT-SWAP','JST-USDT-SWAP','JTO-USDT-SWAP','JUP-USDT-SWAP','KAITO-USDT-SWAP','KMNO-USDT-SWAP','KNC-USDT-SWAP','KSM-USDT-SWAP','LAUNCHCOIN-USDT-SWAP','LA-USDT-SWAP','LAYER-USDT-SWAP','LDO-USDT-SWAP','LINK-USDT-SWAP','LOOKS-USDT-SWAP','LPT-USDT-SWAP','LQTY-USDT-SWAP','LRC-USDT-SWAP','LSK-USDT-SWAP','LTC-USDT-SWAP','LUNA-USDT-SWAP','LUNC-USDT-SWAP','MAGIC-USDT-SWAP','MAJOR-USDT-SWAP','MANA-USDT-SWAP','MASK-USDT-SWAP','MEME-USDT-SWAP','MERL-USDT-SWAP','METIS-USDT-SWAP','ME-USDT-SWAP','MEW-USDT-SWAP','MINA-USDT-SWAP','MKR-USDT-SWAP','MOODENG-USDT-SWAP','MORPHO-USDT-SWAP','MOVE-USDT-SWAP','MUBARAK-USDT-SWAP','NC-USDT-SWAP','NEAR-USDT-SWAP','NEIROETH-USDT-SWAP','NEIRO-USDT-SWAP','NEO-USDT-SWAP','NIL-USDT-SWAP','NMR-USDT-SWAP','NOT-USDT-SWAP','NXPC-USDT-SWAP','OL-USDT-SWAP','OM-USDT-SWAP','ONDO-USDT-SWAP','ONE-USDT-SWAP','ONT-USDT-SWAP','OP-USDT-SWAP','ORBS-USDT-SWAP','ORDI-USDT-SWAP','PARTI-USDT-SWAP','PENGU-USDT-SWAP','PEOPLE-USDT-SWAP','PEPE-USDT-SWAP','PERP-USDT-SWAP','PIPPIN-USDT-SWAP','PI-USDT-SWAP','PLUME-USDT-SWAP','PNUT-USDT-SWAP','POL-USDT-SWAP','POPCAT-USDT-SWAP','PRCL-USDT-SWAP','PROMPT-USDT-SWAP','PYTH-USDT-SWAP','QTUM-USDT-SWAP','RAY-USDT-SWAP','RDNT-USDT-SWAP','RENDER-USDT-SWAP','RESOLV-USDT-SWAP','RSR-USDT-SWAP','RVN-USDT-SWAP','SAND-USDT-SWAP','SATS-USDT-SWAP','SCR-USDT-SWAP','SHELL-USDT-SWAP','SHIB-USDT-SWAP','SIGN-USDT-SWAP','SLERF-USDT-SWAP','SLP-USDT-SWAP','SNX-USDT-SWAP','SOL-USDT-SWAP','SOLV-USDT-SWAP','SONIC-USDT-SWAP','SOON-USDT-SWAP','SOPH-USDT-SWAP','SSV-USDT-SWAP','STORJ-USDT-SWAP','STRK-USDT-SWAP','STX-USDT-SWAP','SUI-USDT-SWAP','S-USDT-SWAP','SUSHI-USDT-SWAP','SWARMS-USDT-SWAP','TAO-USDT-SWAP','THETA-USDT-SWAP','TIA-USDT-SWAP','TNSR-USDT-SWAP','TON-USDT-SWAP','TRB-USDT-SWAP','TRUMP-USDT-SWAP','TRX-USDT-SWAP','TURBO-USDT-SWAP','T-USDT-SWAP','UMA-USDT-SWAP','UNI-USDT-SWAP','USDC-USDT-SWAP','USTC-USDT-SWAP','UXLINK-USDT-SWAP','VANA-USDT-SWAP','VINE-USDT-SWAP','VIRTUAL-USDT-SWAP','WAL-USDT-SWAP','WAXP-USDT-SWAP','WCT-USDT-SWAP','WIF-USDT-SWAP','WLD-USDT-SWAP','WOO-USDT-SWAP','W-USDT-SWAP','XAUT-USDT-SWAP','XCH-USDT-SWAP','XLM-USDT-SWAP','XRP-USDT-SWAP','XTZ-USDT-SWAP','YFI-USDT-SWAP','YGG-USDT-SWAP','ZENT-USDT-SWAP','ZEREBRO-USDT-SWAP','ZETA-USDT-SWAP','ZIL-USDT-SWAP','ZK-USDT-SWAP','ZRO-USDT-SWAP','ZRX-USDT-SWAP']  # Add your desired trading pairs


macd_fast = 12
macd_slow = 26
macd_signal = 9
rsi_period = 30

timezone = pytz.timezone('Asia/Manila')
okx = ccxt.okx({'enableRateLimit': True})

# ========== FUNCTIONS ==========

def get_ohlcv(symbol, timeframe, limit=100):
    try:
        ohlcv = okx.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
        df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['datetime'] = pd.to_datetime(df['timestamp'], unit='ms')
        return df
    except Exception as e:
        print(f"[ERROR] Fetching {timeframe} data for {symbol}: {e}")
        return None

def add_indicators(df):
    rsi = RSIIndicator(df['close'], window=rsi_period)
    macd = MACD(df['close'], window_slow=macd_slow, window_fast=macd_fast, window_sign=macd_signal)
    df['rsi'] = rsi.rsi()
    df['macd'] = macd.macd()
    df['signal'] = macd.macd_signal()
    return df

def get_latest_macd_cross(df):
    for i in range(len(df) - 2, 0, -1):
        prev_macd = df['macd'].iloc[i]
        prev_signal = df['signal'].iloc[i]
        curr_macd = df['macd'].iloc[i + 1]
        curr_signal = df['signal'].iloc[i + 1]
        if pd.notna(prev_macd) and pd.notna(prev_signal):
            if prev_macd < prev_signal and curr_macd > curr_signal:
                return 'bullish'
            elif prev_macd > prev_signal and curr_macd < curr_signal:
                return 'bearish'
    return None

def is_rsi_above_50_or_crossing(df):
    if pd.isna(df['rsi'].iloc[-1]) or pd.isna(df['rsi'].iloc[-2]):
        return False
    return df['rsi'].iloc[-1] > 50 or (df['rsi'].iloc[-2] < 50 and df['rsi'].iloc[-1] > 50)

def send_discord_alert(symbol, message):
    now_manila = datetime.now(timezone).strftime('%Y-%m-%d %H:%M:%S')
    content = f"🔔🟢 Bullish Alert \n Symbol: {symbol}\nDate: {now_manila}\n=================================="
    try:
        requests.post(DISCORD_WEBHOOK_URL, json={"content": content})
        print(f"[ALERT SENT] {symbol}")
    except Exception as e:
        print(f"[ERROR] Sending Discord alert: {e}")

# ========== MAIN ==========
for symbol in symbols:
    print(f"\n🔍 Checking {symbol}...")

    # 1D MACD Bullish Cross
    df_1d = get_ohlcv(symbol, '1d')
    if df_1d is None:
        continue
    df_1d = add_indicators(df_1d)
    if get_latest_macd_cross(df_1d) != 'bullish':
        print(f"[INFO] No bullish MACD cross on 1D for {symbol}")
        continue
    print(f"[✓] 1D MACD Bullish cross detected for {symbol}")

    # 4H RSI > 50 or crossed
    df_4h = get_ohlcv(symbol, '4h')
    if df_4h is None:
        continue
    df_4h = add_indicators(df_4h)
    if not is_rsi_above_50_or_crossing(df_4h):
        print(f"[INFO] RSI(30) not above or crossing 50 on 4H for {symbol}")
        continue
    print(f"[✓] 4H RSI(30) > 50 or crossing confirmed for {symbol}")

    # 4H MACD Bearish Cross
    if get_latest_macd_cross(df_4h) != 'bearish':
        print(f"[INFO] No bearish MACD cross on 4H for {symbol}")
        continue
    print(f"[✓] 4H MACD Bearish cross detected for {symbol}")

    # All conditions met - Send alert
    alert_message = (
        ""
        
    )
    send_discord_alert(symbol, alert_message)

#============================================================================================





