<p>系统运行时期货端手工发起冲正期货转银行请求，银行处理完毕后报盘发回的通知，无Req属于私有流回报</p>
<span class="anchor" id="36be8d1f-26ca-4a0d-bfcb-624c213e6477"></span>
## 1.函数原型
<p>virtual void OnRtnRepealFromFutureToBankByFutureManual(CThostFtdcRspRepealField *pRspRepeal) {};</p>
<span class="anchor" id="738c606e-0f17-4e5d-84ce-5d3a133e58a0"></span>
## 2.参数
<p>pRspRepeal：冲正响应</p>
<pre><code>struct CThostFtdcRspRepealField
{
    ///冲正时间间隔
    TThostFtdcRepealTimeIntervalType RepealTimeInterval;
    ///已经冲正次数
    TThostFtdcRepealedTimesType RepealedTimes;
    ///银行冲正标志
    TThostFtdcBankRepealFlagType BankRepealFlag;
    ///期商冲正标志
    TThostFtdcBrokerRepealFlagType BrokerRepealFlag;
    ///被冲正平台流水号
    TThostFtdcPlateSerialType PlateRepealSerial;
    ///被冲正银行流水号
    TThostFtdcBankSerialType BankRepealSerial;
    ///被冲正期货流水号
    TThostFtdcFutureSerialType FutureRepealSerial;
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
<p>TradeCode：203002 期货发起冲正期货转银行</p>
<p>BankBranchID：填0000</p>
<p>BrokerBranchID：一般为空</p>
<p>BankPassWord：为密文，显示为“*”</p>
<p>Password：为密文，显示为“*”</p>
<p>InstallID：CTP内部使用</p>
<p>TransferStatus：转账状态</p>
<p>ErrorMsg：报错信息明文，若成功则显示为“交易成功”</p>
<span class="anchor" id="b7751877-f740-43f0-a530-78c1ef20121c"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="453ef9f5-e430-4657-871f-3a3a21b6a649"></span>
## 4.FAQ
<p>无</p>
