<p>银行发起变更银行账号通知，无Req属于私有流回报</p>
<span class="anchor" id="a79f0c30-b03e-4ecd-98f7-7b8651234193"></span>
## 1.函数原型
<p>virtual void OnRtnChangeAccountByBank(CThostFtdcChangeAccountField *pChangeAccount) {};</p>
<span class="anchor" id="68d6e97c-b6b4-4d90-ba1b-1a9f14511329"></span>
## 2.参数
<p>pChangeAccount：银期变更银行账号信息</p>
<pre><code>struct CThostFtdcChangeAccountField
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
    ///新银行帐号
    TThostFtdcBankAccountType NewBankAccount;
    ///新银行密码
    TThostFtdcPasswordType NewBankPassWord;
    ///投资者帐号
    TThostFtdcAccountIDType AccountID;
    ///期货密码
    TThostFtdcPasswordType Password;
    ///银行帐号类型
    TThostFtdcBankAccTypeType BankAccType;
    ///安装编号
    TThostFtdcInstallIDType InstallID;
    ///验证客户证件号码标志
    TThostFtdcYesNoIndicatorType VerifyCertNoFlag;
    ///币种代码
    TThostFtdcCurrencyIDType CurrencyID;
    ///期货公司银行编码
    TThostFtdcBankCodingForFutureType BrokerIDByBank;
    ///银行密码标志
    TThostFtdcPwdFlagType BankPwdFlag;
    ///期货资金密码核对标志
    TThostFtdcPwdFlagType SecuPwdFlag;
    ///交易ID
    TThostFtdcTIDType TID;
    ///摘要
    TThostFtdcDigestType Digest;
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
    ///长客户姓名
    TThostFtdcLongIndividualNameType LongCustomerName;
};
</code></pre>
<p>TradeCode：101003 银行发起银行账号变更</p>
<p>BankBranchID：填0000</p>
<p>BrokerBranchID：一般为空</p>
<p>InstallID：CTP内部使用</p>
<span class="anchor" id="ca69a41a-864e-4cd9-82f4-5a12507686d2"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="ba25f9ea-58e3-421d-a428-cef6817675e9"></span>
## 4.FAQ
<p>无</p>
