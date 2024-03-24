<p>报价录入错误回报，当执行ReqQuoteInsert后有字段填写不对之类的CTP报错则通过此接口返回</p>
<span class="anchor" id="7fd5add2-717a-4090-ad7c-dcbc6a8716c5"></span>
## 1.函数原型
<p>virtual void OnErrRtnQuoteInsert(CThostFtdcInputQuoteField *pInputQuote, CThostFtdcRspInfoField *pRspInfo) {};</p>
<span class="anchor" id="b112aa69-c230-4b5b-b7b1-d3a6326e80d1"></span>
## 2.参数
<p>pInputQuote：输入的报价</p>
<pre><code>struct CThostFtdcInputQuoteField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///报价引用
    TThostFtdcOrderRefType QuoteRef;
    ///用户代码
    TThostFtdcUserIDType UserID;
    ///卖价格
    TThostFtdcPriceType AskPrice;
    ///买价格
    TThostFtdcPriceType BidPrice;
    ///卖数量
    TThostFtdcVolumeType AskVolume;
    ///买数量
    TThostFtdcVolumeType BidVolume;
    ///请求编号
    TThostFtdcRequestIDType RequestID;
    ///业务单元
    TThostFtdcBusinessUnitType BusinessUnit;
    ///卖开平标志
    TThostFtdcOffsetFlagType AskOffsetFlag;
    ///买开平标志
    TThostFtdcOffsetFlagType BidOffsetFlag;
    ///卖投机套保标志
    TThostFtdcHedgeFlagType AskHedgeFlag;
    ///买投机套保标志
    TThostFtdcHedgeFlagType BidHedgeFlag;
    ///衍生卖报单引用
    TThostFtdcOrderRefType AskOrderRef;
    ///衍生买报单引用
    TThostFtdcOrderRefType BidOrderRef;
    ///应价编号
    TThostFtdcOrderSysIDType ForQuoteSysID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
    ///交易编码
    TThostFtdcClientIDType ClientID;
    ///IP地址
    TThostFtdcIPAddressType IPAddress;
    ///Mac地址
    TThostFtdcMacAddressType MacAddress;
};
</code></pre>
<p>ForQuoteSysID：应价编号对应市场上询价的编号</p>
<p>pRspInfo：响应信息</p>
<pre><code>struct CThostFtdcRspInfoField
{
    ///错误代码
    TThostFtdcErrorIDType ErrorID;
    ///错误信息
    TThostFtdcErrorMsgType ErrorMsg;
};
</code></pre>
<span class="anchor" id="0dbde41e-2b26-4664-b4a4-c1dcb28147a6"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="9cc74cfa-4a4b-49e3-8c77-0e0208499f14"></span>
## 4.FAQ
<p>无</p>
