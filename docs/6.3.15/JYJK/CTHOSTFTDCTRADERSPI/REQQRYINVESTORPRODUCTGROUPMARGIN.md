<p>请求查询投资者品种/跨品种保证金</p>
<p>响应: OnRspQryInvestorProductGroupMargin</p>
<span class="anchor" id="4dafd89b-fb42-457b-a5cb-9592fa90c2b9"></span>
## 1.函数原型
<p>virtual int ReqQryInvestorProductGroupMargin(CThostFtdcQryInvestorProductGroupMarginField *pQryInvestorProductGroupMargin, int nRequestID) = 0;</p>
<span class="anchor" id="c636a856-dd57-4046-aeee-02bd6a9c17d2"></span>
## 2.参数
<p>pQryInvestorProductGroupMargin：查询投资者品种/跨品种保证金</p>
<pre><code>struct CThostFtdcQryInvestorProductGroupMarginField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///品种/跨品种标示
    TThostFtdcInstrumentIDType ProductGroupID;
    ///投机套保标志
    TThostFtdcHedgeFlagType HedgeFlag;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="d2fbe11e-f8c9-4558-9930-8d162ac1466e"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="dee9ec03-69ea-4ad9-a154-4e0f69c44917"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="b257a988-c9e3-47f6-9cf2-e0347ca6d5ac"></span>
## 5.FAQ
<p>无</p>
