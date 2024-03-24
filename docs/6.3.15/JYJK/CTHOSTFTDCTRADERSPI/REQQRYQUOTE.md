<p>请求查询报价</p>
<p>响应: OnRspQryQuote</p>
<span class="anchor" id="8cfddcf9-65c7-4af0-892c-bda69c8ab7a4"></span>
## 1.函数原型
<p>virtual int ReqQryQuote(CThostFtdcQryQuoteField *pQryQuote, int nRequestID) = 0;</p>
<span class="anchor" id="124a0464-83f7-4a7d-b3f2-be2d3036a442"></span>
## 2.参数
<p>pQryQuote：报价查询</p>
<pre><code>struct CThostFtdcQryQuoteField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///报价编号
    TThostFtdcOrderSysIDType QuoteSysID;
    ///开始时间
    TThostFtdcTimeType InsertTimeStart;
    ///结束时间
    TThostFtdcTimeType InsertTimeEnd;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="8ee49429-084a-45df-84da-d77485097002"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="daec429d-68b0-421a-b39c-7e7114eb098c"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="e04fd7d2-9825-4955-9994-188a894a59e4"></span>
## 5.FAQ
<p>无</p>
