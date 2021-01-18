while True:
    print("Which currency do you want to stack up?")
    print("1. BTC 💰")
    print("2. USD 💵")

    based_input = input("Choose your currency (Default = BTC) : ") or 'BTC'
    print()

    if (based_input == '1') or (based_input == 'btc') or (based_input == 'BTC') or (based_input == 'bitcoin') or (based_input == 'bit'):
        base = "BTC"
        round_off = 6
        while True:
            print("Here are the supported Pairs: ")
            print("1. BNB-BTC")
            print("2. LINK-BTC 🔥")
            print("3. SUSHI-BTC 🔥")
            print("4. 1INCH-BTC")
            print("5. TRX-BTC")
            print("6. XRP-BTC")

            asset_input = input("Choose your Pair (Default SUSHI) : ") or 'SUSHI'
            if (asset_input == '1') or (asset_input == 'bnb') or (asset_input == 'BNB'):
                asset = "BNB"
                break
            elif (asset_input == '2') or (asset_input == 'link') or (asset_input == 'LINK'):
                asset = "LINK"
                break
            elif (asset_input == '3') or (asset_input == 'sushi') or (asset_input == 'SUSHI'):
                asset = "SUSHI"
                break
            elif (asset_input == '4') or (asset_input == '1inch') or (asset_input == '1INCH'):
                asset = "1INCH"
                break
            elif (asset_input == '5') or (asset_input == 'trx') or (asset_input == 'TRX'):
                asset = "TRX"
                break
            elif (asset_input == '6') or (asset_input == 'xrp') or (asset_input == 'XRP'):
                asset = "XRP"
                break
            else: print("❗Invalid Number❗Try again❗\n")

        pair = asset + base
        core_input = input("\nSet your Core Number for " + asset + "-" + base + " (Default 0.003) : ") or 0.003
        break

    elif (based_input == '2') or (based_input == 'usdt') or (based_input == 'USDT') or (based_input == 'usd') or (based_input == 'USD'):
        base = "USDT"
        round_off = 4
        while True:
            print("Here are the supported Pairs: ")
            print("1. BTC-USDT")
            print("2. ETH-USDT 🔥")
            print("3. BNB-USDT")
            print("4. LINK-USDT")
            print("5. SUSHI-USDT")
            print("6. 1INCH-USDT")
            print("7. TRX-USDT")
            print("8. XRP-USDT")

            asset_input = input("Choose your Pair (Default = ETH) : ") or 'ETH'
            if (asset_input == '1') or (asset_input == 'btc') or (asset_input == 'BTC'):
                asset = "BTC"
                break
            elif (asset_input == '2') or (asset_input == 'eth') or (asset_input == 'ETH'):
                asset = "ETH"
                break
            elif (asset_input == '3') or (asset_input == 'bnb') or (asset_input == 'BNB'):
                asset = "BNB"
                break
            elif (asset_input == '4') or (asset_input == 'link') or (asset_input == 'LINK'):
                asset = "LINK"
                break
            elif (asset_input == '5') or (asset_input == 'sushi') or (asset_input == 'SUSHI'):
                asset = "SUSHI"
                break
            elif (asset_input == '6') or (asset_input == '1inch') or (asset_input == '1INCH'):
                asset = "1INCH"
                break
            elif (asset_input == '7') or (asset_input == 'trx') or (asset_input == 'TRX'):
                asset = "TRX"
                break
            elif (asset_input == '8') or (asset_input == 'xrp') or (asset_input == 'XRP'):
                asset = "XRP"
                break
            else: print("❗Invalid Number❗Try again❗\n")

        pair =  asset + base
        core_input = input("\nSet your Core Number for " + asset + "-" + base + " (Default 300) : ") or 300
        break

    else: print("❗Invalid Number❗Try again❗\n")

core = float(core_input)
real_trade_input = input("Trade For Real? [Y/n] ") or 'n'
if real_trade_input == 'Y': 
    live_trade = True
    print("✅ " + str(live_trade))
else: 
    live_trade = False
    print("❌ " + str(live_trade))

print("Pair :   " + asset + "-" + base)
print("Core :   " + str(core) + "\n")
