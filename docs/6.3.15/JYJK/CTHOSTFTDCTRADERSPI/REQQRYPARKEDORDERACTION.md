<p>请求查询预埋撤单</p>
<p>响应: OnRspQryParkedOrderAction</p>
<span class="anchor" id="64f5fc19-6087-430b-ab97-be9ef645bd1f"></span>
## 1.函数原型
<p>virtual int ReqQryParkedOrderAction(CThostFtdcQryParkedOrderActionField *pQryParkedOrderAction, int nRequestID) = 0;</p>
<span class="anchor" id="a1ddee95-3622-4f2c-8124-2454b48fb49b"></span>
## 2.参数
<p>pQryParkedOrderAction：查询预埋撤单</p>
<pre><code>struct CThostFtdcQryParkedOrderActionField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="16081d98-ef65-46d0-80eb-2f920e3d3edf"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="2c83c2b1-2995-4922-8f52-d3ad5a1a89ad"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="8ae74ab9-129e-4447-8104-cee0ce9bb505"></span>
## 5.FAQ
<p>无</p>
