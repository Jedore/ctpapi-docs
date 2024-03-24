<p>请求查询投资者品种/跨品种保证金</p>
<p>响应: OnRspQryInvestorProductGroupMargin</p>
<span class="anchor" id="27d3c3e2-588f-488a-8d1f-b4708fe66fb8"></span>
## 1.函数原型
<p>virtual int ReqQryInvestorProductGroupMargin(CThostFtdcQryInvestorProductGroupMarginField *pQryInvestorProductGroupMargin, int nRequestID) = 0;</p>
<span class="anchor" id="ca39354f-dab2-4f8a-8dfb-2e2b0f77fab7"></span>
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
<span class="anchor" id="5e3f7289-1dbd-4c18-a027-078dac036cc9"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="d6e60787-8bf1-412a-b2a6-51cd6fbf6e5f"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="2d41ebc1-71fb-4c3e-8ce8-278261ce6d38"></span>
## 5.FAQ
<p>无</p>
