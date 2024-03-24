<p>期货发起查询银行余额通知，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQUERYBANKACCOUNTMONEYBYFUTURE/">ReqQueryBankAccountMoneyByFuture</a>后并且报出后，收到返回则调用此接口，私有流回报。</p>
<span class="anchor" id="5a40cc56-0535-4eea-aedc-97359c534885"></span>
## 1.函数原型
<p>virtual void OnRtnQueryBankBalanceByFuture(CThostFtdcNotifyQueryAccountField *pNotifyQueryAccount) {};</p>
<span class="anchor" id="92674696-0c51-4899-a780-8a04db997a80"></span>
## 2.参数
<p>pNotifyQueryAccount：查询账户信息通知</p>
<pre><code>struct CThostFtdcNotifyQueryAccountField
{
    ///业务功能码
    TThostFtdcTradeCodeType TradeCode;
    ///银行代码
    TThostFtdcBankIDType BankID;
    ///银行分支机构代码
    TThostFtdcBankBrchIDType BankBranchID;
    ///期商代码
    TThostFtdcBrokerIDType BrokerID;
    ///期商分支机构代码
    TThostFtdcFutureBranchIDType BrokerBranchID;
    ///交易日期
    TThostFtdcTradeDateType TradeDate;
    ///交易时间
    TThostFtdcTradeTimeType TradeTime;
    ///银行流水号
    TThostFtdcBankSerialType BankSerial;
    ///交易系统日期 
    TThostFtdcTradeDateType TradingDay;
    ///银期平台消息流水号
    TThostFtdcSerialType PlateSerial;
    ///最后分片标志
    TThostFtdcLastFragmentType LastFragment;
    ///会话号
    TThostFtdcSessionIDType SessionID;
    ///客户姓名
    TThostFtdcIndividualNameType CustomerName;
    ///证件类型
    TThostFtdcIdCardTypeType IdCardType;
    ///证件号码
    TThostFtdcIdentifiedCardNoType IdentifiedCardNo;
    ///客户类型
    TThostFtdcCustTypeType CustType;
    ///银行帐号
    TThostFtdcBankAccountType BankAccount;
    ///银行密码
    TThostFtdcPasswordType BankPassWord;
    ///投资者帐号
    TThostFtdcAccountIDType AccountID;
    ///期货密码
    TThostFtdcPasswordType Password;
    ///期货公司流水号
    TThostFtdcFutureSerialType FutureSerial;
    ///安装编号
    TThostFtdcInstallIDType InstallID;
    ///用户标识
    TThostFtdcUserIDType UserID;
    ///验证客户证件号码标志
    TThostFtdcYesNoIndicatorType VerifyCertNoFlag;
    ///币种代码
    TThostFtdcCurrencyIDType CurrencyID;
    ///摘要
    TThostFtdcDigestType Digest;
    ///银行帐号类型
    TThostFtdcBankAccTypeType BankAccType;
    ///渠道标志
    TThostFtdcDeviceIDType DeviceID;
    ///期货单位帐号类型
    TThostFtdcBankAccTypeType BankSecuAccType;
    ///期货公司银行编码
    TThostFtdcBankCodingForFutureType BrokerIDByBank;
    ///期货单位帐号
    TThostFtdcBankAccountType BankSecuAcc;
    ///银行密码标志
    TThostFtdcPwdFlagType BankPwdFlag;
    ///期货资金密码核对标志
    TThostFtdcPwdFlagType SecuPwdFlag;
    ///交易柜员
    TThostFtdcOperNoType OperNo;
    ///请求编号
    TThostFtdcRequestIDType RequestID;
    ///交易ID
    TThostFtdcTIDType TID;
    ///银行可用金额
    TThostFtdcTradeAmountType BankUseAmount;
    ///银行可取金额
    TThostFtdcTradeAmountType BankFetchAmount;
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
    ///长客户姓名
    TThostFtdcLongIndividualNameType LongCustomerName;
};
</code></pre>
<p>TradeCode: 204002 期货发起查询银行余额</p>
<p>BankBranchID：填0000</p>
<p>BrokerBranchID：一般为空</p>
<p>BankPassWord：为密文，显示为“*”</p>
<p>Password: 为密文，显示为“*”</p>
<p>ErrorMsg：返回是否成功的回报</p>
<span class="anchor" id="ea0aebef-fa2c-4c81-9deb-13cb749a11d9"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="b9609401-1524-47e0-82d8-178d2b19e253"></span>
## 4.FAQ
<p>无</p>
