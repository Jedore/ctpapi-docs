<p>请求查询转帐流水响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQRYTRANSFERSERIAL/">ReqQryTransferSerial</a>后，该方法被调用。</p>
<span class="anchor" id="821bd17c-63f6-492c-a7c0-cd9e33f321b5"></span>
## 1.函数原型
<p>virtual void OnRspQryTransferSerial(CThostFtdcTransferSerialField *pTransferSerial, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="4d938131-985d-46b0-9e73-8d43c83a3e6b"></span>
## 2.参数
<p>pTransferSerial：银期转账交易流水表</p>
<pre><code>struct CThostFtdcTransferSerialField
{
    ///平台流水号
    TThostFtdcPlateSerialType PlateSerial;
    ///交易发起方日期
    TThostFtdcTradeDateType TradeDate;
    ///交易日期
    TThostFtdcDateType TradingDay;
    ///交易时间
    TThostFtdcTradeTimeType TradeTime;
    ///交易代码
    TThostFtdcTradeCodeType TradeCode;
    ///会话编号
    TThostFtdcSessionIDType SessionID;
    ///银行编码
    TThostFtdcBankIDType BankID;
    ///银行分支机构编码
    TThostFtdcBankBrchIDType BankBranchID;
    ///银行帐号类型
    TThostFtdcBankAccTypeType BankAccType;
    ///银行帐号
    TThostFtdcBankAccountType BankAccount;
    ///银行流水号
    TThostFtdcBankSerialType BankSerial;
    ///期货公司编码
    TThostFtdcBrokerIDType BrokerID;
    ///期商分支机构代码
    TThostFtdcFutureBranchIDType BrokerBranchID;
    ///期货公司帐号类型
    TThostFtdcFutureAccTypeType FutureAccType;
    ///投资者帐号
    TThostFtdcAccountIDType AccountID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///期货公司流水号
    TThostFtdcFutureSerialType FutureSerial;
    ///证件类型
    TThostFtdcIdCardTypeType IdCardType;
    ///证件号码
    TThostFtdcIdentifiedCardNoType IdentifiedCardNo;
    ///币种代码
    TThostFtdcCurrencyIDType CurrencyID;
    ///交易金额
    TThostFtdcTradeAmountType TradeAmount;
    ///应收客户费用
    TThostFtdcCustFeeType CustFee;
    ///应收期货公司费用
    TThostFtdcFutureFeeType BrokerFee;
    ///有效标志
    TThostFtdcAvailabilityFlagType AvailabilityFlag;
    ///操作员
    TThostFtdcOperatorCodeType OperatorCode;
    ///新银行帐号
    TThostFtdcBankAccountType BankNewAccount;
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<p>BankBranchID：填0000</p>
<p>BrokerBranchID：填0000</p>
<p>AvailabilityFlag：是否转账成功，不成功则CTP会自动发起冲正</p>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<p>nRequestID：返回用户操作请求的ID，该ID 由用户在操作请求时指定。</p>
<p>bIsLast：指示该次返回是否为针对nRequestID的最后一次返回。</p>
<span class="anchor" id="d90aea1b-cea1-4a36-80c7-355d01c6ed65"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="5a5fb9bd-83a5-4ae8-88d1-8fd3f4bafa8a"></span>
## 4.FAQ
<p>无</p>
