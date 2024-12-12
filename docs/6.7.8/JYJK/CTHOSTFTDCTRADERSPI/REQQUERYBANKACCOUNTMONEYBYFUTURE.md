<p>期货发起查询银行余额请求</p>
<p>错误响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRSPQUERYBANKACCOUNTMONEYBYFUTURE/">OnRspQueryBankAccountMoneyByFuture</a></p>
<p>正确响应: <a href="../../CTHOSTFTDCTRADERAPI/ONRTNQUERYBANKBALANCEBYFUTURE/">OnRtnQueryBankBalanceByFuture</a></p>
<span class="anchor" id="1c7e93c2-996e-48d8-ba94-66d932aecdc9"></span>
## 1.函数原型
<p>virtual int ReqQueryBankAccountMoneyByFuture(CThostFtdcReqQueryAccountField *pReqQueryAccount, int nRequestID) = 0;</p>
<span class="anchor" id="cfd16c8c-0aa2-4564-ab65-23f88dd604c2"></span>
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
<p>TradeCode：204002 期货发起查询银行余额</p>
<p>BankBranchID：填0000</p>
<p>InstallID：ctp内部使用，不用填</p>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<p><span alt="" id="anchor-id-01"></span> </p>
<p>Brokerid:必填项</p>
<p>InvestorID:必填项</p>
<p>UserID:必填项</p>
<span class="anchor" id="acfc2c55-6a54-4465-a19d-59e4afe9c8c1"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="290eebe6-f113-4c88-a7df-9705f24bb62b"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="a0255de2-9727-4feb-8d96-f74a8ef5c709"></span>
## 5.FAQ
<p>无</p>
