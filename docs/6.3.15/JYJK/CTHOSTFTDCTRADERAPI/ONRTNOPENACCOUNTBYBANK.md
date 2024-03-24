<p>银行发起银期开户通知，无Req属于私有流回报</p>
<span class="anchor" id="35dedaab-bb57-4365-9324-0d06c0b9cc0c"></span>
## 1.函数原型
<p>virtual void OnRtnOpenAccountByBank(CThostFtdcOpenAccountField *pOpenAccount) {};</p>
<span class="anchor" id="6d2ffa88-1b99-41c3-aca9-2b91490f64a1"></span>
## 2.参数
<p>pOpenAccount：银期开户信息</p>
<pre><code>struct CThostFtdcOpenAccountField
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
    ///性别
    TThostFtdcGenderType Gender;
    ///国家代码
    TThostFtdcCountryCodeType CountryCode;
    ///客户类型
    TThostFtdcCustTypeType CustType;
    ///地址
    TThostFtdcAddressType Address;
    ///邮编
    TThostFtdcZipCodeType ZipCode;
    ///电话号码
    TThostFtdcTelephoneType Telephone;
    ///手机
    TThostFtdcMobilePhoneType MobilePhone;
    ///传真
    TThostFtdcFaxType Fax;
    ///电子邮件
    TThostFtdcEMailType EMail;
    ///资金账户状态
    TThostFtdcMoneyAccountStatusType MoneyAccountStatus;
    ///银行帐号
    TThostFtdcBankAccountType BankAccount;
    ///银行密码
    TThostFtdcPasswordType BankPassWord;
    ///投资者帐号
    TThostFtdcAccountIDType AccountID;
    ///期货密码
    TThostFtdcPasswordType Password;
    ///安装编号
    TThostFtdcInstallIDType InstallID;
    ///验证客户证件号码标志
    TThostFtdcYesNoIndicatorType VerifyCertNoFlag;
    ///币种代码
    TThostFtdcCurrencyIDType CurrencyID;
    ///汇钞标志
    TThostFtdcCashExchangeCodeType CashExchangeCode;
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
    ///交易ID
    TThostFtdcTIDType TID;
    ///用户标识
    TThostFtdcUserIDType UserID;
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
    ///长客户姓名
    TThostFtdcLongIndividualNameType LongCustomerName;
};
</code></pre>
<p>TradeCode：101001 银行发起转账开户</p>
<p>BankBranchID：填0000</p>
<p>BrokerBranchID：一般为空</p>
<p>InstallID：CTP内部使用</p>
<span class="anchor" id="fd3fe16e-cc4d-4c40-a07f-28673d40ee9d"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="2954ad47-aec6-468e-9b27-c2bc36267519"></span>
## 4.FAQ
<p>无</p>
