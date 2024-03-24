<p>报价操作请求响应，当执行ReqQuoteAction后有字段填写不对之类的CTP报错则通过此接口返回。</p>
<span class="anchor" id="bb4ce355-e4a4-4046-a04d-f2d69e5429bf"></span>
## 1.函数原型
<p>virtual void OnRspQuoteAction(CThostFtdcInputQuoteActionField *pInputQuoteAction, CThostFtdcRspInfoField *pRspInfo, int nRequestID, bool bIsLast) {};</p>
<span class="anchor" id="e26a11e0-a941-4f3b-ba09-be45b2150a78"></span>
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
<span class="anchor" id="5a0faa4b-a89a-4e1f-870c-572219724190"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="aadf6680-d11a-4e1c-8ed1-884a3dfb0bc9"></span>
## 4.FAQ
<p>无</p>
