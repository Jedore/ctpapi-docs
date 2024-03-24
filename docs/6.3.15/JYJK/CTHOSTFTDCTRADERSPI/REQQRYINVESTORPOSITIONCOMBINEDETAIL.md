<p>请求查询投资者持仓明细</p>
<p>响应: OnRspQryInvestorPositionCombineDetail</p>
<span class="anchor" id="df05cef8-5148-4f48-af39-44a3215794a5"></span>
## 1.函数原型
<p>virtual int ReqQryInvestorPositionCombineDetail(CThostFtdcQryInvestorPositionCombineDetailField *pQryInvestorPositionCombineDetail, int nRequestID) = 0;</p>
<span class="anchor" id="dc786b77-1fb3-47f9-be48-96a859366453"></span>
## 2.参数
<p>pQryInvestorPositionCombineDetail：查询组合持仓明细</p>
<pre><code>struct CThostFtdcQryInvestorPositionCombineDetailField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///组合持仓合约编码
    TThostFtdcInstrumentIDType CombInstrumentID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="88a3ee11-f627-4cf9-88fb-42394bdd024b"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="7009ae7c-e2b1-46ed-9ec2-70b758d9750f"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="e62b5b4d-6a76-4089-a51d-60e68154d007"></span>
## 5.FAQ
<p>无</p>
