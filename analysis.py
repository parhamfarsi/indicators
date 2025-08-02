import numpy as np
import pandas as pd 
import functions as f

def analyze_indicators(high, low, close, volume):

    sar = f.parabolic_sar(high, low)
    rsi_values = f.rsi(close)
    k, d = f.stochastic_oscillator(high, low, close)
    obv_values = f.obv(close, volume)
    mfi_values = f.mfi(high, low, close, volume)
    middle_band, upper_band, lower_band = f.bollinger_bands(close)
    atr_values = f.atr(high, low, close)
    sma_values = f.sma(close)
    ema_values = f.ema(close)

    signals = []

    # 1. Parabolic SAR Signal
    if sar[-1] < close[-1]:
        signals.append('Buy')
    else:
        signals.append('Sell')

    # 2. RSI Signal
    if rsi_values[-1] < 30:
        signals.append('Buy')
    elif rsi_values[-1] > 70:
        signals.append('Sell')
    else:
        signals.append('Hold')

    # 3. Stochastic Oscillator Signal
    if k[-1] > d[-1] and k[-1] < 20 and d[-1] < 20:
        signals.append('Buy')
    elif k[-1] < d[-1] and k[-1] > 80 and d[-1] > 80:
        signals.append('Sell')
    else:
        signals.append('Hold')

    # 4. OBV Signal
    price_change = close[-1] - close[-2] if len(close) >= 2 else 0
    obv_change = obv_values[-1] - obv_values[-2] if len(obv_values) >= 2 else 0
    if price_change > 0 and obv_change > 0:
        signals.append('Buy')
    elif price_change < 0 and obv_change < 0:
        signals.append('Sell')
    else:
        signals.append('Hold')

    # 5. MFI Signal
    if mfi_values[-1] < 20:
        signals.append('Buy')
    elif mfi_values[-1] > 80:
        signals.append('Sell')
    else:
        signals.append('Hold')

    # 6. Bollinger Bands Signal
    if close[-1] <= lower_band[-1]:
        signals.append('Buy')
    elif close[-1] >= upper_band[-1]:
        signals.append('Sell')
    else:
        signals.append('Hold')

    # 7. SMA Signal
    if abs(close[-1] - sma_values[-1]) / sma_values[-1] < 0.01:
        signals.append('Hold')
    elif close[-1] > sma_values[-1]:
        signals.append('Buy')
    else:
        signals.append('Sell')

    # 8. EMA Signal
    if abs(close[-1] - ema_values[-1]) / ema_values[-1] < 0.01:
        signals.append('Hold')
    elif close[-1] > ema_values[-1]:
        signals.append('Buy')
    else:
        signals.append('Sell')


    buy_count = signals.count('Buy')
    sell_count = signals.count('Sell')
    hold_count = signals.count('Hold')

    #print(buy_count)
    #print(sell_count)
    #print(hold_count)


    if buy_count > sell_count and buy_count > hold_count:
        return 'Buy'
    elif sell_count > buy_count and sell_count > hold_count:
        return 'Sell'
    else:
        return 'Hold'

