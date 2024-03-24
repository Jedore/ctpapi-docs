<p>请求查询预埋撤单</p>
<p>响应: OnRspQryParkedOrderAction</p>
<span class="anchor" id="fd68336b-755d-4611-b0dc-b13edb780f27"></span>
## 1.函数原型
<p>virtual int ReqQryParkedOrderAction(CThostFtdcQryParkedOrderActionField *pQryParkedOrderAction, int nRequestID) = 0;</p>
<span class="anchor" id="33552ac3-d838-42fa-99a3-6a849f64feb9"></span>
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
<span class="anchor" id="cad0d280-7a90-4522-8b87-1f15f1ec2b28"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="ff6da475-13ef-4df8-9261-3cfb3677cfa2"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="ec21b18e-8f0c-4fd5-bcd8-441a0f879a45"></span>
## 5.FAQ
<p>无</p>
