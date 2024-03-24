<p>报价操作请求响应，当执行ReqQuoteAction后有字段填写不对之类的CTP报错则通过此接口返回。</p>
<span class="anchor" id="61d4d071-de3c-444f-bb2c-01f30b29a9dc"></span>
## 1.函数原型
<p>virtual void OnRspQuoteAction(CThostFtdcInputQuoteActionField *pInputQuoteAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="1809e96c-62d7-4438-a2eb-e14d7d569b12"></span>
## 2.参数
<p>pInputQuoteAction：输入报价操作</p>
<pre><code>struct CThostFtdcInputQuoteActionField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///报价操作引用
    TThostFtdcOrderActionRefType QuoteActionRef;
    ///报价引用
    TThostFtdcOrderRefType QuoteRef;
    ///请求编号
    TThostFtdcRequestIDType RequestID;
    ///前置编号
    TThostFtdcFrontIDType FrontID;
    ///会话编号
    TThostFtdcSessionIDType SessionID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///报价操作编号
    TThostFtdcOrderSysIDType QuoteSysID;
    ///操作标志
    TThostFtdcActionFlagType ActionFlag;
    ///用户代码
    TThostFtdcUserIDType UserID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
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
<span class="anchor" id="6d560117-d8cd-44d7-a97c-8a1b445505dc"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="aa53084c-be15-42d1-b0f9-38c9deed6a57"></span>
## 4.FAQ
<p>无</p>
