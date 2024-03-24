<p>请求查询报价</p>
<p>响应: OnRspQryQuote</p>
<span class="anchor" id="8e8056c8-17e4-4ff5-8883-d5b708532686"></span>
## 1.函数原型
<p>virtual int ReqQryQuote(CThostFtdcQryQuoteField *pQryQuote, int nRequestID) = 0;</p>
<span class="anchor" id="cae0a6a0-f8bb-4c74-8599-9768416fc831"></span>
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
<span class="anchor" id="c9c13b10-3349-4642-9f8e-640b138e6d6c"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="b6b9ea20-ad86-462b-8062-a8eefd5d2a61"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="99ff9e9f-d75d-4b78-8f9f-71d038dad0ce"></span>
## 5.FAQ
<p>无</p>
