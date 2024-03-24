<span class="anchor" id="2101c5b3-15cf-457c-a96b-494345931a0b"></span>
## 1.说明
<p>期货发起银行资金转期货通知，当执行ReqFromBankToFutureByFuture后并且报出后，收到返回则调用此接口，私有流回报。</p>
<span class="anchor" id="f647ea32-d24a-4127-965c-1173dec22d52"></span>
## 2.函数原型
<p>virtual void OnRtnFromBankToFutureByFuture(CThostFtdcRspTransferField *pRspTransfer) {};</p>
<span class="anchor" id="8418dbe9-1def-4611-83ef-04f28ac02a29"></span>
## 3.参数
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
<p>TradeCode：202001 期货发起银行资金转期货</p>
<p>BankBranchID：填0000</p>
<p>BrokerBranchID：一般为空</p>
<p>TransferStatus：转账的最后状态，“正常”说明转账成功，“被冲正”说明转账失败</p>
<span class="anchor" id="21b8bd12-af07-4e56-a20a-af0678241c15"></span>
## 4.返回
<p>无</p>
<span class="anchor" id="116edd8a-de6b-4c05-b2bf-79b6be08562d"></span>
## 5.FAQ
<p>无</p>
