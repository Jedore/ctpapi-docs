<p>请求查询询价</p>
<p>响应：OnRspQryForQuote</p>
<span class="anchor" id="d1f79cf9-41f3-4f2d-9bd1-515c88025f3c"></span>
## 1.函数原型
<p>virtual int ReqQryForQuote(CThostFtdcQryForQuoteField *pQryForQuote, int nRequestID) = 0;</p>
<span class="anchor" id="c20d0920-587e-4bcd-9b5b-43049afcd6d2"></span>
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
<span class="anchor" id="d10986db-4e8c-42c4-a260-968032ca14b9"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="1bd34d75-df8b-483d-8efb-f54f43dca866"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="d2b0ce0f-b36b-48a5-9b99-60ba4f053da4"></span>
## 5.FAQ
<p>无</p>
