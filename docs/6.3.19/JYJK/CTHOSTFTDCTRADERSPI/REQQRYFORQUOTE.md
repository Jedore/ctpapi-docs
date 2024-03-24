<p>请求查询询价</p>
<p>响应：OnRspQryForQuote</p>
<span class="anchor" id="e6e588d3-36d3-472c-b2b9-05e7db4a6ab9"></span>
## 1.函数原型
<p>virtual int ReqQryForQuote(CThostFtdcQryForQuoteField *pQryForQuote, int nRequestID) = 0;</p>
<span class="anchor" id="a9ff08e2-6a26-4c27-9f88-2adae5d89e8f"></span>
## 2.参数
<p>pQryForQuote：询价查询</p>
<pre><code>struct CThostFtdcQryForQuoteField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///开始时间
    TThostFtdcTimeType InsertTimeStart;
    ///结束时间
    TThostFtdcTimeType InsertTimeEnd;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="108984be-f2f6-46a3-91df-7a8a0de70576"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="2ea3e7a9-627f-48de-a551-a2b77fb2b028"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="4163181b-a0f8-4c8d-80f4-6b81f3a75ec8"></span>
## 5.FAQ
<p>无</p>
