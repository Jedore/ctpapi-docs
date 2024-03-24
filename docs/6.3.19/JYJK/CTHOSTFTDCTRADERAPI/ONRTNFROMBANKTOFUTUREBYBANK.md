<p>银行发起银行资金转期货通知，无Req属于私有流回报</p>
<span class="anchor" id="cf7547c9-363c-49c0-8f2d-2d47ae6e7f2a"></span>
## 1.函数原型
<p>virtual void OnRtnFromBankToFutureByBank(CThostFtdcRspTransferField *pRspTransfer) {};</p>
<span class="anchor" id="a4f57aad-803d-4402-aaa0-afb7011b5b08"></span>
## 2.参数
<p>pRspTransfer：银行发起银行资金转期货响应</p>
<pre><code>struct CThostFtdcRspTransferField
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
    ///安装编号
    TThostFtdcInstallIDType InstallID;
    ///期货公司流水号
    TThostFtdcFutureSerialType FutureSerial;
    ///用户标识
    TThostFtdcUserIDType UserID;
    ///验证客户证件号码标志
    TThostFtdcYesNoIndicatorType VerifyCertNoFlag;
    ///币种代码
    TThostFtdcCurrencyIDType CurrencyID;
    ///转帐金额
    TThostFtdcTradeAmountType TradeAmount;
    ///期货可取金额
    TThostFtdcTradeAmountType FutureFetchAmount;
    ///费用支付标志
    TThostFtdcFeePayFlagType FeePayFlag;
    ///应收客户费用
    TThostFtdcCustFeeType CustFee;
    ///应收期货公司费用
    TThostFtdcFutureFeeType BrokerFee;
    ///发送方给接收方的消息
    TThostFtdcAddInfoType Message;
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
    ///转账交易状态
    TThostFtdcTransferStatusType TransferStatus;
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
    ///长客户姓名
    TThostFtdcLongIndividualNameType LongCustomerName;
};
</code></pre>
<p>TradeCode：102001 银行发起银行资金转期货</p>
<p>BankBranchID：填0000</p>
<p>BrokerBranchID：填空</p>
<p>InstallID：CTP内部使用</p>
<span class="anchor" id="e51ea731-7f57-4527-91d9-e0512027adee"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="a9f1ceaa-5483-4226-aec1-738f1a688e7b"></span>
## 4.FAQ
<p>无</p>
