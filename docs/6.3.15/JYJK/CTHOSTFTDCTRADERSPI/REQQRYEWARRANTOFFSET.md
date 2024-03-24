<p>请求查询仓单折抵信息</p>
<p>响应: OnRspQryEWarrantOffset</p>
<span class="anchor" id="d842445d-29a2-4425-96ed-7dc0876cfab9"></span>
## 1.函数原型
<p>virtual int ReqQryEWarrantOffset(CThostFtdcQryEWarrantOffsetField *pQryEWarrantOffset, int nRequestID) = 0;</p>
<span class="anchor" id="5fa8876a-f18f-47f0-b3c4-76cce68ff236"></span>
## 2.参数
<p>pQryEWarrantOffset：查询仓单折抵信息</p>
<pre><code>struct CThostFtdcQryEWarrantOffsetField
{
    ///经纪公司代码
    TThostFtdcBrokerIDType BrokerID;
    ///投资者代码
    TThostFtdcInvestorIDType InvestorID;
    ///交易所代码
    TThostFtdcExchangeIDType ExchangeID;
    ///合约代码
    TThostFtdcInstrumentIDType InstrumentID;
    ///投资单元代码
    TThostFtdcInvestUnitIDType InvestUnitID;
};
</code></pre>
<p>nRequestID：请求ID，对应响应里的nRequestID，无递增规则，由用户自行维护。</p>
<span class="anchor" id="b4c2624d-5873-4216-bf48-791ef9c137f2"></span>
## 3.返回
<p>0，代表成功。</p>
<p>-1，表示网络连接失败；</p>
<p>-2，表示未处理请求超过许可数；</p>
<p>-3，表示每秒发送请求数超过许可数。</p>
<span class="anchor" id="c551025e-1f61-4041-a1ad-a7f9a7aad14e"></span>
## 4.调用示例
<p>无</p>
<span class="anchor" id="8011dc0a-04bd-4308-b948-f6596de1273c"></span>
## 5.FAQ
<p>无</p>
