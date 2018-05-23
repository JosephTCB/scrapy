from WXBizDataCrypt import WXBizDataCrypt

def main():
    appId = 'wx98279ca8a9547044'
    sessionKey = 'tiihtNczf"Lpq2+zliAL+g128qoEDGoE8B1Bp1ctMismckxAvcV1MYg4nmRAtt14UIFhfJJE5YsLrVc1tbKZP3Obn/osvYQXNl21tQIWJ6UrxZcUiSOT1UMAb4RbeOo1JSfK/dSMjOicTVyIa/Ja1oGP/ED0j1cOkJnV9xa4IsTvKCouCSb3iB2VzXjdJbMrv8rJdODxjueZMhiKU4Y8l6lqtEz8l+NtpCWZ4heXrJruq/pWDzwHiwhxh5pb6HU/Z8siZGcmHsspxNxSi4P/aomkhGwqwud2F4Fp9f2xkbscUWfrtNdFq68Kq81ugDr4/8nVlO1f1EsPBrpliPFD9FyAin+EJeSwL1M74TzJCd81/FapZuAXvToG0mcQ2FNhotutB/JAQQllZTcsjQjC2s6yMe5fknXo7YT4z8Fwheie/geShtBVsZl30YXZfUL8gIeVr5fXbr1Zfqio9uq7HkJjvEutnyDg=="5v6AKRyjwEUhQ=='
    encryptedData = 'Lpq2+zliAL+g128qoEDGoE8B1Bp1ctMismckxAvcV1MYg4nmRAtt14UIFhfJJE5YsLrVc1tbKZP3Obn/osvYQXNl21tQIWJ6UrxZcUiSOT1UMAb4RbeOo1JSfK/dSMjOicTVyIa/Ja1oGP/ED0j1cOkJnV9xa4IsTvKCouCSb3iB2VzXjdJbMrv8rJdODxjueZMhiKU4Y8l6lqtEz8l+NtpCWZ4heXrJruq/pWDzwHiwhxh5pb6HU/Z8siZGcmHsspxNxSi4P/aomkhGwqwud2F4Fp9f2xkbscUWfrtNdFq68Kq81ugDr4/8nVlO1f1EsPBrpliPFD9FyAin+EJeSwL1M74TzJCd81/FapZuAXvToG0mcQ2FNhotutB/JAQQllZTcsjQjC2s6yMe5fknXo7YT4z8Fwheie/geShtBVsZl30YXZfUL8gIeVr5fXbr1Zfqio9uq7HkJjvEutnyDg=='
    iv = 'NWodoZj3YHkgriSD+Yfj3Q=='

    pc = WXBizDataCrypt(appId, sessionKey)

    print(pc.decrypt(encryptedData, iv))

if __name__ == '__main__':
    main()
