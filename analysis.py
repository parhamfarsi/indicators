import numpy as np

def analyze_indicators(all_data):
    sar = all_data['SAR']
    rsi_values = all_data['RSI']
    k, d = all_data['k'],all_data['d']
    obv_values = all_data['OBV']
    mfi_values = all_data['MFI']
    middle_band, upper_band, lower_band = (
        all_data['Middle_band'],
        all_data['Upper_band'],
        all_data['Lower_band']
    )
    atr_values = all_data['ATR']
    sma_values = all_data['SMA']
    ema_values = all_data['EMA']
    close = all_data['Price']  

    signals_all_days = []

    # loop through all days
    for i in range(len(close)):
        # skip if any of the indicators for this day is NaN
        if (
            np.isnan(sar[i]) or np.isnan(rsi_values[i]) or 
            np.isnan(k[i]) or np.isnan(d[i]) or
            np.isnan(obv_values[i]) or np.isnan(mfi_values[i]) or
            np.isnan(middle_band[i]) or np.isnan(upper_band[i]) or np.isnan(lower_band[i]) or
            np.isnan(atr_values[i]) or np.isnan(sma_values[i]) or np.isnan(ema_values[i])
        ):
            signals_all_days.append(None)  # no signal for this day
            continue

        signals = []

        # 1. Parabolic SAR Signal
        if sar[i] < close[i]:
            signals.append('Buy')
        else:
            signals.append('Sell')

        # 2. RSI Signal
        if rsi_values[i] < 30:
            signals.append('Buy')
        elif rsi_values[i] > 70:
            signals.append('Sell')
        else:
            signals.append('Hold')

        # 3. Stochastic Oscillator Signal
        if k[i] > d[i] and k[i] < 20 and d[i] < 20:
            signals.append('Buy')
        elif k[i] < d[i] and k[i] > 80 and d[i] > 80:
            signals.append('Sell')
        else:
            signals.append('Hold')

        # 4. OBV Signal
        price_change = close[i] - close[i-1] if i >= 1 else 0
        obv_change = obv_values[i] - obv_values[i-1] if i >= 1 else 0
        if price_change > 0 and obv_change > 0:
            signals.append('Buy')
        elif price_change < 0 and obv_change < 0:
            signals.append('Sell')
        else:
            signals.append('Hold')

        # 5. MFI Signal
        if mfi_values[i] < 20:
            signals.append('Buy')
        elif mfi_values[i] > 80:
            signals.append('Sell')
        else:
            signals.append('Hold')

        # 6. Bollinger Bands Signal
        if close[i] <= lower_band[i]:
            signals.append('Buy')
        elif close[i] >= upper_band[i]:
            signals.append('Sell')
        else:
            signals.append('Hold')

        # 7. SMA Signal
        if abs(close[i] - sma_values[i]) / sma_values[i] < 0.01:
            signals.append('Hold')
        elif close[i] > sma_values[i]:
            signals.append('Buy')
        else:
            signals.append('Sell')

        # 8. EMA Signal
        if abs(close[i] - ema_values[i]) / ema_values[i] < 0.01:
            signals.append('Hold')
        elif close[i] > ema_values[i]:
            signals.append('Buy')
        else:
            signals.append('Sell')

        # majority voting
        buy_count = signals.count('Buy')
        sell_count = signals.count('Sell')
        hold_count = signals.count('Hold')

        if buy_count > sell_count and buy_count > hold_count:
            signals_all_days.append('Buy')
        elif sell_count > buy_count and sell_count > hold_count:
            signals_all_days.append('Sell')
        else:
            signals_all_days.append('Hold')

    return signals_all_days
