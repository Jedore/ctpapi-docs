<p>期货发起查询银行余额错误回报，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQUERYBANKACCOUNTMONEYBYFUTURE/">ReqQueryBankAccountMoneyByFuture</a>后有字段填写不对之类的CTP报错则通过此接口返回</p>
<span class="anchor" id="c8f578d9-7ffc-49ab-ac70-09d0038d5f22"></span>
## 1.函数原型
<p>virtual void OnErrRtnQueryBankBalanceByFuture(CThostFtdcReqQueryAccountField *pReqQueryAccount, CThostFtdcRspInfoField *pRspInfo) {};</p>
<span class="anchor" id="e9034938-1a17-4f98-bb00-36b136b57b77"></span>
## 2.参数
<p>pReqQueryAccount：查询账户信息请求</p>
<pre><code>struct CThostFtdcReqQueryAccountField
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
    ///长客户姓名
    TThostFtdcLongIndividualNameType LongCustomerName;
};
</code></pre>
<p>TradeCode: 204002期货发起查询银行余额</p>
<p>BankID：返回银行在期货公司的代码</p>
<p>BankBranchID：填0000</p>
<p>BrokerBranchID：一般为空</p>
<p>CustomerName：客户姓名</p>
<p>BankPassWord：返回银行的密码，都是“*”密码不显示，</p>
<p>Password：返回期货账户的密码，都是“*”密码不显示</p>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<span class="anchor" id="59225df6-58e4-4358-9602-543c9b7c53d9"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="e2e8c109-44ed-4e4b-bb3e-b45c96036d05"></span>
## 4.FAQ
<p>无</p>
