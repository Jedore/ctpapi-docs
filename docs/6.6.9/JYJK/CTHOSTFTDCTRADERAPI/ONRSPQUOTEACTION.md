<p>报价操作请求响应，当执行<a href="../../CTHOSTFTDCTRADERSPI/REQQUOTEACTION/">ReqQuoteAction</a>后有字段填写不对之类的CTP报错则通过此接口返回。</p>
<span class="anchor" id="0942d369-45c0-4f4a-8bec-f66d98966fe9"></span>
## 1.函数原型
<p>virtual void OnRspQuoteAction(CThostFtdcInputQuoteActionField *pInputQuoteAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="c2a45f7a-b83b-40ef-903e-f75b76659e1e"></span>
## 2.参数
<p>pInputQuoteAction：输入报价操作</p>
<pre><code>struct CThostFtdcInputQuoteActionField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType  BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType    InvestorID;
    ///报价操作引用
    TThostFtdcOrderActionRefType    QuoteActionRef;
    ///报价引用
    TThostFtdcOrderRefType  QuoteRef;
    ///请求编号
    TThostFtdcRequestIDType RequestID;
    ///前置编号
    TThostFtdcFrontIDType   FrontID;
    ///会话编号
    TThostFtdcSessionIDType SessionID;
    ///交易所代码
    TThostFtdcExchangeIDType    ExchangeID;
    ///报价操作编号
    TThostFtdcOrderSysIDType    QuoteSysID;
    ///操作标志
    TThostFtdcActionFlagType    ActionFlag;
    ///用户代码
    TThostFtdcUserIDType    UserID;
    ///保留的无效字段
    TThostFtdcOldInstrumentIDType   reserve1;
    ///投资单元代码
    TThostFtdcInvestUnitIDType  InvestUnitID;
    ///交易编码
    TThostFtdcClientIDType  ClientID;
    ///保留的无效字段
    TThostFtdcOldIPAddressType  reserve2;
    ///Mac地址
    TThostFtdcMacAddressType    MacAddress;
    ///合约代码
    TThostFtdcInstrumentIDType  InstrumentID;
    ///IP地址
    TThostFtdcIPAddressType IPAddress;
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
<span class="anchor" id="77bb2d22-d463-41d7-834a-be6b54e4d906"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="86e44ce5-3a4b-4df8-bec1-bbfd73d1589b"></span>
## 4.FAQ
<p>无</p>
