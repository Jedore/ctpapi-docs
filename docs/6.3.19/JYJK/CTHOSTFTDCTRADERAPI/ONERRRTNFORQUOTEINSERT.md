<p>询价录入错误回报，当执行ReqForQuoteInsert后有字段填写不对之类的CTP报错则通过此接口返回</p>
<span class="anchor" id="62133434-3de9-42c1-8df2-a4709e580324"></span>
## 1.函数原型
<p>virtual void OnErrRtnForQuoteInsert(CThostFtdcInputForQuoteField *pInputForQuote, CThostFtdcRspInfoField *pRspInfo) {};</p>
<span class="anchor" id="0f97b80b-0fb2-4265-87fd-08f7d5738a75"></span>
## 2.参数
<p>pInputForQuote：输入的询价</p>
<pre><code>struct CThostFtdcInputForQuoteField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///询价引用
    TThostFtdcOrderRefType ForQuoteRef;
    ///用户代码
    TThostFtdcUserIDType UserID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
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
<span class="anchor" id="01329a8c-013f-472b-90a3-3f3f1227a5ff"></span>
## 3.返回
<p>无</p>
<span class="anchor" id="81e698d0-7555-45eb-875b-3ff77ec60fd7"></span>
## 4.FAQ
<p>无</p>
