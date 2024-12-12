<p>银行发起银期开户通知，无Req属于私有流回报</p>
<span class="anchor" id="b04d1859-9281-47ae-8dc2-565505ad078c"></span>
## 1.函数原型
<p>virtual void OnRtnOpenAccountByBank(CThostFtdcOpenAccountField *pOpenAccount) {};</p>
<span class="anchor" id="96ae0753-b0f0-45b9-9dde-6ef6763e620c"></span>
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
<span class="anchor" id="c37c9cf7-df1b-43e8-9ee0-fce030efa416"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="d087eece-71d7-4a39-8e11-c5eacf46801a"></span>
## 4.FAQ
<p>无</p>
